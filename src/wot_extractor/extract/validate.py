"""Validacao do conteudo extraido (sem o executar nem alterar).

Resultados possiveis:
  valid            conteudo bem formado
  valid_bigworld   XML de texto BigWorld: bem formado, mas com prefixos de tag
                   nao declarados (ex.: <xmlns:xmlref>), aceites pelo motor
  valid_jsonc      JSON com comentarios/virgulas finais (ex.: tsconfig.json)
  packed           XML binario BigWorld (descodificacao fora do ambito da fase B)
  empty            ficheiro vazio
  unknown          .pyc com magic desconhecido
  invalid: <msg>   mal formado
"""

from __future__ import annotations

import json
import re
import xml.etree.ElementTree as ET

from ..constants import PACKED_XML_MAGIC
from ..detect.pkgprobe import pyc_version

# Incrementar sempre que as regras mudarem: forca a revalidacao das entradas
# inalteradas (a partir da copia ja extraida, sem reescrever).
VALIDATOR_VERSION = 2

# Categorias cujo conteudo e lido para memoria para validacao.
NEEDS_DATA = frozenset({"xml", "json", "python_bytecode", "scaleform"})
MAX_VALIDATE_SIZE = 64 * 1024 * 1024
_SWF_SIGNATURES = {b"FWS": "FWS", b"CWS": "CWS", b"ZWS": "ZWS"}
_TAG_PREFIX_RE = re.compile(rb"<(/?)([A-Za-z_][\w.\-]*):")
_TRAILING_COMMA_RE = re.compile(r",(\s*[}\]])")


def strip_json_comments(text: str) -> str:
    """Remove comentarios // e /* */ fora de strings."""
    out = []
    i, n = 0, len(text)
    in_str = False
    while i < n:
        c = text[i]
        if in_str:
            out.append(c)
            if c == "\\" and i + 1 < n:
                out.append(text[i + 1])
                i += 2
                continue
            if c == '"':
                in_str = False
            i += 1
        elif c == '"':
            in_str = True
            out.append(c)
            i += 1
        elif text.startswith("//", i):
            j = text.find("\n", i)
            i = n if j < 0 else j
        elif text.startswith("/*", i):
            j = text.find("*/", i + 2)
            i = n if j < 0 else j + 2
        else:
            out.append(c)
            i += 1
    return "".join(out)


def validate_xml(data: bytes) -> str:
    if data[:4] == PACKED_XML_MAGIC:
        return "packed"
    head = data[:4096]
    if b"<!ENTITY" in head or b"<!DOCTYPE" in head:
        return "invalid: DTD/entidades recusadas"
    try:
        ET.fromstring(data)
        return "valid"
    except (ET.ParseError, ValueError) as exc:
        first = str(exc)
    if "unbound prefix" in first:
        try:
            ET.fromstring(_TAG_PREFIX_RE.sub(rb"<\1\2__", data))
            return "valid_bigworld"
        except (ET.ParseError, ValueError):
            pass
    return f"invalid: {first}"


def _validate_json(data: bytes) -> str:
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        return f"invalid: {exc}"
    try:
        json.loads(text)
        return "valid"
    except ValueError as exc:
        first = str(exc)
    try:
        json.loads(_TRAILING_COMMA_RE.sub(r"\1", strip_json_comments(text)))
        return "valid_jsonc"
    except ValueError:
        return f"invalid: {first}"


def inspect_content(category: str, data: bytes, name: str = "") -> tuple[str | None, dict]:
    """Devolve (validacao, info) para o conteudo `data` do ficheiro `name`."""
    if category not in NEEDS_DATA:
        return None, {}
    if not data:
        return "empty", {}
    if category == "xml":
        v = validate_xml(data)
        return v, ({"format": "bigworld_packed_xml"} if v == "packed" else {})
    if category == "json":
        return _validate_json(data), {}
    if category == "python_bytecode":
        ver = pyc_version(data[:4])
        if ver == "invalid":
            return "invalid: cabecalho .pyc invalido", {}
        return ("valid" if not ver.startswith("unknown") else "unknown"), {"pyc_version": ver}
    if category == "scaleform":
        if name.lower().endswith(".swc"):
            # .swc = biblioteca de componentes Flash: zip com catalog.xml + library.swf
            if data[:4] == b"PK\x03\x04":
                return "valid", {"swc": "zip"}
            return "invalid: .swc sem assinatura zip", {}
        sig = _SWF_SIGNATURES.get(data[:3])
        if sig is None:
            return "invalid: assinatura SWF desconhecida", {}
        info = {"swf_signature": sig}
        if len(data) >= 8:
            info["swf_version"] = data[3]
            info["swf_declared_size"] = int.from_bytes(data[4:8], "little")
        return "valid", info
    return None, {}
