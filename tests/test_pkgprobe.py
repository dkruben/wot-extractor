import tempfile
import unittest
import zipfile
from pathlib import Path

from wot_extractor.detect.pkgprobe import categorize, is_gameface, probe_package, pyc_version

from .helpers import PYC27, PYC38, make_zip


class HelperTests(unittest.TestCase):
    def test_categorize(self):
        self.assertEqual(categorize("a/b.PYC"), "python_bytecode")
        self.assertEqual(categorize("gui/flash/x.swf"), "scaleform")
        self.assertEqual(categorize("x/y.def"), "xml")
        self.assertEqual(categorize("noext"), "other")

    def test_gameface_prefix(self):
        self.assertTrue(is_gameface("gui/gameface/_dist/production/a.html"))
        self.assertTrue(is_gameface("res/gui/gameface/mods/x/window.html"))
        self.assertFalse(is_gameface("gui/flash/x.swf"))

    def test_pyc_version(self):
        self.assertEqual(pyc_version(PYC27[:4]), "2.7")
        self.assertEqual(pyc_version(PYC38[:4]), "3.8")
        self.assertEqual(pyc_version(b"\x01\x02\r\n"), "unknown:513")
        self.assertEqual(pyc_version(b"abcd"), "invalid")
        self.assertEqual(pyc_version(b"\x03"), "invalid")


class ProbeTests(unittest.TestCase):
    def test_probe(self):
        with tempfile.TemporaryDirectory() as td:
            p = make_zip(Path(td) / "t.pkg", {
                "scripts/a.pyc": PYC27,
                "scripts/b.pyc": PYC38,
                "gui/gameface/x/x.html": b"<html/>",
                "gui/flash/y.swf": b"FWS",
                "../evil.txt": b"x",
            })
            pr = probe_package(p)
            self.assertIsNone(pr.error)
            self.assertEqual(pr.files, 5)
            self.assertEqual(pr.categories["python_bytecode"], 2)
            self.assertEqual(pr.categories["scaleform"], 1)
            self.assertEqual(pr.gameface_entries, 1)
            self.assertEqual(pr.pyc_versions, {"2.7": 1, "3.8": 1})
            self.assertEqual(pr.unsafe_names, ["../evil.txt"])
            self.assertEqual(pr.compression, {"stored": 5})

    def test_sample_limit(self):
        with tempfile.TemporaryDirectory() as td:
            p = make_zip(Path(td) / "t.pkg", {f"m{i}.pyc": PYC27 for i in range(10)})
            self.assertEqual(sum(probe_package(p, pyc_sample=3).pyc_versions.values()), 3)

    def test_deflated_and_bad_zip(self):
        with tempfile.TemporaryDirectory() as td:
            p = make_zip(Path(td) / "d.pkg", {"a.xml": b"<a/>" * 100}, zipfile.ZIP_DEFLATED)
            self.assertEqual(probe_package(p).compression, {"deflated": 1})
            bad = Path(td) / "bad.pkg"
            bad.write_bytes(b"PK\x03\x04 isto nao e um zip")
            self.assertIsNotNone(probe_package(bad).error)
            self.assertIsNotNone(probe_package(Path(td) / "missing.pkg").error)


if __name__ == "__main__":
    unittest.main()
