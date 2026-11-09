import ast
import base64
import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from wot_extractor.config import load_config
from wot_extractor.decompile.backends import WorkerProcess
from wot_extractor.detect.install import inspect_install
from wot_extractor.extract import ExtractOptions, ManifestError, run_extract
from wot_extractor.extract.writer import long_path
from wot_extractor.stubs import StubOptions, find_python27, run_stubs
from wot_extractor.stubs.engine import WORKER, module_of, stub_rel
from wot_extractor.stubs.render import render_module, render_native

from .helpers import make_install

_PY27 = None


def py27():
    global _PY27
    if _PY27 is None:
        tmp = Path(tempfile.mkdtemp())
        interp, _ = find_python27(None, tmp)
        shutil.rmtree(tmp, ignore_errors=True)
        _PY27 = interp or False
    return _PY27 or None


def fn(name, *args, decorators=(), vararg=None, kwarg=None, doc=None, defaults=None):
    defaults = defaults or {}
    return {"name": name, "args": [{"name": a, "has_default": a in defaults, "default": defaults.get(a)} for a in args],
            "vararg": vararg, "kwarg": kwarg, "decorators": list(decorators), "doc": doc}


class RenderTests(unittest.TestCase):
    def test_module_rendering(self):
        desc = {"mode": "ast", "doc": 'Modulo "x"', "future": [],
                "imports": [{"kind": "import", "name": "utils", "asname": None},
                            {"kind": "import", "name": "BigWorld", "asname": None},
                            {"kind": "from", "module": "helpers", "level": 0, "names": [["dependency", None]]},
                            {"kind": "from", "module": "gui.shared", "level": 0, "names": [["events", "ev"]]}],
                "assigns": [{"name": "LIMIT", "kind": "int", "value": "5"},
                            {"name": "NAMES", "kind": "tuple", "value": None},
                            {"name": "g_x", "kind": None, "value": None, "alias": None},
                            {"name": "Alias", "kind": None, "value": None, "alias": "Foo"}],
                "classes": [{"name": "Foo", "bases": [{"src": "object", "simple": True},
                                                      {"src": "with_metaclass(...)", "simple": False}],
                             "metaclass": "Meta", "decorators": ["six.add_metaclass(...)"],
                             "doc": 'Doc com """aspas""" e \\barra', "attrs": [{"name": "A", "kind": "str", "value": "'a'"}],
                             "instance_attrs": ["_x", "value"], "classes": [],
                             "methods": [fn("__init__", "self", "x", defaults={"x": "None"}),
                                         fn("value", "self", decorators=["property"]),
                                         fn("value", "self", "v", decorators=["value.setter"]),
                                         fn("run", "self", vararg="args", kwarg="kw",
                                            decorators=["adisp.adisp_process"]),
                                         fn("bad", "self", "async"),
                                         fn("make", "cls", decorators=["classmethod"])]}],
                "functions": [fn("helper", "a", "b", defaults={"b": "..."}), fn("helper", "a")]}
        exists = {"gui.utils", "gui", "helpers"}.__contains__
        text, stats = render_module(desc, "gui.foo", False, "sources/x.py", exists)
        ast.parse(text)
        self.assertIn("from . import utils as utils", text)  # import relativo implicito (Python 2)
        self.assertIn("import BigWorld as BigWorld", text)
        self.assertIn("from helpers import dependency as dependency", text)
        self.assertIn("from gui.shared import events as ev", text)
        self.assertIn("LIMIT = 5", text)
        self.assertIn("NAMES: tuple", text)
        self.assertIn("g_x: Any", text)
        self.assertIn("Alias = Foo", text)
        self.assertIn("class Foo(object, metaclass=Meta):", text)
        self.assertIn("# base nao representavel no stub: with_metaclass(...)", text)
        self.assertIn("    @value.setter", text)
        self.assertIn("    # decorador original: @adisp.adisp_process", text)
        self.assertIn("def run(self, *args, **kw):", text)
        self.assertIn("    _x: Any", text)
        self.assertNotIn("    value: Any", text)  # e uma property, nao um atributo
        self.assertNotIn("def bad", text)
        self.assertIn("    @classmethod", text)
        self.assertEqual(text.count("def helper("), 1)  # a ultima definicao prevalece
        self.assertIn("def helper(a):", text)
        self.assertEqual((stats["classes"], stats["failed"]), (1, False))
        self.assertTrue(any("bad" in o for o in stats["omitted"]))

    def test_absolute_import_and_any_alias(self):
        desc = {"mode": "ast", "future": ["absolute_import"], "imports": [
            {"kind": "import", "name": "utils", "asname": None},
            {"kind": "from", "module": "typing", "level": 0, "names": [["Any", None]]}],
            "assigns": [{"name": "x", "kind": None, "value": None}], "classes": [], "functions": []}
        text, _ = render_module(desc, "gui.foo", False, "s", {"gui.utils"}.__contains__)
        self.assertIn("import utils as utils", text)
        self.assertIn("from typing import Any as _Any", text)
        self.assertIn("x: _Any", text)

    def test_bytecode_mode(self):
        desc = {"mode": "bytecode", "imports": [], "assigns": [], "functions": [],
                "classes": [{"name": "C", "bases": [], "bases_unknown": True, "methods": [
                    {"name": "m", "args": [{"name": "self", "has_default": False, "default_unknown": True}],
                     "vararg": None, "kwarg": None, "decorators": []}], "attrs": [], "instance_attrs": [],
                    "classes": []}]}
        text, _ = render_module(desc, "a.b", False, "sources/a/b.pyc", lambda m: False)
        ast.parse(text)
        self.assertIn("BYTECODE", text)
        self.assertIn("classes base desconhecidas", text)
        self.assertIn("def __getattr__(name: str) -> Any", text)

    def test_native(self):
        text = render_native("BigWorld", {
            "callback": {"uses": 3, "calls": 3, "min": 2, "max": 2, "kw": set(), "imported": 0},
            "player": {"uses": 5, "calls": 5, "min": 0, "max": 0, "kw": set(), "imported": 1},
            "ATTR": {"uses": 2, "calls": 0, "min": None, "max": None, "kw": set(), "imported": 0}}, 4)
        ast.parse(text)
        self.assertIn("def callback(*args: Any, **kwargs: Any) -> Any: ...  # chamado 3x com 2 argumento(s)", text)
        self.assertIn("ATTR: Any  # usado sem chamada 2x", text)
        self.assertIn("SEM CODIGO no cliente", text)

    def test_module_paths(self):
        self.assertEqual(module_of("scripts/client/gui/shared/events.pyc"), ("gui.shared.events", False, "client", False))
        self.assertEqual(module_of("comp7/scripts/client/comp7/__init__.pyc"), ("comp7", True, "client", False))
        self.assertEqual(module_of("scripts/common/Lib/json/__init__.pyc"), ("json", True, "common", True))
        self.assertIsNone(module_of("gui/flash/x.swf"))
        self.assertEqual(stub_rel("gui.shared", True), "__stubs/gui/shared/__init__.pyi")


