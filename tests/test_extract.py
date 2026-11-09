import hashlib
import json
import os
import shutil
import tempfile
import unittest
from pathlib import Path

from wot_extractor.config import load_config
from wot_extractor.constants import PACKED_XML_MAGIC
from wot_extractor.detect import inspect_install
from wot_extractor.extract import ExtractOptions, Filters, ManifestError, build_plan, run_extract
from wot_extractor.extract.validate import inspect_content
from wot_extractor.extract.writer import long_path
from wot_extractor.safety import ProtectedPathError

from .helpers import PYC27, SAMPLE_PACKED, make_install, make_zip, snapshot

PACKED = PACKED_XML_MAGIC + b"\x00binario"


def pkgs(**extra):
    base = {
        "scripts.pkg": {
            "scripts/client/gui/__init__.pyc": PYC27,
            "scripts/client/gui/shared/utils.pyc": PYC27 + b"x",
            "scripts/item_defs/vehicles/list.xml": SAMPLE_PACKED,
            "scripts/plain.xml": b"<root><a>1</a></root>",
        },
        "gui-part1.pkg": {
            "gui/flash/battle.swf": b"CWS\x20" + (1234).to_bytes(4, "little") + b"zz",
            "gui/gameface/_dist/production/lobby/a/a.html": b"<html></html>",
            "gui/gameface/_dist/production/lobby/a/img.png": b"\x89PNG",
            "gui/gameface/_dist/production/lobby/a/data.json": b'{"a": 1}',
            "gui/maps/icons/x.png": b"\x89PNG",
            "gui/bad.json": b"{nope",
        },
        "hd_only.pkg": {"content/x.dds": b"DDS "},
    }
    base.update(extra)
    return base


MODS = {"me.mod_1.0.wotmod": {
    "meta.xml": b"<root><id>me.mod</id></root>",
    "res/scripts/client/gui/__init__.pyc": PYC27 + b"mod",
    "res/gui/gameface/mods/x/window.html": b"<html/>",
}}


class ValidateTests(unittest.TestCase):
    def test_inspect(self):
        self.assertEqual(inspect_content("xml", PACKED)[0], "packed")
        self.assertEqual(inspect_content("xml", b"<a/>")[0], "valid")
        self.assertTrue(inspect_content("xml", b"<a>")[0].startswith("invalid"))
        self.assertTrue(inspect_content("xml", b'<!DOCTYPE a [<!ENTITY x "y">]><a/>')[0].startswith("invalid"))
        self.assertEqual(inspect_content("json", b'\xef\xbb\xbf{"a":1}')[0], "valid")
        self.assertTrue(inspect_content("json", b"{x")[0].startswith("invalid"))
        self.assertEqual(inspect_content("python_bytecode", PYC27), ("valid", {"pyc_version": "2.7"}))
        v, info = inspect_content("scaleform", b"FWS\x0a\x10\x00\x00\x00")
        self.assertEqual((v, info["swf_version"], info["swf_declared_size"]), ("valid", 10, 16))
        self.assertTrue(inspect_content("scaleform", b"XYZ")[0].startswith("invalid"))
        self.assertEqual(inspect_content("image", b"x"), (None, {}))
        # falsos positivos encontrados no cliente real
        self.assertEqual(inspect_content("scaleform", b"PK\x03\x04...", "gui/flash/swc/battle.swc"),
                         ("valid", {"swc": "zip"}))
        self.assertEqual(inspect_content("xml", b"<root>\n<xmlns:xmlref> http://bwt/xmlref </xmlns:xmlref>\n</root>")[0],
                         "valid_bigworld")
        jsonc = b'{\n  /* c */ "a": "http://x", // fim\n  "b": [1, 2,],\n}'
        self.assertEqual(inspect_content("json", jsonc)[0], "valid_jsonc")
        self.assertTrue(inspect_content("json", b'{"a": }')[0].startswith("invalid"))
        self.assertEqual(inspect_content("xml", b"")[0], "empty")


