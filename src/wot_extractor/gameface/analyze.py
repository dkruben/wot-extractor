"""Analise de um ficheiro Gameface (executada num processo de trabalho; so leitura e escrita em sources_gameface).

Por ficheiro: tipo, minificado ou nao, copia formatada (JS/CSS/HTML com scripts inline) verificada token a
token e, se existir, pelo `node --check` (so analisa a sintaxe, nunca executa), estrutura do webpack
(modulos, chunks, modulo de entrada) e referencias usadas pelas ligacoes ao Python (R.views, engine.*,
comandos do ViewModel, nomes de propriedades).
"""

from __future__ import annotations

import json
import os
import re
import subprocess
from pathlib import Path

from ..extract.writer import long_path, remove_file, write_atomic
from ..formats.jsfmt import (COMMENT, FORMATTER_VERSION, ID, NUM, PUNCT, STR, FormatError, format_css,
                             format_tokens, is_minified, tokenize_js, verify_same_tokens)

ANALYZER_VERSION = 3
GF_DIR = "sources_gameface"
PROD = "/gui/gameface/_dist/production/"
NODE_TIMEOUT = 120
MAX_NAMES = 20000
MAX_LIST = 400

_IDENT = re.compile(r"^[A-Za-z_$][\w$]*$")
_LICENSE = re.compile(r"@license\s+([^\n*]+?)\s*(?:\n|\*)")
_SCRIPT = re.compile(r"(<script\b[^>]*>)(.*?)(</script\s*>)", re.S | re.I)
_STYLE = re.compile(r"(<style\b[^>]*>)(.*?)(</style\s*>)", re.S | re.I)
_ATTR = re.compile(r"""\b(src|href)\s*=\s*["']([^"']+)["']""", re.I)
_LINK = re.compile(r"<link\b[^>]*>", re.I)
_WEBPACK_ENTRY = re.compile(r"__webpack_require__\.O\(void 0,\s*\[([\d,\s]*)\],\s*\(\)\s*=>\s*__webpack_require__\(\s*(\d+)\s*\)\)")
_UNBOUND_DEF = re.compile(r"\(def\s+(\w+)\s+([\w.]+)")
_UNBOUND_SRC = re.compile(r"#\s*source:\s*(\S+)")

HEADER_JS = ("/* wot-extractor: JavaScript FORMATADO a partir de sources/{key}. So foram alterados espacos e quebras "
             "de linha (verificado token a token{node}). NAO e o codigo-fonte original: o webpack/minificador "
             "encurtou nomes e removeu comentarios. */\n")
HEADER_CSS = ("/* wot-extractor: CSS FORMATADO a partir de sources/{key}. So foram alterados espacos e quebras de "
              "linha (verificado token a token). NAO e o ficheiro original. */\n")
HEADER_HTML = ("<!-- wot-extractor: HTML de sources/{key} com os scripts/estilos inline minificados FORMATADOS "
               "(exceto bibliotecas de terceiros com @license; so espacos e quebras de linha, verificado token a "
               "token). NAO e o original. -->\n")


def decode_text(raw: bytes) -> tuple[str, str]:
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    try:
        return raw.decode("utf-8"), "utf-8"
    except UnicodeDecodeError:
        return raw.decode("latin-1"), "latin-1"


def file_kind(virtual: str) -> str:
    """Tipo pelo caminho virtual (o papel de view/chunk/vendor e decidido no motor, que ve a pasta toda)."""
    v = virtual.lower()
    if v.endswith(".d.ts"):
        return "typings"
    if v.endswith(".ts"):
        return "ts_source"
    if v.endswith(".unbound"):
        return "unbound"
    ext = v.rsplit(".", 1)[-1] if "." in v.rsplit("/", 1)[-1] else ""
    if ext in ("js", "mjs"):
        return "js"
    if ext == "css":
        return "css"
    if ext in ("html", "htm"):
        return "html"
    return "asset"


