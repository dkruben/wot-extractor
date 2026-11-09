# -*- coding: utf-8 -*-
"""Worker de descricao de modulos para os stubs do wot-extractor.

Corre no Python 2.7 (o codigo do jogo e Python 2) e fala por linhas JSON (um pedido por linha em stdin,
uma resposta por linha em stdout). Compativel com Python 2.7 e 3.x, so biblioteca padrao.

Seguranca: nada e executado. O codigo-fonte so e analisado com compile(..., ast.PyCF_ONLY_AST) e o
bytecode (quando a descompilacao falhou) so e lido com marshal.loads e percorrido como dados.

Pedidos:
  {"op": "hello"}
  {"op": "stdlib", "names": [...]}          -> quais sao modulos da biblioteca padrao/embutidos do 2.7
  {"op": "known", "names": [...]}           -> nomes de topo de modulos com codigo (o resto pode ser nativo)
  {"op": "describe", "id": 1, "name": "...", "source": <b64>|null, "pyc": <b64>|null}
  {"op": "quit"}
"""

from __future__ import print_function

import ast
import base64
import imp
import json
import marshal
import os
import sys
import traceback

PY2 = sys.version_info[0] == 2
if PY2:
    text_type = unicode  # noqa: F821
    string_types = (str, unicode)  # noqa: F821
else:
    text_type = str
    string_types = (str, bytes)

MAX_DOC_LINES = 30
KNOWN = set()

if os.path.dirname(os.path.abspath(__file__)) in sys.path:
    sys.path.remove(os.path.dirname(os.path.abspath(__file__)))


def _u(s):
    if s is None:
        return None
    if isinstance(s, bytes):
        return s.decode("utf-8", "replace")
    return text_type(s)


def _doc(s):
    if not isinstance(s, string_types):
        return None
    s = _u(s).strip("\n")
    lines = s.split("\n")
    if len(lines) > MAX_DOC_LINES:
        lines = lines[:MAX_DOC_LINES] + [u"[...]"]
    return u"\n".join(lines)


# ------------------------------------------------------------------ expressoes -> texto

def src(node):
    """Texto de uma expressao simples; None se nao for representavel com seguranca."""
    if isinstance(node, ast.Name):
        return node.id
    if hasattr(ast, "NameConstant") and isinstance(node, ast.NameConstant):
        return repr(node.value)
    if isinstance(node, ast.Attribute):
        base = src(node.value)
        return None if base is None else base + "." + node.attr
    if isinstance(node, ast.Num):
        return repr(node.n).rstrip("L") if PY2 else repr(node.n)
    if isinstance(node, ast.Str):
        v = node.s
        if isinstance(v, bytes):
            try:
                v = v.decode("utf-8")
            except UnicodeDecodeError:
                return None
        if len(v) > 80:
            return None
        return repr(_u(v)).lstrip("u") if PY2 else repr(v)
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub) and isinstance(node.operand, ast.Num):
        inner = src(node.operand)
        return None if inner is None else "-" + inner
    if isinstance(node, (ast.Tuple, ast.List)) and len(node.elts) <= 8:
        parts = [src(e) for e in node.elts]
        if any(p is None for p in parts):
            return None
        if isinstance(node, ast.List):
            return "[" + ", ".join(parts) + "]"
        return "(" + ", ".join(parts) + ("," if len(parts) == 1 else "") + ")"
    if isinstance(node, ast.Dict) and not node.keys:
        return "{}"
    if isinstance(node, ast.Call):
        f = src(node.func)
        return None if f is None else f + "(...)"
    if isinstance(node, ast.Subscript):
        base = src(node.value)
        return None if base is None else base + "[...]"
    return None


def literal_kind(node):
    if isinstance(node, ast.Num):
        return "float" if isinstance(node.n, float) else ("complex" if isinstance(node.n, complex) else "int")
    if isinstance(node, ast.Str):
        return "str"
    if hasattr(ast, "NameConstant") and isinstance(node, ast.NameConstant):
        return "None" if node.value is None else "bool"
    if isinstance(node, ast.Name) and node.id in ("True", "False"):
        return "bool"
    if isinstance(node, ast.Name) and node.id == "None":
        return "None"
    if isinstance(node, ast.UnaryOp) and isinstance(node.operand, ast.Num):
        return literal_kind(node.operand)
    for t, k in ((ast.Tuple, "tuple"), (ast.List, "list"), (ast.Dict, "dict"), (ast.Set, "set")):
        if isinstance(node, t):
            return k
    if isinstance(node, (ast.ListComp,)):
        return "list"
    if isinstance(node, (ast.DictComp,)):
        return "dict"
    return None


