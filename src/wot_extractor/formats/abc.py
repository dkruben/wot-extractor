"""Leitor de bytecode ActionScript 3 (ABC, AVM2) - so leitura, nada e executado.

Le a estrutura completa de um bloco ABC (tag DoABC/DoABC2): constantes,
metodos, metadados, classes, scripts e corpos de metodos. Serve para:
  - inventariar as classes de cada SWF (verificar se o descompilador externo
    exportou todas);
  - gerar declaracoes AS3 (pacote, classe, heranca, campos, assinaturas) quando
    nao ha descompilador, sem inventar nada: tudo vem do bytecode.

Referencia: "ActionScript Virtual Machine 2 (AVM2) Overview" (Adobe, 2007).
"""

from __future__ import annotations

import json
import math
import struct
from dataclasses import dataclass, field

PARSER_VERSION = 1

# tipos de namespace
NS_PRIVATE = 0x05
NS_NAMESPACE = 0x08
NS_PACKAGE = 0x16
NS_PACKAGE_INTERNAL = 0x17
NS_PROTECTED = 0x18
NS_EXPLICIT = 0x19
NS_STATIC_PROTECTED = 0x1A
NS_KINDS = {NS_PRIVATE, NS_NAMESPACE, NS_PACKAGE, NS_PACKAGE_INTERNAL, NS_PROTECTED, NS_EXPLICIT,
            NS_STATIC_PROTECTED}

# multinames
MN_QNAME, MN_QNAMEA = 0x07, 0x0D
MN_RTQNAME, MN_RTQNAMEA = 0x0F, 0x10
MN_RTQNAMEL, MN_RTQNAMELA = 0x11, 0x12
MN_MULTINAME, MN_MULTINAMEA = 0x09, 0x0E
MN_MULTINAMEL, MN_MULTINAMELA = 0x1B, 0x1C
MN_TYPENAME = 0x1D

# metodos
M_NEED_REST = 0x04
M_HAS_OPTIONAL = 0x08
M_HAS_PARAM_NAMES = 0x80

# classes
C_SEALED, C_FINAL, C_INTERFACE, C_PROTECTED_NS = 0x01, 0x02, 0x04, 0x08

# traits
T_SLOT, T_METHOD, T_GETTER, T_SETTER, T_CLASS, T_FUNCTION, T_CONST = range(7)
A_FINAL, A_OVERRIDE, A_METADATA = 0x1, 0x2, 0x4


class AbcError(Exception):
    pass


class _Reader:
    __slots__ = ("d", "p", "n")

    def __init__(self, data: bytes):
        self.d = data
        self.p = 0
        self.n = len(data)

    def need(self, k: int) -> None:
        if self.p + k > self.n:
            raise AbcError(f"fim inesperado dos dados no byte {self.p} (faltam {self.p + k - self.n} B)")

    def u8(self) -> int:
        self.need(1)
        v = self.d[self.p]
        self.p += 1
        return v

    def u16(self) -> int:
        self.need(2)
        v = self.d[self.p] | (self.d[self.p + 1] << 8)
        self.p += 2
        return v

    def u32v(self) -> int:
        """Inteiro de comprimento variavel (u30/u32: ate 5 bytes de 7 bits)."""
        result = shift = 0
        for _ in range(5):
            if self.p >= self.n:
                raise AbcError(f"inteiro variavel truncado no byte {self.p}")
            b = self.d[self.p]
            self.p += 1
            result |= (b & 0x7F) << shift
            if not b & 0x80:
                return result & 0xFFFFFFFF
            shift += 7
        return result & 0xFFFFFFFF

    def s32v(self) -> int:
        v = self.u32v()
        return v - 0x100000000 if v & 0x80000000 else v

    def d64(self) -> float:
        self.need(8)
        v = struct.unpack_from("<d", self.d, self.p)[0]
        self.p += 8
        return v

    def raw(self, k: int) -> bytes:
        self.need(k)
        v = self.d[self.p:self.p + k]
        self.p += k
        return bytes(v)

    def count(self, what: str, min_bytes: int = 1) -> int:
        """Contagem com verificacao: cada item ocupa pelo menos `min_bytes`."""
        c = self.u32v()
        if c * min_bytes > self.n - self.p:
            raise AbcError(f"contagem impossivel de {what}: {c} (restam {self.n - self.p} B)")
        return c


@dataclass
class Namespace:
    kind: int
    name: str


@dataclass
class Multiname:
    kind: int
    name: str | None = None  # None = nome em tempo de execucao
    ns: int = 0  # indice de namespace (QName)
    ns_set: int = 0  # indice de conjunto de namespaces (Multiname)
    qname: int = 0  # TypeName: tipo base
    params: tuple[int, ...] = ()  # TypeName: parametros


