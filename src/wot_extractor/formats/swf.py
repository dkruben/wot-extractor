"""Leitor de ficheiros SWF (Flash/Scaleform) - so leitura, nada e executado.

Descomprime (FWS sem compressao, CWS zlib, ZWS LZMA) com limite de tamanho,
percorre as tags e produz um catalogo: cabecalho, atributos, metadados,
simbolos exportados/importados (bibliotecas partilhadas), ligacao
simbolo->classe, blocos ABC (ActionScript 3) com o inventario de classes,
codigo AS1/2, fontes, imagens, sons, dados binarios e etiquetas de cena.
"""

from __future__ import annotations

import io
import lzma
import struct
import zipfile
import zlib
from collections import Counter
from dataclasses import dataclass, field

from .abc import PARSER_VERSION as ABC_PARSER_VERSION
from .abc import AbcError, AbcFile, parse_abc

SWF_PARSER_VERSION = 1
MAX_SWF_BYTES = 512 * 1024 * 1024  # tamanho descomprimido maximo aceite
MAX_SPRITE_DEPTH = 16

TAG_NAMES = {
    0: "End", 1: "ShowFrame", 2: "DefineShape", 4: "PlaceObject", 5: "RemoveObject", 6: "DefineBits",
    7: "DefineButton", 8: "JPEGTables", 9: "SetBackgroundColor", 10: "DefineFont", 11: "DefineText",
    12: "DoAction", 13: "DefineFontInfo", 14: "DefineSound", 15: "StartSound", 17: "DefineButtonSound",
    18: "SoundStreamHead", 19: "SoundStreamBlock", 20: "DefineBitsLossless", 21: "DefineBitsJPEG2",
    22: "DefineShape2", 23: "DefineButtonCxform", 24: "Protect", 26: "PlaceObject2", 28: "RemoveObject2",
    32: "DefineShape3", 33: "DefineText2", 34: "DefineButton2", 35: "DefineBitsJPEG3", 36: "DefineBitsLossless2",
    37: "DefineEditText", 39: "DefineSprite", 41: "ProductInfo", 43: "FrameLabel", 45: "SoundStreamHead2",
    46: "DefineMorphShape", 48: "DefineFont2", 56: "ExportAssets", 57: "ImportAssets", 58: "EnableDebugger",
    59: "DoInitAction", 60: "DefineVideoStream", 61: "VideoFrame", 62: "DefineFontInfo2", 63: "DebugID",
    64: "EnableDebugger2", 65: "ScriptLimits", 66: "SetTabIndex", 69: "FileAttributes", 70: "PlaceObject3",
    71: "ImportAssets2", 72: "DoABC", 73: "DefineFontAlignZones", 74: "CSMTextSettings", 75: "DefineFont3",
    76: "SymbolClass", 77: "Metadata", 78: "DefineScalingGrid", 82: "DoABC2", 83: "DefineShape4",
    84: "DefineMorphShape2", 86: "DefineSceneAndFrameLabelData", 87: "DefineBinaryData", 88: "DefineFontName",
    89: "StartSound2", 90: "DefineBitsJPEG4", 91: "DefineFont4", 93: "EnableTelemetry",
    # extensoes Scaleform GFx
    1000: "ExporterInfo", 1001: "DefineExternalImage", 1002: "FontTextureInfo", 1003: "DefineExternalGradient",
    1004: "DefineGradientMap", 1005: "DefineCompactedFont", 1006: "DefineExternalSound",
    1007: "DefineExternalStreamSound", 1008: "DefineSubImage", 1009: "DefineExternalImage2",
}
IMAGE_TAGS = {6, 20, 21, 35, 36, 90}
SHAPE_TAGS = {2, 22, 32, 83, 46, 84}
FONT_TAGS = {10, 48, 75, 91, 1005}
SOUND_TAGS = {14}
TEXT_TAGS = {11, 33, 37}
BUTTON_TAGS = {7, 34}
DEFINE_TAGS = IMAGE_TAGS | SHAPE_TAGS | FONT_TAGS | SOUND_TAGS | TEXT_TAGS | BUTTON_TAGS | {39, 60, 87}
EXTERNAL_TAGS = {1001, 1006, 1007, 1009}


class SwfError(Exception):
    pass


@dataclass
class Tag:
    code: int
    offset: int
    data: memoryview

    @property
    def name(self) -> str:
        return TAG_NAMES.get(self.code, f"Unknown{self.code}")