def literal_value(node):
    """Valor literal curto (int/str/bool/None) para escrever no stub, ou None."""
    k = literal_kind(node)
    if k in ("int", "float", "bool", "None", "str"):
        s = src(node)
        if s is not None and len(s) <= 80:
            return s
    return None


# ------------------------------------------------------------------ AST

def _decorators(fn):
    return [src(d) or "<expr>" for d in getattr(fn, "decorator_list", [])]


def _args(a):
    out = []
    names = a.args
    defaults = a.defaults
    first_default = len(names) - len(defaults)
    for i, arg in enumerate(names):
        d = None
        has_default = i >= first_default
        if has_default:
            d = literal_value(defaults[i - first_default]) or "..."
        if isinstance(arg, ast.Name):
            out.append({"name": arg.id, "default": d, "has_default": has_default})
        elif hasattr(ast, "arg") and isinstance(arg, ast.arg):
            out.append({"name": arg.arg, "default": d, "has_default": has_default})
        else:  # desempacotamento de tuplo (so Python 2): def f(a, (b, c))
            out.append({"name": None, "tuple": src(arg) or "(...)", "default": d, "has_default": has_default})
    va = a.vararg
    kw = a.kwarg
    if va is not None and not isinstance(va, string_types):
        va = va.arg
    if kw is not None and not isinstance(kw, string_types):
        kw = kw.arg
    return out, va, kw


def describe_function(fn):
    args, va, kw = _args(fn.args)
    return {"name": fn.name, "args": args, "vararg": va, "kwarg": kw, "decorators": _decorators(fn),
            "doc": _doc(ast.get_docstring(fn, clean=True)), "line": fn.lineno}


def _targets(node):
    if isinstance(node, ast.Assign):
        return node.targets, node.value
    if hasattr(ast, "AnnAssign") and isinstance(node, ast.AnnAssign):
        return [node.target], node.value
    return [], None


def _names_in_target(t):
    if isinstance(t, ast.Name):
        return [t.id]
    if isinstance(t, (ast.Tuple, ast.List)):
        out = []
        for e in t.elts:
            out += _names_in_target(e)
        return out
    return []


def _flatten(body):
    """Instrucoes de topo, incluindo as de blocos if/try ao mesmo nivel (definicoes condicionais)."""
    for node in body:
        if isinstance(node, ast.If):
            for x in _flatten(node.body):
                yield x
            for x in _flatten(node.orelse):
                yield x
        elif (hasattr(ast, "TryExcept") and isinstance(node, ast.TryExcept)) or \
                (hasattr(ast, "Try") and isinstance(node, ast.Try)):
            for x in _flatten(node.body):
                yield x
            for h in node.handlers:
                for x in _flatten(h.body):
                    yield x
            for x in _flatten(getattr(node, "orelse", [])):
                yield x
            for x in _flatten(getattr(node, "finalbody", [])):
                yield x
        elif hasattr(ast, "TryFinally") and isinstance(node, ast.TryFinally):
            for x in _flatten(node.body):
                yield x
            for x in _flatten(node.finalbody):
                yield x
        else:
            yield node


def _instance_attrs(cls_node):
    found = []
    for node in ast.walk(cls_node):
        targets, _ = _targets(node)
        if hasattr(ast, "AugAssign") and isinstance(node, ast.AugAssign):
            targets = [node.target]
        for t in targets:
            for e in (t.elts if isinstance(t, (ast.Tuple, ast.List)) else [t]):
                if isinstance(e, ast.Attribute) and isinstance(e.value, ast.Name) and e.value.id == "self":
                    if e.attr not in found:
                        found.append(e.attr)
    return found