PY2_SRC = b'''"""Doc do modulo."""
import BigWorld
from debug_utils import LOG_ERROR
CONST = 7

class Foo(object):
    """Classe Foo."""
    NAME = 'foo'

    def __init__(self, a, (b, c)=(1, 2), *args):
        self._a = a
        print "ola"

    @property
    def a(self):
        return self._a

def handler(x, y=None, **kw):
    try:
        BigWorld.callback(0.1, x)
    except Exception, e:
        LOG_ERROR(e)
    return BigWorld.player().id
'''


@unittest.skipUnless(py27() is not None, "Python 2.7 nao disponivel")
class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(long_path(self.tmp), ignore_errors=True))
        self.w = WorkerProcess(py27().path, self.tmp, WORKER)
        self.addCleanup(self.w.close)

    def test_ast_and_bytecode(self):
        r = self.w.request({"op": "describe", "id": 1, "name": "m.py", "known": ["debug_utils"],
                            "source": base64.b64encode(PY2_SRC).decode()}, 60)
        self.assertTrue(r["ok"], r)
        self.assertEqual(r["mode"], "ast")
        foo = r["classes"][0]
        init = foo["methods"][0]
        self.assertEqual([a.get("name") for a in init["args"]], ["self", "a", None])
        self.assertEqual(init["vararg"], "args")
        self.assertEqual(foo["instance_attrs"], ["_a"])
        self.assertEqual(r["functions"][0]["args"][1], {"name": "y", "default": "None", "has_default": True})
        self.assertEqual(r["native_usage"]["BigWorld"]["callback"][:4], [1, 1, 2, 2])
        self.assertEqual(r["native_usage"]["BigWorld"]["player"][1], 1)
        # bytecode compilado pelo proprio Python 2.7 (sem executar o modulo)
        src, pyc = self.tmp / "m.py", self.tmp / "m.pyc"
        src.write_bytes(PY2_SRC)
        subprocess.run([str(py27().path), "-c", "import py_compile,sys; py_compile.compile(sys.argv[1], sys.argv[2], "
                        "doraise=True)", str(src), str(pyc)], check=True)
        r = self.w.request({"op": "describe", "id": 2, "name": "m.pyc", "source": base64.b64encode(b"def (:").decode(),
                            "pyc": base64.b64encode(pyc.read_bytes()).decode()}, 60)
        self.assertEqual(r["mode"], "bytecode")
        self.assertIn("SyntaxError", r["ast_error"])
        foo = r["classes"][0]
        self.assertEqual((foo["name"], [m["name"] for m in foo["methods"]]), ("Foo", ["__init__", "a"]))
        h = r["functions"][0]
        self.assertEqual([(a["name"], a["has_default"]) for a in h["args"]], [("x", False), ("y", True)])
        self.assertEqual(h["kwarg"], "kw")
        self.assertIn({"kind": "from", "module": "debug_utils", "level": 0, "names": [["LOG_ERROR", None]]},
                      r["imports"])
        r = self.w.request({"op": "stdlib", "names": ["os", "BigWorld", "weakref"]}, 30)
        self.assertEqual(sorted(r["stdlib"]), ["os", "weakref"])


