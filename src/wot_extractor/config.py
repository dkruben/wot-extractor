"""Carregamento da configuracao (TOML opcional + defaults)."""

from __future__ import annotations

import tomllib
from dataclasses import dataclass, field
from pathlib import Path

from .constants import DEFAULT_PREFERRED_DRIVE, SUPPORTED_REALMS

CONFIG_FILENAME = "wot_extractor.toml"


class ConfigError(Exception):
    pass


@dataclass
class RealmConfig:
    realm: str
    install: Path | None = None
    preferred_drive: str = ""


@dataclass
class Config:
    project_root: Path
    output_root: Path
    scan_drives: bool = True
    scan_depth: int = 2
    realms: dict[str, RealmConfig] = field(default_factory=dict)
    python27: Path | None = None  # interpretador para descompilar/validar bytecode 2.7
    python3: Path | None = None  # interpretador do descompilador alternativo (omissao: o atual)
    decompile_timeout: float = 120.0
    ffdec: Path | None = None  # ffdec-cli.jar/ffdec.jar ou a pasta do FFDec
    java: Path | None = None
    java_heap: str = "4g"
    actionscript_timeout: float = 3600.0
    rabcdasm: Path | None = None  # pasta com abcexport/rabcdasm (RABCDAsm)
    node: Path | None = None  # node.exe para verificar o JS formatado (vazio = PATH)
    source: Path | None = None  # ficheiro de onde veio (None = defaults)

    def realm(self, name: str) -> RealmConfig:
        name = name.upper()
        if name not in self.realms:
            self.realms[name] = RealmConfig(name, None, DEFAULT_PREFERRED_DRIVE.get(name, ""))
        return self.realms[name]

    def realm_output_dir(self, name: str) -> Path:
        return self.output_root / f"wot_src_{name.upper()}"


def _norm_drive(value: str) -> str:
    value = (value or "").strip().rstrip("\\/")
    if len(value) == 1 and value.isalpha():
        value += ":"
    return value.upper()


def load_config(path: Path | None = None, project_root: Path | None = None) -> Config:
    """Carrega `path` (ou wot_extractor.toml na raiz do projeto, se existir)."""
    project_root = (project_root or Path.cwd()).resolve()
    data: dict = {}
    source: Path | None = None
    if path is None:
        candidate = project_root / CONFIG_FILENAME
        if candidate.is_file():
            path = candidate
    if path is not None:
        path = Path(path).resolve()
        if not path.is_file():
            raise ConfigError(f"Ficheiro de configuracao nao encontrado: {path}")
        try:
            data = tomllib.loads(path.read_text(encoding="utf-8"))
        except (tomllib.TOMLDecodeError, UnicodeDecodeError) as exc:
            raise ConfigError(f"Configuracao invalida em {path}: {exc}") from exc
        source = path

    base = source.parent if source else project_root
    paths = data.get("paths", {}) or {}
    out = paths.get("output_root") or "."
    output_root = (base / out).resolve() if not Path(out).is_absolute() else Path(out).resolve()

    det = data.get("detect", {}) or {}
    scan_depth = det.get("scan_depth", 2)
    if not isinstance(scan_depth, int) or not 0 <= scan_depth <= 4:
        raise ConfigError("detect.scan_depth deve ser um inteiro entre 0 e 4")

    dec = data.get("decompile", {}) or {}
    timeout = dec.get("timeout", 120)
    if not isinstance(timeout, (int, float)) or isinstance(timeout, bool) or not 1 <= timeout <= 3600:
        raise ConfigError("decompile.timeout deve ser um numero entre 1 e 3600 (segundos)")

    asx = data.get("actionscript", {}) or {}
    as_timeout = asx.get("timeout", 3600)
    if not isinstance(as_timeout, (int, float)) or isinstance(as_timeout, bool) or not 10 <= as_timeout <= 86400:
        raise ConfigError("actionscript.timeout deve ser um numero entre 10 e 86400 (segundos)")
    heap = str(asx.get("java_heap", "4g")).strip().lower()
    if not heap[:-1].isdigit() or heap[-1] not in "mg":
        raise ConfigError("actionscript.java_heap deve ser do tipo '4g' ou '2048m'")

    def _interp(name, section=None):
        value = ((section if section is not None else dec).get(name) or "").strip()
        return None if not value else (Path(value) if Path(value).is_absolute() else (base / value).resolve())

    cfg = Config(
        project_root=project_root,
        output_root=output_root,
        scan_drives=bool(det.get("scan_drives", True)),
        scan_depth=scan_depth,
        python27=_interp("python27"),
        python3=_interp("python3"),
        decompile_timeout=float(timeout),
        ffdec=_interp("ffdec", asx),
        java=_interp("java", asx),
        java_heap=heap,
        actionscript_timeout=float(as_timeout),
        rabcdasm=_interp("rabcdasm", asx),
        node=_interp("node", data.get("gameface", {}) or {}),
        source=source,
    )
    for name in SUPPORTED_REALMS:
        cfg.realm(name)
    for name, section in (data.get("realms", {}) or {}).items():
        if not isinstance(section, dict):
            raise ConfigError(f"realms.{name} deve ser uma tabela")
        rc = cfg.realm(name)
        install = (section.get("install") or "").strip()
        if install:
            rc.install = Path(install)
        if section.get("preferred_drive"):
            rc.preferred_drive = _norm_drive(section["preferred_drive"])
    return cfg
