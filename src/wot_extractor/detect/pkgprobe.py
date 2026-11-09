"""Sondagem dos contentores (.pkg / .wotmod): le apenas o diretorio central
do zip e alguns bytes de amostra dos .pyc. Nao extrai nada."""

from __future__ import annotations

import zipfile
from collections import Counter
from dataclasses import asdict, dataclass, field
from pathlib import Path, PurePosixPath

from ..constants import EXT_CATEGORIES, GAMEFACE_PREFIXES, PYC_MAGIC_VERSIONS
from ..safety import UnsafePathError, normalize_member_name


def categorize(name: str) -> str:
    suffix = PurePosixPath(name.replace("\\", "/")).suffix.lower()
    return EXT_CATEGORIES.get(suffix, "other")


def strip_res_prefix(name: str) -> str:
    """Os .wotmod guardam o conteudo sob 'res/'; os .pkg nao."""
    n = name.replace("\\", "/")
    return n[4:] if n.lower().startswith("res/") else n


def is_gameface(name: str) -> bool:
    n = strip_res_prefix(name).lower()
    return any(n.startswith(p) for p in GAMEFACE_PREFIXES)


def pyc_version(header: bytes) -> str:
    """Versao CPython a partir do cabecalho de um .pyc ('unknown:<n>' se desconhecida)."""
    if len(header) < 4 or header[2:4] != b"\r\n":
        return "invalid"
    magic = int.from_bytes(header[:2], "little")
    return PYC_MAGIC_VERSIONS.get(magic, f"unknown:{magic}")


@dataclass
class PackageProbe:
    name: str
    path: str
    size: int
    entries: int = 0
    files: int = 0
    uncompressed_size: int = 0
    categories: dict[str, int] = field(default_factory=dict)
    gameface_entries: int = 0
    pyc_versions: dict[str, int] = field(default_factory=dict)  # amostra
    compression: dict[str, int] = field(default_factory=dict)
    unsafe_names: list[str] = field(default_factory=list)
    error: str | None = None

    def to_dict(self) -> dict:
        return asdict(self)


_COMPRESSION_NAMES = {zipfile.ZIP_STORED: "stored", zipfile.ZIP_DEFLATED: "deflated",
                      zipfile.ZIP_BZIP2: "bzip2", zipfile.ZIP_LZMA: "lzma"}


def probe_package(path: Path, pyc_sample: int = 16, max_unsafe_listed: int = 20) -> PackageProbe:
    path = Path(path)
    try:
        size = path.stat().st_size
    except OSError as exc:
        return PackageProbe(path.name, str(path), 0, error=f"stat: {exc}")
    probe = PackageProbe(path.name, str(path), size)
    try:
        with zipfile.ZipFile(path, "r") as zf:
            cats: Counter[str] = Counter()
            comp: Counter[str] = Counter()
            pyv: Counter[str] = Counter()
            sampled = 0
            infos = zf.infolist()
            probe.entries = len(infos)
            for info in infos:
                comp[_COMPRESSION_NAMES.get(info.compress_type, str(info.compress_type))] += 1
                if info.is_dir():
                    continue
                probe.files += 1
                probe.uncompressed_size += info.file_size
                try:
                    normalize_member_name(info.filename)
                except UnsafePathError:
                    if len(probe.unsafe_names) < max_unsafe_listed:
                        probe.unsafe_names.append(info.filename)
                cat = categorize(info.filename)
                cats[cat] += 1
                if is_gameface(info.filename):
                    probe.gameface_entries += 1
                if cat == "python_bytecode" and sampled < pyc_sample:
                    sampled += 1
                    try:
                        with zf.open(info) as fh:
                            pyv[pyc_version(fh.read(4))] += 1
                    except (OSError, zipfile.BadZipFile, RuntimeError, NotImplementedError) as exc:
                        pyv[f"read_error:{type(exc).__name__}"] += 1
            probe.categories = dict(cats.most_common())
            probe.compression = dict(comp)
            probe.pyc_versions = dict(pyv)
    except (zipfile.BadZipFile, OSError, ValueError) as exc:
        probe.error = f"{type(exc).__name__}: {exc}"
    return probe