@unittest.skipUnless(py27() is not None, "Python 2.7 nao disponivel")
class EngineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(long_path(self.tmp), ignore_errors=True))
        self.files = {
            "scripts/client/gui/__init__.py": b"",
            "scripts/client/gui/utils.py": b"def helper(a, b=2):\n    pass\n",
            "scripts/client/gui/foo.py": b"import utils\n" + PY2_SRC,
            "scripts/client/gui/broken.py": b"def (:\n",
            "scripts/common/Lib/mystd.py": b"X = 1\n",
        }
        self.cfg = load_config(project_root=self.tmp)
        self.cfg.output_root = self.tmp / "out"
        self.out = self.cfg.realm_output_dir("EU")

    def _extract(self, files=None, prune=False):
        root = make_install(self.tmp / "game", pkgs={"scripts.pkg": files or self.files})
        return run_extract(self.cfg, inspect_install(root, ["cli"], deep=False), ExtractOptions(jobs=2, prune=prune))

    def _run(self, **kw):
        kw.setdefault("jobs", 2)
        return run_stubs(self.cfg, "EU", StubOptions(**kw), interp=py27(), interp_label="py27")

    def test_requires_manifest(self):
        with self.assertRaises(ManifestError):
            self._run()

    def test_cycle(self):
        self._extract()
        r = self._run()
        self.assertEqual(r.stdlib_skipped, 1)
        self.assertEqual(r.totals, {"success": 3, "failed": 1}, r.problems)
        foo = (self.out / "__stubs/gui/foo.pyi").read_text(encoding="utf-8")
        ast.parse(foo)
        self.assertIn("from . import utils as utils", foo)
        self.assertIn("class Foo(object):", foo)
        self.assertIn("def __init__(self, a, __p2=..., *args):", foo)
        self.assertIn("def handler(x, y=None, **kw):", foo)
        self.assertIn("CONST = 7", foo)
        self.assertTrue((self.out / "__stubs/gui/__init__.pyi").is_file())
        bw = (self.out / "__stubs/BigWorld.pyi").read_text(encoding="utf-8")
        self.assertIn("def callback(*args: Any, **kwargs: Any) -> Any: ...  # chamado 1x com 2 argumento(s)", bw)
        self.assertIn("player", bw)
        du = (self.out / "__stubs/debug_utils.pyi").read_text(encoding="utf-8")  # sem codigo neste cliente
        self.assertIn("LOG_ERROR: Any  # importado com 'from debug_utils import' em 1 ficheiro(s)", du)
        self.assertFalse((self.out / "__stubs/mystd.pyi").exists())
        e = json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))["entries"]
        self.assertEqual(e["res/scripts/client/gui/foo.py"]["stubs"]["status"], "success")
        self.assertEqual(e["res/scripts/client/gui/broken.py"]["stubs"]["status"], "failed")
        index = json.loads((self.out / "__stubs/stubs_index.json").read_text(encoding="utf-8"))["modules"]
        self.assertEqual(index["BigWorld"]["status"], "native")
        self.assertTrue((self.out / "__stubs/README.md").is_file())
        self.assertTrue((self.out / "stubs_report.json").is_file())

        r2 = self._run()  # nada mudou: atalho, nada e reescrito
        self.assertEqual((r2.described, r2.written, r2.reused), (0, 0, 4))
        self.assertEqual(r2.totals, {"success": 3, "failed": 1})
        r2b = self._run(stdlib=True)  # outra opcao: volta a escrever a partir da cache das descricoes
        self.assertEqual((r2b.described, r2b.reused), (1, 4))
        files = dict(self.files)
        del files["scripts/client/gui/utils.py"]
        self._extract(files, prune=True)
        self.assertIn("stubs", json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))["entries"][
            "res/scripts/client/gui/foo.py"])
        r3 = self._run()
        self.assertEqual(r3.removed, 2)  # gui/utils.pyi (removido do jogo) e mystd.pyi (sem --stdlib)
        self.assertFalse((self.out / "__stubs/mystd.pyi").exists())
        self.assertFalse((self.out / "__stubs/gui/utils.pyi").exists())
        self.assertIn("import utils as utils", (self.out / "__stubs/gui/foo.pyi").read_text(encoding="utf-8"))

    def test_dry_run_and_stdlib(self):
        self._extract()
        r = self._run(dry_run=True)
        self.assertEqual((r.selected, r.described), (4, 4))
        self.assertFalse((self.out / "__stubs/gui/foo.pyi").exists())
        r = self._run(stdlib=True)
        self.assertTrue((self.out / "__stubs/mystd.pyi").is_file())


if __name__ == "__main__":
    unittest.main()
