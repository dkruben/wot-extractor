"""Melhorias apos a fase G: RABCDAsm (.asasm), indice de APIs (index/search) e comparacao de realms."""

import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from wot_extractor.actionscript import ASOptions, run_actionscript
from wot_extractor.actionscript import ffdec as ffdec_mod
from wot_extractor.actionscript import rabcdasm as rabcdasm_mod
from wot_extractor.actionscript.ffdec import ExportRun, FFDec
from wot_extractor.actionscript.rabcdasm import Rabc, find_rabcdasm
from wot_extractor.apiindex import build_index, search
from wot_extractor.compare import compare_realms, norm_key
from wot_extractor.config import load_config
from wot_extractor.detect.install import inspect_install
from wot_extractor.extract import ExtractOptions, run_extract
from wot_extractor.extract.writer import long_path
from wot_extractor.gameface import GFOptions, run_gameface

from .helpers import make_install
from .swfgen import sample_swf
from .test_stubs import py27

FF = FFDec(Path("java"), Path("ffdec-cli.jar"), "99.0")


def real_rabc():
    try:
        cfg = load_config()  # wot_extractor.toml do projeto, se existir
        r, _ = find_rabcdasm(cfg.rabcdasm)
    except Exception:  # noqa: BLE001
        r = None
    return r


def fake_export(ff, swf, out_dir, items, timeout, mt, ct):
    d = out_dir / "scripts" / "net" / "test"
    d.mkdir(parents=True)
    (d / "Foo.as").write_text("package net.test {\n public class Foo {\n  public function run(a:int) : void {\n"
                              "   §§push(1);\n  }\n }\n}\n", encoding="utf-8")
    return ExportRun(0, 0.1, False, "log")


def fake_disassemble(rabc, swf_bytes, work, timeout=0):
    d = work / "movie-0" / "net" / "test"
    d.mkdir(parents=True)
    (d / "Foo.class.asasm").write_text("class\n refid \"net.test:Foo\"\n", encoding="utf-8")
    (d / "Foo.script.asasm").write_text("script\n", encoding="utf-8")
    return [work / "movie-0"], "", 0.1


