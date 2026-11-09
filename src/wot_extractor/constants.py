"""Constantes partilhadas. Apenas valores verificados nos clientes reais ou em
especificacoes publicas (magic numbers do CPython)."""

from __future__ import annotations

SUPPORTED_REALMS: tuple[str, ...] = ("EU", "CT")
DEFAULT_PREFERRED_DRIVE: dict[str, str] = {"EU": "D:", "CT": "C:"}

GAME_EXE = "WorldOfTanks.exe"
VERSION_XML = "version.xml"
GAME_INFO_XML = "game_info.xml"
APP_TYPE_XML = "app_type.xml"
PATHS_XML = "paths.xml"

# Pastas onde a pesquisa nos discos procura instalacoes (relativas a raiz).
SCAN_BASE_DIRS: tuple[str, ...] = ("", "Games", "Wargaming.net", "Program Files (x86)", "Program Files")
# Nomes de pasta que indicam uma instalacao do WoT (comparacao em minusculas).
INSTALL_DIR_HINTS: tuple[str, ...] = ("world_of_tanks", "worldoftanks", "world of tanks")

# Preferencias do Wargaming Game Center (lista de jogos instalados).
WGC_PREFERENCES = r"Wargaming.net\GameCenter\preferences.xml"

# Magic numbers do CPython (2 primeiros bytes, little-endian) -> versao.
# Fonte: Lib/importlib/_bootstrap_external.py (valores finais de cada versao).
PYC_MAGIC_VERSIONS: dict[int, str] = {
    62211: "2.7",
    3379: "3.6",
    3394: "3.7",
    3413: "3.8",
    3425: "3.9",
    3439: "3.10",
    3495: "3.11",
    3531: "3.12",
    3571: "3.13",
}

# Categorias de conteudo por extensao (usadas no inventario e mais tarde na extracao).
EXT_CATEGORIES: dict[str, str] = {
    ".pyc": "python_bytecode",
    ".pyo": "python_bytecode",
    ".py": "python_source",
    ".swf": "scaleform",
    ".swc": "scaleform",
    ".gfx": "scaleform",
    ".xml": "xml",
    ".def": "xml",
    ".json": "json",
    ".html": "web",
    ".htm": "web",
    ".css": "web",
    ".js": "web",
    ".mjs": "web",
    ".ts": "web",
    ".unbound": "web",
    ".png": "image",
    ".dds": "image",
    ".jpg": "image",
    ".jpeg": "image",
    ".svg": "image",
    ".gif": "image",
    ".webp": "image",
    ".tga": "image",
    ".ttf": "font",
    ".otf": "font",
    ".woff": "font",
    ".woff2": "font",
    ".fnt": "font",
    ".bnk": "audio",
    ".wem": "audio",
    ".ogg": "audio",
    ".wav": "audio",
    ".webm": "video",
    ".usm": "video",
    ".mp4": "video",
    ".txt": "text",
    ".csv": "text",
    ".yml": "text",
    ".yaml": "text",
    ".mo": "text",
    ".po": "text",
    ".pth": "text",
}

# Prefixo (dentro dos pacotes) onde o cliente guarda as interfaces Gameface.
GAMEFACE_PREFIXES: tuple[str, ...] = ("gui/gameface/",)

# XML binario BigWorld ("packed section"): 4 primeiros bytes. Verificado em
# 3981/4000 XML amostrados nos .pkg do cliente EU 2.4.1.1.
PACKED_XML_MAGIC = b"\x45\x4e\xa1\x62"

# Perfis de extracao: categorias incluidas (None = tudo).
# - dev : codigo e recursos textuais/UI necessarios para mods (~0.8 GB/realm)
# - gui : dev + tudo o que esta sob gui/ (imagens, video, ...) (~6 GB/realm)
# - full: tudo (~95 GB no cliente EU hd)
DEV_CATEGORIES = frozenset({"python_bytecode", "python_source", "xml", "json", "web", "scaleform", "font", "text"})
PROFILES: dict[str, frozenset[str] | None] = {"dev": DEV_CATEGORIES, "gui": DEV_CATEGORIES, "full": None}
# Prefixos virtuais incluidos por completo em cada perfil (alem das categorias).
PROFILE_PREFIXES: dict[str, tuple[str, ...]] = {"dev": GAMEFACE_PREFIXES, "gui": ("gui/",), "full": ()}

# Arvore de saida por realm (seccao 3 da especificacao).
OUTPUT_SKELETON: tuple[str, ...] = (
    "sources/mods", "sources/res_mods", "sources/res",
    "sources_xml",  # copias legiveis dos XML binarios BigWorld (extensao a especificacao)
    "sources_as/scripts", "sources_as/swf", "sources_as/assets",
    "sources_gameface/html", "sources_gameface/css", "sources_gameface/js",
    "sources_gameface/assets", "sources_gameface/manifests",
    "__stubs/gui", "__stubs/helpers", "__stubs/battle", "__stubs/engine",
)
MANIFEST_SCHEMA = 1