@dataclass
class MethodInfo:
    params: list[int]
    return_type: int
    name: str
    flags: int
    optional: list[tuple[int, int]] = field(default_factory=list)  # (indice do valor, tipo)
    param_names: list[str] = field(default_factory=list)
    body_size: int | None = None  # bytes de bytecode (None = sem corpo, ex.: interface/nativo)


@dataclass
class Trait:
    name: int
    kind: int
    attrs: int
    slot_id: int = 0
    type_name: int = 0
    vindex: int = 0
    vkind: int = 0
    index: int = 0  # metodo, classe ou funcao
    metadata: list[int] = field(default_factory=list)


@dataclass
class Metadata:
    name: str
    items: list[tuple[str, str]]


@dataclass
class ClassInfo:
    name: int
    super_name: int
    flags: int
    protected_ns: int
    interfaces: list[int]
    iinit: int
    itraits: list[Trait]
    cinit: int = 0
    ctraits: list[Trait] = field(default_factory=list)


@dataclass
class Script:
    init: int
    traits: list[Trait]


@dataclass
class AbcFile:
    minor: int
    major: int
    ints: list[int]
    uints: list[int]
    doubles: list[float]
    strings: list[str]
    namespaces: list[Namespace]
    ns_sets: list[list[int]]
    multinames: list[Multiname]
    methods: list[MethodInfo]
    metadata: list[Metadata]
    classes: list[ClassInfo]
    scripts: list[Script]
    bodies: int = 0
    code_bytes: int = 0
    non_utf8_strings: int = 0

    # ---------------------------------------------------------------- nomes
    def ns_name(self, i: int) -> str:
        return self.namespaces[i].name if 0 < i < len(self.namespaces) else ""

    def qualified(self, mn_index: int) -> tuple[str, str]:
        """(pacote, nome) de um multiname; pacote vazio se nao for QName de pacote."""
        if not 0 < mn_index < len(self.multinames):
            return "", "*"
        m = self.multinames[mn_index]
        if m.kind in (MN_QNAME, MN_QNAMEA):
            ns = self.namespaces[m.ns] if 0 < m.ns < len(self.namespaces) else None
            pkg = ns.name if ns and ns.kind in (NS_PACKAGE, NS_PACKAGE_INTERNAL) else ""
            return pkg, m.name or ""
        if m.kind == MN_TYPENAME:
            base = self.qualified(m.qname)
            params = ", ".join(self.type_str(p) for p in m.params)
            return base[0], f"{base[1]}.<{params}>"
        return "", m.name if m.name is not None else "*"

    def full_name(self, mn_index: int) -> str:
        pkg, name = self.qualified(mn_index)
        return f"{pkg}.{name}" if pkg else name

    def type_str(self, mn_index: int) -> str:
        if mn_index == 0:
            return "*"
        return self.full_name(mn_index)

    def trait_namespace(self, t: Trait) -> Namespace | None:
        m = self.multinames[t.name] if 0 < t.name < len(self.multinames) else None
        if m and m.kind in (MN_QNAME, MN_QNAMEA) and 0 < m.ns < len(self.namespaces):
            return self.namespaces[m.ns]
        return None

    def class_list(self) -> list[dict]:
        out = []
        for c in self.classes:
            pkg, name = self.qualified(c.name)
            kind = "interface" if c.flags & C_INTERFACE else "class"
            m = self.multinames[c.name]
            ns = self.namespaces[m.ns] if m.kind in (MN_QNAME, MN_QNAMEA) and 0 < m.ns < len(self.namespaces) else None
            item = {"name": f"{pkg}.{name}" if pkg else name, "kind": kind,
                    "extends": self.full_name(c.super_name) if c.super_name else None,
                    "implements": [self.full_name(i) for i in c.interfaces]}
            if ns is not None and ns.kind == NS_PRIVATE:
                item["private"] = True  # classe auxiliar no ficheiro de outra classe
            out.append(item)
        return out


# ------------------------------------------------------------------ leitura

def _traits(r: _Reader) -> list[Trait]:
    out = []
    for _ in range(r.count("traits", 2)):
        name = r.u32v()
        kb = r.u8()
        kind, attrs = kb & 0x0F, kb >> 4
        t = Trait(name, kind, attrs)
        if kind in (T_SLOT, T_CONST):
            t.slot_id = r.u32v()
            t.type_name = r.u32v()
            t.vindex = r.u32v()
            if t.vindex:
                t.vkind = r.u8()
        elif kind in (T_METHOD, T_GETTER, T_SETTER, T_CLASS, T_FUNCTION):
            t.slot_id = r.u32v()
            t.index = r.u32v()
        else:
            raise AbcError(f"tipo de trait desconhecido: {kind}")
        if attrs & A_METADATA:
            t.metadata = [r.u32v() for _ in range(r.count("metadados do trait"))]
        out.append(t)
    return out


