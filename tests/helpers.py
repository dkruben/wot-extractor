"""Construcao de instalacoes falsas (minimas) para testes."""

from __future__ import annotations

import os
import zipfile
from pathlib import Path

PYC27 = bytes.fromhex("03f30d0a") + b"\x00" * 4 + b"c"
PYC38 = (3413).to_bytes(2, "little") + b"\r\n" + b"\x00" * 12

VERSION_TMPL = """<version.xml>
\t<appname>\t#menu:login/version\t</appname>
\t<version> {version} </version>
\t<meta>
\t\t<client> 2653317 </client>
\t\t<realm> {realm} </realm>
\t\t<branch> v2.4.1 </branch>
\t</meta>
</version.xml>
"""

GAME_INFO_TMPL = """<?xml version="1.0" encoding="utf-8"?>
<protocol name="game_info" version="2.16">
    <game>
        <id>WOT.{realm}.PRODUCTION</id>
        <localization>EN</localization>
        <client_type>{app_type}</client_type>
        <version_name>2.4.1.5514</version_name>
        <part_versions>
            <version name="client" installed="2.4.1.24120" available="2.4.1.24120"/>
        </part_versions>
    </game>
</protocol>
"""

APP_TYPE_TMPL = """<?xml version="1.0" encoding="UTF-8"?>
<protocol name="app_type" version="3.0"><app_type>{app_type}</app_type></protocol>
"""

DEFAULT_PKGS = {
    "scripts.pkg": {
        "scripts/client/gui/__init__.pyc": PYC27,
        "scripts/client/gui/shared/utils.pyc": PYC27,
        "scripts/item_defs/vehicles/list.xml": b"<root/>",
    },
    "gui-part1.pkg": {
        "gui/flash/battle.swf": b"CWS\x0a" + b"\x00" * 8,
        "gui/gameface/_dist/production/lobby/a/a.html": b"<html></html>",
        "gui/gameface/_dist/production/lobby/a/a.js": b"var a=1;",
        "gui/maps/icons/x.png": b"\x89PNG",
    },
    "hd_only.pkg": {"content/x.dds": b"DDS "},
}


def make_zip(path: Path, entries: dict[str, bytes], compression=zipfile.ZIP_STORED) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w", compression) as zf:
        for name, data in entries.items():
            zf.writestr(name, data)
    return path


def make_install(root: Path, realm: str = "EU", version: str = "v.2.4.1.1 #993", app_type: str = "hd",
                 folder: str | None = None, pkgs: dict | None = None, wotmods: dict | None = None,
                 paths_xml: bool = True, game_info_realm: str | None = None, extra_listed: list[str] = ()) -> Path:
    """Cria uma instalacao falsa em `root`."""
    from wot_extractor.detect.xmlinfo import parse_version_string

    num, suffix, _ = parse_version_string(version)
    folder = folder or f"{num} {suffix}".strip()
    pkgs = DEFAULT_PKGS if pkgs is None else pkgs
    root.mkdir(parents=True, exist_ok=True)
    (root / "WorldOfTanks.exe").write_bytes(b"MZ")
    (root / "version.xml").write_text(VERSION_TMPL.format(version=version, realm=realm), encoding="utf-8")
    (root / "game_info.xml").write_text(GAME_INFO_TMPL.format(realm=game_info_realm or realm, app_type=app_type), encoding="utf-8")
    (root / "app_type.xml").write_text(APP_TYPE_TMPL.format(app_type=app_type), encoding="utf-8")
    pkg_dir = root / "res" / "packages"
    pkg_dir.mkdir(parents=True, exist_ok=True)
    for name, entries in pkgs.items():
        make_zip(pkg_dir / name, entries)
    (root / "res" / "text").mkdir(parents=True, exist_ok=True)
    (root / "res" / "text" / "lc.mo").write_bytes(b"\xde\x12\x04\x95")
    (root / "res_mods" / folder).mkdir(parents=True, exist_ok=True)
    (root / "res_mods" / folder / "engine_config.xml").write_text("<root/>", encoding="utf-8")
    mods_dir = root / "mods" / folder
    mods_dir.mkdir(parents=True, exist_ok=True)
    for name, entries in (wotmods or {}).items():
        make_zip(mods_dir / name, entries)
    if paths_xml:
        lines = [f'    <Path cacheSubdirs="true">./res_mods/{folder}</Path>',
                 f'    <Path mask="*.wotmod" mode="recursive" root="res">./mods/{folder}</Path>',
                 "    <Packages>"]
        for name in list(pkgs) + list(extra_listed):
            types = "hd" if name.startswith("hd_") else "sd,hd"
            lines.append(f'      <Package type="{types}">./res/packages/{name}</Package>')
        lines.append("    </Packages>")
        lines.append("    <Path>./res</Path>")
        (root / "paths.xml").write_text("<root>\n  <Paths>\n" + "\n".join(lines) + "\n  </Paths>\n</root>\n", encoding="utf-8")
    return root


