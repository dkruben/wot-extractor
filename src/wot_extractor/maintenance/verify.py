"""Comando `verify`: verifica, so com leitura, a arvore wot_src_<R> contra o manifesto e a instalacao.

  1. manifesto e .version_name coerentes;
  2. cada ficheiro extraido em sources/ existe e tem o tamanho e o SHA-256 do manifesto (--quick: so tamanho);
  3. saidas derivadas: .py descompilados e XML descodificados (SHA-256), catalogos/pastas do actionscript,
     copias/analises do gameface e stubs existem;
  4. ficheiros em sources/ que nenhum registo explica (orfaos);
  5. instalacao: versao instalada vs extraida e, por ficheiro, CRC/tamanho no .pkg/.wotmod (lidos do diretorio
     central do zip, sem descomprimir) ou tamanho/data dos ficheiros soltos -> diz se e preciso um `update`.

Nada e alterado: o resultado vai para verify_report.json (e .state/reports/verify_<data>.json).
"""

from __future__ import annotations

import hashlib
import os
import time
import zipfile
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .. import TOOL_NAME, __version__
from ..config import Config
from ..extract.manifest import ManifestError, load_manifest
from ..extract.writer import long_path, save_json_atomic

OK_ENTRY = frozenset({"extracted", "unchanged"})
MAX_LISTED = 500
CHUNK = 1 << 20


@dataclass
class VerifyOptions:
    quick: bool = False
    install: bool = True
    derived: bool = True
    orphans: bool = True
    jobs: int = 8


@dataclass
class VerifyResult:
    realm: str
    out_dir: Path
    started: str = ""
    elapsed: float = 0.0
    version_name: str | None = None
    version_file: str | None = None
    installed_version: str | None = None
    install_path: str | None = None
    consistent: bool | None = None
    checked: int = 0
    bytes_hashed: int = 0
    problems: dict[str, list] = field(default_factory=dict)  # tipo -> [itens]
    derived: Counter = field(default_factory=Counter)
    orphans: list[str] = field(default_factory=list)
    removed_kept: list[str] = field(default_factory=list)
    cleaned: int = 0  # apagados pelo `clean` (marcados no manifesto)  # removidos do jogo, ainda na arvore (sem --prune)
    install_checked: int = 0
    install_changed: list[dict] = field(default_factory=list)
    install_missing: list[str] = field(default_factory=list)
    install_error: str = ""
    report_path: Path | None = None

    def add(self, kind: str, item) -> None:
        self.problems.setdefault(kind, []).append(item)

    @property
    def integrity_ok(self) -> bool:
        return not self.problems and not self.orphans

    @property
    def update_needed(self) -> bool:
        return bool(self.install_changed or self.install_missing or (
            self.installed_version and self.version_name and self.installed_version != self.version_name))

    def to_report(self) -> dict:
        return {
            "tool": TOOL_NAME, "tool_version": __version__, "realm": self.realm, "started": self.started,
            "elapsed_s": round(self.elapsed, 2),
            "integrity_ok": self.integrity_ok, "update_needed": self.update_needed,
            "versions": {"manifest": self.version_name, "version_file": self.version_file,
                         "installed": self.installed_version, "install_path": self.install_path,
                         "manifest_consistent": self.consistent},
            "counts": {"files_checked": self.checked, "bytes_hashed": self.bytes_hashed,
                       "problems": {k: len(v) for k, v in self.problems.items()},
                       "derived_checked": dict(self.derived), "orphans": len(self.orphans),
                       "removed_from_game_kept": len(self.removed_kept), "cleaned": self.cleaned,
                       "install_checked": self.install_checked, "install_changed": len(self.install_changed),
                       "install_missing": len(self.install_missing)},
            "problems": {k: v[:MAX_LISTED] for k, v in self.problems.items()},
            "orphans": self.orphans[:MAX_LISTED],
            "removed_from_game_kept": self.removed_kept[:MAX_LISTED],
            "install_changed": self.install_changed[:MAX_LISTED],
            "install_missing": self.install_missing[:MAX_LISTED],
            "install_error": self.install_error or None,
        }