def parse_abc(data: bytes) -> AbcFile:
    r = _Reader(data)
    minor, major = r.u16(), r.u16()
    if major != 46:
        raise AbcError(f"versao ABC nao suportada: {major}.{minor} (esperado 46.x)")

    def pool(what, reader, min_bytes=1):
        n = r.count(what, min_bytes)
        return [None] + [reader() for _ in range(max(0, n - 1))]

    ints = pool("inteiros", r.s32v)
    uints = pool("inteiros sem sinal", r.u32v)
    doubles = pool("doubles", r.d64, 8)
    bad_utf8 = 0

    def string():
        nonlocal bad_utf8
        raw = r.raw(r.u32v())
        try:
            return raw.decode("utf-8")
        except UnicodeDecodeError:
            bad_utf8 += 1
            return raw.decode("utf-8", "replace")

    strings = pool("strings", string)
    strings[0] = ""

    def namespace():
        kind = r.u8()
        if kind not in NS_KINDS:
            raise AbcError(f"tipo de namespace desconhecido: 0x{kind:02x}")
        return Namespace(kind, _s(strings, r.u32v()))

    namespaces = pool("namespaces", namespace, 2)
    ns_sets = pool("conjuntos de namespaces", lambda: [r.u32v() for _ in range(r.count("namespaces do conjunto"))])

    def multiname():
        kind = r.u8()
        if kind in (MN_QNAME, MN_QNAMEA):
            ns = r.u32v()
            return Multiname(kind, _s(strings, r.u32v()), ns=ns)
        if kind in (MN_RTQNAME, MN_RTQNAMEA):
            return Multiname(kind, _s(strings, r.u32v()))
        if kind in (MN_RTQNAMEL, MN_RTQNAMELA):
            return Multiname(kind)
        if kind in (MN_MULTINAME, MN_MULTINAMEA):
            name = _s(strings, r.u32v())
            return Multiname(kind, name, ns_set=r.u32v())
        if kind in (MN_MULTINAMEL, MN_MULTINAMELA):
            return Multiname(kind, ns_set=r.u32v())
        if kind == MN_TYPENAME:
            q = r.u32v()
            return Multiname(kind, qname=q, params=tuple(r.u32v() for _ in range(r.count("parametros do tipo"))))
        raise AbcError(f"tipo de multiname desconhecido: 0x{kind:02x}")

    multinames = pool("multinames", multiname)

    methods = []
    for _ in range(r.count("metodos", 4)):
        pc = r.u32v()
        if pc > r.n - r.p:
            raise AbcError(f"numero de parametros impossivel: {pc}")
        ret = r.u32v()
        params = [r.u32v() for _ in range(pc)]
        name = _s(strings, r.u32v())
        flags = r.u8()
        mi = MethodInfo(params, ret, name, flags)
        if flags & M_HAS_OPTIONAL:
            for _ in range(r.count("parametros opcionais", 2)):
                v = r.u32v()
                mi.optional.append((v, r.u8()))
        if flags & M_HAS_PARAM_NAMES:
            mi.param_names = [_s(strings, r.u32v()) for _ in range(pc)]
        methods.append(mi)

    metadata = []
    for _ in range(r.count("metadados", 2)):
        name = _s(strings, r.u32v())
        n = r.count("itens de metadados", 2)
        keys = [_s(strings, r.u32v()) for _ in range(n)]
        vals = [_s(strings, r.u32v()) for _ in range(n)]
        metadata.append(Metadata(name, list(zip(keys, vals))))

    n_classes = r.count("classes", 5)
    classes = []
    for _ in range(n_classes):
        name, sup, flags = r.u32v(), r.u32v(), r.u8()
        pns = r.u32v() if flags & C_PROTECTED_NS else 0
        intf = [r.u32v() for _ in range(r.count("interfaces"))]
        iinit = r.u32v()
        classes.append(ClassInfo(name, sup, flags, pns, intf, iinit, _traits(r)))
    for c in classes:
        c.cinit = r.u32v()
        c.ctraits = _traits(r)

    scripts = []
    for _ in range(r.count("scripts", 2)):
        init = r.u32v()
        scripts.append(Script(init, _traits(r)))

    abc = AbcFile(minor, major, ints, uints, doubles, strings, namespaces, ns_sets, multinames, methods,
                  metadata, classes, scripts)
    abc.non_utf8_strings = bad_utf8
    n_bodies = r.count("corpos de metodos", 6)
    for _ in range(n_bodies):
        m = r.u32v()
        for _ in range(4):  # max_stack, locals, init/max scope depth
            r.u32v()
        code_len = r.u32v()
        r.need(code_len)
        r.p += code_len
        for _ in range(r.count("excecoes", 5)):
            for _ in range(5):
                r.u32v()
        _traits(r)
        if not 0 <= m < len(methods):
            raise AbcError(f"corpo para metodo inexistente: {m}")
        methods[m].body_size = code_len
        abc.code_bytes += code_len
    abc.bodies = n_bodies
    if r.p != r.n:
        raise AbcError(f"{r.n - r.p} B por ler no fim do bloco ABC")
    _check_refs(abc)
    return abc


