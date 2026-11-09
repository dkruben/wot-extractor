"""Motor de extracao: executa o plano para um realm, de forma incremental,
paralela e retomavel, e escreve manifest.json / extraction_report.json."""

from __future__ import annotations

import platform
import threading
import time
import zipfile
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .. import TOOL_NAME, __version__
from ..config import Config
from ..constants import MANIFEST_SCHEMA, OUTPUT_SKELETON
from ..detect.install import ClientInstall
from ..logutil import get_logger
from ..safety import ArchiveLimits, WriteGuard, resolve_within
from .manifest import Journal, ManifestError, StateLock, load_manifest
from .plan import Entry, Filters, Plan, build_plan
from ..formats.bwxml import DECODER_VERSION
from .validate import MAX_VALIDATE_SIZE, NEEDS_DATA, VALIDATOR_VERSION, inspect_content
from .xmldecode import XML_DIR, DecodeStats, run_decode_pass
from .writer import existing_size, long_path, remove_file, save_json_atomic, write_atomic

log = get_logger("extract")

OK_STATUSES = frozenset({"extracted", "unchanged"})
MAX_LISTED = 500  # limite de itens listados no relatorio (os totais sao sempre completos)


@dataclass
class ExtractOptions:
    filters: Filters = field(default_factory=Filters)
    jobs: int = 4
    force: bool = False
    dry_run: bool = False
    prune: bool = False
    decode_xml: bool = True
    limits: ArchiveLimits = field(default_factory=ArchiveLimits)


@dataclass
class ExtractResult:
    realm: str
    out_dir: Path
    version_name: str
    previous_version: str | None = None
    started: str = ""
    elapsed: float = 0.0
    found: int = 0
    filtered_out: int = 0
    selected: int = 0
    selected_bytes: int = 0
    counts: Counter = field(default_factory=Counter)
    by_tree: dict[str, Counter] = field(default_factory=dict)
    by_category: Counter = field(default_factory=Counter)
    validation: dict[str, Counter] = field(default_factory=dict)
    invalid: list[dict] = field(default_factory=list)
    bytes_written: int = 0
    failures: list[dict] = field(default_factory=list)
    removed: list[str] = field(default_factory=list)
    pruned: list[str] = field(default_factory=list)
    skipped_containers: list[dict] = field(default_factory=list)
    collisions: list[dict] = field(default_factory=list)
    shadowed: int = 0
    overridden: list[dict] = field(default_factory=list)
    resumed: int = 0
    to_extract: int = 0
    long_paths: int = 0  # destinos com mais de 259 caracteres (exigem \\?\ ou LongPathsEnabled)
    revalidated: int = 0  # entradas inalteradas revalidadas por mudanca de versao do validador
    xml: DecodeStats | None = None  # descodificacao dos XML binarios (None = desativada)
    interrupted: bool = False
    consistent: bool = False
    dry_run: bool = False
    manifest_path: Path | None = None
    report_path: Path | None = None
    filters: dict = field(default_factory=dict)

    @property
    def failed_total(self) -> int:
        return len(self.failures)

    def to_report(self) -> dict:
        return {
            "tool": TOOL_NAME, "tool_version": __version__,
            "realm": self.realm, "version_name": self.version_name, "previous_version": self.previous_version,
            "started": self.started, "elapsed_s": round(self.elapsed, 2),
            "dry_run": self.dry_run, "interrupted": self.interrupted, "consistent": self.consistent,
            "filters": self.filters,
            "counts": {
                "found": self.found, "filtered_out": self.filtered_out, "selected": self.selected,
                "selected_bytes": self.selected_bytes, "resumed_from_journal": self.resumed,
                "processed": self.counts.get("extracted", 0) + self.counts.get("unchanged", 0) + self.counts.get("failed", 0),
                "extracted": self.counts.get("extracted", 0), "unchanged": self.counts.get("unchanged", 0),
                "failed": self.failed_total, "removed": len(self.removed), "pruned": len(self.pruned),
                "bytes_written": self.bytes_written, "shadowed": self.shadowed, "overridden": len(self.overridden),
                "long_paths": self.long_paths, "revalidated": self.revalidated,
            },
            "by_tree": {k: dict(v) for k, v in self.by_tree.items()},
            "by_category": dict(self.by_category.most_common()),
            "validation": {k: dict(v) for k, v in self.validation.items()},
            "invalid_files": self.invalid[:MAX_LISTED],
            "failures": self.failures[:MAX_LISTED],
            "removed": self.removed[:MAX_LISTED],
            "pruned": self.pruned[:MAX_LISTED],
            "skipped_containers": self.skipped_containers,
            "collisions": self.collisions[:MAX_LISTED],
            "overridden_by_mods": self.overridden[:MAX_LISTED],
            "xml_decode": self.xml.to_dict(MAX_LISTED) if self.xml else None,
        }


