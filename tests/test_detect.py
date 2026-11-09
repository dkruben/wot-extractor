import tempfile
import unittest
from pathlib import Path

from wot_extractor.config import load_config
from wot_extractor.detect import detect, inspect_install
from wot_extractor.detect.detector import _rank
from wot_extractor.detect.install import ClientInstall
from wot_extractor.detect.sources import scan_candidates, wgc_candidates
from wot_extractor.detect.xmlinfo import VersionInfo

from .helpers import PYC27, make_install, snapshot


class InspectTests(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.tmp = Path(self._td.name)

    def tearDown(self):
        self._td.cleanup()

    def test_full_inspection_eu(self):
        root = make_install(self.tmp / "EU", wotmods={"me.mod_1.0.wotmod": {
            "meta.xml": b"<root/>", "res/scripts/client/gui/mods/mod_x.pyc": PYC27,
            "res/gui/gameface/mods/x/window.html": b"<html/>"}})
        inst = inspect_install(root, ["test"], deep=True)
        self.assertTrue(inst.valid, inst.issues)
        self.assertEqual((inst.realm, inst.realm_source, inst.app_type), ("EU", "version.xml", "hd"))
        self.assertEqual(inst.version.number, "2.4.1.1")
        self.assertEqual(Path(inst.dirs["res_mods"]).name, "2.4.1.1")
        self.assertEqual(inst.packages["on_disk"], 3)
        self.assertEqual(inst.packages["active_for_app_type"], 3)
        self.assertEqual(inst.packages["missing_active"], [])
        self.assertEqual([m["name"] for m in inst.mods], ["me.mod_1.0.wotmod"])
        self.assertEqual(inst.res_mods["files"], 1)
        self.assertEqual(inst.loose_res["files"], 1)  # res/text/lc.mo; packages excluidos
        pk = inst.content["packages"]
        self.assertEqual(pk["categories"]["python_bytecode"], 2)
        self.assertEqual(pk["gameface_entries"], 2)
        self.assertEqual(pk["pyc_versions_sample"], {"2.7": 2})
        self.assertEqual(pk["containers_with"]["python_bytecode"], ["scripts.pkg"])
        self.assertEqual(pk["containers_with"]["scaleform"], ["gui-part1.pkg"])
        md = inst.content["mods"]
        self.assertEqual((md["gameface_entries"], md["categories"]["python_bytecode"]), (1, 1))
        self.assertEqual(inst.issues, [])

    def test_sd_client_filters_hd_packages_and_flags_missing(self):
        root = make_install(self.tmp / "CT", realm="CT", version="v.2.4.2.0 Common Test #995",
                            app_type="sd", extra_listed=["gone.pkg"])
        inst = inspect_install(root, deep=False)
        self.assertEqual(inst.version.folder_name, "2.4.2.0 Common Test")
        self.assertEqual(Path(inst.dirs["mods"]).name, "2.4.2.0 Common Test")
        self.assertEqual(inst.packages["active_for_app_type"], 3)  # hd_only excluido, gone incluido
        self.assertEqual(inst.packages["missing_active"], ["gone.pkg"])
        self.assertTrue(any("em falta no disco" in i for i in inst.issues))

    def test_unlisted_and_no_paths_xml(self):
        root = make_install(self.tmp / "EU", paths_xml=False)
        inst = inspect_install(root, deep=False)
        self.assertTrue(inst.valid)
        self.assertIsNone(inst.paths)
        self.assertEqual(Path(inst.dirs["res_mods"]).name, "2.4.1.1")  # fallback pela versao
        self.assertEqual(len(inst.packages["unlisted_on_disk"]), 3)

    def test_realm_inconsistency_and_invalid(self):
        root = make_install(self.tmp / "X", realm="EU", game_info_realm="NA")
        inst = inspect_install(root, deep=False)
        self.assertEqual(inst.realm, "EU")
        self.assertTrue(any("inconsistente" in i for i in inst.issues))
        empty = self.tmp / "vazio"
        empty.mkdir()
        self.assertFalse(inspect_install(empty).valid)
        self.assertFalse(inspect_install(self.tmp / "nao_existe").valid)

    def test_corrupt_package_reported(self):
        root = make_install(self.tmp / "EU")
        (root / "res" / "packages" / "scripts.pkg").write_bytes(b"corrompido")
        inst = inspect_install(root, deep=True)
        self.assertTrue(any("ilegivel scripts.pkg" in i for i in inst.issues))
        self.assertNotIn("scripts.pkg", inst.content["packages"]["containers_with"]["python_bytecode"])

    def test_detection_is_read_only(self):
        root = make_install(self.tmp / "EU", wotmods={"a.wotmod": {"res/x.pyc": PYC27}})
        before = snapshot(root)
        inspect_install(root, deep=True)
        self.assertEqual(snapshot(root), before)


class DetectTests(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.tmp = Path(self._td.name)
        self.eu = make_install(self.tmp / "Games" / "World_of_Tanks_EU")
        self.ct = make_install(self.tmp / "Games" / "World_of_Tanks_CT", realm="CT",
                               version="v.2.4.2.0 Common Test #995", app_type="sd")
        self.cfg = load_config(project_root=self.tmp)

    def tearDown(self):
        self._td.cleanup()

    def _cfg_with(self, **installs):
        for realm, p in installs.items():
            self.cfg.realm(realm).install = p
            self.cfg.realm(realm).preferred_drive = ""
        return self.cfg

    def test_config_paths(self):
        res = detect(self._cfg_with(EU=self.eu, CT=self.ct), deep=False, use_system=False)
        self.assertTrue(res.ok, res.errors)
        self.assertEqual(res.selected["EU"].path, self.eu)
        self.assertEqual(res.selected["CT"].path, self.ct)
        self.assertIn("config:EU", res.selected["EU"].sources)

    def test_cli_override_wins_and_realm_mismatch(self):
        res = detect(self._cfg_with(EU=self.eu), realms=["EU"], overrides={"EU": self.ct}, deep=False, use_system=False)
        self.assertIsNone(res.selected["EU"])
        self.assertIn("pertence ao realm CT", res.errors["EU"])

    def test_invalid_manual_path(self):
        res = detect(self.cfg, realms=["EU"], overrides={"EU": self.tmp / "nada"}, deep=False, use_system=False)
        self.assertIn("invalido", res.errors["EU"])
        self.assertEqual(len(res.rejected), 1)

    def test_missing_realm(self):
        res = detect(self._cfg_with(EU=self.eu), deep=False, use_system=False)
        self.assertFalse(res.ok)
        self.assertIn("CT", res.errors)
        self.assertIsNotNone(res.selected["EU"])

    def test_to_dict(self):
        d = detect(self._cfg_with(EU=self.eu, CT=self.ct), deep=True, use_system=False).to_dict()
        self.assertEqual(d["selected"]["EU"]["version"]["number"], "2.4.1.1")
        self.assertEqual(d["selected"]["CT"]["version"]["folder_name"], "2.4.2.0 Common Test")
        self.assertTrue(d["selected"]["EU"]["package_probes"])

    def test_scan_finds_installs(self):
        found = {c.path.name for c in scan_candidates([str(self.tmp)], depth=2)}
        self.assertEqual(found, {"World_of_Tanks_EU", "World_of_Tanks_CT"})
        self.assertEqual(scan_candidates([str(self.tmp)], depth=0), [])

    def test_wgc_preferences(self):
        pd = self.tmp / "ProgramData"
        pref = pd / "Wargaming.net" / "GameCenter" / "preferences.xml"
        pref.parent.mkdir(parents=True)
        pref.write_text(f"<protocol><application><games_manager><games><game><working_dir>{self.eu}</working_dir>"
                        "</game></games></games_manager></application></protocol>", encoding="utf-8")
        self.assertEqual([c.path for c in wgc_candidates(pd)], [self.eu])
        self.assertEqual(wgc_candidates(self.tmp / "nada"), [])


class RankTests(unittest.TestCase):
    def _inst(self, path, number, build, sources=("scan",)):
        i = ClientInstall(Path(path), list(sources), True, "EU")
        i.version = VersionInfo(raw="", number=number, build=build)
        return i

    def test_preferred_drive_then_version(self):
        a = self._inst("D:/WoT_old", "2.4.0.0", 990)
        b = self._inst("E:/WoT_new", "2.4.1.1", 993)
        c = self._inst("D:/WoT_new", "2.4.1.1", 993)
        order = sorted([a, b, c], key=lambda i: _rank(i, "D:"))
        self.assertEqual([str(i.path) for i in order], [str(c.path), str(a.path), str(b.path)])
        order = sorted([a, b, c], key=lambda i: _rank(i, ""))
        self.assertEqual(order[-1].path, a.path)


if __name__ == "__main__":
    unittest.main()
