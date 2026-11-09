"""Descodificador do XML binario BigWorld ("packed section").

Formato (little-endian):
  magic   4 B   45 4E A1 62
  versao  1 B
  dicionario: strings terminadas em \\0, terminado por uma string vazia
  elemento raiz

  elemento:
    n_filhos            uint16
    descritor proprio   uint32  (bits 0-27: fim do bloco de dados; bits 28-31: tipo)
    n_filhos x (indice_nome uint16, descritor uint32)
    blocos de dados contiguos: [proprio][filho 0][filho 1]...
      cada bloco vai de fim_anterior ate ao 'fim' do seu descritor
      (deslocamentos relativos ao inicio da zona de dados do elemento)

  tipos: 0 elemento aninhado, 1 string, 2 inteiro (0/1/2/4/8 B), 3 floats
         (4 B cada; 12 floats = matriz row0..row3), 4 booleano, 5 binario (base64)

O descodificador nunca executa nada: so le bytes e produz texto XML. Verifica
que cada elemento aninhado ocupa exatamente o seu bloco e que o ficheiro e
consumido por completo.
"""

from __future__ import annotations

import base64
import re
import struct
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from decimal import Decimal

MAGIC = b"\x45\x4e\xa1\x62"
DECODER_VERSION = 1
MAX_DEPTH = 256
# Nomes de tag aceites tal como estao. Inclui a notacao BigWorld com prefixo
# (ex.: <xmlns:xmlref>, <xmlns:germany>), igual a dos XML de texto do jogo; o
# resultado deixa de ser XML com namespaces valido e e classificado como
# 'valid_bigworld'. So nomes que nao seriam lidos por nenhum parser (ex.:
# comecados por digito) sao renomeados com prefixo '_'.
_XML_NAME_RE = re.compile(r"^[A-Za-z_][\w.\-]*(?::[A-Za-z_][\w.\-]*)?$")
_INVALID_XML_CHARS_RE = re.compile("[\x00-\x08\x0b\x0c\x0e-\x1f\ud800-\udfff￾￿]")
TYPE_NAMES = {0: "element", 1: "string", 2: "int", 3: "float", 4: "bool", 5: "blob"}


class PackedXmlError(ValueError):
    pass


@dataclass
class DecodeResult:
    root: ET.Element
    version: int
    elements: int = 0
    warnings: list[str] = field(default_factory=list)
    trailing_bytes: int = 0
    renamed_tags: int = 0
    non_utf8_strings: int = 0
    escaped_strings: int = 0

    @property
    def status(self) -> str:
        return "partial" if self.trailing_bytes else "success"

    def to_text(self) -> str:
        tree = ET.ElementTree(self.root)
        ET.indent(tree, space="\t")
        return ET.tostring(self.root, encoding="unicode") + "\n"


def is_packed(data: bytes) -> bool:
    return data[:4] == MAGIC


def _positional(s: str) -> str:
    """'2e+01' -> '20', '1.5e-05' -> '0.000015' (sem expoente, sem zeros a mais)."""
    if "e" not in s and "E" not in s:
        return s
    out = format(Decimal(s), "f")
    if "." in out:
        out = out.rstrip("0").rstrip(".")
    return out or "0"


def format_float32(raw: bytes) -> str:
    """Representacao decimal mais curta (sem expoente) que reproduz exatamente o float32."""
    (v,) = struct.unpack("<f", raw)
    if v != v or v in (float("inf"), float("-inf")):
        return repr(v)
    for p in range(1, 10):
        s = f"{v:.{p}g}"
        if struct.pack("<f", float(s)) == raw:
            s = _positional(s)
            return "0" if s == "-0" and raw != b"\x00\x00\x00\x80" else s
    return repr(v)


