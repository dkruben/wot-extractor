"""Motor do comando `actionscript`: catalogo dos SWF, recuperacao do codigo
ActionScript e extracao dos recursos incorporados, para sources_as/.

Por SWF (chave <arvore>/<caminho> do manifesto):
  sources_as/swf/<chave>.json      catalogo (cabecalho, tags, classes, imports/exports, fontes...)
  sources_as/scripts/<chave>/      codigo AS3: descompilado pelo FFDec, ou so declaracoes
  sources_as/assets/<chave>/       imagens, fontes, sons, dados binarios, simbolo->classe (FFDec)
e, para todos, sources_as/catalog.json (indice classe -> SWF) e actionscript_report.json.

Estados (campo "actionscript" de cada SWF no manifesto):
  success      catalogo lido e codigo descompilado sem falhas (todas as classes exportadas)
  partial      ha falhas: metodos nao descompilados, classes em falta, so declaracoes, ou erro num componente
  failed       o SWF nao pode ser lido
  extracted    SWF sem codigo ActionScript (so recursos)
  unsupported  codigo AS1/2 sem descompilador disponivel
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import shutil
import time
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .. import TOOL_NAME, __version__
from ..config import Config
from ..extract.manifest import Journal, ManifestError, StateLock, load_manifest
from ..extract.writer import long_path, remove_file, remove_tree, save_json_atomic, write_atomic
from ..formats.abc import PARSER_VERSION as ABC_VERSION
from ..formats.abc import class_declaration
from ..formats.swf import SWF_PARSER_VERSION, SwfError, parse_swf, swf_from_container
from ..logutil import get_logger
from ..safety import resolve_within
from . import ffdec as ffdec_mod
from . import rabcdasm as rabcdasm_mod
from .ffdec import FFDec

log = get_logger("actionscript")

AS_DIR = "sources_as"
OK_ENTRY = frozenset({"extracted", "unchanged"})
RANK = {"success": 4, "extracted": 4, "partial": 3, "unsupported": 2, "failed": 1}
JOURNAL_NAME = "actionscript_journal.jsonl"
MAX_LISTED = 2000
DEFAULT_TIMEOUT = 3600.0


@dataclass
class ASOptions:
    jobs: int = 4
    timeout: float = DEFAULT_TIMEOUT  # por SWF (FFDec)
    method_timeout: int = 60
    class_timeout: int = 600
    use_ffdec: bool = True
    assets: bool = True
    force: bool = False
    retry: bool = False
    globs: tuple[str, ...] = ()
    trees: frozenset[str] = frozenset()
    limit: int = 0
    dry_run: bool = False
    # SWF com muito codigo (ABC >= heavy_abc_bytes) consomem varios GB cada no FFDec: no maximo
    # heavy_jobs em simultaneo (6 em paralelo esgotaram a RAM fisica na 1.a execucao real)
    heavy_jobs: int = 2
    heavy_abc_bytes: int = 2 * 1024 * 1024
    # desmontagem RABCDAsm (.asasm): "partial" (so SWF com falhas do FFDec), "all" ou "none"
    asasm: str = "partial"
    rabc: object | None = None  # rabcdasm.Rabc


@dataclass
class ASResult:
    realm: str
    out_dir: Path
    started: str = ""
    elapsed: float = 0.0
    candidates: int = 0
    selected: int = 0
    to_process: int = 0
    limited: int = 0
    resumed: int = 0
    processed: Counter = field(default_factory=Counter)
    unchanged: Counter = field(default_factory=Counter)
    totals: Counter = field(default_factory=Counter)
    code: Counter = field(default_factory=Counter)  # as3 / as2 / none
    classes: int = 0
    unique_classes: int = 0
    scripts_files: int = 0
    asset_files: int = 0
    methods_failed: int = 0
    problems: list[dict] = field(default_factory=list)  # partial/failed/unsupported
    tool: dict = field(default_factory=dict)
    ffdec_error: str = ""
    interrupted: bool = False
    dry_run: bool = False
    manifest_path: Path | None = None
    report_path: Path | None = None
    catalog_path: Path | None = None
    asasm_selected: int = 0
    asasm_done: int = 0
    asasm_files: int = 0

    def to_report(self) -> dict:
        return {
            "tool": TOOL_NAME, "tool_version": __version__, "realm": self.realm, "started": self.started,
            "elapsed_s": round(self.elapsed, 2), "dry_run": self.dry_run, "interrupted": self.interrupted,
            "decompiler": self.tool or None, "decompiler_unavailable": self.ffdec_error or None,
            "counts": {"candidates": self.candidates, "selected": self.selected, "to_process": self.to_process,
                       "not_processed_due_to_limit": self.limited, "resumed_from_journal": self.resumed,
                       "processed": dict(self.processed), "unchanged": dict(self.unchanged),
                       "totals": dict(self.totals), "actionscript": dict(self.code),
                       "classes": self.classes, "unique_classes": self.unique_classes,
                       "script_files_now": self.scripts_files, "asset_files_now": self.asset_files,
                       "methods_not_decompiled_now": self.methods_failed,
                       "asasm_selected": self.asasm_selected, "asasm_done": self.asasm_done,
                       "asasm_files": self.asasm_files},
            "not_fully_recovered": self.problems[:MAX_LISTED],
        }


# ------------------------------------------------------------------ utilitarios

def catalog_rel(key: str) -> str:
    return f"{AS_DIR}/swf/{key}.json"


def scripts_rel(key: str) -> str:
    return f"{AS_DIR}/scripts/{key}"


def assets_rel(key: str) -> str:
    return f"{AS_DIR}/assets/{key}"


def outputs_of(rec: dict | None) -> list[str]:
    """Caminhos (relativos a wot_src_<R>) produzidos para um SWF."""
    a = (rec or {}).get("actionscript") or {}
    out = []
    if a.get("catalog"):
        out.append(a["catalog"])
    for k in ("scripts", "assets"):
        d = (a.get(k) or {}).get("dir")
        if d:
            out.append(d)
    return out


def remove_outputs(out_dir: Path, rec: dict | None) -> int:
    n = 0
    asasm = (((rec or {}).get("actionscript") or {}).get("asasm") or {}).get("dir")
    for rel in outputs_of(rec) + ([asasm] if asasm else []):
        target = resolve_within(out_dir, rel)
        if rel.endswith(".json"):
            n += remove_file(target)
        else:
            n += remove_tree(target)
    return n


def _walk_files(root: Path) -> list[Path]:
    files = []
    for dirpath, _, names in os.walk(long_path(root)):
        for n in names:
            files.append(Path(dirpath) / n)
    return files


def _expected_paths(classes: list[dict]) -> set[str]:
    return {c["name"].replace(".", "/") + ".as" for c in classes if not c.get("private")}


def case_collisions(classes: list[dict]) -> list[list[str]]:
    """Pacotes cujos nomes so diferem em maiusculas/minusculas (no Windows partilham uma pasta)."""
    groups: dict[str, set[str]] = {}
    for c in classes:
        if c.get("private") or "." not in c["name"]:
            continue
        pkg = c["name"].rsplit(".", 1)[0]
        groups.setdefault(pkg.lower(), set()).add(pkg)
    return sorted(sorted(v) for v in groups.values() if len(v) > 1)


def _scan_scripts(root: Path) -> tuple[set[str], int, int, int]:
    """(caminhos .as relativos, ficheiros, metodos nao descompilados, linhas sem estrutura)."""
    rels, failed, unstructured = set(), 0, 0
    base = long_path(root)
    files = _walk_files(root)
    for f in files:
        rel = os.path.relpath(str(f), base).replace("\\", "/")
        if not rel.endswith(".as"):
            continue
        rels.add(rel)
        try:
            text = Path(f).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        failed += text.count(ffdec_mod.FAIL_MARKER)
        unstructured += sum(1 for line in text.splitlines() if ffdec_mod.UNSTRUCTURED_MARKER in line)
    return rels, len(files), failed, unstructured


MOVE_ATTEMPTS = 6


def _move_dir(src: Path, dest: Path) -> None:
    """Move uma pasta; tolera bloqueios temporarios do Windows (antivirus/indexacao) com novas tentativas
    e, por fim, copia e apaga."""
    remove_tree(dest)
    os.makedirs(long_path(dest.parent), exist_ok=True)
    for attempt in range(MOVE_ATTEMPTS):
        try:
            os.replace(long_path(src), long_path(dest))
            return
        except PermissionError:
            if attempt == MOVE_ATTEMPTS - 1:
                break
            time.sleep(0.25 * 2 ** attempt)
    remove_tree(dest)
    shutil.copytree(long_path(src), long_path(dest))
    remove_tree(src)


def _header_for_decl(key: str) -> str:
    return f"sources/{key}"


# ------------------------------------------------------------------ um SWF

def code_weight(out_dir: Path, key: str) -> int:
    """Bytes de ABC do SWF (sem ler o bytecode): estimativa do custo no FFDec. 0 se ilegivel."""
    try:
        with open(long_path(resolve_within(out_dir / "sources", key)), "rb") as fh:
            data = fh.read()
        swf_bytes, _ = swf_from_container(data, key)
        info, _ = parse_swf(swf_bytes, with_abc=False)
    except (OSError, SwfError, ValueError, IndexError, MemoryError):
        return 0
    return sum(b.get("size", 0) for b in info.abc)


def process_swf(key: str, rec: dict, out_dir: Path, opts: ASOptions, ff: FFDec | None, slot: int) -> dict:
    """Executado numa thread. Devolve o novo registo "actionscript"."""
    t0 = time.perf_counter()
    res: dict = {"input_sha256": rec.get("sha256"), "parser": [SWF_PARSER_VERSION, ABC_VERSION]}
    src = resolve_within(out_dir / "sources", key)
    try:
        with open(long_path(src), "rb") as fh:
            data = fh.read()
    except OSError as exc:
        return {**res, "status": "failed", "error": f"leitura do SWF extraido: {exc}"}
    if rec.get("sha256") and hashlib.sha256(data).hexdigest() != rec["sha256"]:
        return {**res, "status": "failed", "error": "o SWF em sources/ nao corresponde ao manifesto (corra 'extract')"}
    try:
        swf_bytes, inner = swf_from_container(data, key)
        info, _ = parse_swf(swf_bytes)
    except (SwfError, ValueError, IndexError, MemoryError) as exc:
        return {**res, "status": "failed", "error": f"{type(exc).__name__}: {exc}",
                "elapsed": round(time.perf_counter() - t0, 2)}

    catalog = info.to_dict()
    catalog = {"source": f"sources/{key}", "container_member": inner, **catalog}
    write_atomic(resolve_within(out_dir, catalog_rel(key)),
                 json.dumps(catalog, ensure_ascii=False, indent=1).encode("utf-8"))
    res.update(catalog=catalog_rel(key), code=info.code_kind, version=info.version,
               compression=info.compression, classes=len(info.classes))
    problems: list[str] = []
    if info.errors:
        problems.append(f"{len(info.errors)} componente(s) ilegivel(eis): {info.errors[0]}")

    swf_path = src
    tmp_root = out_dir / ".state" / "as_tmp" / f"w{slot}"
    remove_tree(tmp_root)
    if inner:  # .swc: o FFDec recebe o library.swf
        swf_path = tmp_root / "library.swf"
        write_atomic(swf_path, swf_bytes)

    want_scripts = info.code_kind != "none"
    want_assets = opts.assets and (info.images or info.fonts or info.sounds or info.binary_data
                                   or info.symbol_classes)
    scripts: dict = {}
    assets: dict = {}
    if ff is not None and (want_scripts or want_assets):
        items = ",".join(([ffdec_mod.ITEMS_SCRIPTS] if want_scripts else [])
                         + ([ffdec_mod.ITEMS_ASSETS] if want_assets else []))
        tmp_out = tmp_root / "out"
        run = ffdec_mod.export(ff, swf_path, tmp_out, items, opts.timeout, opts.method_timeout, opts.class_timeout)
        ffdec_err = ""
        if run.out_of_memory:
            ffdec_err = ("o Java ficou sem memoria (reduza -j/--heavy-jobs ou aumente java_heap): "
                         f"{run.log_tail[-200:]}")
        elif run.timed_out:
            ffdec_err = f"FFDec excedeu o tempo limite de {opts.timeout:.0f} s"
        elif run.returncode != 0:
            ffdec_err = f"FFDec terminou com o codigo {run.returncode}: {run.log_tail[-300:]}"
        if want_scripts:
            sdir = tmp_out / "scripts"
            if sdir.is_dir() and not run.timed_out:
                rels, nfiles, failed, unstructured = _scan_scripts(sdir)
                # NTFS nao distingue maiusculas: pacotes como net.wg.data.VO e net.wg.data.vo partilham a
                # mesma pasta, por isso a comparacao com o que o FFDec escreveu ignora a caixa
                found = {r.lower() for r in rels}
                missing = (sorted(p for p in _expected_paths(info.classes) if p.lower() not in found)
                           if info.code_kind == "as3" else [])
                _move_dir(sdir, resolve_within(out_dir, scripts_rel(key)))
                scripts = {"tool": ff.label(), "kind": "decompiled", "dir": scripts_rel(key), "files": nfiles,
                           "methods_not_decompiled": failed, "unstructured_lines": unstructured,
                           "missing_classes": len(missing)}
                collisions = case_collisions(info.classes)
                if collisions:
                    scripts["case_collisions"] = collisions
                if missing:
                    scripts["missing_examples"] = missing[:10]
                    # as classes que o FFDec nao exportou ficam com as declaracoes do ABC
                    decl = _write_declarations(key, swf_bytes, out_dir, only=set(missing))
                    scripts["declarations_for_missing"] = decl.get("files", 0)
                    problems.append(f"{len(missing)} classe(s) sem ficheiro exportado pelo FFDec "
                                    f"({decl.get('files', 0)} com so declaracoes)")
                if failed:
                    problems.append(f"{failed} metodo(s) nao descompilado(s) pelo FFDec")
                if unstructured:
                    problems.append(f"{unstructured} linha(s) com fluxo nao reconstruido (§§)")
                if ffdec_err:
                    problems.append(ffdec_err)
            else:
                problems.append(ffdec_err or "o FFDec nao exportou scripts")
        if want_assets:
            moved = Counter()
            dest_root = resolve_within(out_dir, assets_rel(key))
            remove_tree(dest_root)
            for sub in ("images", "fonts", "binaryData", "sounds", "symbolClass"):
                d = tmp_out / sub
                if d.is_dir():
                    n = len(_walk_files(d))
                    if n:
                        _move_dir(d, dest_root / sub)
                        moved[sub] = n
            if moved:
                assets = {"tool": ff.label(), "dir": assets_rel(key), "files": sum(moved.values()), **moved}
            elif not ffdec_err:
                assets = {"tool": ff.label(), "files": 0}
            if ffdec_err and not want_scripts:
                problems.append(ffdec_err)

    if want_scripts and not scripts:
        # sem FFDec (ou falhou): declaracoes AS3 a partir do bytecode, sem corpos
        if info.code_kind == "as3":
            scripts = _write_declarations(key, swf_bytes, out_dir)
            if scripts.get("error"):
                problems.append(scripts["error"])
            elif ff is not None:
                problems.append("so declaracoes (o FFDec falhou)")
        elif info.code_kind == "as2":
            scripts = {"kind": "none", "note": "codigo AS1/2 sem descompilador disponivel"}
    remove_tree(tmp_root)

    if info.code_kind == "none":
        status = "partial" if problems else "extracted"
    elif info.code_kind == "as2" and not scripts.get("dir"):
        status = "unsupported"
    elif scripts.get("kind") == "declarations":
        status = "partial"
        problems.insert(0, "corpos dos metodos nao descompilados (so declaracoes)")
    else:
        status = "partial" if problems else "success"
    res.update(status=status, scripts=scripts or None, assets=assets or None,
               elapsed=round(time.perf_counter() - t0, 2))
    if problems:
        res["error"] = "; ".join(problems)
    return {k: v for k, v in res.items() if v is not None}


def _write_declarations(key: str, swf_bytes: bytes, out_dir: Path, only: set[str] | None = None) -> dict:
    """Declaracoes AS3 de todas as classes (substitui a pasta) ou so das de `only` (caminhos .as)."""
    try:
        _, abcs = parse_swf(swf_bytes, keep_abc=True)
    except (SwfError, ValueError, IndexError) as exc:
        return {"kind": "declarations", "error": f"declaracoes: {exc}"}
    dest = resolve_within(out_dir, scripts_rel(key))
    if only is None:
        remove_tree(dest)
    n = 0
    seen: set[str] = set()
    for _, abc in abcs:
        for i in range(len(abc.classes)):
            name, text = class_declaration(abc, i, f"sources/{key}")
            rel = name.replace(".", "/") + ".as"
            if rel.lower() in seen or (only is not None and rel not in only):  # repetida (ou noutra caixa)
                continue
            seen.add(rel.lower())
            target = resolve_within(dest, rel)
            if only is not None and os.path.exists(long_path(target)):
                continue  # nunca substituir codigo exportado pelo FFDec (ex.: mesma pasta noutra caixa)
            write_atomic(target, text.encode("utf-8"))
            n += 1
    return {"tool": f"{TOOL_NAME} {__version__} (declaracoes ABC)", "kind": "declarations",
            "dir": scripts_rel(key), "files": n}


# ------------------------------------------------------------------ execucao

def _selected(rec: dict, key: str, opts: ASOptions) -> bool:
    if rec.get("category") != "scaleform" or rec.get("status") not in OK_ENTRY:
        return False
    if opts.trees and rec.get("tree") not in opts.trees:
        return False
    if opts.globs:
        v = rec.get("virtual", "")
        return any(fnmatch.fnmatchcase(v, g) or fnmatch.fnmatchcase(key, g) for g in opts.globs)
    return True


def _tool_sig(ff: FFDec | None, opts: ASOptions) -> str:
    return f"swf{SWF_PARSER_VERSION}/abc{ABC_VERSION}/{ff.label() if ff else 'sem-ffdec'}/assets={int(opts.assets)}"


def _reusable(prev: dict | None, rec: dict, out_dir: Path, sig: str, opts: ASOptions) -> bool:
    if opts.force or not prev or prev.get("status") not in RANK:
        return False
    if prev.get("input_sha256") != rec.get("sha256"):
        return False
    for rel in outputs_of({"actionscript": prev}):
        if not os.path.exists(long_path(out_dir / rel)):
            return False
    if prev.get("tool_sig") != sig:
        return False
    if prev["status"] in ("success", "extracted"):
        return True
    return not opts.retry


def run_actionscript(cfg: Config, realm: str, options: ASOptions | None = None, progress=None,
                     ff: FFDec | None = None, ff_error: str = "") -> ASResult:
    opts = options or ASOptions()
    t0 = time.perf_counter()
    out_dir = cfg.realm_output_dir(realm)
    manifest_path = out_dir / "manifest.json"
    res = ASResult(realm=realm, out_dir=out_dir, dry_run=opts.dry_run,
                   started=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    if not manifest_path.is_file():
        raise ManifestError(f"{manifest_path} nao existe: corra primeiro 'extract --realm {realm}'")
    if not opts.use_ffdec:
        ff = None
    res.tool = ff.to_dict() if ff else {}
    res.ffdec_error = "" if ff else (ff_error or "FFDec desativado (--no-ffdec)")
    if opts.dry_run:
        return _run(cfg, realm, opts, res, ff, manifest_path, progress, t0)
    with StateLock(out_dir):
        return _run(cfg, realm, opts, res, ff, manifest_path, progress, t0)


def _run(cfg, realm, opts, res, ff, manifest_path, progress, t0) -> ASResult:
    out_dir = res.out_dir
    manifest = load_manifest(manifest_path)
    if manifest.get("realm") != realm:
        raise ManifestError(f"{manifest_path} pertence ao realm {manifest.get('realm')}, nao a {realm}")
    entries: dict[str, dict] = manifest["entries"]
    state_dir = out_dir / ".state"
    journal = Journal(state_dir / JOURNAL_NAME)
    resumed = {k: r.get("actionscript") for k, r in journal.load().items() if r.get("actionscript")}
    res.resumed = len(resumed)
    sig = _tool_sig(ff, opts)

    results: dict[str, dict] = {}
    todo: list[str] = []
    for key, rec in entries.items():
        if rec.get("category") == "scaleform" and rec.get("status") in OK_ENTRY:
            res.candidates += 1
        if not _selected(rec, key, opts):
            continue
        res.selected += 1
        prev = resumed.get(key) or rec.get("actionscript")
        if _reusable(prev, rec, out_dir, sig, opts) or (
                rec.get("cleaned") and prev and prev.get("input_sha256") == rec.get("sha256")):
            res.unchanged[prev["status"]] += 1
            results[key] = prev
            continue
        todo.append(key)
    if opts.limit and len(todo) > opts.limit:
        res.limited = len(todo) - opts.limit
        todo = sorted(todo)[:opts.limit]
    res.to_process = len(todo)
    if opts.dry_run:
        res.elapsed = time.perf_counter() - t0
        return res

    # os que tem mais codigo primeiro (sao os que demoram), com um limite de pesados em simultaneo
    with ThreadPoolExecutor(max_workers=max(1, opts.jobs)) as ex:
        weight = dict(zip(todo, ex.map(lambda k: code_weight(out_dir, k), todo)))
    todo.sort(key=lambda k: (-weight[k], -(entries[k].get("size") or 0)))
    heavy = {k for k in todo if weight[k] >= opts.heavy_abc_bytes}
    heavy_limit = max(1, opts.heavy_jobs)

    (out_dir / AS_DIR).mkdir(parents=True, exist_ok=True)
    free_slots = list(range(max(1, opts.jobs)))
    done = 0

    def job(key: str, slot: int) -> tuple[str, int, dict]:
        rec = entries[key]
        prev = resumed.get(key) or rec.get("actionscript")
        try:
            if prev:  # resultados antigos (outra versao do SWF ou das ferramentas)
                remove_outputs(out_dir, {"actionscript": prev})
            new = process_swf(key, rec, out_dir, opts, ff, slot)
        except Exception as exc:  # regista e continua
            new = {"status": "failed", "input_sha256": rec.get("sha256"), "error": f"{type(exc).__name__}: {exc}"}
        new["tool_sig"] = sig
        return key, slot, new

    try:
        with ThreadPoolExecutor(max_workers=max(1, opts.jobs), thread_name_prefix="actionscript") as ex:
            inflight = set()
            pending = list(todo)
            running_heavy = 0
            try:
                while True:
                    while free_slots and pending:
                        pick = next((i for i, k in enumerate(pending)
                                     if k not in heavy or running_heavy < heavy_limit), None)
                        if pick is None:  # so restam pesados e o limite foi atingido
                            break
                        key = pending.pop(pick)
                        running_heavy += key in heavy
                        inflight.add(ex.submit(job, key, free_slots.pop()))
                    if not inflight:
                        break
                    finished, inflight = wait(inflight, return_when=FIRST_COMPLETED)
                    for f in finished:
                        key, slot, new = f.result()
                        running_heavy -= key in heavy
                        free_slots.append(slot)
                        results[key] = new
                        journal.write({"key": key, "actionscript": new})
                        res.processed[new["status"]] += 1
                        res.scripts_files += (new.get("scripts") or {}).get("files", 0)
                        res.asset_files += (new.get("assets") or {}).get("files", 0)
                        res.methods_failed += (new.get("scripts") or {}).get("methods_not_decompiled", 0)
                        done += 1
                    if progress:
                        progress(done, len(todo), res.processed)
            except KeyboardInterrupt:
                res.interrupted = True
                for f in inflight:
                    f.cancel()
                ex.shutdown(wait=True, cancel_futures=True)
    finally:
        journal.close()
    if res.interrupted:
        res.elapsed = time.perf_counter() - t0
        return res

    for key, a in sorted(results.items()):
        res.totals[a["status"]] += 1
        if a.get("code"):
            res.code[a["code"]] += 1
        res.classes += a.get("classes", 0)
        if a["status"] in ("partial", "failed", "unsupported"):
            res.problems.append({"key": key, "status": a["status"], "error": a.get("error", "")})
        entries[key]["actionscript"] = a

    if opts.asasm != "none" and opts.rabc is not None:
        _asasm_pass(out_dir, entries, results.keys(), opts, res)
    res.catalog_path, res.unique_classes = _write_index(out_dir, entries)
    overall = Counter()
    for rec in entries.values():
        if rec.get("category") == "scaleform" and rec.get("status") in OK_ENTRY:
            overall[(rec.get("actionscript") or {}).get("status", "not_processed")] += 1
    now = datetime.now(timezone.utc)
    manifest["actionscript"] = {"date": now.isoformat(timespec="seconds"), "decompiler": res.tool or None,
                                "tool_sig": sig, "counts": dict(overall)}
    manifest.setdefault("tool_versions", {})["actionscript"] = sig
    write_atomic(state_dir / "manifest.prev.json", manifest_path.read_bytes())
    save_json_atomic(manifest_path, manifest, indent=None)
    res.manifest_path = manifest_path
    res.elapsed = time.perf_counter() - t0
    report = res.to_report()
    report["manifest_counts"] = dict(overall)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    save_json_atomic(state_dir / "reports" / f"actionscript_{stamp}.json", report)
    save_json_atomic(out_dir / "actionscript_report.json", report)
    res.report_path = out_dir / "actionscript_report.json"
    journal.remove()
    remove_tree(state_dir / "as_tmp")
    return res


def _write_index(out_dir: Path, entries: dict) -> tuple[Path, int]:
    """sources_as/catalog.json: SWF -> resumo e classe -> SWF(s) que a definem."""
    swfs: dict[str, dict] = {}
    class_index: dict[str, list[str]] = {}
    for key, rec in sorted(entries.items()):
        a = rec.get("actionscript")
        if not a or rec.get("status") not in OK_ENTRY or not a.get("catalog"):
            continue
        try:
            cat = json.loads(Path(long_path(out_dir / a["catalog"])).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        swfs[key] = {"status": a["status"], "actionscript": cat.get("actionscript"),
                     "classes": len(cat.get("classes", [])),
                     "imports": [i["url"] for i in cat.get("imports", [])],
                     "exports": len(cat.get("exports", [])), "scripts": (a.get("scripts") or {}).get("dir"),
                     "assets": (a.get("assets") or {}).get("dir")}
        for c in cat.get("classes", []):
            lst = class_index.setdefault(c["name"], [])
            if key not in lst:
                lst.append(key)
    path = out_dir / AS_DIR / "catalog.json"
    save_json_atomic(path, {"swf": swfs, "classes": dict(sorted(class_index.items()))})
    return path, len(class_index)


# ------------------------------------------------------------------ RABCDAsm (.asasm)

ASASM_SIG = "rabc1"


def asasm_rel(key: str) -> str:
    return f"{AS_DIR}/asasm/{key}"


def _wants_asasm(a: dict, mode: str) -> bool:
    if a.get("code") != "as3" or a.get("status") not in ("success", "partial"):
        return False
    return mode == "all" or (mode == "partial" and a["status"] == "partial")


def _unstructured_map(out_dir: Path, a: dict, asasm_root: Path) -> list[dict]:
    """Ficheiros .as com linhas §§ e o .class.asasm correspondente (o RABCDAsm pode renomear pastas, ex.: vo_)."""
    sdir = (a.get("scripts") or {}).get("dir")
    if not sdir or not (a.get("scripts") or {}).get("unstructured_lines"):
        return []
    root = out_dir / sdir
    by_name: dict[str, list[str]] = {}
    base = long_path(asasm_root)
    for dirpath, _, names in os.walk(base):
        for n in names:
            if n.endswith(".class.asasm"):
                by_name.setdefault(n, []).append(os.path.relpath(os.path.join(dirpath, n), base).replace("\\", "/"))
    out = []
    for f in _walk_files(root):
        try:
            text = Path(f).read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        if ffdec_mod.UNSTRUCTURED_MARKER not in text:
            continue
        rel = os.path.relpath(str(f), long_path(root)).replace("\\", "/")
        cands = by_name.get(rel.rsplit("/", 1)[-1][:-3] + ".class.asasm", [])
        want = rel[:-3].lower()
        best = next((c for c in cands if c.split("/", 1)[-1][: -len(".class.asasm")].lower().replace("_/", "/") == want),
                    cands[0] if cands else None)
        out.append({"as": f"{sdir}/{rel}", "asasm": f"{asasm_rel_from(asasm_root, out_dir)}/{best}" if best else None,
                    "lines": sum(1 for line in text.splitlines() if ffdec_mod.UNSTRUCTURED_MARKER in line)})
        if len(out) >= 50:
            break
    return out


def asasm_rel_from(asasm_root: Path, out_dir: Path) -> str:
    return os.path.relpath(str(asasm_root), str(out_dir)).replace("\\", "/")


def _asasm_pass(out_dir: Path, entries: dict, keys, opts: "ASOptions", res: "ASResult") -> None:
    rabc = opts.rabc
    todo = []
    for key in sorted(keys):
        a = entries[key].get("actionscript") or {}
        if not _wants_asasm(a, opts.asasm) or entries[key].get("cleaned"):
            continue
        prev = a.get("asasm") or {}
        if not opts.force and prev.get("sig") == ASASM_SIG and prev.get("input_sha256") == a.get("input_sha256") and (
                prev.get("error") or (prev.get("dir") and os.path.exists(long_path(out_dir / prev["dir"])))):
            continue
        todo.append(key)
    res.asasm_selected = len(todo)
    if not todo:
        return
    free = list(range(max(1, opts.jobs)))
    import threading
    lock = threading.Lock()

    def one(key: str) -> tuple[str, dict]:
        with lock:
            slot = free.pop()
        try:
            a = entries[key]["actionscript"]
            try:
                with open(long_path(resolve_within(out_dir / "sources", key)), "rb") as fh:
                    data = fh.read()
                swf_bytes, _ = swf_from_container(data, key)
            except (OSError, SwfError, ValueError) as exc:
                return key, {"sig": ASASM_SIG, "input_sha256": a.get("input_sha256"), "error": f"leitura: {exc}"}
            work = out_dir / ".state" / "as_tmp" / f"rabc{slot}"
            dirs, err, secs = rabcdasm_mod.disassemble(rabc, swf_bytes, work, opts.timeout)
            dest = resolve_within(out_dir, asasm_rel(key))
            remove_tree(dest)
            files = 0
            for d in dirs:
                files += len(_walk_files(d))
                _move_dir(d, dest / d.name)
            remove_tree(work)
            rec = {"sig": ASASM_SIG, "tool": rabc.label(), "input_sha256": a.get("input_sha256"),
                   "elapsed": round(secs, 1)}
            if dirs:
                rec.update(dir=asasm_rel(key), blocks=len(dirs), files=files)
                um = _unstructured_map(out_dir, a, dest)
                if um:
                    rec["unstructured"] = um
            if err:
                rec["error"] = err
            return key, rec
        finally:
            with lock:
                free.append(slot)

    with ThreadPoolExecutor(max_workers=max(1, opts.jobs), thread_name_prefix="rabcdasm") as ex:
        for key, rec in ex.map(one, todo):
            entries[key]["actionscript"]["asasm"] = rec
            if rec.get("dir"):
                res.asasm_done += 1
                res.asasm_files += rec.get("files", 0)
            if rec.get("error"):
                res.problems.append({"key": key, "status": "asasm", "error": rec["error"]})
