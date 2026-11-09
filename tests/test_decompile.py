import base64
import json
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest
from pathlib import Path
from unittest import mock

from wot_extractor.config import load_config
from wot_extractor.decompile import backends
from wot_extractor.decompile.backends import WorkerCrashed, WorkerProcess, WorkerTimeout, find_toolchain
from wot_extractor.decompile.engine import (DecompileOptions, _reusable, _Runner, classify, header_line, output_rel,
                                            run_decompile)
from wot_extractor.detect.install import inspect_install
from wot_extractor.extract import ExtractOptions, ManifestError, run_extract
from wot_extractor.extract.manifest import StateLock, StateLocked
from wot_extractor.extract.writer import long_path

from .helpers import PYC38, make_install

_TC = None


def toolchain():
    global _TC
    if _TC is None:
        _TC = find_toolchain()
    return _TC


def compile27(source: str, name: str) -> bytes:
    """Gera um .pyc 2.7 a partir de codigo de teste (o interpretador so compila)."""
    tmp = Path(tempfile.mkdtemp())
    try:
        (tmp / "src.py").write_text(source, encoding="utf-8")
        script = ("import marshal, imp, sys\n"
                  "src = open(sys.argv[1], 'rb').read()\n"
                  "co = compile(src, sys.argv[3], 'exec')\n"
                  "open(sys.argv[2], 'wb').write(imp.get_magic() + b'\\0\\0\\0\\0' + marshal.dumps(co))\n")
        subprocess.run([str(toolchain().py27.path), "-c", script, str(tmp / "src.py"), str(tmp / "out.pyc"), name],
                       check=True, capture_output=True)
        return (tmp / "out.pyc").read_bytes()
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


MOD_A = textwrap.dedent('''\
    """Modulo de teste."""
    import os
    from gui.shared import events
    CONST = {'a': 1, 'b': (2, 3)}

    class Panel(object):
        def __init__(self, name):
            self.name = name

        def render(self, items):
            for i in items:
                if i > 2:
                    print 'big', i
            return [x * 2 for x in items if x]

    def helper(*args, **kwargs):
        try:
            return os.path.join(*args)
        except TypeError:
            return None
    ''')


# --------------------------------------------------------------------- unitarios

class ClassifyTests(unittest.TestCase):
    def test_states(self):
        ok = {"source": "x", "code_lines": 10}
        self.assertEqual(classify(ok), ("success", "valid", ""))
        self.assertEqual(classify({"source": "x", "code_lines": 0})[0], "success")  # modulo vazio
        st, val, err = classify({"source": "x", "code_lines": 5, "markers": 2})
        self.assertEqual((st, val), ("partial", "valid"))
        self.assertIn("2 seccao", err)
        st, val, err = classify({"source": "x", "code_lines": 5, "syntax_error": "SyntaxError: bad (linha 3)"})
        self.assertEqual(st, "partial")
        self.assertTrue(val.startswith("invalid: SyntaxError"))
        st, _, err = classify({"source": "x", "code_lines": 5, "error": "SourceWalkerError: x"})
        self.assertEqual(st, "partial")
        self.assertEqual(classify({"source": "x", "code_lines": 0, "error": "AssertionError"})[0], "failed")
        self.assertEqual(classify({"status": "failed", "error": "tempo limite"}), ("failed", "", "tempo limite"))

    def test_output_rel(self):
        self.assertEqual(output_rel("res/scripts/a/b.pyc", {}), "sources/res/scripts/a/b.py")
        self.assertEqual(output_rel("res/scripts/a/b.pyo", {}), "sources/res/scripts/a/b.py")
        self.assertEqual(output_rel("res/scripts/a/b.pyc", {"res/scripts/a/b.py": {}}),
                         "sources/res/scripts/a/b.decompiled.py")

    def test_header_is_ascii_comment(self):
        h = header_line("res/scripts/ç.pyc", "uncompyle6 3.9.2 / Python 2.7.18")
        self.assertTrue(h.startswith("# wot-extractor:") and h.endswith("\n"))
        h.encode("ascii")

    def test_reusable(self):
        sig = ["uncompyle6=x"]
        rec = {"sha256": "aa"}
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, True)
        (tmp / "o.py").write_bytes(b"12345")
        opts = DecompileOptions()
        good = {"status": "success", "input_sha256": "aa", "output": "o.py", "size": 5, "chain": ["outra"]}
        self.assertTrue(_reusable(good, rec, tmp, sig, opts))
        self.assertFalse(_reusable({**good, "input_sha256": "bb"}, rec, tmp, sig, opts))
        self.assertFalse(_reusable({**good, "size": 6}, rec, tmp, sig, opts))
        self.assertFalse(_reusable(good, rec, tmp, sig, DecompileOptions(force=True)))
        failed = {"status": "failed", "input_sha256": "aa", "chain": sig}
        self.assertTrue(_reusable(failed, rec, tmp, sig, opts))
        self.assertFalse(_reusable(failed, rec, tmp, ["uncompyle6=nova"], opts))  # outra cadeia: tenta de novo
        self.assertFalse(_reusable(failed, rec, tmp, sig, DecompileOptions(retry=True)))