class _Decoder:
    def __init__(self, data: bytes):
        self.raw = data
        self.data = memoryview(data)
        self.n = len(data)
        self.res: DecodeResult | None = None
        self.names: list[str] = []

    # ---- leitura de primitivas
    def _need(self, pos: int, size: int) -> None:
        if pos < 0 or pos + size > self.n:
            raise PackedXmlError(f"fim inesperado do ficheiro (posicao {pos}, faltam {pos + size - self.n} B)")

    def u16(self, pos: int) -> int:
        self._need(pos, 2)
        return struct.unpack_from("<H", self.data, pos)[0]

    def u32(self, pos: int) -> int:
        self._need(pos, 4)
        return struct.unpack_from("<I", self.data, pos)[0]

    # ---- estrutura
    def decode(self) -> DecodeResult:
        if self.n < 5 or bytes(self.data[:4]) != MAGIC:
            raise PackedXmlError("assinatura de XML binario BigWorld em falta")
        version = self.data[4]
        pos = 5
        raw_names: list[bytes] = []
        while True:
            end = self.raw.find(b"\x00", pos)
            if end < 0:
                raise PackedXmlError("dicionario sem terminador")
            word = self.raw[pos:end]
            pos = end + 1
            if not word:
                break
            raw_names.append(word)
        root = ET.Element("root")
        self.res = DecodeResult(root=root, version=version)
        self.renamed: set[int] = set()
        self.names = []
        for i, w in enumerate(raw_names):
            name, renamed = self._tag_name(w)
            if renamed:
                self.renamed.add(i)
            self.names.append(name)
        end_pos = self.element(root, pos, 0)
        self.res.trailing_bytes = self.n - end_pos
        if self.res.trailing_bytes:
            self.res.warnings.append(f"{self.res.trailing_bytes} B nao consumidos no fim do ficheiro")
        return self.res

    def _tag_name(self, raw: bytes) -> tuple[str, bool]:
        try:
            name = raw.decode("utf-8")
        except UnicodeDecodeError:
            name = raw.decode("latin-1")
        if _XML_NAME_RE.match(name):
            return name, False
        # nome invalido em XML (ex.: comeca por digito): prefixo '_' e o original fica registado
        safe = "_" + re.sub(r"[^\w.\-]", "_", name)
        if len(self.res.warnings) < 20:
            self.res.warnings.append(f"tag {name!r} renomeada para {safe!r}")
        return safe, True

    def element(self, el: ET.Element, pos: int, depth: int) -> int:
        """Le um elemento a partir de `pos`; devolve a posicao a seguir aos seus dados."""
        if depth > MAX_DEPTH:
            raise PackedXmlError("profundidade excessiva (ficheiro corrompido?)")
        self.res.elements += 1
        n_children = self.u16(pos)
        own = self.u32(pos + 2)
        pos += 6
        children = []
        for _ in range(n_children):
            idx = self.u16(pos)
            desc = self.u32(pos + 2)
            pos += 6
            if idx >= len(self.names):
                raise PackedXmlError(f"indice de nome {idx} fora do dicionario ({len(self.names)})")
            children.append((idx, desc))
        data_start = pos
        prev_end = 0
        prev_end = self.data_block(el, data_start, prev_end, own, depth)
        for idx, desc in children:
            child = ET.SubElement(el, self.names[idx])
            if idx in self.renamed:
                self.res.renamed_tags += 1
            prev_end = self.data_block(child, data_start, prev_end, desc, depth)
        return data_start + prev_end

    def data_block(self, el: ET.Element, data_start: int, prev_end: int, desc: int, depth: int) -> int:
        end = desc & 0x0FFFFFFF
        typ = desc >> 28
        length = end - prev_end
        start = data_start + prev_end
        if length < 0:
            raise PackedXmlError(f"bloco com tamanho negativo em <{el.tag}>")
        self._need(start, length)
        raw = bytes(self.data[start:start + length])
        if typ == 0:
            consumed = self.element(el, start, depth + 1)
            if consumed != start + length:
                raise PackedXmlError(f"elemento <{el.tag}> ocupa {consumed - start} B, bloco tem {length} B")
        elif typ == 1:
            el.text = self._string(raw)
        elif typ == 2:
            el.text = str(self._int(raw, el.tag))
        elif typ == 3:
            if length % 4:
                raise PackedXmlError(f"floats com tamanho {length} em <{el.tag}>")
            vals = [format_float32(raw[i:i + 4]) for i in range(0, length, 4)]
            if len(vals) == 12:
                for r in range(4):
                    ET.SubElement(el, f"row{r}").text = " ".join(vals[r * 3:r * 3 + 3])
            else:
                el.text = " ".join(vals)
        elif typ == 4:
            if length > 1:
                raise PackedXmlError(f"booleano com {length} B em <{el.tag}>")
            el.text = "true" if length == 1 and raw[0] == 1 else "false"
        elif typ == 5:
            el.text = base64.b64encode(raw).decode("ascii")
        else:
            raise PackedXmlError(f"tipo de dados desconhecido {typ} em <{el.tag}>")
        return end

    def _string(self, raw: bytes) -> str:
        try:
            s = raw.decode("utf-8")
        except UnicodeDecodeError:
            s = raw.decode("latin-1")
            self.res.non_utf8_strings += 1
        if _INVALID_XML_CHARS_RE.search(s):
            # caracteres proibidos em XML 1.0: representacao escapada e assinalada
            self.res.escaped_strings += 1
            s = _INVALID_XML_CHARS_RE.sub(lambda m: f"\\x{ord(m.group()):02x}", s)
        return s

    @staticmethod
    def _int(raw: bytes, tag: str) -> int:
        n = len(raw)
        if n == 0:
            return 0
        fmt = {1: "<b", 2: "<h", 4: "<i", 8: "<q"}.get(n)
        if fmt is None:
            raise PackedXmlError(f"inteiro com {n} B em <{tag}>")
        return struct.unpack(fmt, raw)[0]


def decode_packed_xml(data: bytes) -> DecodeResult:
    """Descodifica `data`; levanta PackedXmlError se a estrutura for invalida."""
    return _Decoder(bytes(data)).decode()
