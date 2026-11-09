"""Orquestracao da detecao: recolhe candidatos, valida-os, identifica o realm
e escolhe uma instalacao por realm."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .. import TOOL_NAME, __version__
from ..config import Config
from ..constants import SUPPORTED_REALMS
from ..logutil import get_logger
from .install import ClientInstall, inspect_install
from .sources import (SOURCE_PRIORITY, Candidate, path_key, registry_candidates,
                      scan_candidates, wgc_candidates)

log = get_logger("detect")


@dataclass
class DetectionResult:
    selected: dict[str, ClientInstall | None] = field(default_factory=dict)
    installs: list[ClientInstall] = field(default_factory=list)     # todas as validas
    rejected: list[ClientInstall] = field(default_factory=list)     # candidatos invalidos
    errors: dict[str, str] = field(default_factory=dict)            # por realm
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat(timespec="seconds"))

    @property
    def ok(self) -> bool:
        return all(v is not None for v in self.selected.values()) and not self.errors

    def to_dict(self) -> dict:
        sel_keys = {path_key(i.path) for i in self.selected.values() if i}
        return {
            "tool": TOOL_NAME,
            "tool_version": __version__,
            "timestamp": self.timestamp,
            "selected": {r: (i.to_dict() if i else None) for r, i in self.selected.items()},
            "other_installs": [i.to_dict(include_probes=False) for i in self.installs if path_key(i.path) not in sel_keys],
            "rejected_candidates": [{"path": str(i.path), "sources": i.sources, "issues": i.issues} for i in self.rejected],
            "errors": dict(self.errors),
        }


def gather_candidates(cfg: Config, overrides: dict[str, Path] | None = None,
                      use_system: bool = True) -> list[Candidate]:
    cands: list[Candidate] = []
    for realm, path in (overrides or {}).items():
        cands.append(Candidate(Path(path), "cli", realm))
    for realm, rc in cfg.realms.items():
        if rc.install:
            cands.append(Candidate(rc.install, "config", realm))
    if use_system:
        cands += wgc_candidates()
        cands += registry_candidates()
        if cfg.scan_drives:
            cands += scan_candidates(depth=cfg.scan_depth)
    return cands


def _rank(inst: ClientInstall, preferred_drive: str) -> tuple:
    drive = inst.path.drive.upper()
    best_source = min((SOURCE_PRIORITY.get(s.split(":")[0], 9) for s in inst.sources), default=9)
    vt = inst.version.number_tuple if inst.version else ()
    build = (inst.version.build or 0) if inst.version else 0
    # menor = melhor
    return (0 if preferred_drive and drive == preferred_drive.upper() else 1,
            tuple(-x for x in vt), -build, best_source, str(inst.path).lower())


def detect(cfg: Config, realms: list[str] | None = None, overrides: dict[str, Path] | None = None,
           deep: bool = True, use_system: bool = True) -> DetectionResult:
    realms = [r.upper() for r in (realms or SUPPORTED_REALMS)]
    overrides = {k.upper(): Path(v) for k, v in (overrides or {}).items()}
    result = DetectionResult()

    # 1. candidatos (deduplicados por caminho; acumula fontes)
    by_key: dict[str, tuple[Path, list[str]]] = {}
    forced: dict[str, str] = {}  # realm -> path_key escolhido manualmente
    for c in gather_candidates(cfg, overrides, use_system):
        k = path_key(c.path)
        tag = f"{c.source}:{c.note}" if c.source in ("cli", "config") else c.source
        if k not in by_key:
            by_key[k] = (c.path, [])
        if tag not in by_key[k][1]:
            by_key[k][1].append(tag)
        if c.source in ("cli", "config"):
            realm = c.note.upper()
            # cli tem prioridade sobre config
            if realm not in forced or c.source == "cli":
                forced[realm] = k

    # 2. inspecao leve de cada candidato
    light: dict[str, ClientInstall] = {}
    for k, (p, srcs) in by_key.items():
        inst = inspect_install(p, srcs, deep=False)
        if inst.valid:
            light[k] = inst
        else:
            result.rejected.append(inst)
            log.info("Candidato rejeitado %s: %s", p, "; ".join(inst.issues))

    # 3. escolha por realm
    for realm in realms:
        rc = cfg.realm(realm)
        chosen_key: str | None = None
        if realm in forced:
            k = forced[realm]
            inst = light.get(k)
            if inst is None:
                result.errors[realm] = f"caminho configurado manualmente invalido: {by_key[k][0]}"
            elif inst.realm != realm:
                result.errors[realm] = f"o caminho configurado ({inst.path}) pertence ao realm {inst.realm}, nao a {realm}"
            else:
                chosen_key = k
        else:
            matches = [(k, i) for k, i in light.items() if i.realm == realm]
            if matches:
                matches.sort(key=lambda ki: _rank(ki[1], rc.preferred_drive))
                chosen_key = matches[0][0]
                if rc.preferred_drive and matches[0][1].path.drive.upper() != rc.preferred_drive.upper():
                    log.warning("%s: nenhuma instalacao no disco preferido %s; usada %s", realm, rc.preferred_drive, matches[0][1].path)
            else:
                result.errors[realm] = "nenhuma instalacao encontrada (configure o caminho manualmente)"
        result.selected[realm] = None
        if chosen_key is not None:
            p, srcs = by_key[chosen_key]
            full = inspect_install(p, srcs, deep=deep) if deep else light[chosen_key]
            if rc.preferred_drive and full.path.drive.upper() != rc.preferred_drive.upper():
                full.issues.append(f"instalacao fora do disco preferido ({rc.preferred_drive})")
            others = [i for k, i in light.items() if i.realm == realm and k != chosen_key]
            if others:
                full.issues.append("outras instalacoes do mesmo realm ignoradas: " + ", ".join(str(i.path) for i in others))
            result.selected[realm] = full

    sel_keys = {path_key(i.path) for i in result.selected.values() if i}
    result.installs = [result.selected[r] for r in realms if result.selected.get(r)]
    result.installs += [i for k, i in light.items() if k not in sel_keys]
    return result
