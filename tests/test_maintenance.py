import contextlib
import io
import json
import os
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

from wot_extractor.cli import EXIT_FAIL, EXIT_OK, main
from wot_extractor.extract.writer import long_path
from wot_extractor.maintenance.update import diff

from .helpers import make_install

JS = ("(()=>{var __webpack_modules__={1:e=>{e.exports=R.views.lobby.Foo}};" + "var p=[" +
      ",".join(str(i) for i in range(900)) + "];})();").encode()


def run(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(argv)
    return code, out.getvalue(), err.getvalue()


def files_v1():
    return {"gui-part1.pkg": {
        "gui/gameface/_dist/production/lobby/Foo/Foo.js": JS,
        "gui/gameface/_dist/production/lobby/Foo/Foo.html": b"<html><script src='Foo.js'></script></html>",
        "scripts/client/a.py": b"x = 1\n",
        "gui/x.xml": b"<root><a>1</a></root>",
    }}


class DiffTests(unittest.TestCase):
    def test_diff(self):
        d = diff({"a": "1", "b": "2", "c": "3"}, {"a": "1", "b": "9", "d": "4"})
        self.assertEqual(d, {"new": ["d"], "changed": ["b"], "removed": ["c"]})
        self.assertEqual(diff({}, {"a": "1"})["new"], ["a"])


class MaintenanceCycleTests(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.tmp = Path(self._td.name)
        self.game = self.tmp / "World_of_Tanks_EU"
        make_install(self.game, pkgs=files_v1())
        self._cwd = os.getcwd()
        os.chdir(self.tmp)  # sem wot_extractor.toml real: a saida fica em tmp/wot_src_EU
        self.out = self.tmp / "wot_src_EU"

    def tearDown(self):
        os.chdir(self._cwd)
        shutil.rmtree(long_path(self.tmp), ignore_errors=True)
        self._td.cleanup()

    def _cli(self, *argv):
        base = list(argv[:1]) + ["--no-system", "--realm", "EU"] + list(argv[1:])
        if argv[0] in ("update", "verify"):
            base += ["--path", str(self.game)]
        return run(base)

    def _json(self, name):
        return json.loads((self.out / name).read_text(encoding="utf-8"))

    def test_update_verify_report(self):
        code, out, err = self._cli("update", "--steps", "extract,gameface")
        self.assertEqual(code, EXIT_OK, out + err)
        rep = self._json("update_report.json")
        self.assertEqual((rep["state"], rep["completed"], rep["diff"]["new_total"]), ("primeira extracao", True, 6))  # 4 do pkg + lc.mo + engine_config.xml
        self.assertEqual(list(rep["steps"]), ["extract", "gameface"])
        self.assertTrue((self.out / "sources_gameface/manifests/index.json").is_file())

        code, out, err = self._cli("verify")
        self.assertEqual(code, EXIT_OK, out + err)
        v = self._json("verify_report.json")
        self.assertEqual((v["integrity_ok"], v["update_needed"]), (True, False))
        self.assertEqual(v["counts"]["install_checked"], 6)

        # o jogo e atualizado: a.py alterado, b.py novo, x.xml removido, nova versao
        v2 = files_v1()
        v2["gui-part1.pkg"]["scripts/client/a.py"] = b"x = 2\n"
        v2["gui-part1.pkg"]["scripts/client/b.py"] = b"y = 1\n"
        del v2["gui-part1.pkg"]["gui/x.xml"]
        shutil.rmtree(self.game / "res" / "packages")
        make_install(self.game, version="v.2.4.1.2 #994", pkgs=v2)
        code, out, _ = self._cli("verify", "--no-derived")
        self.assertEqual(code, EXIT_OK)  # a arvore esta integra; so desatualizada
        v = self._json("verify_report.json")
        self.assertTrue(v["update_needed"])
        # a.py mudou no .pkg (CRC); lc.mo foi reescrito pelo make_install (ficheiro solto: tamanho/data)
        self.assertEqual([c["key"] for c in v["install_changed"]], ["res/scripts/client/a.py", "res/text/lc.mo"])
        self.assertEqual(v["install_missing"], ["res/gui/x.xml"])
        self.assertIn("corra 'update'", out)

        code, out, err = self._cli("update", "--steps", "extract,gameface")
        self.assertEqual(code, EXIT_OK, out + err)
        rep = self._json("update_report.json")
        self.assertEqual(rep["state"], "NOVA VERSAO: 2.4.1.1 -> 2.4.1.2")
        self.assertEqual((rep["diff"]["new"], rep["diff"]["changed"], rep["diff"]["removed"]),
                         (["res/scripts/client/b.py", "res_mods/2.4.1.2/engine_config.xml"],
                          ["res/scripts/client/a.py"],
                          ["res/gui/x.xml", "res_mods/2.4.1.1/engine_config.xml"]))  # res_mods/<versao> muda
        self.assertEqual(rep["version_name_now"], "2.4.1.2")
        self.assertTrue((self.out / "sources/res/gui/x.xml").exists())  # sem --prune nada e apagado
        self.assertGreaterEqual(len(list((self.out / ".state" / "reports").glob("update_*.json"))), 1)

        # corrupcao e orfaos sao detetados
        (self.out / "sources/res/scripts/client/a.py").write_bytes(b"x = 3\n")
        (self.out / "sources/res/intruso.txt").write_bytes(b"?")
        code, out, _ = self._cli("verify", "--no-install")
        self.assertEqual(code, EXIT_FAIL)
        v = self._json("verify_report.json")
        self.assertEqual(v["problems"]["hash_mismatch"][0]["key"], "res/scripts/client/a.py")
        self.assertEqual(v["orphans"], ["sources/res/intruso.txt"])
        self.assertIn("res/gui/x.xml", v["removed_from_game_kept"])  # nao e orfao: esta no manifesto como removido
        self.assertFalse(v["integrity_ok"])

        code, out, err = run(["report", "--realm", "EU"])
        self.assertEqual(code, EXIT_OK, out + err)
        r = self._json("report.json")
        self.assertEqual(r["version_name"], "2.4.1.2")
        self.assertFalse(r["phases"]["decompile"]["done"])
        self.assertTrue(r["phases"]["gameface"]["done"])
        self.assertFalse(r["verify"]["integrity_ok"])
        md = (self.out / "REPORT.md").read_text(encoding="utf-8")
        self.assertIn("ORIGINAL", md)
        self.assertIn("not run", md)
        self.assertIn("PROBLEMS FOUND", md)

    def test_update_stops_when_extraction_fails(self):
        # membro com CRC errado: a extracao falha, a versao nao avanca e as fases seguintes nao correm
        pkg = self.game / "res" / "packages" / "gui-part1.pkg"
        pkg.unlink()
        with zipfile.ZipFile(pkg, "w", zipfile.ZIP_STORED) as zf:
            zf.writestr("scripts/client/a.py", b"x = 1234567890\n")
            zf.writestr("gui/gameface/_dist/production/lobby/Foo/Foo.js", JS)
        data = bytearray(pkg.read_bytes())
        i = data.find(b"1234567890")
        data[i] = ord("9")
        pkg.write_bytes(bytes(data))
        code, out, err = self._cli("update", "--steps", "extract,gameface")
        self.assertEqual(code, EXIT_FAIL, out + err)
        rep = self._json("update_report.json")
        self.assertFalse(rep["completed"])
        self.assertIn("nao foi consistente", rep["stopped"])
        self.assertEqual(list(rep["steps"]), ["extract"])
        self.assertFalse((self.out / ".version_name").exists())

    def test_purge_mods_tree(self):
        shutil.rmtree(self.game)
        make_install(self.game, pkgs=files_v1(), wotmods={"me.mod.wotmod": {
            "res/scripts/client/a.py": b"x = 'mod'\n", "res/scripts/client/me/mod.py": b"y = 1\n"}})
        (self.game / "mods" / "configs" / "me").mkdir(parents=True)
        (self.game / "mods" / "configs" / "me" / "c.json").write_text("{}", encoding="utf-8")
        self.assertEqual(self._cli("update", "--steps", "extract,gameface")[0], EXIT_OK)
        m = self._json("manifest.json")
        self.assertIn("overridden_by", m["entries"]["res/scripts/client/a.py"])
        code, out, _ = run(["purge", "--realm", "EU", "--dry-run"])
        self.assertEqual(code, EXIT_OK)
        self.assertIn("3 entradas seriam retiradas", out)
        self.assertTrue((self.out / "sources/mods").exists())
        self.assertEqual(run(["purge", "--realm", "EU"])[0], 2)  # sem --yes nao apaga
        code, out, err = run(["purge", "--realm", "EU", "--yes"])
        self.assertEqual(code, EXIT_OK, out + err)
        self.assertFalse((self.out / "sources/mods").exists())
        m = self._json("manifest.json")
        self.assertFalse([k for k in m["entries"] if k.startswith("mods/")])
        self.assertNotIn("overridden_by", m["entries"]["res/scripts/client/a.py"])  # volta a ser o efetivo
        self.assertEqual(m["filters"]["trees"], ["res", "res_mods"])
        self.assertTrue(self.game.joinpath("mods", "configs", "me", "c.json").is_file())  # o jogo nao e tocado
        code, out, err = self._cli("update", "--steps", "extract")
        self.assertEqual(code, EXIT_OK, out + err)
        d = self._json("update_report.json")["diff"]
        self.assertEqual((d["new_total"], d["removed_total"]), (0, 0))  # os mods nao voltam
        # a pasta sources/mods faz parte da estrutura pedida no readme: fica, mas vazia
        self.assertEqual([p for p in (self.out / "sources/mods").rglob("*") if p.is_file()], [])

    def test_clean_cycle(self):
        from .swfgen import sample_swf
        files = files_v1()
        files["gui-part1.pkg"]["gui/flash/anim.swf"] = sample_swf(with_abc=False)  # sem codigo: 'extracted'
        shutil.rmtree(self.game)
        make_install(self.game, pkgs=files)
        code, out, err = self._cli("update", "--steps", "extract,actionscript,clean")
        self.assertEqual(code, EXIT_OK, out + err)
        swf = self.out / "sources/res/gui/flash/anim.swf"
        self.assertFalse(swf.exists())  # processado e limpo no fim do update
        m = self._json("manifest.json")
        rec = m["entries"]["res/gui/flash/anim.swf"]
        self.assertIn("processado", rec["cleaned"]["reason"])
        self.assertTrue((self.out / rec["actionscript"]["catalog"]).is_file())
        self.assertEqual(m["clean"]["removed"].get("swf"), 1)
        self.assertNotIn("cleaned", m["entries"]["res/scripts/client/a.py"])  # .py original: nunca limpo

        code, out, err = run(["clean", "--realm", "EU"])
        self.assertEqual(code, 2)  # sem --yes
        code, out, err = self._cli("update", "--steps", "extract,actionscript")
        self.assertEqual(code, EXIT_OK, out + err)
        self.assertIn("Extraidos 0", out)  # o limpo conta como inalterado: nao e reextraido
        self.assertFalse(swf.exists())
        self.assertIn("reaproveitados 1", out)
        code, out, err = self._cli("verify")
        self.assertEqual(code, EXIT_OK, out + err)
        v = self._json("verify_report.json")
        self.assertEqual((v["integrity_ok"], v["counts"]["cleaned"]), (True, 1))

        # o jogo muda o SWF: volta a ser extraido, processado e limpo
        files["gui-part1.pkg"]["gui/flash/anim.swf"] = sample_swf("lzma", with_abc=False)
        shutil.rmtree(self.game / "res" / "packages")
        make_install(self.game, pkgs=files)
        code, out, err = self._cli("update", "--steps", "extract,actionscript,clean")
        self.assertEqual(code, EXIT_OK, out + err)
        self.assertEqual(self._json("update_report.json")["diff"]["changed"], ["res/gui/flash/anim.swf"])
        rec = self._json("manifest.json")["entries"]["res/gui/flash/anim.swf"]
        self.assertEqual(rec["actionscript"]["compression"], "lzma")  # reprocessado
        self.assertIn("cleaned", rec)
        self.assertFalse(swf.exists())

    def test_dry_run_and_usage(self):
        code, out, _ = self._cli("update", "--dry-run")
        self.assertEqual(code, EXIT_OK, out)
        self.assertIn("Simulacao", out)
        self.assertFalse((self.out / "manifest.json").exists())
        self.assertEqual(self._cli("update", "--steps", "extract,nada")[0], 2)


if __name__ == "__main__":
    unittest.main()
