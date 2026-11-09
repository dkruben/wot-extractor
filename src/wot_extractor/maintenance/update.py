"""Comando `update`: atualizacao incremental de um realm depois de uma atualizacao do jogo.

Ordem (cada passo e o comando normal, incremental e retomavel):
  1. detetar a versao instalada e comparar com a extraida (.version_name / manifesto);
  2. extract com os MESMOS filtros da extracao anterior (perfil, extensoes, pacotes, arvores);
  3. diferencas face ao manifesto anterior: novos, alterados, removidos;
  4. se a extracao foi consistente: decompile, actionscript, gameface, stubs e o indice de APIs (so o que mudou e
     reprocessado) e, no fim, clean (apaga de sources/ o que ja foi processado);
     se nao foi: para aqui (a versao nao avanca e nada e apagado);
  5. update_report.json (+ .state/reports/update_<data>.json); os relatorios anteriores sao preservados.
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from .. import TOOL_NAME, __version__
from ..extract.manifest import load_manifest
from ..extract.writer import save_json_atomic

OK_ENTRY = frozenset({"extracted", "unchanged"})
STEPS = ("extract", "decompile", "actionscript", "gameface", "stubs", "index", "clean")
MAX_LISTED = 500


def snapshot(manifest_path: Path) -> tuple[dict[str, str], dict]:
    """(chave -> sha256 das entradas validas, manifesto) ou ({}, {}) se ainda nao houver extracao."""
    if not manifest_path.is_file():
        return {}, {}
    m = load_manifest(manifest_path)
    return {k: r.get("sha256") for k, r in m["entries"].items() if r.get("status") in OK_ENTRY}, m


def diff(before: dict[str, str], after: dict[str, str]) -> dict[str, list[str]]:
    return {"new": sorted(k for k in after if k not in before),
            "changed": sorted(k for k in after if k in before and after[k] != before[k]),
            "removed": sorted(k for k in before if k not in after)}


def previous_filters(manifest: dict) -> dict:
    f = manifest.get("filters") or {}
    return {"profile": f.get("profile", "dev"), "extensions": f.get("extensions", []),
            "containers": f.get("containers", []), "trees": f.get("trees", [])}


def save_report(out_dir: Path, data: dict) -> Path:
    data = {"tool": TOOL_NAME, "tool_version": __version__, **data}
    for k in ("new", "changed", "removed"):
        if k in data.get("diff", {}):
            data["diff"][f"{k}_total"] = len(data["diff"][k])
            data["diff"][k] = data["diff"][k][:MAX_LISTED]
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    save_json_atomic(out_dir / ".state" / "reports" / f"update_{stamp}.json", data)
    save_json_atomic(out_dir / "update_report.json", data)
    return out_dir / "update_report.json"
