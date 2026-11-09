# -*- coding: utf-8 -*-
"""Worker de descompilacao do wot-extractor.

Corre num interpretador separado (Python 2.7 ou 3.x) e fala com o processo
principal por linhas JSON: um pedido por linha em stdin, uma resposta por
linha em stdout. Este ficheiro tem de ser compativel com Python 2.7 e 3.x e
usar apenas a biblioteca padrao mais o descompilador do proprio interpretador.

Seguranca: o bytecode NUNCA e executado. E lido com xdis (unmarshal para
objetos de codigo), convertido em texto pelo uncompyle6 e o texto e apenas
analisado com compile(..., ast.PyCF_ONLY_AST), que constroi a arvore
sintatica sem executar nada. O worker nao abre ficheiros: recebe os bytes do
.pyc e devolve os bytes do .py, ambos em base64.

Pedidos:
  {"op": "hello"}
  {"op": "decompile", "id": 1, "name": "scripts/x.pyc", "data": <b64>, "validate": true,
   "header": "# linha a colocar no topo
"}
  {"op": "validate", "id": 2, "name": "scripts/x.py", "source": <b64>}
  {"op": "quit"}
"""

from __future__ import print_function

import ast
import base64
import io
import json
import re
import sys
import threading
import time
import traceback

PY2 = sys.version_info[0] == 2
FAIL_MARKER = b"--- This code section failed: ---"
NOTE_MARKER = b"# NOTE: have internal decompilation grammar errors."
CODING_RE = re.compile(br"^[ \t\f]*#.*?coding[:=][ \t]*([-\w.]+)")
STACK_SIZE = 192 * 1024 * 1024  # recursao profunda do uncompyle6 (Py2 no Windows aceita < 256 MB)

_proto = None  # stream do protocolo (stdout original)


def _send(obj):
    _proto.write(json.dumps(obj) + "\n")
    _proto.flush()


def _b64e(data):
    return base64.b64encode(data).decode("ascii")


def _b64d(text):
    return base64.b64decode(text.encode("ascii") if not isinstance(text, bytes) else text)


def _has_cookie(src):
    for line in src.split(b"\n", 2)[:2]:
        if CODING_RE.match(line):
            return True
    return False


def _with_cookie(src):
    """Acrescenta uma declaracao de codificacao quando ha bytes nao-ASCII.

    Em Python 2 um literal str conserva os bytes tal como estao no ficheiro,
    por isso a declaracao nao altera o valor; so torna o ficheiro analisavel."""
    try:
        src.decode("ascii")
        return src, None
    except UnicodeDecodeError:
        pass
    if _has_cookie(src):
        return src, None
    try:
        src.decode("utf-8")
        enc = "utf-8"
    except UnicodeDecodeError:
        enc = "latin-1"
    return ("# -*- coding: %s -*-\n" % enc).encode("ascii") + src, enc


def _exc_text(exc, tb=None):
    """Tipo e mensagem; se a mensagem estiver vazia, acrescenta onde ocorreu."""
    msg = "%s: %s" % (type(exc).__name__, exc)
    if not str(exc):
        frames = traceback.extract_tb(tb or sys.exc_info()[2])
        if frames:
            f = frames[-1]
            msg += "(em %s:%s, %s)" % (f[0].replace("\\", "/").rsplit("/", 1)[-1], f[1], f[2])
    return msg


def _validate(src, name):
    """None se o texto for sintaticamente valido; senao a mensagem."""
    try:
        compile(src, name, "exec", ast.PyCF_ONLY_AST, True)
        return None
    except SyntaxError as exc:
        return "SyntaxError: %s (linha %s)" % (exc.msg, exc.lineno)
    except (ValueError, TypeError, MemoryError, RecursionError if not PY2 else RuntimeError) as exc:
        return "%s: %s" % (type(exc).__name__, exc)


