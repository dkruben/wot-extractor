"""Gerador minimo de SWF e ABC para testes (so dados; nada e executado)."""

from __future__ import annotations

import struct
import zlib


def u30(v: int) -> bytes:
    out = bytearray()
    while True:
        b = v & 0x7F
        v >>= 7
        if v:
            out.append(b | 0x80)
        else:
            out.append(b)
            return bytes(out)


def s(text: str) -> bytes:
    raw = text.encode("utf-8")
    return u30(len(raw)) + raw


def make_abc(classes=(("net.test", "Foo", "flash.display", "Sprite"),), extra_method_names=False) -> bytes:
    """ABC com classes `pkg.Name extends superPkg.Super`, um campo const e um metodo `run(a:int, b:String="x"):void`."""
    strings = [""]
    namespaces = [None]
    multinames = [None]

    def si(t):
        if t not in strings:
            strings.append(t)
        return strings.index(t)

    def nsi(kind, name):
        key = (kind, si(name))
        if key not in namespaces:
            namespaces.append(key)
        return namespaces.index(key)

    def qn(pkg, name, kind=0x16):
        key = (0x07, nsi(kind, pkg), si(name))
        if key not in multinames:
            multinames.append(key)
        return multinames.index(key)

    int_mn = qn("", "int")
    str_mn = qn("", "String")
    void_mn = qn("", "void")
    methods = []  # (params, ret, flags, optional, names)
    insts = []
    for pkg, name, spkg, sup in classes:
        cname = qn(pkg, name)
        sname = qn(spkg, sup)
        iinit = len(methods)
        methods.append(([], 0, 0, [], []))
        cinit = len(methods)
        methods.append(([], 0, 0, [], []))
        run = len(methods)
        methods.append(([int_mn, str_mn], void_mn, 0x08 | (0x80 if extra_method_names else 0),
                        [(si("x"), 0x01)], ["a", "b"] if extra_method_names else []))
        const_name = qn("", "LIMIT")
        run_name = qn("", "run")
        sinit = len(methods)
        methods.append(([], 0, 0, [], []))
        insts.append((cname, sname, iinit, cinit, run, const_name, run_name, sinit))

    out = bytearray(struct.pack("<HH", 16, 46))
    out += u30(0) + u30(0) + u30(0)  # int, uint, double
    # strings sao precisas antes, mas sao criadas ao montar; montar o resto num buffer
    body = bytearray()
    body += u30(len(namespaces))
    for kind, name in namespaces[1:]:
        body += bytes([kind]) + u30(name)
    body += u30(0)  # ns_sets
    body += u30(len(multinames))
    for kind, ns, name in multinames[1:]:
        body += bytes([kind]) + u30(ns) + u30(name)
    body += u30(len(methods))
    for params, ret, flags, opt, names in methods:
        body += u30(len(params)) + u30(ret) + b"".join(u30(p) for p in params) + u30(0) + bytes([flags])
        if flags & 0x08:
            body += u30(len(opt)) + b"".join(u30(v) + bytes([k]) for v, k in opt)
        if flags & 0x80:
            body += b"".join(u30(si(n)) for n in names)
    body += u30(0)  # metadata
    body += u30(len(insts))
    for cname, sname, iinit, cinit, run, const_name, run_name, _ in insts:
        body += u30(cname) + u30(sname) + bytes([0x01]) + u30(0) + u30(iinit)
        body += u30(1) + u30(run_name) + bytes([0x01]) + u30(0) + u30(run)  # trait metodo
    for cname, sname, iinit, cinit, run, const_name, run_name, _ in insts:
        body += u30(cinit) + u30(1) + u30(const_name) + bytes([0x06]) + u30(0) + u30(int_mn) + u30(0)
    body += u30(len(insts))  # um script por classe, com o trait da classe
    for ci, inst in enumerate(insts):
        body += u30(inst[7]) + u30(1) + u30(inst[0]) + bytes([0x04]) + u30(1) + u30(ci)
    body += u30(len(methods))
    for i in range(len(methods)):
        code = b"\xd0\x30\x47"  # getlocal_0, pushscope, returnvoid
        body += u30(i) + u30(1) + u30(1) + u30(0) + u30(1) + u30(len(code)) + code + u30(0) + u30(0)
    out += u30(len(strings))
    for t in strings[1:]:
        out += s(t)
    return bytes(out + body)


def tag(code: int, data: bytes) -> bytes:
    if len(data) < 0x3F:
        return struct.pack("<H", (code << 6) | len(data)) + data
    return struct.pack("<HI", (code << 6) | 0x3F, len(data)) + data


def make_swf(tags: list[bytes], version: int = 11, compress: str = "zlib") -> bytes:
    rect = bytes([0x00])  # RECT com nbits=0
    body = rect + struct.pack("<BBH", 0, 30, 1) + b"".join(tags) + tag(0, b"")
    length = 8 + len(body)
    if compress == "zlib":
        return b"CWS" + bytes([version]) + struct.pack("<I", length) + zlib.compress(body)
    if compress == "lzma":
        import lzma
        filt = {"id": lzma.FILTER_LZMA1, "dict_size": 1 << 16, "lc": 3, "lp": 0, "pb": 2}
        comp = lzma.compress(body, format=lzma.FORMAT_RAW, filters=[filt])
        props = bytes([(2 * 5 + 0) * 9 + 3]) + struct.pack("<I", 1 << 16)
        return b"ZWS" + bytes([version]) + struct.pack("<II", length, len(comp)) + props + comp
    return b"FWS" + bytes([version]) + struct.pack("<I", length) + body


def sample_swf(compress="zlib", with_abc=True) -> bytes:
    tags = [tag(69, bytes([0x08, 0, 0, 0])), tag(9, b"\x10\x20\x30")]
    tags.append(tag(71, b"lib.swf\x00\x01\x00" + struct.pack("<H", 1) + struct.pack("<H", 5) + b"Btn\x00"))
    tags.append(tag(56, struct.pack("<H", 1) + struct.pack("<H", 2) + b"Panel\x00"))
    tags.append(tag(75, struct.pack("<H", 3) + bytes([0x01, 0, 5]) + b"Arial" + struct.pack("<H", 0)))
    tags.append(tag(43, b"start\x00"))
    if with_abc:
        tags.append(tag(82, struct.pack("<I", 1) + b"frame1\x00" + make_abc()))
        tags.append(tag(76, struct.pack("<H", 1) + struct.pack("<H", 0) + b"net.test.Foo\x00"))
    tags.append(tag(1, b""))
    return make_swf(tags, compress=compress)
