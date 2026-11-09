import tempfile
import unittest
from pathlib import Path

from wot_extractor.detect.xmlinfo import (MetadataError, parse_app_type, parse_game_info, parse_paths_xml,
                                          parse_version_string, parse_version_xml)

from .helpers import make_install


class VersionStringTests(unittest.TestCase):
    def test_variants(self):
        self.assertEqual(parse_version_string("v.2.4.1.1 #993"), ("2.4.1.1", "", 993))
        self.assertEqual(parse_version_string("v.2.4.2.0 Common Test #995"), ("2.4.2.0", "Common Test", 995))
        self.assertEqual(parse_version_string("v.1.25.0.0"), ("1.25.0.0", "", None))
        self.assertEqual(parse_version_string("lixo"), ("", "", None))


class MetadataTests(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.root = make_install(Path(self._td.name) / "wot", realm="CT", version="v.2.4.2.0 Common Test #995", app_type="sd")

    def tearDown(self):
        self._td.cleanup()

    def test_version_xml(self):
        v = parse_version_xml(self.root / "version.xml")
        self.assertEqual((v.number, v.suffix, v.build, v.realm), ("2.4.2.0", "Common Test", 995, "CT"))
        self.assertEqual(v.folder_name, "2.4.2.0 Common Test")
        self.assertEqual(v.number_tuple, (2, 4, 2, 0))

    def test_game_info_and_app_type(self):
        g = parse_game_info(self.root / "game_info.xml")
        self.assertEqual((g.game_id, g.realm, g.client_type), ("WOT.CT.PRODUCTION", "CT", "sd"))
        self.assertEqual(g.part_versions["client"], "2.4.1.24120")
        self.assertEqual(parse_app_type(self.root / "app_type.xml"), "sd")

    def test_paths_xml(self):
        p = parse_paths_xml(self.root / "paths.xml")
        self.assertEqual(p.res_mods, ["./res_mods/2.4.2.0 Common Test"])
        self.assertEqual(p.mods[0].mask, "*.wotmod")
        names = [e.name for e in p.packages]
        self.assertIn("scripts.pkg", names)
        hd = next(e for e in p.packages if e.name == "hd_only.pkg")
        self.assertFalse(hd.active_for("sd"))
        self.assertTrue(hd.active_for("hd"))

    def test_rejects_dtd_and_malformed(self):
        bad = self.root / "bad.xml"
        bad.write_text('<!DOCTYPE x [<!ENTITY a "aaaa">]><version.xml><version>&a;</version></version.xml>')
        with self.assertRaises(MetadataError):
            parse_version_xml(bad)
        bad.write_text("<version.xml><version>v.1</version>")
        with self.assertRaises(MetadataError):
            parse_version_xml(bad)
        bad.write_text("<version.xml><meta/></version.xml>")
        with self.assertRaises(MetadataError):
            parse_version_xml(bad)
        with self.assertRaises(MetadataError):
            parse_version_xml(self.root / "nao_existe.xml")


if __name__ == "__main__":
    unittest.main()
