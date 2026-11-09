"""Testes (so leitura) contra os clientes reais. Saltados se nao existirem.
Os caminhos podem ser alterados com WOT_TEST_EU / WOT_TEST_CT."""

import os
import unittest
from pathlib import Path

from wot_extractor.detect import inspect_install
from wot_extractor.detect.pkgprobe import probe_package

REAL = {
    "EU": Path(os.environ.get("WOT_TEST_EU", r"D:\Games\World_of_Tanks_EU")),
    "CT": Path(os.environ.get("WOT_TEST_CT", r"C:\Games\World_of_Tanks_CT")),
}


class RealInstallTests(unittest.TestCase):
    def _check(self, realm):
        path = REAL[realm]
        if not (path / "version.xml").is_file():
            self.skipTest(f"cliente {realm} nao encontrado em {path}")
        before = (path / "version.xml").stat().st_mtime_ns
        inst = inspect_install(path, deep=False)
        self.assertTrue(inst.valid, inst.issues)
        self.assertEqual(inst.realm, realm)
        self.assertTrue(inst.version.number_tuple)
        self.assertIsNotNone(inst.dirs["packages"])
        self.assertGreater(inst.packages["on_disk"], 0)
        self.assertEqual(inst.packages["missing_active"], [])
        pr = probe_package(path / "res" / "packages" / "scripts.pkg")
        self.assertIsNone(pr.error)
        self.assertGreater(pr.categories.get("python_bytecode", 0), 1000)
        self.assertEqual(set(pr.pyc_versions), {"2.7"})
        self.assertEqual((path / "version.xml").stat().st_mtime_ns, before)

    def test_eu(self):
        self._check("EU")

    def test_ct(self):
        self._check("CT")


if __name__ == "__main__":
    unittest.main()
