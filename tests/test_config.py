import tempfile
import unittest
from pathlib import Path

from wot_extractor.config import ConfigError, load_config


class ConfigTests(unittest.TestCase):
    def test_defaults(self):
        with tempfile.TemporaryDirectory() as td:
            cfg = load_config(project_root=Path(td))
            self.assertIsNone(cfg.source)
            self.assertEqual(cfg.output_root, Path(td).resolve())
            self.assertEqual(cfg.realm("EU").preferred_drive, "D:")
            self.assertEqual(cfg.realm("CT").preferred_drive, "C:")
            self.assertIsNone(cfg.realm("EU").install)
            self.assertEqual(cfg.realm_output_dir("ct"), Path(td).resolve() / "wot_src_CT")

    def test_file_overrides(self):
        with tempfile.TemporaryDirectory() as td:
            (Path(td) / "wot_extractor.toml").write_text(
                '[paths]\noutput_root = "out"\n[detect]\nscan_drives = false\nscan_depth = 1\n'
                '[realms.EU]\ninstall = "X:/WoT"\npreferred_drive = "x"\n[realms.CT]\ninstall = ""\n',
                encoding="utf-8")
            cfg = load_config(project_root=Path(td))
            self.assertEqual(cfg.output_root, (Path(td) / "out").resolve())
            self.assertFalse(cfg.scan_drives)
            self.assertEqual(cfg.scan_depth, 1)
            self.assertEqual(cfg.realm("EU").install, Path("X:/WoT"))
            self.assertEqual(cfg.realm("EU").preferred_drive, "X:")
            self.assertIsNone(cfg.realm("CT").install)

    def test_errors(self):
        with tempfile.TemporaryDirectory() as td:
            f = Path(td) / "c.toml"
            f.write_text("[detect]\nscan_depth = 9\n", encoding="utf-8")
            with self.assertRaises(ConfigError):
                load_config(f)
            f.write_text("isto = nao e toml [", encoding="utf-8")
            with self.assertRaises(ConfigError):
                load_config(f)
            with self.assertRaises(ConfigError):
                load_config(Path(td) / "nao_existe.toml")


if __name__ == "__main__":
    unittest.main()