@dataclass
class SwfInfo:
    signature: str
    compression: str
    version: int
    declared_length: int
    actual_length: int = 0
    frame_size: tuple[float, float, float, float] = (0, 0, 0, 0)
    frame_rate: float = 0.0
    frame_count: int = 0
    background: str | None = None
    as3: bool | None = None
    use_network: bool | None = None
    metadata: str | None = None
    product_info: dict | None = None
    exporter_info: dict | None = None
    tag_counts: Counter = field(default_factory=Counter)
    exports: list[dict] = field(default_factory=list)
    imports: list[dict] = field(default_factory=list)
    symbol_classes: list[dict] = field(default_factory=list)
    abc: list[dict] = field(default_factory=list)  # um por tag DoABC
    classes: list[dict] = field(default_factory=list)
    as2_actions: int = 0  # tags DoAction/DoInitAction
    fonts: list[dict] = field(default_factory=list)
    external: list[dict] = field(default_factory=list)  # recursos externos (Scaleform)
    frame_labels: list[str] = field(default_factory=list)
    scenes: list[str] = field(default_factory=list)
    images: int = 0
    shapes: int = 0
    sprites: int = 0
    sounds: int = 0
    binary_data: int = 0
    texts: int = 0
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)  # componentes que falharam (ex.: ABC ilegivel)

    @property
    def code_kind(self) -> str:
        if self.abc:
            return "as3"
        if self.as2_actions:
            return "as2"
        return "none"

    def to_dict(self) -> dict:
        d = {
            "signature": self.signature, "compression": self.compression, "version": self.version,
            "declared_length": self.declared_length, "actual_length": self.actual_length,
            "frame_size_px": [round(v, 2) for v in self.frame_size], "frame_rate": self.frame_rate,
            "frame_count": self.frame_count, "background": self.background,
            "actionscript": self.code_kind, "as3_flag": self.as3, "use_network": self.use_network,
            "tags": {TAG_NAMES.get(k, f"Unknown{k}"): v for k, v in sorted(self.tag_counts.items())},
            "counts": {"images": self.images, "shapes": self.shapes, "sprites": self.sprites, "sounds": self.sounds,
                       "binary_data": self.binary_data, "texts": self.texts, "fonts": len(self.fonts),
                       "classes": len(self.classes), "abc_blocks": len(self.abc), "as2_action_tags": self.as2_actions},
            "exports": self.exports, "imports": self.imports, "symbol_classes": self.symbol_classes,
            "abc": self.abc, "classes": self.classes, "fonts": self.fonts, "external_resources": self.external,
            "frame_labels": self.frame_labels, "scenes": self.scenes,
            "parser": {"swf": SWF_PARSER_VERSION, "abc": ABC_PARSER_VERSION},
        }
        for k in ("metadata", "product_info", "exporter_info"):
            if getattr(self, k):
                d[k] = getattr(self, k)
        if self.warnings:
            d["warnings"] = self.warnings[:50]
        if self.errors:
            d["errors"] = self.errors[:50]
        return d


# ------------------------------------------------------------------ descompressao

def decompress(data: bytes, max_bytes: int = MAX_SWF_BYTES) -> tuple[SwfInfo, bytes]:
    """Cabecalho + corpo descomprimido (sem os 8 bytes iniciais)."""
    if len(data) < 8:
        raise SwfError("ficheiro demasiado pequeno para ser SWF")
    sig = data[:3]
    version = data[3]
    length = struct.unpack_from("<I", data, 4)[0]
    if length > max_bytes:
        raise SwfError(f"tamanho declarado {length} B acima do limite de {max_bytes} B")
    want = max(0, length - 8)
    if sig == b"FWS":
        info = SwfInfo("FWS", "none", version, length)
        body = data[8:]
    elif sig == b"CWS":
        info = SwfInfo("CWS", "zlib", version, length)
        d = zlib.decompressobj()
        try:
            body = d.decompress(data[8:], want + 1)
        except zlib.error as exc:
            raise SwfError(f"zlib: {exc}") from exc
    elif sig == b"ZWS":
        info = SwfInfo("ZWS", "lzma", version, length)
        if len(data) < 17:
            raise SwfError("cabecalho LZMA truncado")
        props = data[12:17]
        pb, rem = divmod(props[0], 45)
        lp, lc = divmod(rem, 9)
        filt = {"id": lzma.FILTER_LZMA1, "dict_size": struct.unpack_from("<I", props, 1)[0],
                "lc": lc, "lp": lp, "pb": pb}
        try:
            d = lzma.LZMADecompressor(lzma.FORMAT_RAW, filters=[filt])
            body = d.decompress(data[17:], want + 1)
        except lzma.LZMAError as exc:
            raise SwfError(f"lzma: {exc}") from exc
    else:
        raise SwfError(f"assinatura desconhecida: {sig!r}")
    if len(body) > want:
        info.warnings.append(f"dados descomprimidos excedem o tamanho declarado ({want} B); cortados")
        body = body[:want]
    elif len(body) < want:
        info.warnings.append(f"corpo com {len(body)} B, menos do que os {want} B declarados")
    info.actual_length = len(body) + 8
    return info, body