def prod_parts(virtual: str) -> tuple[str | None, list[str]] | None:
    """(feature ou None, partes do caminho relativo a _dist/production/) ou None se fora do _dist."""
    v = "/" + virtual
    if PROD not in v:
        return None
    pre, rel = v.split(PROD, 1)
    feature = pre.strip("/") or None
    if feature and feature.endswith("/res"):  # pastas res/<x>/ dentro de mods
        feature = None
    return feature, rel.split("/")


# ------------------------------------------------------------------ JavaScript

def _dotted(toks, i: int) -> tuple[str, int]:
    """Le id(.id)* a partir de toks[i]; devolve (caminho, indice seguinte)."""
    parts = [toks[i].value]
    j = i + 1
    while j + 1 < len(toks) and toks[j].type == PUNCT and toks[j].value == "." and toks[j + 1].type == ID:
        parts.append(toks[j + 1].value)
        j += 2
    return ".".join(parts), j


def _str_value(tok) -> str:
    v = tok.value
    return v[1:-1] if len(v) >= 2 else v


def js_references(toks) -> dict:
    r_views: set[str] = set()
    r_other: dict[str, set[str]] = {}
    engine: set[str] = set()
    view_env: set[str] = set()
    commands: set[str] = set()
    urls: set[str] = set()
    names: set[str] = set()
    n = len(toks)
    for i, t in enumerate(toks):
        tt = t.type
        if tt == ID:
            v = t.value
            if v == "R" and i + 2 < n and toks[i + 1].value == "." and toks[i + 2].type == ID and (
                    i == 0 or toks[i - 1].value != "."):
                path, _ = _dotted(toks, i)
                parts = path.split(".")
                if len(parts) >= 3:
                    if parts[1] == "views":
                        r_views.add(".".join(parts[2:]))
                    else:
                        r_other.setdefault(parts[1], set()).add(".".join(parts[2:]))
            elif v == "engine" and i + 4 < n and toks[i + 1].value == "." and toks[i + 3].value == "(" \
                    and toks[i + 4].type == STR:
                engine.add(f"{toks[i + 2].value}:{_str_value(toks[i + 4])}")
            elif v == "viewEnv" and i + 2 < n and toks[i + 1].value == "." and toks[i + 2].type == ID:
                view_env.add(toks[i + 2].value)
            elif v in ("createCallback", "createCallbackNoArgs") and i + 1 < n and toks[i + 1].value == "(":
                depth = 0
                for j in range(i + 1, min(n, i + 60)):
                    tj = toks[j]
                    if tj.type == PUNCT and tj.value in "([{":
                        depth += 1
                    elif tj.type == PUNCT and tj.value in ")]}":
                        depth -= 1
                        if depth == 0:
                            break
                    elif tj.type == STR and depth == 1:
                        commands.add(_str_value(tj))
                        break
            if i and toks[i - 1].type == PUNCT and toks[i - 1].value in (".", "?.") and len(v) >= 3:
                names.add(v)
        elif tt == STR:
            s = _str_value(t)
            if 3 <= len(s) <= 64 and _IDENT.match(s):
                names.add(s)
            elif "://" in s[:12]:
                urls.add(s)
    return {
        "r_views": sorted(r_views),
        "r_other": {k: len(v) for k, v in sorted(r_other.items())},
        "r_other_examples": {k: sorted(v)[:20] for k, v in sorted(r_other.items())},
        "engine": sorted(engine),
        "viewEnv": sorted(view_env),
        "commands": sorted(commands),
        "urls": sorted(urls)[:MAX_LIST],
        "names": sorted(names)[:MAX_NAMES],
    }


def _parse_object(toks, start: int) -> tuple[list[tuple[str, int]], int]:
    """Propriedades de um objeto literal que comeca em toks[start] == "{" -> ([(chave, indice)], fim)."""
    entries: list[tuple[str, int]] = []
    depth = 0
    expect_key = True
    i = start
    n = len(toks)
    while i < n:
        t = toks[i]
        if t.type == PUNCT and t.value in "([{":
            depth += 1
            if depth == 1 and t.value == "{":
                expect_key = True
                i += 1
                continue
        elif t.type == PUNCT and t.value in ")]}":
            depth -= 1
            if depth == 0:
                return entries, i
        elif depth == 1:
            if t.type == PUNCT and t.value == ",":
                expect_key = True
            elif expect_key and t.type in (NUM, STR, ID) and i + 1 < n and toks[i + 1].value == ":":
                entries.append((_str_value(t) if t.type == STR else t.value, i))
                expect_key = False
            else:
                expect_key = False
        i += 1
    return entries, i