def _s(strings: list, i: int) -> str:
    if not 0 <= i < len(strings):
        raise AbcError(f"indice de string fora do limite: {i}")
    return strings[i] if i else ""


def _check_refs(abc: AbcFile) -> None:
    nm, nmeth = len(abc.multinames), len(abc.methods)
    for c in abc.classes:
        if not 0 < c.name < nm or c.super_name >= nm or not 0 <= c.iinit < nmeth or not 0 <= c.cinit < nmeth:
            raise AbcError("classe com referencias fora dos limites")
    for m in abc.multinames[1:]:
        if m.kind in (MN_QNAME, MN_QNAMEA) and m.ns >= len(abc.namespaces):
            raise AbcError("multiname com namespace fora dos limites")


# ------------------------------------------------------------------ declaracoes AS3

def _const_value(abc: AbcFile, vindex: int, vkind: int) -> str | None:
    try:
        if vkind == 0x01:
            return json.dumps(abc.strings[vindex], ensure_ascii=False)
        if vkind == 0x03:
            return str(abc.ints[vindex])
        if vkind == 0x04:
            return str(abc.uints[vindex])
        if vkind == 0x06:
            v = abc.doubles[vindex]
            if math.isnan(v):
                return "NaN"
            if math.isinf(v):
                return "Infinity" if v > 0 else "-Infinity"
            return repr(v)[:-2] if repr(v).endswith(".0") else repr(v)
        if vkind == 0x0A:
            return "false"
        if vkind == 0x0B:
            return "true"
        if vkind == 0x0C:
            return "null"
        if vkind == 0x00:
            return "undefined"
        if vkind in NS_KINDS:
            return json.dumps(abc.namespaces[vindex].name, ensure_ascii=False)
    except (IndexError, TypeError):
        return None
    return None


def _visibility(abc: AbcFile, t: Trait) -> str:
    ns = abc.trait_namespace(t)
    if ns is None:
        return ""
    if ns.kind == NS_PACKAGE:
        return "public"
    if ns.kind == NS_PRIVATE:
        return "private"
    if ns.kind in (NS_PROTECTED, NS_STATIC_PROTECTED):
        return "protected"
    if ns.kind == NS_PACKAGE_INTERNAL:
        return "internal"
    return ns.name or "internal"  # namespace definido pelo utilizador (ex.: mx_internal)


class _Types:
    """Nomes de tipo curtos + imports (nome completo quando ha conflito)."""

    def __init__(self, abc: AbcFile, own_pkg: str):
        self.abc = abc
        self.own_pkg = own_pkg
        self.imports: dict[str, str] = {}  # nome curto -> nome completo

    def __call__(self, mn_index: int) -> str:
        if mn_index == 0:
            return "*"
        m = self.abc.multinames[mn_index] if mn_index < len(self.abc.multinames) else None
        if m is not None and m.kind == MN_TYPENAME:
            base = self(m.qname)
            return f"{base}.<{', '.join(self(p) for p in m.params)}>"
        pkg, name = self.abc.qualified(mn_index)
        if not pkg or pkg == self.own_pkg:
            return name
        full = f"{pkg}.{name}"
        have = self.imports.get(name)
        if have is None:
            self.imports[name] = full
            return name
        return name if have == full else full


def _signature(abc: AbcFile, mi: MethodInfo, ty: _Types, is_setter=False) -> str:
    parts = []
    n = len(mi.params)
    first_opt = n - len(mi.optional)
    for i, p in enumerate(mi.params):
        pname = mi.param_names[i] if i < len(mi.param_names) and mi.param_names[i] else f"param{i + 1}"
        s = f"{pname}:{ty(p)}"
        if i >= first_opt:
            vi, vk = mi.optional[i - first_opt]
            val = _const_value(abc, vi, vk)
            s += f" = {val if val is not None else '?'}"
        parts.append(s)
    if mi.flags & M_NEED_REST:
        parts.append("... rest")
    return "(" + ", ".join(parts) + ")"


