"""Parsers dos ficheiros de metadados na raiz do cliente:
version.xml, game_info.xml, app_type.xml e paths.xml."""

from __future__ import annotations

import re
import xml.etree.ElementTree as ET
from dataclasses import asdict, dataclass, field
from pathlib import Path

MAX_META_XML_SIZE = 4 * 1024 * 1024  # metadados reais tem < 20 KB


class MetadataError(Exception):
    pass


def _read_xml(path: Path) -> ET.Element:
    path = Path(path)
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise MetadataError(f"nao foi possivel ler {path.name}: {exc}") from exc
    if size > MAX_META_XML_SIZE:
        raise MetadataError(f"{path.name} demasiado grande ({size} B)")
    text = path.read_bytes().decode("utf-8-sig", errors="replace")
    if "<!ENTITY" in text or "<!DOCTYPE" in text:
        raise MetadataError(f"{path.name} contem DTD/entidades (recusado)")
    try:
        return ET.fromstring(text)
    except ET.ParseError as exc:
        raise MetadataError(f"XML invalido em {path.name}: {exc}") from exc


def _text(el: ET.Element | None) -> str:
    return (el.text or "").strip() if el is not None else ""


# ---------------------------------------------------------------- version.xml

_VERSION_RE = re.compile(r"v\.?\s*(?P<num>\d+(?:\.\d+)+)\s*(?P<suffix>[^#]*?)\s*(?:#(?P<build>\d+))?\s*$")


@dataclass
class VersionInfo:
    raw: str
    number: str = ""          # "2.4.1.1"
    suffix: str = ""          # "Common Test" (vazio no cliente de producao)
    build: int | None = None  # 993
    realm: str = ""           # <meta><realm>
    branch: str = ""
    client_revision: str = ""

    @property
    def number_tuple(self) -> tuple[int, ...]:
        try:
            return tuple(int(p) for p in self.number.split("."))
        except ValueError:
            return ()

    @property
    def folder_name(self) -> str:
        """Nome usado em res_mods/<x> e mods/<x> (ex.: '2.4.2.0 Common Test')."""
        return f"{self.number} {self.suffix}".strip()

    def to_dict(self) -> dict:
        d = asdict(self)
        d["folder_name"] = self.folder_name
        return d


def parse_version_string(raw: str) -> tuple[str, str, int | None]:
    m = _VERSION_RE.search(raw.strip())
    if not m:
        return "", "", None
    build = int(m.group("build")) if m.group("build") else None
    return m.group("num"), m.group("suffix").strip(), build


def parse_version_xml(path: Path) -> VersionInfo:
    root = _read_xml(path)
    raw = _text(root.find("version"))
    if not raw:
        raise MetadataError("version.xml sem <version>")
    number, suffix, build = parse_version_string(raw)
    meta = root.find("meta")
    return VersionInfo(
        raw=raw,
        number=number,
        suffix=suffix,
        build=build,
        realm=_text(meta.find("realm")).upper() if meta is not None else "",
        branch=_text(meta.find("branch")) if meta is not None else "",
        client_revision=_text(meta.find("client")) if meta is not None else "",
    )


# -------------------------------------------------------------- game_info.xml

@dataclass
class GameInfo:
    game_id: str = ""        # WOT.EU.PRODUCTION
    realm: str = ""          # EU (derivado do id)
    version_name: str = ""   # 2.4.1.5514
    client_type: str = ""    # sd / hd
    localization: str = ""
    part_versions: dict[str, str] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return asdict(self)


def parse_game_info(path: Path) -> GameInfo:
    root = _read_xml(path)
    game = root.find("game")
    if game is None:
        raise MetadataError("game_info.xml sem <game>")
    gid = _text(game.find("id"))
    parts = gid.split(".")
    info = GameInfo(
        game_id=gid,
        realm=parts[1].upper() if len(parts) >= 2 and parts[0].upper() == "WOT" else "",
        version_name=_text(game.find("version_name")),
        client_type=_text(game.find("client_type")).lower(),
        localization=_text(game.find("localization")),
    )
    pv = game.find("part_versions")
    if pv is not None:
        for v in pv.findall("version"):
            if v.get("name"):
                info.part_versions[v.get("name")] = v.get("installed", "")
    return info


# --------------------------------------------------------------- app_type.xml

def parse_app_type(path: Path) -> str:
    root = _read_xml(path)
    return _text(root.find("app_type")).lower()


# ------------------------------------------------------------------ paths.xml

@dataclass
class ModsPath:
    path: str
    mask: str = ""
    mode: str = ""
    root: str = ""


@dataclass
class PackageEntry:
    path: str
    types: tuple[str, ...] = ()

    @property
    def name(self) -> str:
        return self.path.replace("\\", "/").rsplit("/", 1)[-1]

    def active_for(self, app_type: str) -> bool:
        return not self.types or not app_type or app_type in self.types


@dataclass
class PathsInfo:
    plain: list[str] = field(default_factory=list)       # <Path> sem mask (res_mods/<v>, ./res)
    mods: list[ModsPath] = field(default_factory=list)
    packages: list[PackageEntry] = field(default_factory=list)
    order: list[str] = field(default_factory=list)       # ordem de pesquisa: "path:<p>", "mods:<p>", "packages"

    @property
    def res_mods(self) -> list[str]:
        return [p for p in self.plain if "res_mods" in p.replace("\\", "/").lower()]

    def to_dict(self) -> dict:
        return {
            "res_mods": self.res_mods,
            "plain_paths": list(self.plain),
            "mods": [asdict(m) for m in self.mods],
            "packages_count": len(self.packages),
            "search_order": list(self.order),
        }


def parse_paths_xml(path: Path) -> PathsInfo:
    root = _read_xml(path)
    paths = root.find("Paths")
    if paths is None:
        raise MetadataError("paths.xml sem <Paths>")
    info = PathsInfo()
    for child in paths:
        if child.tag == "Path":
            value = _text(child)
            if not value:
                continue
            if child.get("mask") or child.get("mode"):
                info.mods.append(ModsPath(value, child.get("mask", ""), child.get("mode", ""), child.get("root", "")))
                info.order.append(f"mods:{value}")
            else:
                info.plain.append(value)
                info.order.append(f"path:{value}")
        elif child.tag == "Packages":
            info.order.append("packages")
            for p in child.findall("Package"):
                value = _text(p)
                if value:
                    types = tuple(t.strip().lower() for t in (p.get("type") or "").split(",") if t.strip())
                    info.packages.append(PackageEntry(value, types))
    return info