class FilterTests(unittest.TestCase):
    def test_profiles(self):
        dev, gui, full = Filters("dev"), Filters("gui"), Filters("full")
        self.assertTrue(dev.accepts("res", "scripts/a.pyc", "python_bytecode", "scripts.pkg", "zip"))
        self.assertFalse(dev.accepts("res", "gui/maps/x.png", "image", "gui-part1.pkg", "zip"))
        self.assertTrue(dev.accepts("res", "gui/gameface/x.png", "image", "gui-part1.pkg", "zip"))
        self.assertTrue(gui.accepts("res", "gui/maps/x.png", "image", "gui-part1.pkg", "zip"))
        self.assertFalse(gui.accepts("res", "content/x.dds", "image", "x.pkg", "zip"))
        self.assertTrue(full.accepts("res", "content/x.dds", "image", "x.pkg", "zip"))
        with self.assertRaises(ValueError):
            Filters("nope")

    def test_ext_container_tree(self):
        f = Filters("full", extensions=frozenset({".pyc"}), containers=("scripts*",))
        self.assertTrue(f.accepts("res", "a/b.pyc", "python_bytecode", "scripts.pkg", "zip"))
        self.assertFalse(f.accepts("res", "a/b.xml", "xml", "scripts.pkg", "zip"))
        self.assertFalse(f.accepts("res", "a/b.pyc", "python_bytecode", "gui.pkg", "zip"))
        self.assertFalse(f.accepts("res", "a/b.pyc", "python_bytecode", "b.pyc", "file"))
        self.assertFalse(Filters("full", trees=frozenset({"mods"})).accepts("res", "a", "other", "x", "file"))