# ------------------------------------------------ XML binario BigWorld (codificador de teste)

import struct as _struct


class N:
    """No para o codificador: N(nome, (tipo, payload), [filhos])."""

    def __init__(self, name, value=(1, b""), children=()):
        self.name, self.value, self.children = name, value, list(children)


def S(text):
    return (1, text.encode("utf-8"))


def I(n, size=4):
    return (2, b"" if size == 0 else _struct.pack({1: "<b", 2: "<h", 4: "<i", 8: "<q"}[size], n))


def F(*vals):
    return (3, b"".join(_struct.pack("<f", v) for v in vals))


def B(flag, empty=False):
    return (4, b"" if empty else (b"\x01" if flag else b"\x00"))


def BLOB(data):
    return (5, data)


def pack_xml(root: N, version: int = 0) -> bytes:
    names: list[str] = []

    def collect(n):
        for c in n.children:
            if c.name not in names:
                names.append(c.name)
            collect(c)

    collect(root)

    def element(n) -> bytes:
        blocks = [n.value]
        for c in n.children:
            blocks.append((0, element(c)) if c.children else c.value)
        descs, data, end = [], b"", 0
        for typ, payload in blocks:
            end += len(payload)
            descs.append((typ << 28) | end)
            data += payload
        out = _struct.pack("<HI", len(n.children), descs[0])
        for c, d in zip(n.children, descs[1:]):
            out += _struct.pack("<HI", names.index(c.name), d)
        return out + data

    head = b"\x45\x4e\xa1\x62" + bytes([version])
    head += b"".join(n.encode("utf-8") + b"\x00" for n in names) + b"\x00"
    return head + element(root)


SAMPLE_PACKED = pack_xml(N("root", S(""), [
    N("xmlns:xmlref", S(" http://bwt/xmlref ")),
    N("vehicle", S(""), [N("id", I(7, 1)), N("price", I(373000)), N("tags", S("mediumTank secret"))]),
    N("speed", F(20.0)),
    N("color", F(1.0, 0.725, 0.45)),
    N("transform", F(1, 0, 0, 0, 1, 0, 0, 0, 1, 5, 6, 7)),
    N("enabled", B(True)),
    N("hidden", B(False, empty=True)),
    N("blob", BLOB(b"\x00\x01\x02")),
    N("big", I(-2**40, 8)),
    N("zero", I(0, 0)),
]))


def snapshot(root: Path) -> dict[str, tuple[int, int]]:
    """Mapa caminho -> (tamanho, mtime_ns) para verificar que nada foi escrito."""
    snap = {}
    for dirpath, _, files in os.walk(root):
        for fn in files:
            p = Path(dirpath) / fn
            st = p.stat()
            snap[str(p.relative_to(root))] = (st.st_size, st.st_mtime_ns)
    return snap