class _ZipPool:
    """Um ZipFile por thread e por contentor (ZipFile partilhado serializa leituras)."""

    def __init__(self):
        self._local = threading.local()
        self._all: list[zipfile.ZipFile] = []
        self._lock = threading.Lock()

    def get(self, path: Path) -> zipfile.ZipFile:
        cache = getattr(self._local, "cache", None)
        if cache is None:
            cache = self._local.cache = {}
        zf = cache.get(path)
        if zf is None:
            zf = zipfile.ZipFile(long_path(path), "r")
            cache[path] = zf
            with self._lock:
                self._all.append(zf)
        return zf

    def close(self) -> None:
        with self._lock:
            for zf in self._all:
                try:
                    zf.close()
                except OSError:
                    pass
            self._all.clear()


def _process(e: Entry, install_root: Path, sources_dir: Path, pool: _ZipPool) -> dict:
    rec = e.base_record()
    try:
        dest = resolve_within(sources_dir / e.tree, e.path)
        data = None
        want_data = e.category in NEEDS_DATA and e.size <= MAX_VALIDATE_SIZE
        if e.kind == "zip":
            zf = pool.get(install_root / e.container)
            if want_data:
                data = zf.read(e.member)  # verifica o CRC
                size, sha = write_atomic(dest, data)
            else:
                with zf.open(e.member) as fh:
                    size, sha = write_atomic(dest, fh)
        else:
            with open(long_path(install_root / e.container), "rb") as fh:
                if want_data:
                    data = fh.read()
                    size, sha = write_atomic(dest, data)
                else:
                    size, sha = write_atomic(dest, fh)
        if size != e.size:
            raise OSError(f"tamanho inesperado: {size} B (esperado {e.size} B)")
        rec["status"] = "extracted"
        rec["sha256"] = sha
        if data is not None:
            validation, info = inspect_content(e.category, data, e.path)
            if validation:
                rec["validation"] = validation
            if info:
                rec["info"] = info
    except Exception as exc:  # regista e continua
        rec["status"] = "failed"
        rec["error"] = f"{type(exc).__name__}: {exc}"
    return rec


def _in_scope(filters: Filters, rec: dict) -> bool:
    return filters.accepts(rec.get("tree", ""), rec.get("virtual", ""), rec.get("category", "other"),
                           rec.get("container", "").rsplit("/", 1)[-1], rec.get("source", "file"))


def run_extract(cfg: Config, install: ClientInstall, options: ExtractOptions | None = None,
                progress=None) -> ExtractResult:
    options = options or ExtractOptions()
    out_dir = WriteGuard([install.path]).check_output_root(cfg.realm_output_dir(install.realm))
    if options.dry_run:
        return _run_extract(cfg, install, options, progress)
    with StateLock(out_dir):  # extract e decompile nao alteram a mesma arvore ao mesmo tempo
        return _run_extract(cfg, install, options, progress)