class _Base(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.tmp = Path(self._td.name)
        self.game = self.tmp / "World_of_Tanks_EU"
        make_install(self.game, pkgs=pkgs(), wotmods=MODS)
        (self.game / "mods" / "configs" / "me").mkdir(parents=True)
        (self.game / "mods" / "configs" / "me" / "cfg.json").write_text('{"on": true}', encoding="utf-8")
        self.cfg = load_config(project_root=self.tmp / "proj")
        self.out = self.cfg.realm_output_dir("EU")

    def tearDown(self):
        self._td.cleanup()

    def install(self, app_type=None):
        return inspect_install(self.game, deep=False)

    def extract(self, **kw):
        return run_extract(self.cfg, self.install(), ExtractOptions(jobs=kw.pop("jobs", 3), **kw))

    def manifest(self):
        return json.loads((self.out / "manifest.json").read_text(encoding="utf-8"))


class PlanTests(_Base):
    def test_plan_layout(self):
        plan = build_plan(self.install())
        keys = {e.key: e for e in plan.entries}
        self.assertIn("res/scripts/client/gui/__init__.pyc", keys)
        self.assertIn("res/gui/flash/battle.swf", keys)
        self.assertIn("res/gui/gameface/_dist/production/lobby/a/img.png", keys)   # gameface: tudo
        self.assertNotIn("res/gui/maps/icons/x.png", keys)                         # dev: sem imagens
        self.assertNotIn("res/content/x.dds", keys)
        self.assertIn("res/text/lc.mo", keys)                                      # res solto
        self.assertIn("res_mods/2.4.1.1/engine_config.xml", keys)
        self.assertEqual(keys["res_mods/2.4.1.1/engine_config.xml"].virtual, "engine_config.xml")
        mod_key = "mods/2.4.1.1/me.mod_1.0.wotmod/res/scripts/client/gui/__init__.pyc"
        self.assertEqual(keys[mod_key].virtual, "scripts/client/gui/__init__.pyc")
        self.assertIn("mods/2.4.1.1/me.mod_1.0.wotmod/meta.xml", keys)
        self.assertIn("mods/configs/me/cfg.json", keys)
        self.assertEqual(keys["res/scripts/client/gui/__init__.pyc"].overridden_by,
                         ["mods:mods/2.4.1.1/me.mod_1.0.wotmod"])
        self.assertEqual(plan.containers[:3], ["res/packages/scripts.pkg", "res/packages/gui-part1.pkg",
                                               "res/packages/hd_only.pkg"])
        self.assertGreater(plan.filtered_out, 0)
        self.assertEqual(plan.failures, [])

    def test_precedence_shadowing_and_collisions(self):
        make_install(self.game, pkgs={
            "a.pkg": {"scripts/x.xml": b"<a/>", "scripts/Case.xml": b"<a/>"},
            "b.pkg": {"scripts/x.xml": b"<b/>", "scripts/case.xml": b"<b/>"},
        })
        for f in ("scripts.pkg", "gui-part1.pkg", "hd_only.pkg"):
            (self.game / "res" / "packages" / f).unlink()
        plan = build_plan(self.install())
        keys = {e.key: e for e in plan.entries}
        self.assertEqual(keys["res/scripts/x.xml"].container, "res/packages/a.pkg")
        self.assertEqual(keys["res/scripts/x.xml"].shadows, ["res/packages/b.pkg"])
        self.assertEqual(len(plan.collisions), 1)
        self.assertNotIn("res/scripts/case.xml", keys)

    def test_sd_client_skips_hd_pkgs(self):
        make_install(self.game, app_type="sd", pkgs=pkgs())
        plan = build_plan(self.install(), Filters("full"))
        self.assertTrue(any(s["container"].endswith("hd_only.pkg") for s in plan.skipped_containers))
        self.assertFalse(any(e.container.endswith("hd_only.pkg") for e in plan.entries))

    def test_unsafe_and_corrupt(self):
        make_zip(self.game / "res" / "packages" / "scripts.pkg", {"../evil.xml": b"<a/>", "ok.xml": b"<a/>"})
        (self.game / "res" / "packages" / "gui-part1.pkg").write_bytes(b"corrompido")
        plan = build_plan(self.install())
        errs = " ".join(f["error"] for f in plan.failures)
        self.assertIn("path traversal", errs)
        self.assertIn("ilegivel", errs)
        self.assertIn("res/ok.xml", {e.key for e in plan.entries})


class ExtractTests(_Base):
    def test_first_extraction(self):
        before = snapshot(self.game)
        r = self.extract()
        self.assertTrue(r.consistent, r.failures)
        self.assertEqual(snapshot(self.game), before)  # instalacao intacta
        pyc = self.out / "sources" / "res" / "scripts" / "client" / "gui" / "__init__.pyc"
        self.assertEqual(pyc.read_bytes(), PYC27)
        self.assertEqual((self.out / "sources" / "mods" / "2.4.1.1" / "me.mod_1.0.wotmod" / "res" / "scripts"
                          / "client" / "gui" / "__init__.pyc").read_bytes(), PYC27 + b"mod")
        self.assertTrue((self.out / "sources" / "res_mods" / "2.4.1.1" / "engine_config.xml").is_file())
        for d in ("sources_as/swf", "sources_gameface/manifests", "__stubs/gui"):
            self.assertTrue((self.out / d).is_dir(), d)
        self.assertEqual((self.out / ".version_name").read_text().strip(), "2.4.1.1")
        m = self.manifest()
        self.assertEqual((m["realm"], m["version_name"], m["consistent"]), ("EU", "2.4.1.1", True))
        e = m["entries"]["res/scripts/client/gui/__init__.pyc"]
        self.assertEqual(e["sha256"], hashlib.sha256(PYC27).hexdigest())
        self.assertEqual((e["status"], e["container"], e["info"]["pyc_version"]), ("extracted", "res/packages/scripts.pkg", "2.7"))
        self.assertEqual(m["entries"]["res/scripts/item_defs/vehicles/list.xml"]["validation"], "packed")
        self.assertEqual(m["entries"]["res/scripts/plain.xml"]["validation"], "valid")
        self.assertTrue(m["entries"]["res/gui/bad.json"]["validation"].startswith("invalid"))
        self.assertEqual(m["entries"]["res/gui/flash/battle.swf"]["info"]["swf_signature"], "CWS")
        self.assertEqual(m["counts"]["failed"], 0)
        rep = json.loads((self.out / "extraction_report.json").read_text(encoding="utf-8"))
        self.assertEqual(rep["validation"]["xml"]["packed"], 1)
        self.assertEqual(rep["invalid_files"][0]["path"], "res/gui/bad.json")
        self.assertEqual(len(list((self.out / ".state" / "reports").glob("extraction_*.json"))), 1)
        self.assertFalse((self.out / ".state" / "journal.jsonl").exists())
        self.assertFalse(list(self.out.rglob("*.part~")))
        # copia legivel do XML binario; original intacto
        orig = self.out / "sources" / "res" / "scripts" / "item_defs" / "vehicles" / "list.xml"
        self.assertEqual(orig.read_bytes(), SAMPLE_PACKED)
        dec = self.out / "sources_xml" / "res" / "scripts" / "item_defs" / "vehicles" / "list.xml"
        text = dec.read_text(encoding="utf-8")
        self.assertTrue(text.startswith("<!-- Copia descodificada"))
        self.assertIn("<price>373000</price>", text)
        d = m["entries"]["res/scripts/item_defs/vehicles/list.xml"]["decoded"]
        self.assertEqual((d["status"], d["validation"], d["path"]),
                         ("success", "valid_bigworld", "sources_xml/res/scripts/item_defs/vehicles/list.xml"))
        self.assertEqual(d["sha256"], hashlib.sha256(dec.read_bytes()).hexdigest())
        self.assertNotIn("decoded", m["entries"]["res/scripts/plain.xml"])
        self.assertEqual(rep["xml_decode"]["status"], {"success": 1})
        self.assertEqual(m["tool_versions"]["bwxml_decoder"], 1)

    def test_incremental_and_removed(self):
        self.extract()
        pyc = self.out / "sources" / "res" / "scripts" / "client" / "gui" / "__init__.pyc"
        mtime = pyc.stat().st_mtime_ns
        r = self.extract()
        self.assertEqual(r.counts["extracted"], 0)
        self.assertEqual(r.counts["unchanged"], r.selected)
        self.assertEqual(pyc.stat().st_mtime_ns, mtime)
        # alterar um membro e remover outro
        p = pkgs()
        p["scripts.pkg"]["scripts/client/gui/__init__.pyc"] = PYC27 + b"v2"
        del p["scripts.pkg"]["scripts/plain.xml"]
        make_zip(self.game / "res" / "packages" / "scripts.pkg", p["scripts.pkg"])
        r = self.extract()
        self.assertEqual(r.counts["extracted"], 1)
        self.assertEqual(r.removed, ["res/scripts/plain.xml"])
        self.assertEqual(pyc.read_bytes(), PYC27 + b"v2")
        plain = self.out / "sources" / "res" / "scripts" / "plain.xml"
        self.assertTrue(plain.exists())  # nao apaga sem --prune
        self.assertEqual(self.manifest()["entries"]["res/scripts/plain.xml"]["status"], "removed")
        r = self.extract(prune=True)
        self.assertEqual(r.pruned, ["res/scripts/plain.xml"])
        self.assertFalse(plain.exists())
        self.assertNotIn("res/scripts/plain.xml", self.manifest()["entries"])

    def test_validator_upgrade_revalidates_without_rewriting(self):
        self.extract()
        mpath = self.out / "manifest.json"
        m = self.manifest()
        m["tool_versions"]["validator"] = 1
        m["entries"]["res/gui/bad.json"]["validation"] = "valid"  # veredicto antigo/errado
        mpath.write_text(json.dumps(m), encoding="utf-8")
        target = self.out / "sources" / "res" / "gui" / "bad.json"
        mtime = target.stat().st_mtime_ns
        r = self.extract()
        self.assertEqual(r.counts["extracted"], 0)
        self.assertGreater(r.revalidated, 0)
        self.assertTrue(self.manifest()["entries"]["res/gui/bad.json"]["validation"].startswith("invalid"))
        self.assertEqual(target.stat().st_mtime_ns, mtime)
        self.assertEqual(self.extract().revalidated, 0)

    def _dec_path(self):
        return self.out / "sources_xml" / "res" / "scripts" / "item_defs" / "vehicles" / "list.xml"

    def test_xml_decode_incremental_and_decoder_upgrade(self):
        self.extract()
        mtime = self._dec_path().stat().st_mtime_ns
        r = self.extract()
        self.assertEqual((r.xml.decoded, r.xml.reused), (0, 1))
        self.assertEqual(self._dec_path().stat().st_mtime_ns, mtime)
        m = self.manifest()
        m["entries"]["res/scripts/item_defs/vehicles/list.xml"]["decoded"]["decoder"] = 0
        (self.out / "manifest.json").write_text(json.dumps(m), encoding="utf-8")
        r = self.extract()
        self.assertEqual((r.xml.decoded, r.xml.reused), (1, 0))
        self._dec_path().unlink()  # copia apagada -> regenerada
        self.assertEqual(self.extract().xml.decoded, 1)
        self.assertTrue(self._dec_path().is_file())

    def test_corrupt_packed_xml_does_not_block_consistency(self):
        p = pkgs()
        p["scripts.pkg"]["scripts/broken.xml"] = PACKED  # assinatura certa, estrutura invalida
        make_zip(self.game / "res" / "packages" / "scripts.pkg", p["scripts.pkg"])
        r = self.extract()
        self.assertTrue(r.consistent)
        self.assertEqual(r.xml.status["failed"], 1)
        self.assertEqual(r.xml.failures[0]["key"], "res/scripts/broken.xml")
        self.assertEqual(self.manifest()["entries"]["res/scripts/broken.xml"]["decoded"]["status"], "failed")
        self.assertFalse((self.out / "sources_xml" / "res" / "scripts" / "broken.xml").exists())

    def test_no_decode_option(self):
        r = self.extract(decode_xml=False)
        self.assertIsNone(r.xml)
        self.assertFalse(self._dec_path().exists())

    def test_prune_removes_decoded_copy(self):
        self.extract()
        p = pkgs()
        del p["scripts.pkg"]["scripts/item_defs/vehicles/list.xml"]
        make_zip(self.game / "res" / "packages" / "scripts.pkg", p["scripts.pkg"])
        r = self.extract(prune=True)
        self.assertIn("res/scripts/item_defs/vehicles/list.xml", r.pruned)
        self.assertFalse(self._dec_path().exists())

    def test_parallel_decode_in_processes(self):
        p = pkgs()
        for i in range(70):
            p["scripts.pkg"][f"scripts/many/f{i:02d}.xml"] = SAMPLE_PACKED
        make_zip(self.game / "res" / "packages" / "scripts.pkg", p["scripts.pkg"])
        r = self.extract(jobs=2)
        self.assertTrue(r.xml.parallel)
        self.assertEqual(r.xml.status["success"], 71)
        self.assertTrue((self.out / "sources_xml" / "res" / "scripts" / "many" / "f69.xml").is_file())

    def test_deleted_output_is_restored(self):
        self.extract()
        target = self.out / "sources" / "res" / "gui" / "flash" / "battle.swf"
        target.unlink()
        r = self.extract()
        self.assertEqual(r.counts["extracted"], 1)
        self.assertTrue(target.is_file())

    def test_filtered_run_keeps_out_of_scope_entries(self):
        self.extract()
        n = len(self.manifest()["entries"])
        r = self.extract(filters=Filters("dev", extensions=frozenset({".pyc"})))
        self.assertEqual(r.removed, [])
        self.assertEqual(len(self.manifest()["entries"]), n)

    def test_inconsistent_run_keeps_version_name(self):
        self.extract()
        (self.out / ".version_name").write_text("ANTERIOR\n")
        p = pkgs()
        p["scripts.pkg"]["../evil.pyc"] = PYC27
        make_zip(self.game / "res" / "packages" / "scripts.pkg", p["scripts.pkg"])
        r = self.extract()
        self.assertFalse(r.consistent)
        self.assertEqual((self.out / ".version_name").read_text(), "ANTERIOR\n")
        self.assertFalse(self.manifest()["consistent"])
        self.assertFalse((self.out.parent / "evil.pyc").exists())
        self.assertTrue((self.out / ".state" / "manifest.prev.json").is_file())

    def test_version_change(self):
        self.extract()
        v = self.game / "version.xml"
        v.write_text(v.read_text(encoding="utf-8").replace("v.2.4.1.1 #993", "v.2.4.1.2 #994"), encoding="utf-8")
        (self.game / "res_mods" / "2.4.1.1").rename(self.game / "res_mods" / "2.4.1.2")
        r = self.extract()
        self.assertEqual((r.previous_version, r.version_name), ("2.4.1.1", "2.4.1.2"))
        self.assertEqual((self.out / ".version_name").read_text().strip(), "2.4.1.2")

    def test_interrupt_and_resume(self):
        calls = {"n": 0}

        def boom(done, total, written):
            calls["n"] += 1
            if calls["n"] == 1:
                raise KeyboardInterrupt

        r = run_extract(self.cfg, self.install(), ExtractOptions(jobs=1), progress=boom)
        self.assertTrue(r.interrupted)
        self.assertFalse((self.out / "manifest.json").exists())
        self.assertFalse((self.out / ".version_name").exists())
        journal = self.out / ".state" / "journal.jsonl"
        self.assertTrue(journal.is_file())
        r2 = self.extract()
        self.assertTrue(r2.consistent)
        self.assertGreater(r2.resumed, 0)
        self.assertGreater(r2.counts["unchanged"], 0)
        self.assertFalse(journal.exists())

    def test_dry_run_writes_nothing(self):
        r = self.extract(dry_run=True)
        self.assertGreater(r.to_extract, 0)
        self.assertFalse(self.out.exists())

    def test_realm_mismatch_and_protected_output(self):
        self.out.mkdir(parents=True)
        (self.out / "manifest.json").write_text(json.dumps({"realm": "CT", "entries": {}}))
        with self.assertRaises(ManifestError):
            self.extract()
        cfg = load_config(project_root=self.game / "dentro")
        with self.assertRaises(ProtectedPathError):
            run_extract(cfg, self.install(), ExtractOptions())

    def test_long_paths(self):
        deep = "/".join(["diretorio_com_nome_longo_%02d" % i for i in range(10)]) + "/ficheiro.xml"
        make_zip(self.game / "res" / "packages" / "scripts.pkg", {deep: b"<a/>"})
        r = self.extract()
        self.assertTrue(r.consistent, r.failures)
        target = self.out / "sources" / "res" / deep
        self.assertGreater(len(str(target)), 260)
        self.assertTrue(os.path.isfile(long_path(target)))
        self.assertEqual(r.long_paths, 1)
        shutil.rmtree(long_path(self.out))  # sem LongPathsEnabled o cleanup normal falha

    def test_full_profile(self):
        r = self.extract(filters=Filters("full"))
        self.assertTrue(r.consistent)
        self.assertTrue((self.out / "sources" / "res" / "content" / "x.dds").is_file())
        self.assertTrue((self.out / "sources" / "res" / "gui" / "maps" / "icons" / "x.png").is_file())


if __name__ == "__main__":
    unittest.main()
