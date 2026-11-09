"""Fontes de candidatos a instalacao: Game Center, registo do Windows e
pesquisa limitada nos discos. Nenhuma destas fontes escreve nada."""

from __future__ import annotations

import os
import string
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path

from ..constants import GAME_EXE, INSTALL_DIR_HINTS, SCAN_BASE_DIRS, VERSION_XML, WGC_PREFERENCES
from ..logutil import get_logger

log = get_logger("detect")

# Prioridade (menor = mais forte) usada para desempatar.
SOURCE_PRIORITY = {"cli": 0, "config": 1, "wgc": 2, "registry": 3, "scan": 4}


@dataclass(frozen=True)
class Candidate:
    path: Path
    source: str
    note: str = ""


def path_key(path: Path) -> str:
    try:
        p = Path(path).resolve()
    except OSError:
        p = Path(path)
    return os.path.normcase(str(p)).rstrip("\\/")


# ------------------------------------------------------------- Game Center

def wgc_candidates(program_data: Path | None = None) -> list[Candidate]:
    base = program_data or Path(os.environ.get("ProgramData", r"C:\ProgramData"))
    pref = base / WGC_PREFERENCES
    if not pref.is_file():
        return []
    try:
        text = pref.read_bytes().decode("utf-8-sig", errors="replace")
        if "<!ENTITY" in text:
            return []
        root = ET.fromstring(text)
    except (OSError, ET.ParseError) as exc:
        log.warning("Preferencias do Game Center ilegiveis (%s): %s", pref, exc)
        return []
    found: list[Candidate] = []
    for el in root.iter("working_dir"):
        value = (el.text or "").strip()
        if value:
            found.append(Candidate(Path(value), "wgc", str(pref)))
    return found


# ------------------------------------------------------- Registo do Windows

_UNINSTALL_KEYS = (
    r"Software\Microsoft\Windows\CurrentVersion\Uninstall",
    r"SOFTWARE\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall",
)


def registry_candidates() -> list[Candidate]:
    try:
        import winreg
    except ImportError:  # nao-Windows
        return []
    found: list[Candidate] = []
    for hive, hive_name in ((winreg.HKEY_CURRENT_USER, "HKCU"), (winreg.HKEY_LOCAL_MACHINE, "HKLM")):
        for key_path in _UNINSTALL_KEYS:
            try:
                key = winreg.OpenKey(hive, key_path)
            except OSError:
                continue
            with key:
                i = 0
                while True:
                    try:
                        sub = winreg.EnumKey(key, i)
                    except OSError:
                        break
                    i += 1
                    try:
                        with winreg.OpenKey(key, sub) as sk:
                            name = _reg_value(winreg, sk, "DisplayName")
                            loc = _reg_value(winreg, sk, "InstallLocation")
                    except OSError:
                        continue
                    if name and "world of tanks" in name.lower() and loc:
                        found.append(Candidate(Path(loc.strip().strip('"')), "registry", f"{hive_name}\\...\\{sub} ({name})"))
    return found


def _reg_value(winreg, key, name: str) -> str:
    try:
        value, _ = winreg.QueryValueEx(key, name)
        return str(value)
    except OSError:
        return ""


# ------------------------------------------------------ Pesquisa nos discos

def available_drives() -> list[str]:
    if os.name != "nt":
        return []
    return [f"{d}:" for d in string.ascii_uppercase if os.path.isdir(f"{d}:\\")]


def looks_like_install(path: Path) -> bool:
    return (path / VERSION_XML).is_file() and ((path / GAME_EXE).is_file() or (path / "res" / "packages").is_dir())


def scan_candidates(drives: list[str] | None = None, depth: int = 2) -> list[Candidate]:
    """Procura, em cada disco, pastas com nome tipico do WoT dentro de
    SCAN_BASE_DIRS, ate `depth` niveis abaixo da raiz. Nao percorre o disco
    inteiro (custo controlado)."""
    found: list[Candidate] = []
    seen: set[str] = set()
    for drive in drives if drives is not None else available_drives():
        root = Path(drive + "\\") if len(drive) == 2 and drive.endswith(":") else Path(drive)
        for base_rel in SCAN_BASE_DIRS:
            base = root / base_rel if base_rel else root
            if not base.is_dir():
                continue
            base_depth = len(Path(base_rel).parts) if base_rel else 0
            remaining = depth - base_depth
            if remaining < 1:
                continue
            for cand in _walk_hint_dirs(base, remaining):
                k = path_key(cand)
                if k not in seen:
                    seen.add(k)
                    found.append(Candidate(cand, "scan", f"pesquisa em {base}"))
    return found


def _walk_hint_dirs(base: Path, levels: int):
    try:
        entries = list(os.scandir(base))
    except OSError:
        return
    for e in entries:
        try:
            if not e.is_dir(follow_symlinks=False):
                continue
        except OSError:
            continue
        p = Path(e.path)
        lname = e.name.lower()
        if any(h in lname for h in INSTALL_DIR_HINTS) and looks_like_install(p):
            yield p
        elif levels > 1 and any(h in lname for h in INSTALL_DIR_HINTS + ("wargaming", "games")):
            yield from _walk_hint_dirs(p, levels - 1)