def describe_class(node):
    methods, attrs, classes = [], [], []
    metaclass = None
    for item in _flatten(node.body):
        if isinstance(item, ast.FunctionDef):
            methods.append(describe_function(item))
        elif isinstance(item, ast.ClassDef):
            classes.append(describe_class(item))
        else:
            targets, value = _targets(item)
            for t in targets:
                for n in _names_in_target(t):
                    if n == "__metaclass__" and value is not None:
                        metaclass = src(value)
                        continue
                    attrs.append({"name": n, "kind": literal_kind(value) if value is not None else None,
                                  "value": literal_value(value) if value is not None and isinstance(t, ast.Name) else None,
                                  "alias": src(value) if isinstance(value, (ast.Name, ast.Attribute)) else None})
    bases = []
    for b in node.bases:
        s = src(b)
        bases.append({"src": s, "simple": isinstance(b, (ast.Name, ast.Attribute)) and s is not None})
    return {"name": node.name, "bases": bases, "metaclass": metaclass, "decorators": _decorators(node),
            "doc": _doc(ast.get_docstring(node, clean=True)), "methods": methods, "attrs": attrs,
            "instance_attrs": _instance_attrs(node), "classes": classes, "line": node.lineno}


def _native_usage(tree, aliases):
    """Uso de modulos sem codigo: {modulo: {membro: [ocorrencias, chamadas, min_args, max_args, keywords]}}."""
    usage = {}
    calls = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and \
                isinstance(node.func.value, ast.Name) and node.func.value.id in aliases:
            star = bool(getattr(node, "starargs", None) or getattr(node, "kwargs", None)) or any(
                (hasattr(ast, "Starred") and isinstance(a, ast.Starred)) for a in node.args) or any(
                k.arg is None for k in node.keywords)
            calls[id(node.func)] = (len(node.args), [k.arg for k in node.keywords if k.arg], star)
    for node in ast.walk(tree):
        if isinstance(node, ast.Attribute) and isinstance(node.value, ast.Name) and node.value.id in aliases:
            mod = aliases[node.value.id]
            rec = usage.setdefault(mod, {}).setdefault(node.attr, [0, 0, None, None, []])
            rec[0] += 1
            c = calls.get(id(node))
            if c is not None:
                n, kws, star = c
                rec[1] += 1
                if not star:
                    rec[2] = n if rec[2] is None else min(rec[2], n)
                    rec[3] = n if rec[3] is None else max(rec[3], n)
                for k in kws:
                    if k not in rec[4]:
                        rec[4].append(k)
    return usage


def describe_ast(text, name):
    if PY2 and isinstance(name, text_type):
        name = name.encode("utf-8", "replace")
    # dont_inherit: sem isto o compile herda o print_function deste ficheiro e "print x" seria erro
    tree = compile(text, name, "exec", ast.PyCF_ONLY_AST, True)
    imports, classes, functions, assigns = [], [], [], []
    all_names = None
    future = []
    aliases = {}
    for node in _flatten(tree.body):
        if isinstance(node, ast.Import):
            for a in node.names:
                imports.append({"kind": "import", "name": a.name, "asname": a.asname})
                top = a.name.split(".")[0]
                if top not in KNOWN:
                    aliases[a.asname or top] = a.name if a.asname else top
        elif isinstance(node, ast.ImportFrom):
            mod = node.module or ""
            if mod == "__future__":
                future += [a.name for a in node.names]
                continue
            imports.append({"kind": "from", "module": mod, "level": node.level or 0,
                            "names": [[a.name, a.asname] for a in node.names]})
        elif isinstance(node, ast.FunctionDef):
            functions.append(describe_function(node))
        elif isinstance(node, ast.ClassDef):
            classes.append(describe_class(node))
        else:
            targets, value = _targets(node)
            for t in targets:
                for n in _names_in_target(t):
                    if n == "__all__" and isinstance(value, (ast.List, ast.Tuple)):
                        all_names = [_u(e.s) for e in value.elts if isinstance(e, ast.Str)]
                    assigns.append({"name": n, "kind": literal_kind(value) if value is not None else None,
                                    "value": literal_value(value) if value is not None and isinstance(t, ast.Name) else None,
                                    "alias": src(value) if isinstance(value, (ast.Name, ast.Attribute)) else None})
    # nomes importados de modulos sem codigo (from BigWorld import callback)
    native_from = {}
    for imp_ in imports:
        if imp_["kind"] == "from" and imp_["level"] == 0 and imp_["module"].split(".")[0] not in KNOWN:
            for n, _ in imp_["names"]:
                if n != "*":
                    native_from.setdefault(imp_["module"], []).append(n)
    return {"mode": "ast", "doc": _doc(ast.get_docstring(tree, clean=True)), "imports": imports, "future": future,
            "classes": classes, "functions": functions, "assigns": assigns, "all": all_names,
            "native_usage": _native_usage(tree, aliases), "native_from": native_from}