def webpack_info(toks, text: str) -> tuple[dict | None, dict[str, int]]:
    """Estrutura do webpack 5: modulos definidos (id -> indice do token), chunks declarados, entrada."""
    info: dict = {}
    modules: dict[str, int] = {}
    n = len(toks)
    for i, t in enumerate(toks):
        if t.type != ID:
            continue
        if t.value == "__webpack_modules__" and i + 2 < n and toks[i + 1].value == "=" and toks[i + 2].value == "{":
            ents, _ = _parse_object(toks, i + 2)
            modules.update((k, idx) for k, idx in ents)
            info["runtime"] = True
        elif t.value.startswith("webpackChunk") and "chunk_name" not in info:
            # (self.webpackChunkX=self.webpackChunkX||[]).push([[ids],{modulos}...])
            for j in range(i + 1, min(n, i + 16)):
                if toks[j].value == "push" and j + 3 < n and toks[j + 1].value == "(" and toks[j + 2].value == "[" \
                        and toks[j + 3].value == "[":
                    ids = []
                    k = j + 4
                    while k < n and toks[k].value != "]":
                        if toks[k].type == NUM:
                            ids.append(toks[k].value)
                        elif toks[k].type == STR:
                            ids.append(_str_value(toks[k]))
                        k += 1
                    info["chunk_name"] = t.value
                    info["chunk_ids"] = ids
                    if k + 2 < n and toks[k + 1].value == "," and toks[k + 2].value == "{":
                        ents, _ = _parse_object(toks, k + 2)
                        modules.update((key, idx) for key, idx in ents)
                    break
    m = _WEBPACK_ENTRY.search(text)
    if m:
        info["entry_module"] = m.group(2)
        info["requires_chunks"] = [x.strip() for x in m.group(1).split(",") if x.strip()]
        info["runtime"] = True
    if not info and not modules:
        return None, {}
    info["modules"] = len(modules)
    return info, modules


# ------------------------------------------------------------------ HTML / unbound

def html_info(text: str) -> dict:
    scripts, links, inline = [], [], []
    for m in _SCRIPT.finditer(text):
        attrs = dict((k.lower(), v) for k, v in _ATTR.findall(m.group(1)))
        if "src" in attrs:
            scripts.append(attrs["src"])
        else:
            body = m.group(2)
            lic = _LICENSE.search(body[:2000])
            inline.append({"bytes": len(body), "license": lic.group(1).strip() if lic else None})
    for m in _LINK.finditer(text):
        attrs = dict((k.lower(), v) for k, v in _ATTR.findall(m.group(0)))
        if "href" in attrs:
            links.append(attrs["href"])
    return {"scripts": scripts, "stylesheets": links, "inline_scripts": inline,
            "inline_styles": len(_STYLE.findall(text))}


def unbound_info(text: str) -> dict:
    defs = [{"kind": k, "name": n} for k, n in _UNBOUND_DEF.findall(text)]
    src = _UNBOUND_SRC.search(text[:1000])
    names = sorted({n for n in re.findall(r"[A-Za-z_]\w{2,63}", text)})[:MAX_NAMES]
    return {"defs": defs[:MAX_LIST], "generated_from": src.group(1) if src else None,
            "generated": "This file was generated" in text[:300], "names": names}


# ------------------------------------------------------------------ node