def _decompile(data, name):
    from xdis.load import load_module_from_file_object
    from uncompyle6.main import decompile

    version, timestamp, magic_int, co, is_pypy, source_size = load_module_from_file_object(
        io.BytesIO(data), filename=name)[:6]
    if PY2:
        from StringIO import StringIO
        buf = StringIO()
    else:
        buf = io.StringIO()
    error = None
    try:
        decompile(co, bytecode_version=version, out=buf, timestamp=timestamp, magic_int=magic_int,
                  is_pypy=is_pypy, source_size=source_size)
    except Exception as exc:
        error = _exc_text(exc)
    text = buf.getvalue()
    if not PY2 or isinstance(text, unicode):  # noqa: F821 (so existe em Py2)
        text = text.encode("utf-8", "surrogateescape" if not PY2 else "strict")
    return text, error, version


def _code_lines(src):
    n = 0
    for line in src.splitlines():
        s = line.strip()
        if s and not s.startswith(b"#"):
            n += 1
    return n


def _run_in_big_stack(fn, *args):
    box = {}

    def target():
        try:
            box["ok"] = fn(*args)
        except BaseException as exc:  # noqa: B902 - devolver tudo ao chamador
            box["exc"] = _exc_text(exc)

    th = threading.Thread(target=target)
    th.start()
    th.join()
    if "exc" in box:
        raise RuntimeError(box["exc"])
    return box["ok"]


def handle_decompile(req):
    t0 = time.time()
    name = req.get("name") or "<pyc>"
    data = _b64d(req["data"])
    res = {"id": req.get("id")}
    try:
        src, error, version = _run_in_big_stack(_decompile, data, name)
    except Exception as exc:
        res.update(status="failed", error=str(exc), elapsed=round(time.time() - t0, 3))
        return res
    res["bytecode"] = ".".join(str(x) for x in version[:2]) if isinstance(version, tuple) else str(version)
    markers = src.count(FAIL_MARKER)
    src, cookie = _with_cookie(src)
    code_lines = _code_lines(src)
    header = req.get("header")
    if header:  # 1.a linha; a declaracao de codificacao (se houver) fica na 2.a, como permite a PEP 263
        src = header.encode("ascii") + src
    res.update(markers=markers, cookie=cookie, code_lines=code_lines)
    if error:
        res["error"] = error
    if req.get("validate"):
        res["syntax_error"] = _run_in_big_stack(_validate, src, name[:-1] if name.endswith("c") else name)
    res["source"] = _b64e(src)
    res["elapsed"] = round(time.time() - t0, 3)
    return res


def handle_validate(req):
    src = _b64d(req["source"])
    return {"id": req.get("id"), "syntax_error": _run_in_big_stack(_validate, src, req.get("name") or "<py>")}


def hello():
    info = {"op": "hello", "python": "%d.%d.%d" % sys.version_info[:3]}
    try:
        import uncompyle6
        import xdis
        info["uncompyle6"] = uncompyle6.__version__
        info["xdis"] = xdis.__version__
    except Exception as exc:
        info["error"] = "%s: %s" % (type(exc).__name__, exc)
    return info


def main():
    global _proto
    # a pasta deste script tem modulos do wot-extractor; nao devem sombrear os do descompilador
    if sys.path and sys.path[0] and __file__.startswith(sys.path[0]):
        sys.path.pop(0)
    _proto = sys.stdout
    sys.stdout = sys.stderr  # qualquer print das bibliotecas vai para stderr
    sys.setrecursionlimit(20000)
    threading.stack_size(STACK_SIZE)
    handlers = {"decompile": handle_decompile, "validate": handle_validate}
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
        except ValueError as exc:
            _send({"id": None, "status": "failed", "error": "pedido invalido: %s" % exc})
            continue
        op = req.get("op")
        if op == "quit":
            break
        if op == "hello":
            _send(hello())
            continue
        fn = handlers.get(op)
        if fn is None:
            _send({"id": req.get("id"), "status": "failed", "error": "operacao desconhecida: %r" % op})
            continue
        try:
            _send(fn(req))
        except Exception as exc:
            _send({"id": req.get("id"), "status": "failed",
                   "error": "erro interno do worker: %s: %s" % (type(exc).__name__, exc)})


if __name__ == "__main__":
    main()
