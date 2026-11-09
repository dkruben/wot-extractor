"""Inspecao (so leitura) de uma instalacao do World of Tanks."""

from __future__ import annotations

import os
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

from ..constants import APP_TYPE_XML, GAME_INFO_XML, PATHS_XML, VERSION_XML
from ..logutil import get_logger
from .pkgprobe import PackageProbe, categorize, probe_package
from .sources import looks_like_install
from .xmlinfo import (GameInfo, MetadataError, PathsInfo, VersionInfo, parse_app_type,
                      parse_game_info, parse_paths_xml, parse_version_xml)

log = get_logger("detect")


@dataclass
class ClientInstall:
    path: Path
    sources: list[str] = field(default_factory=list)
    valid: bool = False
    realm: str = ""
    realm_source: str = ""
    version: VersionInfo | None = None
    game_info: GameInfo | None = None
    app_type: str = ""
    paths: PathsInfo | None = None
    dirs: dict[str, str | None] = field(default_factory=dict)
    packages: dict = field(default_factory=dict)
    mods: list[dict] = field(default_factory=list)
    res_mods: dict = field(default_factory=dict)
    loose_res: dict = field(default_factory=dict)
    content: dict = field(default_factory=dict)
    package_probes: list[PackageProbe] = field(default_factory=list)
    mod_probes: list[PackageProbe] = field(default_factory=list)
    deep: bool = False
    issues: list[str] = field(default_factory=list)

    @property
    def version_number(self) -> str:
        return self.version.number if self.version else ""

    def to_dict(self, include_probes: bool = True) -> dict:
        d = {
            "path": str(self.path),
            "sources": list(self.sources),
            "valid": self.valid,
            "realm": self.realm,
            "realm_source": self.realm_source,
            "version": self.version.to_dict() if self.version else None,
            "game_info": self.game_info.to_dict() if self.game_info else None,
            "app_type": self.app_type,
            "paths_xml": self.paths.to_dict() if self.paths else None,
            "dirs": dict(self.dirs),
            "packages": self.packages,
            "mods": self.mods,
            "res_mods": self.res_mods,
            "loose_res": self.loose_res,
            "content": self.content,
            "deep": self.deep,
            "issues": list(self.issues),
        }
        if include_probes:
            d["package_probes"] = [p.to_dict() for p in self.package_probes]
            d["mod_probes"] = [p.to_dict() for p in self.mod_probes]
        return d


def _rel_to_install(install: Path, value: str) -> Path:
    v = value.replace("\\", "/")
    p = Path(v)
    return p if p.is_absolute() else (install / v).resolve()


def _walk_files(root: Path, exclude: set[str] = frozenset()):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if os.path.normcase(os.path.join(dirpath, d)) not in exclude]
        for fn in filenames:
            yield Path(dirpath) / fn


def _summarize_files(files) -> dict:
    cats: Counter[str] = Counter()
    total = 0
    count = 0
    for f in files:
        try:
            total += f.stat().st_size
        except OSError:
            continue
        count += 1
        cats[categorize(f.name)] += 1
    return {"files": count, "bytes": total, "categories": dict(cats.most_common())}