def node_check(node: str | None, path: Path) -> tuple[int | None, str]:
    if not node:
        return None, ""
    try:
        r = subprocess.run([node, "--check", long_path(path)], capture_output=True, timeout=NODE_TIMEOUT,
                           stdin=subprocess.DEVNULL, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    except (OSError, subprocess.TimeoutExpired) as exc:
        return None, f"{type(exc).__name__}: {exc}"
    return r.returncode, r.stderr.decode("utf-8", "replace")[-300:]


# ------------------------------------------------------------------ um ficheiro

def formatted_rel(key: str, kind: str) -> str:
    sub = {"js": "js", "css": "css", "html": "html"}[kind]
    return f"{GF_DIR}/{sub}/{key}"


def analysis_rel(key: str) -> str:
    return f"{GF_DIR}/manifests/files/{key}.json"


def process_file(job: dict) -> dict:
    """job: key, src (caminho absoluto), out_dir, kind, format (bool), node (str|None). Devolve o registo."""
    key, kind = job["key"], job["kind"]
    out_dir = Path(job["out_dir"])
    res: dict = {"kind": kind, "analyzer": [ANALYZER_VERSION, FORMATTER_VERSION]}
    try:
        with open(long_path(job["src"]), "rb") as fh:
            raw = fh.read()
    except OSError as exc:
        return {**res, "status": "failed", "error": f"leitura: {exc}"}
    text, enc = decode_text(raw)
    res["encoding"] = enc
    analysis: dict = {"key": key, "source": f"sources/{key}", "kind": kind, "bytes": len(raw), "encoding": enc}
    problems: list[str] = []
    fmt_out = Path(out_dir, formatted_rel(key, kind)) if kind in ("js", "css", "html") else None
    if fmt_out is not None:
        remove_file(fmt_out)
    minified = is_minified(text) if kind in ("js", "css") else False
    res["minified"] = minified

    if kind == "js":
        try:
            toks = tokenize_js(text)
        except FormatError as exc:
            toks = None
            problems.append(f"JavaScript nao lido pelo lexer: {exc}")
        if toks is not None:
            analysis["tokens"] = len(toks)
            analysis["license"] = _license(toks)
            wp, modules = webpack_info(toks, text)
            analysis.update(js_references(toks))
            if job["format"] and minified:
                ok = _format_js_file(job, key, toks, modules, wp, fmt_out, res, problems)
                if ok and wp is not None:
                    wp["module_lines"] = ok
            if wp is not None:
                wp.setdefault("module_ids", sorted(modules, key=_id_order)[:MAX_NAMES])
                analysis["webpack"] = wp
    elif kind == "css":
        if job["format"] and minified:
            try:
                body, ntok = format_css(text)
                header = HEADER_CSS.format(key=key)
                if body.lstrip().lower().startswith("@charset"):
                    first, _, rest = body.partition("\n")
                    out = first + "\n" + header + rest
                else:
                    out = header + body
                write_atomic(fmt_out, out.encode("utf-8"))
                res["formatted"] = formatted_rel(key, kind)
                res["verify"] = {"tokens": ntok}
            except FormatError as exc:
                problems.append(f"CSS nao formatado: {exc}")
        analysis["classes"] = len(set(re.findall(r"\.([A-Za-z_][\w-]*)", text)))
    elif kind == "html":
        info = html_info(text)
        analysis.update(info)
        if job["format"]:
            _format_html_file(job, key, text, fmt_out, res, problems)
        # referencias dos scripts inline proprios (sem licenca de terceiros)
        refs: dict = {}
        for m in _SCRIPT.finditer(text):
            body = m.group(2)
            if body.strip() and not _LICENSE.search(body[:2000]) and "src=" not in m.group(1).lower():
                try:
                    r = js_references(tokenize_js(body))
                except FormatError:
                    continue
                for k2, v2 in r.items():
                    if isinstance(v2, list):
                        refs.setdefault(k2, set()).update(v2)
        for k2, v2 in refs.items():
            analysis[k2] = sorted(v2)
    elif kind == "unbound":
        analysis.update(unbound_info(text))
    elif kind in ("ts_source", "typings"):
        analysis["lines"] = text.count("\n") + 1
        analysis["imports"] = sorted(set(re.findall(r"""^\s*import\b[^'"]*['"]([^'"]+)['"]""", text, re.M)))[:MAX_LIST]
        analysis["exports"] = sorted(set(re.findall(r"^\s*export\s+(?:default\s+)?(?:declare\s+)?"
                                                    r"(?:abstract\s+)?(?:class|interface|type|function|const|enum|let|var|namespace)\s+(\w+)",
                                                    text, re.M)))[:MAX_LIST]

    write_atomic(Path(out_dir, analysis_rel(key)),
                 json.dumps(analysis, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
    res["analysis"] = analysis_rel(key)
    if problems:
        res["error"] = "; ".join(problems)
    res["status"] = "partial" if problems else "success"
    return res


def _id_order(k: str):
    return (0, int(k)) if k.isdigit() else (1, k)


def _license(toks) -> str | None:
    for t in toks[:5]:
        if t.type == COMMENT:
            m = _LICENSE.search(t.value + "\n")
            if m:
                return m.group(1).strip()
    return None


def _format_js_file(job, key, toks, modules, wp, fmt_out, res, problems) -> dict | None:
    marks = frozenset(modules.values())
    try:
        body, lines = format_tokens(toks, marks=marks)
        verify_same_tokens(toks, tokenize_js(body))
    except FormatError as exc:
        problems.append(f"JavaScript nao formatado: {exc}")
        return None
    node = job.get("node")
    header = HEADER_JS.format(key=key, node=" e pelo node --check" if node else "")
    write_atomic(fmt_out, (header + body).encode("utf-8"))
    verify = {"tokens": len(toks)}
    if node:
        rc, err = node_check(node, fmt_out)
        if rc is None:
            verify["node"] = f"nao executado: {err}" if err else "nao executado"
        elif rc == 0:
            verify["node"] = "ok"
        else:
            rc0, _ = node_check(node, Path(job["src"]))
            if rc0 == 0:  # o original passa e o formatado nao: a formatacao estragou algo
                remove_file(fmt_out)
                problems.append(f"a formatacao alterou a sintaxe (node --check): {err.strip()[:200]}")
                return None
            verify["node"] = "o original tambem nao passa (modulo ES ou sintaxe propria)"
    res["formatted"] = formatted_rel(key, "js")
    res["verify"] = verify
    by_id = {}
    for mid, idx in modules.items():
        if idx in lines:
            by_id[mid] = lines[idx] + 1  # + linha do cabecalho
    return by_id


def _format_html_file(job, key, text, fmt_out, res, problems) -> None:
    changed = 0
    errors = []

    def fmt_script(m):
        nonlocal changed
        open_tag, body, close = m.groups()
        if "src=" in open_tag.lower() or not body.strip() or _LICENSE.search(body[:2000]) or not is_minified(body):
            return m.group(0)
        try:
            toks = tokenize_js(body)
            out, _ = format_tokens(toks)
            verify_same_tokens(toks, tokenize_js(out))
        except FormatError as exc:
            errors.append(f"script inline: {exc}")
            return m.group(0)
        changed += 1
        return f"{open_tag}\n{out}\n{close}"

    def fmt_style(m):
        nonlocal changed
        open_tag, body, close = m.groups()
        if not is_minified(body):
            return m.group(0)
        try:
            out, _ = format_css(body)
        except FormatError as exc:
            errors.append(f"style inline: {exc}")
            return m.group(0)
        changed += 1
        return f"{open_tag}\n{out}\n{close}"

    new = _STYLE.sub(fmt_style, _SCRIPT.sub(fmt_script, text))
    if errors:
        problems.extend(errors)
    if not changed:
        return
    header = HEADER_HTML.format(key=key)
    low = new.lstrip()[:15].lower()
    if low.startswith("<!doctype"):
        end = new.find(">") + 1
        new = new[:end] + "\n" + header + new[end:]
    else:
        new = header + new
    write_atomic(fmt_out, new.encode("utf-8"))
    res["formatted"] = formatted_rel(key, "html")
    res["verify"] = {"inline_formatted": changed}


def outputs_of(rec: dict | None) -> list[str]:
    g = (rec or {}).get("gameface") or {}
    return [g[k] for k in ("formatted", "analysis") if g.get(k)]


def remove_outputs(out_dir: Path, rec: dict | None) -> int:
    from ..safety import resolve_within
    n = 0
    for rel in outputs_of(rec):
        n += remove_file(resolve_within(out_dir, rel))
    return n


def exists(out_dir: Path, rel: str) -> bool:
    return os.path.exists(long_path(Path(out_dir, rel)))