class _Realm(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(lambda: shutil.rmtree(long_path(self.tmp), ignore_errors=True))
        self.cfg = load_config(project_root=self.tmp)
        self.cfg.output_root = self.tmp / "out"

    def extract(self, realm="EU", pkgs=None, wotmods=None, version=None):
        kw = {"realm": realm}
        if version:
            kw["version"] = version
        root = make_install(self.tmp / f"game_{realm}", pkgs=pkgs, wotmods=wotmods, **kw)
        return run_extract(self.cfg, inspect_install(root, ["cli"], deep=False), ExtractOptions(jobs=2))

    def manifest(self, realm="EU"):
        return json.loads((self.cfg.realm_output_dir(realm) / "manifest.json").read_text(encoding="utf-8"))


class AsasmTests(_Realm):
    def test_asasm_pass_for_partial(self):
        self.extract(pkgs={"gui-part1.pkg": {"gui/flash/app.swf": sample_swf()}})
        opts = ASOptions(jobs=1, rabc=Rabc(self.tmp), asasm="partial")
        with mock.patch.object(ffdec_mod, "export", fake_export), \
                mock.patch.object(rabcdasm_mod, "disassemble", side_effect=fake_disassemble) as dis:
            r = run_actionscript(self.cfg, "EU", opts, ff=FF)
            self.assertEqual((r.asasm_selected, r.asasm_done), (1, 1))
            a = self.manifest()["entries"]["res/gui/flash/app.swf"]["actionscript"]
            self.assertEqual(a["status"], "partial")  # §§ no Foo.as
            asm = a["asasm"]
            self.assertEqual((asm["dir"], asm["files"]), ("sources_as/asasm/res/gui/flash/app.swf", 2))
            self.assertEqual(asm["unstructured"][0]["asasm"],
                             "sources_as/asasm/res/gui/flash/app.swf/movie-0/net/test/Foo.class.asasm")
            out = self.cfg.realm_output_dir("EU")
            self.assertTrue((out / asm["unstructured"][0]["asasm"]).is_file())
            r2 = run_actionscript(self.cfg, "EU", opts, ff=FF)  # ja feito: nao repete
            self.assertEqual((r2.asasm_selected, dis.call_count), (0, 1))
            run_actionscript(self.cfg, "EU", ASOptions(jobs=1, rabc=Rabc(self.tmp), asasm="none", force=True), ff=FF)
            self.assertEqual(dis.call_count, 1)

    @unittest.skipUnless(real_rabc() is not None, "RABCDAsm nao configurado")
    def test_real_rabcdasm(self):
        dirs, err, _ = rabcdasm_mod.disassemble(real_rabc(), sample_swf("none"), self.tmp / "w")
        self.assertEqual(err, "")
        self.assertTrue((dirs[0] / "net" / "test" / "Foo.class.asasm").is_file())


@unittest.skipUnless(py27() is not None, "Python 2.7 nao disponivel")
class IndexCompareTests(_Realm):
    PY = (b'"""Modulo foo."""\nimport BigWorld\nLIMIT = 3\n\nclass Foo(object):\n    """Classe Foo."""\n'
          b'    def run(self, a, b=1):\n        BigWorld.callback(0, a)\n\ndef helper(x):\n    pass\n')

    def _realm(self, realm, py, extra=None, version=None):
        files = {"scripts/client/gui/foo.py": py, "gui/flash/app.swf": sample_swf()}
        files.update(extra or {})
        self.extract(realm, pkgs={"gui-part1.pkg": files},
                     wotmods={"me.mod.wotmod": {"res/scripts/client/me/m.py": b"X = 1\n"}}, version=version)
        from wot_extractor.stubs import StubOptions, run_stubs
        run_stubs(self.cfg, realm, StubOptions(jobs=1), interp=py27(), interp_label="py27")
        run_actionscript(self.cfg, realm, ASOptions(jobs=1, use_ffdec=False, asasm="none"))
        run_gameface(self.cfg, realm, GFOptions(jobs=1, use_node=False))

    def test_index_search_compare(self):
        self._realm("EU", self.PY)
        r = build_index(self.cfg, "EU")
        self.assertFalse(r.skipped)
        self.assertEqual(r.counts["class"], 1)
        self.assertGreaterEqual(r.counts["as3_class"], 1)
        self.assertTrue(build_index(self.cfg, "EU").skipped)  # sem alteracoes
        hits = search(self.cfg, "run", kinds=["method"])
        self.assertEqual(hits[0]["qualname"], "gui.foo.Foo.run")
        self.assertEqual(hits[0]["signature"], "(self, a, b=1)")
        self.assertTrue(hits[0]["file"].endswith("gui/foo.py") and hits[0]["line"] == 7)
        self.assertEqual(search(self.cfg, "BigWorld.callback", exact=True)[0]["kind"], "native")
        self.assertEqual(search(self.cfg, "net.test.Foo", exact=True)[0]["kind"], "as3_class")
        self.assertEqual(search(self.cfg, "Classe", kinds=["class"])[0]["name"], "Foo")  # pela docstring

        py_ct = self.PY.replace(b"def run(self, a, b=1)", b"def run(self, a, b=1, c=None)") + b"\nclass Bar:\n    pass\n"
        self._realm("CT", py_ct.replace(b"def helper(x):\n    pass\n", b""), version="v.2.4.2.0 Common Test #995")
        res, jp, mp = compare_realms(self.cfg, "EU", "CT")
        py = res["python_api"]
        self.assertIn({"kind": "class", "name": "gui.foo.Bar", "signature": None}, py["added"])
        self.assertIn("gui.foo.helper", [x["name"] for x in py["removed"]])
        sig = [x for x in py["signature_changed"] if x["name"] == "gui.foo.Foo.run"][0]
        self.assertEqual((sig["before"], sig["after"]), ("(self, a, b=1)", "(self, a, b=1, c=None)"))
        self.assertEqual(res["files"]["counts"]["changed"], 1)  # so o foo.py (o mod em mods/<versao> e igual)
        self.assertTrue(jp.is_file() and mp.is_file())
        self.assertIn("Changed signatures", mp.read_text(encoding="utf-8"))
        hits = search(self.cfg, "gui.foo.Foo.run", exact=True)
        self.assertEqual(sorted(h["realm"] for h in hits), ["CT", "EU"])

    def test_norm_key(self):
        self.assertEqual(norm_key("mods/2.4.1.1/a.wotmod/x.py", {"tree": "mods"}), "mods/*/a.wotmod/x.py")
        self.assertEqual(norm_key("mods/configs/a.json", {"tree": "mods"}), "mods/configs/a.json")
        self.assertEqual(norm_key("res/a.xml", {"tree": "res"}), "res/a.xml")


if __name__ == "__main__":
    unittest.main()