def _sha256(path: Path) -> tuple[str | None, int]:
    h = hashlib.sha256()
    n = 0
    try:
        with open(long_path(path), "rb") as fh:
            while True:
                b = fh.read(CHUNK)
                if not b:
                    break
                h.update(b)
                n += len(b)
    except OSError:
        return None, 0
    return h.hexdigest(), n


def _size(path: Path) -> int | None:
    try:
        return os.stat(long_path(path)).st_size
    except OSError:
        return None


def run_verify(cfg: Config, realm: str, options: VerifyOptions | None = None, install_path: Path | None = None,
               installed_version: str | None = None, progress=None) -> VerifyResult:
    opts = options or VerifyOptions()
    t0 = time.perf_counter()
    out_dir = cfg.realm_output_dir(realm)
    res = VerifyResult(realm=realm, out_dir=out_dir, started=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    manifest_path = out_dir / "manifest.json"
    if not manifest_path.is_file():
        raise ManifestError(f"{manifest_path} nao existe: corra primeiro 'extract --realm {realm}'")
    manifest = load_manifest(manifest_path)
    if manifest.get("realm") != realm:
        raise ManifestError(f"{manifest_path} pertence ao realm {manifest.get('realm')}, nao a {realm}")
    entries: dict[str, dict] = manifest["entries"]
    res.version_name = manifest.get("version_name")
    res.consistent = manifest.get("consistent")
    try:
        res.version_file = (out_dir / ".version_name").read_text(encoding="utf-8").strip()
    except OSError:
        res.version_file = None
    if res.version_file != res.version_name:
        res.add("version", {"error": f".version_name ({res.version_file}) diferente do manifesto ({res.version_name})"})
    if res.consistent is False:
        res.add("version", {"error": "a ultima extracao nao foi consistente (houve falhas)"})

    live = {k: r for k, r in entries.items() if r.get("status") in OK_ENTRY}
    res.cleaned = sum(1 for r in live.values() if r.get("cleaned"))

    # 2. ficheiros extraidos
    def check(item):
        key, rec = item
        path = out_dir / "sources" / key
        if rec.get("cleaned"):
            return key, None, None, 0
        size = _size(path)
        if size is None:
            return key, "missing", None, 0
        if rec.get("size") is not None and size != rec["size"]:
            return key, "size_mismatch", f"{size} != {rec['size']}", 0
        if opts.quick or not rec.get("sha256"):
            return key, None, None, 0
        digest, n = _sha256(path)
        if digest != rec["sha256"]:
            return key, "hash_mismatch", digest, n
        return key, None, None, n

    done = 0
    with ThreadPoolExecutor(max_workers=max(1, opts.jobs)) as ex:
        for key, kind, detail, n in ex.map(check, sorted(live.items()), chunksize=64):
            res.checked += 1
            res.bytes_hashed += n
            if kind:
                res.add(kind, {"key": key, "detail": detail} if detail else {"key": key})
            done += 1
            if progress and done % 500 == 0:
                progress(done, len(live), Counter({"verificados": done}))

    # 3. saidas derivadas
    expected_in_sources: set[str] = {f"sources/{k}" for k, r in live.items() if not r.get("cleaned")}
    for key, rec in entries.items():
        if rec.get("status") == "removed":  # removido do jogo mas mantido (extract sem --prune)
            expected_in_sources.add(f"sources/{key}")
            if os.path.exists(long_path(out_dir / "sources" / key)):
                res.removed_kept.append(key)
        elif rec.get("status") not in OK_ENTRY:
            continue
        out = (rec.get("decompiled") or {}).get("output")  # .py descompilados ao lado dos .pyc em sources/
        if out:
            expected_in_sources.add(out)
    if opts.derived:
        def derived(item):
            key, rec = item
            out = []
            d = rec.get("decompiled") or {}
            if d.get("output"):
                out.append(("decompiled", d["output"], d.get("sha256")))
            x = rec.get("decoded") or {}
            if x.get("path"):
                out.append(("decoded_xml", x["path"], x.get("sha256")))
            a = rec.get("actionscript") or {}
            for rel in [a.get("catalog")] + [(a.get(k) or {}).get("dir") for k in ("scripts", "assets")]:
                if rel:
                    out.append(("actionscript", rel, None))
            g = rec.get("gameface") or {}
            for k in ("formatted", "analysis"):
                if g.get(k):
                    out.append(("gameface", g[k], None))
            s = rec.get("stubs") or {}
            if s.get("output") and s.get("status") != "failed":
                out.append(("stubs", s["output"], None))
            results = []
            for kind, rel, digest in out:
                path = out_dir / rel
                if not os.path.exists(long_path(path)):
                    results.append((kind, {"key": key, "missing": rel}))
                    continue
                if digest and not opts.quick:
                    got, _ = _sha256(path)
                    if got != digest:
                        results.append((kind, {"key": key, "hash_mismatch": rel}))
                        continue
                results.append((kind, None))
            return results

        with ThreadPoolExecutor(max_workers=max(1, opts.jobs)) as ex:
            for results in ex.map(derived, sorted(live.items()), chunksize=64):
                for kind, problem in results:
                    res.derived[kind] += 1
                    if problem:
                        res.add(f"{kind}_output", problem)
        for rel in (manifest.get("stubs") or {}).get("outputs", []):
            if rel.endswith(".pyi") and not os.path.exists(long_path(out_dir / rel)):
                res.add("stubs_output", {"missing": rel})

    # 4. orfaos em sources/
    if opts.orphans:
        base = long_path(out_dir / "sources")
        for dirpath, _, names in os.walk(base):
            for n in names:
                rel = "sources/" + os.path.relpath(os.path.join(dirpath, n), base).replace("\\", "/")
                if rel not in expected_in_sources:
                    # .decompiled.py de tentativas antigas ou ficheiros postos a mao
                    res.orphans.append(rel)
        res.orphans.sort()

    # 5. instalacao
    if opts.install:
        _check_install(res, manifest, live, install_path, installed_version)
    res.install_path = res.install_path or manifest.get("install_path")

    res.elapsed = time.perf_counter() - t0
    report = res.to_report()
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    save_json_atomic(out_dir / ".state" / "reports" / f"verify_{stamp}.json", report)
    save_json_atomic(out_dir / "verify_report.json", report)
    res.report_path = out_dir / "verify_report.json"
    return res


def _check_install(res: VerifyResult, manifest: dict, live: dict, install_path: Path | None,
                   installed_version: str | None) -> None:
    root = Path(install_path or manifest.get("install_path") or "")
    res.install_path = str(root)
    res.installed_version = installed_version
    if not root or not root.is_dir():
        res.install_error = f"instalacao nao encontrada em {root}"
        return
    by_container: dict[str, list[tuple[str, dict]]] = {}
    for key, rec in live.items():
        if rec.get("container"):
            by_container.setdefault(rec["container"], []).append((key, rec))
    for container, items in sorted(by_container.items()):
        path = root / container
        zip_items = [(k, r) for k, r in items if r.get("source") == "zip"]
        file_items = [(k, r) for k, r in items if r.get("source") != "zip"]
        if zip_items:
            try:
                with zipfile.ZipFile(long_path(path), "r") as zf:  # so leitura do diretorio central
                    info = {i.filename: i for i in zf.infolist()}
            except (OSError, zipfile.BadZipFile) as exc:
                for k, _ in zip_items:
                    res.install_missing.append(k)
                res.install_error = res.install_error or f"{container}: {exc}"
                continue
            for k, r in zip_items:
                res.install_checked += 1
                i = info.get(r.get("member"))
                if i is None:
                    res.install_missing.append(k)
                elif (r.get("crc") is not None and i.CRC != r["crc"]) or i.file_size != r.get("size"):
                    res.install_changed.append({"key": k, "container": container})
        for k, r in file_items:
            res.install_checked += 1
            try:
                st = os.stat(long_path(path))
            except OSError:
                res.install_missing.append(k)
                continue
            if st.st_size != r.get("size") or (r.get("mtime_ns") and st.st_mtime_ns != r["mtime_ns"]):
                res.install_changed.append({"key": k, "container": container})
