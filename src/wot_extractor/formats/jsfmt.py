"""Lexer e formatador de JavaScript e CSS minificados (so biblioteca padrao).

A formatacao so mexe em espacos em branco: quebras de linha e indentacao entre tokens. Nunca remove uma
quebra de linha do original (o JavaScript usa-as na insercao automatica de ";") e so acrescenta quebras em
pontos seguros: depois de "{" e ";" (fora de parenteses), antes de "}" e entre "}" e o inicio de uma nova
instrucao. O resultado e verificado voltando a passar o lexer: a sequencia de tokens tem de ser identica.

Isto NAO recupera o codigo-fonte original: nomes encurtados, comentarios removidos e a estrutura do
webpack ficam como estao.
"""

from __future__ import annotations

import re

FORMATTER_VERSION = 1


class FormatError(ValueError):
    """O texto nao pode ser formatado com seguranca (lexer ou verificacao)."""


# ------------------------------------------------------------------ JavaScript

_PUNCT = sorted("""
>>>= ... === !== **= <<= >>= >>> &&= ||= ??= => == != <= >= && || ?? ?. ++ -- += -= *= /= %= &= |= ^= ** << >>
{ } ( ) [ ] ; , < > + - * / % & | ^ ! ~ ? : = . @
""".split(), key=len, reverse=True)
_PUNCT_RE = re.compile("|".join(re.escape(p) for p in _PUNCT))
_WS_RE = re.compile(r"[ \t\f\v ﻿  \r\n]+")
_NUM_RE = re.compile(r"0[xXoObB][0-9a-fA-F_]+n?|(?:\d[\d_]*\.?[\d_]*|\.\d[\d_]*)(?:[eE][+-]?\d[\d_]*)?n?")
_ID_START = re.compile(r"[A-Za-z_$\\\u0080-￿]")
_ID_RE = re.compile(r"(?:[A-Za-z0-9_$\u0080-￿]|\\u[0-9a-fA-F]{4}|\\u\{[0-9a-fA-F]+\})+")
_LINE_TERMINATORS = "\n\r  "

# depois destes identificadores pode vir uma expressao (logo, "/" inicia uma regex)
_KW_EXPR = frozenset("""return typeof instanceof in of new delete void throw case do else yield await extends""".split())

# tipos de token
ID, NUM, STR, TPL, RE, PUNCT, COMMENT = "id", "num", "str", "tpl", "re", "p", "c"


class Tok:
    __slots__ = ("type", "value", "nl", "ws")

    def __init__(self, type_: str, value: str, nl: bool, ws: bool):
        self.type = type_
        self.value = value
        self.nl = nl  # havia uma quebra de linha antes do token
        self.ws = ws  # havia algum espaco em branco antes do token

    def __repr__(self):  # pragma: no cover - depuracao
        return f"Tok({self.type},{self.value!r},nl={self.nl})"


def _regex_allowed(prev: Tok | None, ctrl_close: bool = False) -> bool:
    if prev is None:
        return True
    t, v = prev.type, prev.value
    if t in (NUM, STR, RE):
        return False
    if t == TPL:
        return v.endswith("${")
    if t == ID:
        return v in _KW_EXPR
    if t == PUNCT:
        # ")" e "]" terminam expressoes, exceto o ")" de if/for/while/with (inicia uma instrucao);
        # "}" termina mais vezes um bloco (logo, regex)
        if v == ")":
            return ctrl_close
        return v not in ("]", "++", "--")
    return True  # comentario nunca e "prev" (ver tokenize)


def _scan_string(s: str, i: int) -> int:
    q = s[i]
    j = i + 1
    n = len(s)
    while j < n:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == q:
            return j + 1
        if c in "\n\r":
            raise FormatError(f"string por terminar na posicao {i}")
        j += 1
    raise FormatError(f"string por terminar na posicao {i}")


def _scan_template(s: str, j: int) -> tuple[int, bool]:
    """A partir de j (logo depois de ` ou }), ate ` (fim) ou ${ (interpolacao). Devolve (fim, interpolacao)."""
    n = len(s)
    while j < n:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c == "`":
            return j + 1, False
        if c == "$" and j + 1 < n and s[j + 1] == "{":
            return j + 2, True
        j += 1
    raise FormatError("template literal por terminar")


def _scan_regex(s: str, i: int) -> int:
    j = i + 1
    n = len(s)
    in_class = False
    while j < n:
        c = s[j]
        if c == "\\":
            j += 2
            continue
        if c in _LINE_TERMINATORS:
            raise FormatError(f"regex por terminar na posicao {i}")
        if in_class:
            if c == "]":
                in_class = False
        elif c == "[":
            in_class = True
        elif c == "/":
            j += 1
            m = _ID_RE.match(s, j)
            return m.end() if m else j
        j += 1
    raise FormatError(f"regex por terminar na posicao {i}")