# ------------------------------------------------------------------ tags

def _cstring(b: memoryview, p: int) -> tuple[str, int]:
    end = bytes(b[p:]).find(b"\x00")
    if end < 0:
        raise SwfError("string sem terminador")
    raw = bytes(b[p:p + end])
    return raw.decode("utf-8", "replace"), p + end + 1


def _enc_u32(b: memoryview, p: int) -> tuple[int, int]:
    result = shift = 0
    for _ in range(5):
        v = b[p]
        p += 1
        result |= (v & 0x7F) << shift
        if not v & 0x80:
            break
        shift += 7
    return result, p


def iter_tags(body: memoryview, start: int, end: int, warnings: list[str]):
    p = start
    while p + 2 <= end:
        h = body[p] | (body[p + 1] << 8)
        p += 2
        code, ln = h >> 6, h & 0x3F
        if ln == 0x3F:
            if p + 4 > end:
                warnings.append(f"cabecalho de tag truncado no byte {p}")
                return
            ln = struct.unpack_from("<I", body, p)[0]
            p += 4
        if p + ln > end:
            warnings.append(f"tag {TAG_NAMES.get(code, code)} truncada no byte {p} ({ln} B declarados)")
            return
        yield Tag(code, p, body[p:p + ln])
        p += ln
        if code == 0:
            return
    if p < end:
        warnings.append(f"{end - p} B sem tag no fim")


def _rect(body: bytes) -> tuple[tuple[float, float, float, float], int]:
    nbits = body[0] >> 3
    total = 5 + 4 * nbits
    nbytes = (total + 7) // 8
    if len(body) < nbytes + 4:
        raise SwfError("cabecalho SWF truncado")
    val = int.from_bytes(body[:nbytes], "big")
    vals = []
    for i in range(4):
        shift = nbytes * 8 - 5 - nbits * (i + 1)
        v = (val >> shift) & ((1 << nbits) - 1) if nbits else 0
        if nbits and v & (1 << (nbits - 1)):
            v -= 1 << nbits
        vals.append(v / 20.0)
    return (vals[0], vals[1], vals[2], vals[3]), nbytes


def _symbol_list(d: memoryview, p: int, what: str) -> list[dict]:
    n = struct.unpack_from("<H", d, p)[0]
    p += 2
    out = []
    for _ in range(n):
        cid = struct.unpack_from("<H", d, p)[0]
        name, p = _cstring(d, p + 2)
        out.append({"id": cid, what: name})
    return out


def parse_swf(data: bytes, with_abc: bool = True, keep_abc: bool = False) -> tuple[SwfInfo, list[tuple[str, AbcFile]]]:
    """Catalogo do SWF. Devolve tambem os blocos ABC lidos (se keep_abc)."""
    info, body = decompress(data)
    mv = memoryview(body)
    info.frame_size, n = _rect(body)
    info.frame_rate = body[n + 1] + body[n] / 256.0
    info.frame_count = struct.unpack_from("<H", body, n + 2)[0]
    abcs: list[tuple[str, AbcFile]] = []
    _walk(info, mv, n + 4, len(body), 0, with_abc, keep_abc, abcs)
    return info, abcs


def _walk(info: SwfInfo, mv: memoryview, start: int, end: int, depth: int, with_abc: bool, keep_abc: bool,
          abcs: list) -> None:
    for tag in iter_tags(mv, start, end, info.warnings):
        info.tag_counts[tag.code] += 1
        d = tag.data
        try:
            _handle(info, tag, d, depth, with_abc, keep_abc, abcs)
        except (SwfError, struct.error, IndexError, ValueError) as exc:
            info.errors.append(f"tag {tag.name} no byte {tag.offset}: {type(exc).__name__}: {exc}")