def _run_extract(cfg: Config, install: ClientInstall, options: ExtractOptions, progress) -> ExtractResult:
    t0 = time.perf_counter()
    realm = install.realm
    out_dir = cfg.realm_output_dir(realm)
    # Toda a escrita acontece dentro de wot_src_<R>: essa pasta nao pode estar
    # dentro da instalacao nem conte-la.
    guard = WriteGuard([install.path])
    out_dir = guard.check_output_root(out_dir)
    state_dir = out_dir / ".state"
    sources_dir = out_dir / "sources"
    manifest_path = out_dir / "manifest.json"

    res = ExtractResult(realm=realm, out_dir=out_dir, version_name=install.version.folder_name,
                        started=datetime.now(timezone.utc).isoformat(timespec="seconds"),
                        dry_run=options.dry_run, filters=options.filters.to_dict())

    prev = load_manifest(manifest_path)
    if prev is not None and prev.get("realm") != realm:
        raise ManifestError(f"{manifest_path} pertence ao realm {prev.get('realm')}, nao a {realm} (realms nao se misturam)")
    prev_entries: dict[str, dict] = prev["entries"] if prev else {}
    res.previous_version = prev.get("version_name") if prev else None

    journal = Journal(state_dir / "journal.jsonl")
    resumed = journal.load()
    res.resumed = len(resumed)
    known = dict(prev_entries)
    known.update(resumed)

    plan: Plan = build_plan(install, options.filters, options.limits)
    res.found, res.filtered_out = plan.found, plan.filtered_out
    res.selected, res.selected_bytes = len(plan.entries), plan.selected_bytes
    res.skipped_containers, res.collisions = plan.skipped_containers, plan.collisions
    res.failures = list(plan.failures)
    res.shadowed = sum(len(e.shadows) for e in plan.entries)
    res.overridden = [{"path": e.key, "overridden_by": e.overridden_by} for e in plan.entries if e.overridden_by]
    base_len = len(str(sources_dir)) + 1
    res.long_paths = sum(1 for e in plan.entries if base_len + len(e.tree) + 1 + len(e.path) > 259)

    # ---- o que ja esta extraido e inalterado
    prev_validator = (prev or {}).get("tool_versions", {}).get("validator")
    revalidate = prev is not None and prev_validator != VALIDATOR_VERSION
    records: dict[str, dict] = {}
    todo: list[Entry] = []
    for e in plan.entries:
        rec = known.get(e.key)
        cleaned_ok = bool(rec and (rec.get("cleaned") or {}).get("size") == e.size)  # apagado pelo `clean`
        if (not options.force and rec and rec.get("status") in OK_STATUSES and e.same_source(rec)
                and (cleaned_ok or existing_size(sources_dir / e.tree / e.path) == e.size)):
            new = e.base_record()
            new["status"] = "unchanged"
            for k in ("sha256", "validation", "info", "decoded", "decompiled", "actionscript", "gameface", "stubs",
                      "cleaned"):
                if k in rec:
                    new[k] = rec[k]
            records[e.key] = new
        else:
            todo.append(e)
    res.to_extract = len(todo)

    if revalidate and not options.dry_run:
        for e in plan.entries:
            new = records.get(e.key)
            if new is None or e.category not in NEEDS_DATA or e.size > MAX_VALIDATE_SIZE or new.get("cleaned"):
                continue
            try:
                with open(long_path(sources_dir / e.tree / e.path), "rb") as fh:
                    validation, info = inspect_content(e.category, fh.read(), e.path)
            except OSError:
                continue
            new.pop("validation", None)
            new.pop("info", None)
            if validation:
                new["validation"] = validation
            if info:
                new["info"] = info
            res.revalidated += 1

    if options.dry_run:
        res.counts["unchanged"] = len(records)
        res.elapsed = time.perf_counter() - t0
        return res

    for d in OUTPUT_SKELETON:
        (out_dir / d).mkdir(parents=True, exist_ok=True)
    state_dir.mkdir(parents=True, exist_ok=True)

    # ---- execucao paralela (submissao limitada para nao encher a memoria)
    pool = _ZipPool()
    done_count = len(records)
    total = len(plan.entries)
    max_inflight = max(1, options.jobs) * 32

    def handle(futures):
        nonlocal done_count
        for f in futures:
            rec = f.result()
            key = f"{rec['tree']}/{rec['path']}"
            records[key] = rec
            journal.write({"key": key, **rec})
            if rec["status"] == "extracted":
                res.bytes_written += rec["size"]
            done_count += 1
        if progress:
            progress(done_count, total, res.bytes_written)

    try:
        with ThreadPoolExecutor(max_workers=max(1, options.jobs), thread_name_prefix="extract") as ex:
            inflight = set()
            try:
                for e in todo:
                    inflight.add(ex.submit(_process, e, install.path, sources_dir, pool))
                    if len(inflight) >= max_inflight:
                        finished, inflight = wait(inflight, return_when=FIRST_COMPLETED)
                        handle(finished)
                while inflight:
                    finished, inflight = wait(inflight, return_when=FIRST_COMPLETED)
                    handle(finished)
            except KeyboardInterrupt:
                res.interrupted = True
                ex.shutdown(wait=True, cancel_futures=True)
    finally:
        pool.close()
        journal.close()

    # ---- copias legiveis dos XML binarios (sources_xml/)
    if options.decode_xml and not res.interrupted:
        try:
            res.xml = run_decode_pass(records, known, out_dir, options.jobs, OK_STATUSES)
        except KeyboardInterrupt:
            res.interrupted = True

    if res.interrupted:
        res.counts.update(r["status"] for r in records.values())
        res.elapsed = time.perf_counter() - t0
        log.warning("Extracao interrompida: %d registos no journal; volte a correr para retomar.", len(records))
        return res

    # ---- estatisticas
    for rec in records.values():
        st = rec["status"]
        res.counts[st] += 1
        res.by_tree.setdefault(rec["tree"], Counter())[st] += 1
        res.by_category[rec["category"]] += 1
        if st == "failed":
            res.failures.append({"key": f"{rec['tree']}/{rec['path']}", "container": rec["container"],
                                 "member": rec.get("member", ""), "error": rec.get("error", "")})
        v = rec.get("validation")
        if v:
            bucket = "invalid" if v.startswith("invalid") else v
            res.validation.setdefault(rec["category"], Counter())[bucket] += 1
            if bucket == "invalid" and len(res.invalid) < MAX_LISTED:
                res.invalid.append({"path": f"{rec['tree']}/{rec['path']}", "validation": v})

    # ---- fusao com o manifesto anterior (entradas fora do ambito dos filtros sao mantidas)
    entries: dict[str, dict] = {}
    for k, rec in prev_entries.items():
        if k in records:
            continue
        if _in_scope(options.filters, rec):
            res.removed.append(k)
        else:
            entries[k] = rec
    res.consistent = not res.failures
    if options.prune and res.consistent:
        for k in res.removed:
            rec = prev_entries[k]
            try:
                target = resolve_within(sources_dir / rec["tree"], rec["path"])
            except ValueError:
                continue
            if remove_file(target):
                res.pruned.append(k)
                if rec.get("decoded"):
                    remove_file(resolve_within(out_dir / XML_DIR / rec["tree"], rec["path"]))
                dec_out = (rec.get("decompiled") or {}).get("output")
                if dec_out:
                    remove_file(resolve_within(out_dir, dec_out))
                if rec.get("actionscript"):
                    from ..actionscript.engine import remove_outputs
                    remove_outputs(out_dir, rec)
                if rec.get("gameface"):
                    from ..gameface.analyze import remove_outputs as remove_gf_outputs
                    remove_gf_outputs(out_dir, rec)
    pruned = set(res.pruned)
    for k in res.removed:
        if k not in pruned:
            entries[k] = {**prev_entries[k], "status": "removed"}
    entries.update(records)

    # ---- escrita final: manifesto, relatorios, .version_name
    now = datetime.now(timezone.utc)
    ok = res.counts.get("extracted", 0) + res.counts.get("unchanged", 0)
    manifest = {
        "schema": MANIFEST_SCHEMA,
        "realm": realm,
        "version_name": install.version.folder_name,
        "game_version": install.version.to_dict(),
        "extraction_date": now.isoformat(timespec="seconds"),
        "install_path": str(install.path),
        "app_type": install.app_type,
        "consistent": res.consistent,
        "filters": options.filters.to_dict(),
        "counts": {"found": res.found, "selected": res.selected, "processed": ok + res.counts.get("failed", 0),
                   "success": ok, "failed": res.failed_total, "entries": len(entries)},
        "tool_versions": {"wot_extractor": __version__, "python": platform.python_version(),
                          "manifest_schema": MANIFEST_SCHEMA, "validator": VALIDATOR_VERSION,
                          "bwxml_decoder": DECODER_VERSION},
        "load_order": plan.containers,
        "entries": dict(sorted(entries.items())),
    }
    for section in ("decompile", "actionscript", "gameface", "stubs"):  # resumos das fases C a F
        if prev and prev.get(section):
            manifest[section] = prev[section]
            if section in prev.get("tool_versions", {}):
                manifest["tool_versions"][section] = prev["tool_versions"][section]
    if manifest_path.is_file():
        write_atomic(state_dir / "manifest.prev.json", manifest_path.read_bytes())
    save_json_atomic(manifest_path, manifest, indent=None)
    res.manifest_path = manifest_path
    res.elapsed = time.perf_counter() - t0
    report = res.to_report()
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    save_json_atomic(state_dir / "reports" / f"extraction_{stamp}.json", report)
    save_json_atomic(out_dir / "extraction_report.json", report)
    res.report_path = out_dir / "extraction_report.json"
    if res.consistent:
        write_atomic(out_dir / ".version_name", (install.version.folder_name + "\n").encode("utf-8"))
    journal.remove()
    return res