def inspect_install(path: Path, sources: list[str] | None = None, deep: bool = True) -> ClientInstall:
    install = ClientInstall(path=Path(path), sources=list(sources or []))
    p = install.path
    if not p.is_dir():
        install.issues.append("pasta nao existe")
        return install
    if not looks_like_install(p):
        install.issues.append(f"nao parece uma instalacao do WoT (falta {VERSION_XML} ou WorldOfTanks.exe/res/packages)")
        return install

    # --- metadados
    try:
        install.version = parse_version_xml(p / VERSION_XML)
    except MetadataError as exc:
        install.issues.append(f"version.xml: {exc}")
    if (p / GAME_INFO_XML).is_file():
        try:
            install.game_info = parse_game_info(p / GAME_INFO_XML)
        except MetadataError as exc:
            install.issues.append(f"game_info.xml: {exc}")
    if (p / APP_TYPE_XML).is_file():
        try:
            install.app_type = parse_app_type(p / APP_TYPE_XML)
        except MetadataError as exc:
            install.issues.append(f"app_type.xml: {exc}")
    if not install.app_type and install.game_info:
        install.app_type = install.game_info.client_type

    v_realm = install.version.realm if install.version else ""
    g_realm = install.game_info.realm if install.game_info else ""
    if v_realm:
        install.realm, install.realm_source = v_realm, "version.xml"
    elif g_realm:
        install.realm, install.realm_source = g_realm, "game_info.xml"
    if v_realm and g_realm and v_realm != g_realm:
        install.issues.append(f"realm inconsistente: version.xml={v_realm}, game_info.xml={g_realm}")
    if not install.realm:
        install.issues.append("realm nao identificado")
    install.valid = install.version is not None and bool(install.realm)
    if not install.valid:
        return install

    # --- paths.xml e diretorios
    if (p / PATHS_XML).is_file():
        try:
            install.paths = parse_paths_xml(p / PATHS_XML)
        except MetadataError as exc:
            install.issues.append(f"paths.xml: {exc}")
    folder = install.version.folder_name
    res_mods_dir = _rel_to_install(p, install.paths.res_mods[0]) if install.paths and install.paths.res_mods else p / "res_mods" / folder
    mods_dir = _rel_to_install(p, install.paths.mods[0].path) if install.paths and install.paths.mods else p / "mods" / folder
    if install.paths and folder and Path(str(res_mods_dir)).name != folder:
        install.issues.append(f"pasta res_mods do paths.xml ({res_mods_dir.name}) difere da versao ({folder})")
    res_dir = p / "res"
    pkg_dir = res_dir / "packages"
    install.dirs = {
        "res": str(res_dir) if res_dir.is_dir() else None,
        "packages": str(pkg_dir) if pkg_dir.is_dir() else None,
        "res_mods": str(res_mods_dir) if res_mods_dir.is_dir() else None,
        "mods": str(mods_dir) if mods_dir.is_dir() else None,
        "res_mods_root": str(p / "res_mods") if (p / "res_mods").is_dir() else None,
        "mods_root": str(p / "mods") if (p / "mods").is_dir() else None,
    }
    for key in ("res", "packages"):
        if install.dirs[key] is None:
            install.issues.append(f"pasta {key} em falta")

    # --- pacotes
    disk_pkgs = {f.name.lower(): f for f in pkg_dir.glob("*.pkg")} if pkg_dir.is_dir() else {}
    listed = install.paths.packages if install.paths else []
    listed_names = {e.name.lower() for e in listed}
    active = [e for e in listed if e.active_for(install.app_type)]
    active_names = {e.name.lower() for e in active}
    missing = sorted(e.name for e in active if e.name.lower() not in disk_pkgs)
    unlisted = sorted(f.name for k, f in disk_pkgs.items() if k not in listed_names)
    sizes = {k: f.stat().st_size for k, f in disk_pkgs.items()}
    install.packages = {
        "on_disk": len(disk_pkgs),
        "on_disk_bytes": sum(sizes.values()),
        "listed_in_paths_xml": len(listed),
        "active_for_app_type": len(active),
        "active_on_disk": sum(1 for n in active_names if n in disk_pkgs),
        "missing_active": missing,
        "unlisted_on_disk": unlisted,
        "load_order": [e.name for e in active],
    }
    if missing:
        install.issues.append(f"{len(missing)} pacote(s) ativo(s) no paths.xml em falta no disco")

    # --- mods (.wotmod) e res_mods
    if mods_dir.is_dir():
        for f in sorted(mods_dir.rglob("*.wotmod")):
            install.mods.append({"name": f.name, "relpath": f.relative_to(mods_dir).as_posix(), "size": f.stat().st_size})
    if res_mods_dir.is_dir():
        install.res_mods = _summarize_files(_walk_files(res_mods_dir))
    if res_dir.is_dir():
        install.loose_res = _summarize_files(_walk_files(res_dir, {os.path.normcase(str(pkg_dir))}))

    # --- sondagem dos contentores
    if deep:
        install.deep = True
        for key in sorted(disk_pkgs):
            pr = probe_package(disk_pkgs[key])
            install.package_probes.append(pr)
            if pr.error:
                install.issues.append(f"pacote ilegivel {pr.name}: {pr.error}")
        if mods_dir.is_dir():
            for m in install.mods:
                pr = probe_package(mods_dir / m["relpath"])
                install.mod_probes.append(pr)
                if pr.error:
                    install.issues.append(f"wotmod ilegivel {pr.name}: {pr.error}")
        install.content = {
            "packages": _aggregate([pr for pr in install.package_probes if pr.name.lower() in active_names or not listed]),
            "mods": _aggregate(install.mod_probes),
        }
        unsafe = sum(len(pr.unsafe_names) for pr in install.package_probes + install.mod_probes)
        if unsafe:
            install.issues.append(f"{unsafe} nome(s) de membro inseguros encontrados (serao ignorados na extracao)")
    return install


def _aggregate(probes: list[PackageProbe]) -> dict:
    cats: Counter[str] = Counter()
    pyv: Counter[str] = Counter()
    gameface = 0
    holders: dict[str, list[str]] = {"python_bytecode": [], "scaleform": [], "gameface": []}
    for pr in probes:
        if pr.error:
            continue
        cats.update(pr.categories)
        pyv.update(pr.pyc_versions)
        gameface += pr.gameface_entries
        if pr.categories.get("python_bytecode"):
            holders["python_bytecode"].append(pr.name)
        if pr.categories.get("scaleform"):
            holders["scaleform"].append(pr.name)
        if pr.gameface_entries:
            holders["gameface"].append(pr.name)
    return {
        "containers": len(probes),
        "files": sum(pr.files for pr in probes if not pr.error),
        "uncompressed_bytes": sum(pr.uncompressed_size for pr in probes if not pr.error),
        "categories": dict(cats.most_common()),
        "gameface_entries": gameface,
        "pyc_versions_sample": dict(pyv),
        "containers_with": holders,
    }