# ------------------------------------------------------------------ bytecode (descompilacao falhada)

def _instructions(code):
    import opcode
    co = code.co_code
    co = bytearray(co)
    i, n, ext = 0, len(co), 0
    while i < n:
        op = co[i]
        if op >= opcode.HAVE_ARGUMENT:
            arg = co[i + 1] | (co[i + 2] << 8) | ext
            i += 3
            if op == opcode.EXTENDED_ARG:
                ext = arg << 16
                continue
            ext = 0
            yield opcode.opname[op], arg
        else:
            i += 1
            yield opcode.opname[op], None


def _defaults_count(parent, child_index):
    prev = None
    for name, arg in _instructions(parent):
        if prev == ("LOAD_CONST", child_index) and name in ("MAKE_FUNCTION", "MAKE_CLOSURE"):
            return arg
        prev = (name, arg)
    return None


def _is_class_body(code):
    return code.co_argcount == 0 and "__module__" in code.co_names and not (code.co_flags & 0x0C)


def _bc_function(code, ndefaults):
    names = list(code.co_varnames[:code.co_argcount])
    args = []
    first_default = len(names) - (ndefaults or 0) if ndefaults is not None else None
    for i, n in enumerate(names):
        has = first_default is not None and i >= first_default
        args.append({"name": n if not n.startswith(".") else None, "tuple": "(...)" if n.startswith(".") else None,
                     "default": "..." if has else None, "has_default": has, "default_unknown": ndefaults is None})
    j = code.co_argcount
    va = kw = None
    if code.co_flags & 0x04:
        va = code.co_varnames[j]
        j += 1
    if code.co_flags & 0x08:
        kw = code.co_varnames[j]
    doc = code.co_consts[0] if code.co_consts and isinstance(code.co_consts[0], string_types) else None
    return {"name": code.co_name, "args": args, "vararg": va, "kwarg": kw, "decorators": [],
            "doc": _doc(doc), "line": code.co_firstlineno}


def _name(code, arg):
    if arg is None or arg >= len(code.co_names):
        raise ValueError("bytecode ilegivel (indice de nome invalido; possivelmente ofuscado)")
    return code.co_names[arg]


def _bc_stores(code):
    out = []
    for name, arg in _instructions(code):
        if name in ("STORE_NAME", "STORE_GLOBAL") and arg is not None:
            n = _name(code, arg)
            if n not in out:
                out.append(n)
    return out


def _bc_body(code):
    functions, classes = [], []
    for idx, c in enumerate(code.co_consts):
        if not hasattr(c, "co_code") or c.co_name in ("<lambda>", "<genexpr>", "<listcomp>", "<dictcomp>", "<setcomp>"):
            continue
        if _is_class_body(c):
            fns, cls = _bc_body(c)
            doc = None
            for name, arg in _instructions(c):  # __doc__ = 'texto' no inicio do corpo da classe
                if name == "LOAD_CONST" and isinstance(c.co_consts[arg], string_types):
                    doc = c.co_consts[arg]
                break
            defined = set(f["name"] for f in fns) | set(k["name"] for k in cls)
            attrs = [{"name": n, "kind": None, "value": None, "alias": None} for n in _bc_stores(c)
                     if n not in defined and n not in ("__module__", "__doc__", "__metaclass__")]
            classes.append({"name": c.co_name, "bases": [], "bases_unknown": True, "metaclass": None,
                            "decorators": [], "doc": _doc(doc) if "__doc__" in c.co_names else None,
                            "methods": fns, "attrs": attrs, "instance_attrs": [], "classes": cls,
                            "line": c.co_firstlineno})
        else:
            functions.append(_bc_function(c, _defaults_count(code, idx)))
    return functions, classes