def tokenize_js(s: str) -> list[Tok]:
    """Tokens significativos (com comentarios). Levanta FormatError se o texto nao for JS lexicalmente valido."""
    if s.startswith("﻿"):
        s = s[1:]
    toks: list[Tok] = []
    append = toks.append
    braces: list[str] = []  # "b" = chaveta normal, "t" = interpolacao de template
    parens: list[bool] = []  # por "(" aberto: e o cabecalho de if/for/while/with?
    ctrl_close = False  # o ultimo token foi o ")" de um desses cabecalhos
    prev: Tok | None = None  # ultimo token significativo (sem comentarios)
    i, n = 0, len(s)
    nl = ws = False
    if s.startswith("#!"):  # hashbang
        j = s.find("\n")
        j = n if j < 0 else j
        append(Tok(COMMENT, s[:j], False, False))
        i = j
    while i < n:
        c = s[i]
        m = _WS_RE.match(s, i)
        if m:
            text = m.group()
            ws = True
            if any(t in text for t in _LINE_TERMINATORS):
                nl = True
            i = m.end()
            continue
        if c == "/" and i + 1 < n and s[i + 1] in "/*":
            if s[i + 1] == "/":
                j = i + 2
                while j < n and s[j] not in _LINE_TERMINATORS:
                    j += 1
            else:
                j = s.find("*/", i + 2)
                if j < 0:
                    raise FormatError(f"comentario por terminar na posicao {i}")
                j += 2
            append(Tok(COMMENT, s[i:j], nl, ws))
            nl = ws = False
            i = j
            continue
        if c in "'\"":
            j = _scan_string(s, i)
            tok = Tok(STR, s[i:j], nl, ws)
        elif c == "`":
            j, interp = _scan_template(s, i + 1)
            if interp:
                braces.append("t")
            tok = Tok(TPL, s[i:j], nl, ws)
        elif c == "}" and braces and braces[-1] == "t":
            braces.pop()
            j, interp = _scan_template(s, i + 1)
            if interp:
                braces.append("t")
            tok = Tok(TPL, s[i:j], nl, ws)
        elif c.isdigit() or (c == "." and i + 1 < n and s[i + 1].isdigit()):
            m = _NUM_RE.match(s, i)
            j = m.end()
            tok = Tok(NUM, s[i:j], nl, ws)
        elif c == "#" and i + 1 < n and _ID_START.match(s[i + 1]):
            m = _ID_RE.match(s, i + 1)
            j = m.end()
            tok = Tok(ID, s[i:j], nl, ws)
        elif _ID_START.match(c):
            m = _ID_RE.match(s, i)
            if not m:
                raise FormatError(f"caracter inesperado {c!r} na posicao {i}")
            j = m.end()
            tok = Tok(ID, s[i:j], nl, ws)
        elif c == "/" and _regex_allowed(prev, ctrl_close):
            j = _scan_regex(s, i)
            tok = Tok(RE, s[i:j], nl, ws)
        else:
            m = _PUNCT_RE.match(s, i)
            if not m:
                raise FormatError(f"caracter inesperado {c!r} na posicao {i}")
            v = m.group()
            if v == "?." and i + 2 < n and s[i + 2].isdigit():
                v = "?"  # a?.5:b
            j = i + len(v)
            if v == "{":
                braces.append("b")
            elif v == "}":
                if not braces:
                    raise FormatError(f"'}}' sem par na posicao {i}")
                braces.pop()
            elif v == "(":
                parens.append(prev is not None and prev.type == ID and prev.value in _CTRL)
            elif v == ")":
                if not parens:
                    raise FormatError(f"')' sem par na posicao {i}")
            tok = Tok(PUNCT, v, nl, ws)
        append(tok)
        ctrl_close = tok.type == PUNCT and tok.value == ")" and parens.pop()
        prev = tok
        nl = ws = False
        i = j
    if braces:
        raise FormatError("chavetas ou templates por fechar no fim do ficheiro")
    return toks


_CTRL = frozenset(("if", "for", "while", "with"))
_NO_BREAK_AFTER_CLOSE = frozenset("else catch finally while instanceof in of as".split())