def _metadata_lines(abc: AbcFile, idx: list[int], indent: str) -> list[str]:
    out = []
    for i in idx:
        if not 0 <= i < len(abc.metadata):
            continue
        md = abc.metadata[i]
        args = ", ".join(f'{k}="{v}"' if k else f'"{v}"' for k, v in md.items)
        out.append(f"{indent}[{md.name}{'(' + args + ')' if args else ''}]")
    return out


def _body(mi: MethodInfo) -> str:
    if mi.body_size is None:
        return " { }  // sem corpo no bytecode (nativo)"
    return f" {{ /* corpo nao descompilado: {mi.body_size} B de bytecode AVM2 */ }}"


def class_declaration(abc: AbcFile, ci: int, origin: str) -> tuple[str, str]:
    """(nome completo, texto .as) com as declaracoes da classe `ci`."""
    c = abc.classes[ci]
    pkg, name = abc.qualified(c.name)
    ty = _Types(abc, pkg)
    is_intf = bool(c.flags & C_INTERFACE)
    body: list[str] = []

    def member(t: Trait, static: bool) -> None:
        mod = []
        vis = _visibility(abc, t)
        if t.attrs & A_OVERRIDE:
            mod.append("override")
        if t.attrs & A_FINAL and t.kind in (T_METHOD, T_GETTER, T_SETTER) and not is_intf and not static:
            mod.append("final")
        if vis and not is_intf:
            mod.append(vis)
        if static:
            mod.append("static")
        pre = " ".join(mod) + (" " if mod else "")
        tname = abc.qualified(t.name)[1]
        body.extend(_metadata_lines(abc, t.metadata, "      "))
        if t.kind in (T_SLOT, T_CONST):
            decl = f"{pre}{'const' if t.kind == T_CONST else 'var'} {tname}:{ty(t.type_name)}"
            if t.vindex:
                v = _const_value(abc, t.vindex, t.vkind)
                if v is not None:
                    decl += f" = {v}"
            body.append(f"      {decl};")
        elif t.kind in (T_METHOD, T_GETTER, T_SETTER) and 0 <= t.index < len(abc.methods):
            mi = abc.methods[t.index]
            acc = {T_GETTER: "get ", T_SETTER: "set "}.get(t.kind, "")
            sig = f"{pre}function {acc}{tname}{_signature(abc, mi, ty)}:{ty(mi.return_type)}"
            body.append(f"      {sig}{';' if is_intf else _body(mi)}")
        elif t.kind == T_CLASS:
            body.append(f"      // classe interna: {tname}")
        elif t.kind == T_FUNCTION:
            body.append(f"      // funcao: {tname}")

    for t in c.ctraits:
        member(t, True)
    if c.ctraits:
        body.append("")
    if not is_intf and 0 <= c.iinit < len(abc.methods):
        mi = abc.methods[c.iinit]
        body.append(f"      public function {name}{_signature(abc, mi, ty)}{_body(mi)}")
        body.append("")
    for t in c.itraits:
        member(t, False)

    head = []
    if is_intf:
        head.append(f"public interface {name}")
        if c.interfaces:
            head.append(" extends " + ", ".join(ty(i) for i in c.interfaces))
    else:
        mods = ["public"]
        if c.flags & C_FINAL:
            mods.append("final")
        if not c.flags & C_SEALED:
            mods.append("dynamic")
        head.append(f"{' '.join(mods)} class {name}")
        if c.super_name and abc.full_name(c.super_name) != "Object":
            head.append(f" extends {ty(c.super_name)}")
        if c.interfaces:
            head.append(" implements " + ", ".join(ty(i) for i in c.interfaces))

    lines = [f"// wot-extractor: DECLARACOES recuperadas do bytecode ABC de {origin}",
             "// Os corpos dos metodos NAO foram descompilados (sem descompilador AS3 disponivel).",
             f"package {pkg}".rstrip() + " {", ""]
    for short, full in sorted(ty.imports.items(), key=lambda kv: kv[1]):
        lines.append(f"   import {full};")
    if ty.imports:
        lines.append("")
    lines.append("   " + "".join(head))
    lines.append("   {")
    lines.extend(body)
    lines.append("   }")
    lines.append("}")
    return (f"{pkg}.{name}" if pkg else name), "\n".join(lines) + "\n"