class StateLockTests(unittest.TestCase):
    def test_exclusive(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp, True)
        with StateLock(tmp):
            with self.assertRaises(StateLocked):
                with StateLock(tmp):
                    pass
        with StateLock(tmp):  # libertado
            pass


class WorkerProcessTests(unittest.TestCase):
    """Timeout e terminacao inesperada, com um worker falso no Python atual."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp, True)

    def _fake(self, body: str) -> Path:
        p = self.tmp / "fake_worker.py"
        p.write_text("import sys, time, json\n" + textwrap.dedent(body), encoding="utf-8")
        return p

    def test_timeout_restarts(self):
        fake = self._fake("""
            for line in sys.stdin:
                req = json.loads(line)
                if req.get('slow'):
                    time.sleep(30)
                sys.stdout.write(json.dumps({'id': req.get('id'), 'ok': 1}) + '\\n'); sys.stdout.flush()
            """)
        with mock.patch.object(backends, "WORKER_PATH", fake):
            w = WorkerProcess(Path(sys.executable), self.tmp)
            try:
                self.assertEqual(w.request({"id": 1}, 10)["ok"], 1)
                with self.assertRaises(WorkerTimeout):
                    w.request({"id": 2, "slow": True}, 0.5)
                self.assertEqual(w.request({"id": 3}, 10)["ok"], 1)  # novo processo
            finally:
                w.close()

    def test_crash(self):
        fake = self._fake("sys.stdin.readline(); sys.exit(3)\n")
        with mock.patch.object(backends, "WORKER_PATH", fake):
            w = WorkerProcess(Path(sys.executable), self.tmp)
            try:
                with self.assertRaises(WorkerCrashed) as cm:
                    w.request({"id": 1}, 10)
                self.assertIn("3", str(cm.exception))
            finally:
                w.close()


# --------------------------------------------------------------- integracao (Python 2.7)

@unittest.skipUnless(toolchain().py27 is not None, "Python 2.7 com uncompyle6 nao disponivel")
class WorkerTests(unittest.TestCase):
    def setUp(self):
        self.w = WorkerProcess(toolchain().py27.path, Path(tempfile.gettempdir()))
        self.addCleanup(self.w.close)

    def test_decompile_and_validate(self):
        data = compile27(MOD_A, "scripts/client/mod_a.py")
        r = self.w.request({"op": "decompile", "id": 1, "name": "scripts/client/mod_a.pyc",
                            "data": base64.b64encode(data).decode(), "validate": True, "header": "# H\n"}, 60)
        src = base64.b64decode(r["source"])
        self.assertTrue(src.startswith(b"# H\n# uncompyle6 version"))
        self.assertIsNone(r.get("syntax_error"))
        self.assertEqual(r["markers"], 0)
        self.assertIn(b"class Panel(object):", src)
        self.assertIn(b"print 'big', i", src)  # sintaxe de Python 2 preservada

    def test_validate_op(self):
        bad = base64.b64encode(b"def f(:\n  pass\n").decode()
        r = self.w.request({"op": "validate", "id": 2, "name": "x.py", "source": bad}, 60)
        self.assertIn("SyntaxError", r["syntax_error"])
        good = base64.b64encode(b"print 'ok'\n").decode()  # so valido em Python 2
        self.assertIsNone(self.w.request({"op": "validate", "id": 3, "name": "x.py", "source": good}, 60)["syntax_error"])

    def test_non_ascii_gets_cookie(self):
        data = compile27("# -*- coding: utf-8 -*-\nS = 'ção'\n", "m.py")
        r = self.w.request({"op": "decompile", "id": 1, "name": "m.pyc", "data": base64.b64encode(data).decode(),
                            "validate": True, "header": "# H\n"}, 60)
        src = base64.b64decode(r["source"])
        self.assertIsNone(r.get("syntax_error"))
        if r.get("cookie"):
            self.assertEqual(src.split(b"\n")[1], b"# -*- coding: utf-8 -*-")  # 2.a linha (PEP 263)

    def test_garbage(self):
        data = bytes.fromhex("03f30d0a") + b"\0\0\0\0" + b"\xff\x00garbage"
        r = self.w.request({"op": "decompile", "id": 1, "name": "g.pyc", "data": base64.b64encode(data).decode(),
                            "validate": True}, 60)
        self.assertEqual(r["status"], "failed")
        self.assertTrue(r["error"])


@unittest.skipUnless(toolchain().py27 is not None, "Python 2.7 com uncompyle6 nao disponivel")
class DecompileEngineTests(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(long_path(self.tmp), ignore_errors=True))
        self.mod_a = compile27(MOD_A, "scripts/client/mod_a.py")
        self.mod_b = compile27("X = 1\n", "scripts/client/pkg/b.py")
        self.pkgs = {"scripts.pkg": {
            "scripts/client/mod_a.pyc": self.mod_a,
            "scripts/client/pkg/b.pyc": self.mod_b,
            "scripts/client/pkg/b.py": b"X = 1  # original\n",
            "scripts/client/broken.pyc": bytes.fromhex("03f30d0a") + b"\0\0\0\0" + b"\xff\x00lixo",
            "scripts/client/py38.pyc": PYC38,
        }}
        self.cfg = load_config(project_root=self.tmp)
        self.cfg.output_root = self.tmp / "out"
        self.out = self.cfg.realm_output_dir("EU")

    def _extract(self, pkgs=None, prune=False):
        root = make_install(self.tmp / "game", pkgs=pkgs or self.pkgs)
        inst = inspect_install(root, ["cli"], deep=False)
        return run_extract(self.cfg, inst, ExtractOptions(jobs=2, prune=prune))

    def _dec(self, **kw):
        kw.setdefault("jobs", 2)
        return run_decompile(self.cfg, "EU", DecompileOptions(**kw), toolchain=toolchain())

    def _manifest(self):
        return json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))

    def test_requires_manifest(self):
        with self.assertRaises(ManifestError):
            self._dec()

    def test_full_cycle(self):
        self._extract()
        r = self._dec()
        self.assertEqual(r.totals["success"], 2)
        self.assertEqual(r.totals["failed"], 1)
        self.assertEqual(r.totals["unsupported"], 1)
        src_dir = self.out / "sources" / "res" / "scripts" / "client"
        a = (src_dir / "mod_a.py").read_text(encoding="utf-8")
        self.assertTrue(a.startswith("# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/mod_a.pyc"))
        self.assertIn("def helper(*args, **kwargs):", a)
        # o .py original nunca e substituido
        self.assertEqual((src_dir / "pkg" / "b.py").read_bytes(), b"X = 1  # original\n")
        self.assertTrue((src_dir / "pkg" / "b.decompiled.py").is_file())
        self.assertFalse((src_dir / "broken.py").exists())
        m = self._manifest()
        e = m["entries"]
        d = e["res/scripts/client/mod_a.pyc"]["decompiled"]
        self.assertEqual((d["status"], d["validation"], d["backend"]), ("success", "valid", "uncompyle6"))
        self.assertEqual(d["input_sha256"], e["res/scripts/client/mod_a.pyc"]["sha256"])
        self.assertEqual(e["res/scripts/client/broken.pyc"]["decompiled"]["status"], "failed")
        self.assertTrue(e["res/scripts/client/broken.pyc"]["decompiled"]["error"])
        self.assertEqual(e["res/scripts/client/py38.pyc"]["decompiled"]["status"], "unsupported")
        self.assertEqual(m["decompile"]["counts"], {"success": 2, "failed": 1, "unsupported": 1})
        rep = json.loads((self.out / "decompile_report.json").read_text(encoding="utf-8"))
        self.assertEqual([f["key"] for f in rep["failed"]], ["res/scripts/client/broken.pyc"])
        self.assertFalse((self.out / ".state" / "decompile_journal.jsonl").exists())

        # segunda execucao: tudo reaproveitado (o failed tambem, com a mesma cadeia)
        r2 = self._dec()
        self.assertEqual(r2.to_process, 0)
        self.assertEqual(sum(r2.unchanged.values()), 3)
        # --retry volta a tentar so o que nao teve success
        r3 = self._dec(retry=True)
        self.assertEqual(r3.to_process, 1)

        # extract incremental preserva o estado da descompilacao
        self._extract()
        m = self._manifest()
        self.assertEqual(m["entries"]["res/scripts/client/mod_a.pyc"]["decompiled"]["status"], "success")
        self.assertIn("decompile", m)

    def test_changed_pyc_and_prune(self):
        self._extract()
        self._dec()
        pkgs = {"scripts.pkg": dict(self.pkgs["scripts.pkg"])}
        pkgs["scripts.pkg"]["scripts/client/mod_a.pyc"] = compile27("Y = 2\n", "scripts/client/mod_a.py")
        del pkgs["scripts.pkg"]["scripts/client/pkg/b.pyc"]
        self._extract(pkgs, prune=True)
        m = self._manifest()
        self.assertNotIn("decompiled", m["entries"]["res/scripts/client/mod_a.pyc"])  # mudou: refazer
        self.assertFalse((self.out / "sources/res/scripts/client/pkg/b.decompiled.py").exists())  # apagado com o .pyc
        r = self._dec()
        self.assertEqual(r.to_process, 1)
        self.assertIn("Y = 2", (self.out / "sources/res/scripts/client/mod_a.py").read_text(encoding="utf-8"))

    def test_sha_mismatch(self):
        self._extract()
        p = self.out / "sources/res/scripts/client/mod_a.pyc"
        p.write_bytes(p.read_bytes() + b"x")
        r = self._dec(globs=("*mod_a*",))
        self.assertEqual(r.totals["failed"], 1)
        self.assertIn("nao corresponde ao manifesto", r.failures[0]["error"])

    def test_filters_limit_and_dry_run(self):
        self._extract()
        r = self._dec(dry_run=True)
        self.assertEqual((r.selected, r.to_process), (4, 3))  # py38 = unsupported
        self.assertNotIn("decompiled", self._manifest()["entries"]["res/scripts/client/mod_a.pyc"])
        r = self._dec(globs=("scripts/client/pkg/*",))
        self.assertEqual(r.selected, 1)
        r = self._dec(limit=1)
        self.assertEqual((r.to_process, r.limited), (1, 1))

    def test_worse_result_keeps_previous(self):
        self._extract()
        self._dec()
        out = self.out / "sources/res/scripts/client/mod_a.py"
        before = out.read_bytes()

        def worse(self_, key, rec, path):
            att = {"backend": "uncompyle6", "tool": "t", "status": "partial", "validation": "invalid: x",
                   "error": "sintaxe: x", "markers": 1, "code_lines": 3, "cookie": None, "elapsed": 0.0,
                   "timeout": False, "crash": False, "source": b"# pior\n"}
            return key, att, [att], ""

        with mock.patch.object(_Runner, "run", worse):
            r = self._dec(force=True, globs=("*mod_a*",))
        self.assertEqual(r.kept_previous, 1)
        self.assertEqual(out.read_bytes(), before)
        d = self._manifest()["entries"]["res/scripts/client/mod_a.pyc"]["decompiled"]
        self.assertEqual((d["status"], d["kept_previous"]), ("success", True))
        att = self.out / ".state/decompile/attempts/uncompyle6/res/scripts/client/mod_a.py"
        self.assertEqual(att.read_bytes(), b"# pior\n")  # a tentativa nao se perde

    def test_interrupt_and_resume(self):
        self._extract()
        calls = []

        def stop(done, total, counts):
            calls.append(done)
            raise KeyboardInterrupt

        r = run_decompile(self.cfg, "EU", DecompileOptions(jobs=1), progress=stop, toolchain=toolchain())
        self.assertTrue(r.interrupted)
        self.assertTrue((self.out / ".state" / "decompile_journal.jsonl").exists())
        r2 = self._dec(jobs=1)
        self.assertGreaterEqual(r2.resumed, 1)
        self.assertEqual(r2.totals["success"] + r2.totals["failed"], 3)

    def test_locked_tree(self):
        self._extract()
        with StateLock(self.out):
            with self.assertRaises(StateLocked):
                self._dec()


if __name__ == "__main__":
    unittest.main()
