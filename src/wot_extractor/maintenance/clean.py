"""Comando `clean`: depois da extracao e das fases, apaga de sources/ o que ja tem uma forma processada.

  pyc    .pyc com descompilacao `success` e o .py presente (os partial/failed ficam: sao precisos para nova
         tentativa e para os stubs pelo bytecode)
  xml    XML BigWorld binarios com a copia legivel em sources_xml/ (descodificacao `success`)
  swf    .swf/.swc com estado `success`/`extracted` no actionscript e o catalogo presente (os partial ficam:
         sao precisos para --retry e para o RABCDAsm)
  state  ficheiros de trabalho em .state/: tentativas de descompilacao, temporarios do actionscript, cache do
         indice Python do gameface, ficheiros .tmp e relatorios antigos (ficam os 3 mais recentes de cada tipo).
         As descricoes dos stubs (.state/stubs_desc) ficam: sao a fonte do indice de APIs e da comparacao.

Cada ficheiro apagado fica marcado no manifesto (`cleaned`: data, motivo, tamanho, SHA-256 continua no
registo): a extracao incremental considera-o inalterado enquanto a origem no jogo nao mudar (se mudar, e
extraido e processado de novo, e o `update` volta a limpa-lo no fim); a `verify` conta-o a parte. A
instalacao do jogo nunca e tocada.
"""

from __future__ import annotations

import os
import re
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from ..config import Config
from ..extract.manifest import ManifestError, StateLock, load_manifest
from ..extract.writer import long_path, remove_file, remove_tree, save_json_atomic, write_atomic

KINDS = ("pyc", "xml", "swf", "state")
OK_ENTRY = frozenset({"extracted", "unchanged"})
KEEP_REPORTS = 3
_REPORT = re.compile(r"^([a-z_]+?)_\d{8}T\d{6}Z\.json$")


@dataclass
class CleanResult:
    realm: str
    dry_run: bool = False
    removed: Counter = field(default_factory=Counter)
    freed: Counter = field(default_factory=Counter)
    kept: Counter = field(default_factory=Counter)  # nao limpos (ainda precisos)
    already: int = 0
    state_removed: int = 0
    state_freed: int = 0
    report_path: Path | None = None


def _exists(out_dir: Path, rel: str | None) -> bool:
    return bool(rel) and os.path.exists(long_path(out_dir / rel))


def _size_tree(p: Path) -> tuple[int, int]:
    n = b = 0
    if os.path.isfile(long_path(p)):
        return 1, os.path.getsize(long_path(p))
    for dirpath, _, names in os.walk(long_path(p)):
        for x in names:
            try:
                b += os.path.getsize(os.path.join(dirpath, x))
                n += 1
            except OSError:
                pass
    return n, b


def why_clean(rec: dict, out_dir: Path, kinds: set[str]) -> tuple[str | None, str | None]:
    """(tipo, motivo) se o ficheiro de sources/ ja nao for preciso; (tipo, None) se ainda for; (None, None) fora."""
    cat = rec.get("category")
    if cat == "python_bytecode" and "pyc" in kinds:
        d = rec.get("decompiled") or {}
        if d.get("status") == "success" and _exists(out_dir, d.get("output")):
            return "pyc", f"descompilado: {d['output']}"
        return "pyc", None
    if cat == "xml" and "xml" in kinds and rec.get("validation") == "packed":
        d = rec.get("decoded") or {}
        if d.get("status") == "success" and _exists(out_dir, d.get("path")):
            return "xml", f"descodificado: {d['path']}"
        return "xml", None
    if cat == "scaleform" and "swf" in kinds:
        a = rec.get("actionscript") or {}
        if a.get("status") in ("success", "extracted") and _exists(out_dir, a.get("catalog")):
            return "swf", f"processado: {a['catalog']}"
        return "swf", None
    return None, None


def run_clean(cfg: Config, realm: str, kinds: set[str] | None = None, dry_run: bool = False,
              keep_reports: int = KEEP_REPORTS) -> CleanResult:
    kinds = set(KINDS if kinds is None else kinds)
    out_dir = cfg.realm_output_dir(realm)
    mpath = out_dir / "manifest.json"
    if not mpath.is_file():
        raise ManifestError(f"{mpath} nao existe")
    res = CleanResult(realm=realm, dry_run=dry_run)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    with StateLock(out_dir):
        m = load_manifest(mpath)
        for key, rec in sorted(m["entries"].items()):
            if rec.get("status") not in OK_ENTRY:
                continue
            if rec.get("cleaned"):
                res.already += 1
                continue
            kind, reason = why_clean(rec, out_dir, kinds)
            if kind is None:
                continue
            if reason is None:
                res.kept[kind] += 1
                continue
            src = out_dir / "sources" / key
            size = rec.get("size") or 0
            if not dry_run:
                if not remove_file(src) and os.path.exists(long_path(src)):
                    continue
                rec["cleaned"] = {"date": now, "reason": reason, "size": rec.get("size")}
            res.removed[kind] += 1
            res.freed[kind] += size

        if "state" in kinds:
            st = out_dir / ".state"
            targets = [st / "decompile" / "attempts", st / "as_tmp", st / "gameface_pyindex.json"]
            targets += [p for p in st.glob("*.tmp")]
            reports = st / "reports"
            if reports.is_dir():
                groups: dict[str, list[Path]] = {}
                for p in reports.iterdir():
                    mm = _REPORT.match(p.name)
                    if mm:
                        groups.setdefault(mm.group(1), []).append(p)
                for items in groups.values():
                    targets += sorted(items, key=lambda p: p.name)[:-keep_reports] if len(items) > keep_reports else []
            for t in targets:
                if not os.path.exists(long_path(t)):
                    continue
                n, b = _size_tree(t)
                res.state_removed += n
                res.state_freed += b
                if not dry_run:
                    remove_tree(t) if os.path.isdir(long_path(t)) else remove_file(t)

        if dry_run:
            return res
        m["clean"] = {"date": now, "kinds": sorted(kinds), "removed": dict(res.removed), "freed": dict(res.freed),
                      "kept": dict(res.kept), "cleaned_total": sum(1 for r in m["entries"].values() if r.get("cleaned"))}
        write_atomic(out_dir / ".state" / "manifest.prev.json", mpath.read_bytes())
        save_json_atomic(mpath, m, indent=None)
        report = {"realm": realm, "date": now, "kinds": sorted(kinds), "removed": dict(res.removed),
                  "freed_bytes": dict(res.freed), "kept_still_needed": dict(res.kept), "already_clean": res.already,
                  "state_files_removed": res.state_removed, "state_bytes_freed": res.state_freed,
                  "note": "Os ficheiros apagados ficam marcados 'cleaned' no manifesto; a instalacao nao foi tocada."}
        save_json_atomic(out_dir / "clean_report.json", report)
        stamp = now.replace(":", "").replace("-", "").replace("+0000", "Z")
        save_json_atomic(out_dir / ".state" / "reports" / f"clean_{stamp}.json", report)
        res.report_path = out_dir / "clean_report.json"
    return res