def describe_bytecode(pyc):
    code = marshal.loads(pyc[8:])
    functions, classes = _bc_body(code)
    imports, future = [], []
    seq = list(_instructions(code))
    for k, (name, arg) in enumerate(seq):
        if name == "IMPORT_NAME":
            mod = _name(code, arg)
            froms = []
            for name2, arg2 in seq[k + 1:k + 200]:
                if name2 == "IMPORT_FROM":
                    froms.append([_name(code, arg2), None])
                elif name2 in ("IMPORT_NAME", "IMPORT_STAR"):
                    if name2 == "IMPORT_STAR":
                        froms = [["*", None]]
                    break
                elif name2 == "POP_TOP" and froms:
                    break
            if mod == "__future__":
                future += [n for n, _ in froms]
            elif froms:
                imports.append({"kind": "from", "module": mod, "level": 0, "names": froms})
            else:
                imports.append({"kind": "import", "name": mod, "asname": None})
    defined = set(f["name"] for f in functions) | set(c["name"] for c in classes)
    imported = set()
    for i in imports:
        if i["kind"] == "import":
            imported.add(i["name"].split(".")[0])
        else:
            imported.update(n for n, _ in i["names"])
    assigns = [{"name": n, "kind": None, "value": None, "alias": None} for n in _bc_stores(code)
               if n not in defined and n not in imported and n not in ("__doc__",)]
    doc = code.co_consts[0] if code.co_consts and isinstance(code.co_consts[0], string_types) and \
        "__doc__" in code.co_names else None
    return {"mode": "bytecode", "doc": _doc(doc), "imports": imports, "future": future, "classes": classes,
            "functions": functions, "assigns": assigns, "all": None, "native_usage": {}, "native_from": {}}


# ------------------------------------------------------------------ protocolo

def handle(req):
    op = req.get("op")
    if op == "hello":
        return {"ok": True, "version": sys.version.split()[0], "py2": PY2}
    if op == "known":
        KNOWN.clear()
        KNOWN.update(req.get("names", []))
        return {"ok": True, "known": len(KNOWN)}
    if op == "stdlib":
        found = []
        for n in req.get("names", []):
            if n in sys.builtin_module_names:
                found.append(n)
                continue
            try:
                f, path, _ = imp.find_module(n)
                if f:
                    f.close()
                if path and os.path.abspath(path).lower().startswith(os.path.abspath(sys.prefix).lower()):
                    found.append(n)
            except ImportError:
                pass
        return {"ok": True, "stdlib": found}
    if op == "describe":
        if "known" in req:
            KNOWN.clear()
            KNOWN.update(req["known"])
        name = req.get("name") or "<modulo>"
        source = base64.b64decode(req["source"]) if req.get("source") is not None else None
        pyc = base64.b64decode(req["pyc"]) if req.get("pyc") is not None else None
        ast_error = None
        if source is not None:
            try:
                out = describe_ast(source, name)
                out["ok"] = True
                return out
            except SyntaxError as exc:
                ast_error = "SyntaxError: %s (linha %s)" % (exc.msg, exc.lineno)
            except Exception as exc:  # noqa: BLE001
                ast_error = "%s: %s" % (type(exc).__name__, exc)
        if pyc is not None:
            try:
                out = describe_bytecode(pyc)
                out["ok"] = True
                out["ast_error"] = ast_error
                return out
            except Exception as exc:  # noqa: BLE001
                return {"ok": False, "error": "bytecode: %s: %s" % (type(exc).__name__, exc), "ast_error": ast_error}
        return {"ok": False, "error": ast_error or "sem fonte nem bytecode"}
    return {"ok": False, "error": "operacao desconhecida: %r" % (op,)}


def main():
    sys.setrecursionlimit(20000)
    stdin = sys.stdin if PY2 else sys.stdin.buffer
    stdout = sys.stdout if PY2 else sys.stdout.buffer
    while True:
        line = stdin.readline()
        if not line:
            break
        try:
            req = json.loads(line.decode("utf-8") if isinstance(line, bytes) else line)
        except ValueError:
            continue
        if req.get("op") == "quit":
            break
        try:
            resp = handle(req)
        except Exception:  # noqa: BLE001
            resp = {"ok": False, "error": traceback.format_exc()[-800:]}
        resp["id"] = req.get("id")
        data = json.dumps(resp, ensure_ascii=True)
        stdout.write(data.encode("ascii") if not isinstance(data, bytes) else data)
        stdout.write(b"\n")
        stdout.flush()


if __name__ == "__main__":
    main()