def format_tokens(toks: list[Tok], indent: str = "  ", marks: frozenset[int] = frozenset()) -> tuple[str, dict[int, int]]:
    """Reescreve os tokens com quebras de linha e indentacao. Devolve (texto, {indice marcado: linha 1-based})."""
    out: list[str] = []
    w = out.append
    frames = [0]  # por nivel de chavetas: parenteses/colchetes abertos nesse nivel
    depth = 0
    line = 1
    mark_lines: dict[int, int] = {}
    prev: Tok | None = None
    for idx, t in enumerate(toks):
        v = t.value
        is_close = t.type == PUNCT and v == "}"
        if prev is not None:
            brk = t.nl
            if not brk:
                pv = prev.value
                if prev.type == COMMENT and pv.startswith("//"):
                    brk = True
                elif prev.type == PUNCT and pv == "{" and not is_close:
                    brk = True
                elif is_close and not (prev.type == PUNCT and pv == "{"):
                    brk = True
                elif prev.type == PUNCT and pv == ";" and frames[-1] == 0:
                    brk = True
                elif prev.type == PUNCT and pv == "}" and t.type in (ID, NUM, STR, RE) and v not in _NO_BREAK_AFTER_CLOSE:
                    brk = True
                elif (prev.type == PUNCT and pv == "," and frames[-1] == 0 and idx >= 2
                      and toks[idx - 2].type == PUNCT and toks[idx - 2].value == "}"):
                    brk = True  # "},"  entre propriedades (ex.: modulos do webpack)
            if is_close:
                depth = max(0, depth - 1)
            if brk:
                w("\n")
                line += 1
                w(indent * depth)
            elif t.ws:
                w(" ")
        elif is_close:
            depth = max(0, depth - 1)
        if idx in marks:
            mark_lines[idx] = line
        w(v)
        if t.type == COMMENT or t.type == STR or t.type == TPL:
            line += v.count("\n")  # comentarios de bloco / continuacoes de linha
        if t.type == PUNCT:
            if v == "{":
                depth += 1
                frames.append(0)
            elif v == "}":
                if len(frames) > 1:
                    frames.pop()
            elif v in "([":
                frames[-1] += 1
            elif v in ")]":
                frames[-1] = max(0, frames[-1] - 1)
        prev = t
    return "".join(out), mark_lines


def verify_same_tokens(a: list[Tok], b: list[Tok]) -> None:
    """Mesma sequencia de tokens e nenhuma quebra de linha original perdida."""
    if len(a) != len(b):
        raise FormatError(f"numero de tokens diferente apos formatar ({len(a)} != {len(b)})")
    for i, (x, y) in enumerate(zip(a, b)):
        if x.type != y.type or x.value != y.value:
            raise FormatError(f"token {i} diferente apos formatar: {x.value[:40]!r} != {y.value[:40]!r}")
        if x.nl and not y.nl and i:  # espacos antes do 1.o token sao irrelevantes
            raise FormatError(f"quebra de linha perdida antes do token {i}")


def format_js(src: str, marks: frozenset[int] = frozenset(),
              toks: list[Tok] | None = None) -> tuple[str, dict[int, int], int]:
    """Formata e verifica. Devolve (texto, linhas das marcas, numero de tokens)."""
    toks = toks if toks is not None else tokenize_js(src)
    text, lines = format_tokens(toks, marks=marks)
    verify_same_tokens(toks, tokenize_js(text))
    return text, lines, len(toks)


def is_minified(text: str) -> bool:
    """Heuristica: linhas muito longas (bundles do webpack, CSS numa linha)."""
    if len(text) < 2000:
        return False
    lines = text.count("\n") + 1
    longest = max((len(x) for x in text.split("\n")), default=0)
    return longest > 1000 or len(text) / lines > 300


# ------------------------------------------------------------------ CSS

_CSS_TOKEN = re.compile(r"""
    (?P<ws>\s+)
  | (?P<comment>/\*.*?\*/)
  | (?P<str>"(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*')
  | (?P<url>url\(\s*[^)"'\s]*\s*\))
  | (?P<punct>[{}();:,])
  | (?P<word>[^\s{}();:,"'/]+|/)
""", re.S | re.X | re.I)


def tokenize_css(s: str) -> list[Tok]:
    if s.startswith("﻿"):
        s = s[1:]
    toks: list[Tok] = []
    i, n = 0, len(s)
    nl = ws = False
    depth = 0
    while i < n:
        m = _CSS_TOKEN.match(s, i)
        if not m:
            raise FormatError(f"CSS: nao foi possivel ler a posicao {i}")
        kind = m.lastgroup
        v = m.group()
        i = m.end()
        if kind == "ws":
            ws = True
            nl = nl or "\n" in v
            continue
        if kind == "punct":
            if v == "{":
                depth += 1
            elif v == "}":
                depth -= 1
                if depth < 0:
                    raise FormatError("CSS: '}' sem par")
        toks.append(Tok({"comment": COMMENT, "str": STR, "punct": PUNCT}.get(kind, ID), v, nl, ws))
        nl = ws = False
    if depth:
        raise FormatError("CSS: chavetas por fechar")
    return toks


def format_css(src: str) -> tuple[str, int]:
    toks = tokenize_css(src)
    out: list[str] = []
    w = out.append
    depth = 0
    parens = 0
    prev: Tok | None = None
    for t in toks:
        v = t.value
        is_close = t.type == PUNCT and v == "}"
        if prev is not None:
            pv = prev.value
            brk = t.nl or (prev.type == PUNCT and (pv == "{" or pv == "}" or (pv == ";" and parens == 0))) or is_close
            if is_close:
                depth = max(0, depth - 1)
            if brk:
                w("\n" + "  " * depth)
            elif t.ws:
                w(" ")
        w(v)
        if t.type == PUNCT:
            if v == "{":
                depth += 1
            elif v == "(":
                parens += 1
            elif v == ")":
                parens = max(0, parens - 1)
        prev = t
    text = "".join(out)
    verify_same_tokens(toks, tokenize_css(text))
    return text, len(toks)