def _handle(info, tag, d, depth, with_abc, keep_abc, abcs) -> None:
    c = tag.code
    if c == 69 and len(d) >= 1:
        info.as3 = bool(d[0] & 0x08)
        info.use_network = bool(d[0] & 0x01)
    elif c == 9 and len(d) >= 3:
        info.background = f"#{d[0]:02x}{d[1]:02x}{d[2]:02x}"
    elif c == 77:
        info.metadata = bytes(d).rstrip(b"\x00").decode("utf-8", "replace")[:4000]
    elif c == 41 and len(d) >= 26:
        prod, ed, major, minor, build_lo, build_hi = struct.unpack_from("<IIBBII", d, 0)
        info.product_info = {"product": prod, "edition": ed, "version": f"{major}.{minor}",
                             "build": build_lo | (build_hi << 32)}
    elif c == 1000 and len(d) >= 4:
        info.exporter_info = {"version": struct.unpack_from("<H", d, 0)[0]}
    elif c == 56:
        info.exports.extend(_symbol_list(d, 0, "name"))
    elif c in (57, 71):
        url, p = _cstring(d, 0)
        if c == 71:
            p += 2
        info.imports.append({"url": url, "symbols": _symbol_list(d, p, "name")})
    elif c == 76:
        info.symbol_classes.extend(_symbol_list(d, 0, "class"))
    elif c in (72, 82):
        name, flags, p = "", None, 0
        if c == 82:
            flags = struct.unpack_from("<I", d, 0)[0]
            name, p = _cstring(d, 4)
        block = {"name": name, "lazy": bool(flags & 1) if flags is not None else None, "size": len(d) - p}
        info.abc.append(block)
        if with_abc:
            try:
                abc = parse_abc(bytes(d[p:]))
            except AbcError as exc:
                block["error"] = str(exc)
                info.errors.append(f"ABC '{name}': {exc}")
                return
            cls = abc.class_list()
            block.update(classes=len(cls), methods=len(abc.methods), bodies=abc.bodies, code_bytes=abc.code_bytes)
            for cl in cls:
                cl["abc"] = len(info.abc) - 1
            info.classes.extend(cls)
            if keep_abc:
                abcs.append((name, abc))
    elif c in (12, 59):
        info.as2_actions += 1
    elif c in FONT_TAGS and len(d) >= 4:
        info.fonts.append(_font(c, d))
    elif c == 88 and len(d) >= 3:
        cid = struct.unpack_from("<H", d, 0)[0]
        name, _ = _cstring(d, 2)
        for f in info.fonts:
            if f["id"] == cid:
                f["full_name"] = name
    elif c in EXTERNAL_TAGS:
        info.external.append(_external(c, d))
    elif c == 43:
        info.frame_labels.append(_cstring(d, 0)[0])
    elif c == 86:
        n, p = _enc_u32(d, 0)
        for _ in range(min(n, 10000)):
            _, p = _enc_u32(d, p)
            name, p = _cstring(d, p)
            info.scenes.append(name)
    elif c == 39 and len(d) >= 4:
        info.sprites += 1
        if depth < MAX_SPRITE_DEPTH:
            # tags dentro do sprite: so contagens (sem definicoes de nivel superior)
            sub = Counter()
            for t in iter_tags(d, 4, len(d), info.warnings):
                sub[t.code] += 1
            for k, v in sub.items():
                info.tag_counts[k] += v
            info.as2_actions += sub[12] + sub[59]
    if c in IMAGE_TAGS:
        info.images += 1
    elif c in SHAPE_TAGS:
        info.shapes += 1
    elif c in SOUND_TAGS:
        info.sounds += 1
    elif c == 87:
        info.binary_data += 1
    elif c in TEXT_TAGS:
        info.texts += 1


def _font(code: int, d: memoryview) -> dict:
    cid = struct.unpack_from("<H", d, 0)[0]
    f = {"id": cid, "tag": TAG_NAMES[code]}
    if code in (48, 75) and len(d) >= 5:
        flags = d[2]
        nlen = d[4]
        f["name"] = bytes(d[5:5 + nlen]).rstrip(b"\x00").decode("utf-8", "replace")
        if len(d) >= 7 + nlen:
            f["glyphs"] = struct.unpack_from("<H", d, 5 + nlen)[0]
        f["bold"] = bool(flags & 0x01)
        f["italic"] = bool(flags & 0x02)
    elif code == 91 and len(d) >= 4:
        f["name"] = _cstring(d, 3)[0]
    return f


def _external(code: int, d: memoryview) -> dict:
    """Recurso externo Scaleform: so tipo e tamanho (o formato varia entre versoes do GFx)."""
    return {"tag": TAG_NAMES.get(code, str(code)), "size": len(d)}


# ------------------------------------------------------------------ .swc

MAX_SWC_SWF = 256 * 1024 * 1024


def swf_from_container(data: bytes, name: str) -> tuple[bytes, str | None]:
    """Para .swc (ZIP com library.swf) devolve o library.swf; senao os proprios dados."""
    if not name.lower().endswith(".swc"):
        return data, None
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as zf:
            infos = {i.filename: i for i in zf.infolist()}
            info = infos.get("library.swf")
            if info is None:
                raise SwfError("SWC sem library.swf")
            if info.file_size > MAX_SWC_SWF:
                raise SwfError(f"library.swf com {info.file_size} B acima do limite")
            return zf.read(info), "library.swf"
    except zipfile.BadZipFile as exc:
        raise SwfError(f"SWC invalido: {exc}") from exc
