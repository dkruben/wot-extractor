"""Comando `purge`: retirar de uma arvore wot_src_<R> conteudo que nao e do jogo (por omissao a arvore `mods`).

Para cada entrada selecionada (arvore e/ou padrao): apaga o ficheiro em sources/ e TODAS as saidas derivadas
(XML descodificado, .py descompilado, catalogo/codigo/recursos/.asasm do actionscript, copias e analises do
gameface, stub .pyi e caches), retira-a do manifesto e regista a exclusao nos filtros do manifesto, para que o
`update` (que reutiliza esses filtros) nao a volte a extrair. A instalacao do jogo nunca e tocada: o conteudo
pode ser recuperado com `extract --tree <arvore>`.
"""

from __future__ import annotations

import fnmatch
import os
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from ..config import Config
from ..extract.manifest import ManifestError, StateLock, load_manifest
from ..extract.plan import TREES
from ..extract.writer import long_path, remove_file, remove_tree, save_json_atomic, write_atomic
from ..safety import resolve_within

DERIVED_ROOTS = ("sources", "sources_xml", "sources_as/swf", "sources_as/scripts", "sources_as/assets",
                 "sources_as/asasm", "sources_gameface/js", "sources_gameface/css", "sources_gameface/html",
                 "sources_gameface/manifests/files", ".state/stubs_desc")


@dataclass
class PurgeResult:
    realm: str
    selected: int = 0
    removed_files: int = 0
    by_tree: dict = field(default_factory=dict)
    keys: list[str] = field(default_factory=list)
    unshadowed: int = 0
    dry_run: bool = False
    report_path: Path | None = None


def _rm(out_dir: Path, rel: str | None) -> int:
    if not rel:
        return 0
    try:
        target = resolve_within(out_dir, rel)
    except ValueError:
        return 0
    if os.path.isdir(long_path(target)):
        return 1 if remove_tree(target) else 0
    return 1 if remove_file(target) else 0


def _prune_empty_dirs(root: Path) -> None:
    base = long_path(root)
    if not os.path.isdir(base):
        return
    for dirpath, dirnames, filenames in os.walk(base, topdown=False):
        if dirpath != base and not os.listdir(dirpath):
            try:
                os.rmdir(dirpath)
            except OSError:
                pass


def run_purge(cfg: Config, realm: str, trees: tuple[str, ...] = ("mods",), globs: tuple[str, ...] = (),
              dry_run: bool = False) -> PurgeResult:
    out_dir = cfg.realm_output_dir(realm)
    mpath = out_dir / "manifest.json"
    if not mpath.is_file():
        raise ManifestError(f"{mpath} nao existe")
    res = PurgeResult(realm=realm, dry_run=dry_run)
    with StateLock(out_dir):
        m = load_manifest(mpath)
        entries: dict[str, dict] = m["entries"]
        keys = sorted(k for k, r in entries.items()
                      if r.get("tree") in trees or any(fnmatch.fnmatchcase(k, g) for g in globs))
        res.selected = len(keys)
        res.keys = keys
        for k in keys:
            t = entries[k].get("tree")
            res.by_tree[t] = res.by_tree.get(t, 0) + 1
        if dry_run:
            return res
        for k in keys:
            r = entries[k]
            n = _rm(out_dir, f"sources/{k}")
            n += _rm(out_dir, (r.get("decoded") or {}).get("path"))
            n += _rm(out_dir, (r.get("decompiled") or {}).get("output"))
            a = r.get("actionscript") or {}
            for rel in [a.get("catalog"), (a.get("scripts") or {}).get("dir"), (a.get("assets") or {}).get("dir"),
                        (a.get("asasm") or {}).get("dir")]:
                n += _rm(out_dir, rel)
            g = r.get("gameface") or {}
            n += _rm(out_dir, g.get("formatted")) + _rm(out_dir, g.get("analysis"))
            s = r.get("stubs") or {}
            n += _rm(out_dir, s.get("output"))
            n += _rm(out_dir, f".state/stubs_desc/{k}.json")
            res.removed_files += n
            del entries[k]
        # ficheiros de res que estavam "sobrepostos" pelo que foi retirado voltam a ser os efetivos
        res.unshadowed = 0
        for r in entries.values():
            ob = r.get("overridden_by")
            if ob:
                keep = [x for x in ob if x.split(":", 1)[0] not in trees]
                if len(keep) != len(ob):
                    res.unshadowed += 1
                    if keep:
                        r["overridden_by"] = keep
                    else:
                        del r["overridden_by"]
        for root in DERIVED_ROOTS:
            for t in trees:
                _prune_empty_dirs(out_dir / root / t)
                if os.path.isdir(long_path(out_dir / root / t)) and not os.listdir(long_path(out_dir / root / t)):
                    os.rmdir(long_path(out_dir / root / t))
        _prune_empty_dirs(out_dir / "__stubs")
        filters = m.setdefault("filters", {})
        current = filters.get("trees") or list(TREES)
        filters["trees"] = sorted(t for t in current if t not in trees)
        now = datetime.now(timezone.utc).isoformat(timespec="seconds")
        m.setdefault("purged", []).append({"date": now, "trees": list(trees), "globs": list(globs),
                                           "entries": len(keys)})
        counts = m.get("counts") or {}
        counts["entries"] = len(entries)
        write_atomic(out_dir / ".state" / "manifest.prev.json", mpath.read_bytes())
        save_json_atomic(mpath, m, indent=None)
        report = {"realm": realm, "date": now, "trees": list(trees), "globs": list(globs), "entries_removed": len(keys),
                  "by_tree": res.by_tree, "outputs_removed": res.removed_files, "res_unshadowed": res.unshadowed,
                  "keys": keys[:2000],
                  "note": "A instalacao do jogo nao foi tocada; recuperavel com extract --tree <arvore>."}
        stamp = now.replace(":", "").replace("-", "").replace("+0000", "Z")
        save_json_atomic(out_dir / ".state" / "reports" / f"purge_{stamp}.json", report)
        save_json_atomic(out_dir / "purge_report.json", report)
        res.report_path = out_dir / "purge_report.json"
    return res
