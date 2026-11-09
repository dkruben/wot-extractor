import contextlib
import io
import json
import os
import tempfile
import unittest
from pathlib import Path

from wot_extractor.cli import EXIT_FAIL, EXIT_NOT_IMPLEMENTED, EXIT_OK, EXIT_USAGE, main

from .helpers import make_install


def run(argv):
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = main(argv)
    return code, out.getvalue(), err.getvalue()


class CliTests(unittest.TestCase):
    def setUp(self):
        self._td = tempfile.TemporaryDirectory()
        self.tmp = Path(self._td.name)
        self.eu = make_install(self.tmp / "World_of_Tanks_EU")
        self._cwd = os.getcwd()
        os.chdir(self.tmp)  # evita apanhar um wot_extractor.toml real

    def tearDown(self):
        os.chdir(self._cwd)
        self._td.cleanup()

    def test_detect_manual_path_json(self):
        out_json = self.tmp / "out" / "detect.json"
        code, out, _ = run(["detect", "--no-system", "--realm", "EU", "--path", str(self.eu), "--json", str(out_json)])
        self.assertEqual(code, EXIT_OK, out)
        self.assertIn("2.4.1.1", out)
        data = json.loads(out_json.read_text(encoding="utf-8"))
        self.assertEqual(data["selected"]["EU"]["realm"], "EU")
        self.assertEqual(data["errors"], {})

    def test_json_inside_install_is_blocked(self):
        target = self.eu / "detect.json"
        code, _, err = run(["detect", "--no-system", "--quick", "--realm", "EU", "--path", str(self.eu), "--json", str(target)])
        self.assertEqual(code, EXIT_FAIL)
        self.assertIn("bloqueada", err)
        self.assertFalse(target.exists())

    def test_usage_errors(self):
        self.assertEqual(run(["detect", "--path", str(self.eu)])[0], EXIT_USAGE)
        self.assertEqual(run([])[0], EXIT_USAGE)
        with self.assertRaises(SystemExit):
            run(["detect", "--realm", "XX"])

    def test_missing_realm_fails(self):
        code, out, _ = run(["detect", "--no-system", "--quick"])
        self.assertEqual(code, EXIT_FAIL)
        self.assertIn("NAO ENCONTRADO", out)

    def test_extract_dry_run_and_real(self):
        code, out, _ = run(["extract", "--no-system", "--realm", "EU", "--path", str(self.eu), "--dry-run"])
        self.assertEqual(code, EXIT_OK, out)
        self.assertIn("Simulacao", out)
        self.assertFalse((self.tmp / "wot_src_EU").exists())
        code, out, err = run(["extract", "--no-system", "--realm", "EU", "--path", str(self.eu), "-j", "2"])
        self.assertEqual(code, EXIT_OK, out + err)
        self.assertIn("CONSISTENTE", out)
        self.assertTrue((self.tmp / "wot_src_EU" / "manifest.json").is_file())
        code, out, _ = run(["extract", "--no-system", "--realm", "EU", "--path", str(self.eu)])
        self.assertIn("Extraidos 0", out)

    def test_extract_usage(self):
        self.assertEqual(run(["extract", "--path", str(self.eu)])[0], EXIT_USAGE)
        self.assertEqual(run(["extract", "--realm", "EU", "--path", str(self.eu), "-j", "0"])[0], EXIT_USAGE)
        self.assertEqual(run(["extract", "--no-system", "--realm", "CT"])[0], EXIT_FAIL)

    def test_decompile_cli(self):
        # sem manifesto: erro claro; com manifesto: simulacao
        code, out, err = run(["decompile", "--realm", "EU", "--dry-run"])
        if "Python 2.7 com uncompyle6 nao encontrado" in err:
            self.skipTest("Python 2.7 com uncompyle6 nao disponivel")
        self.assertEqual(code, EXIT_FAIL)
        self.assertIn("corra primeiro 'extract", err)
        run(["extract", "--no-system", "--realm", "EU", "--path", str(self.eu), "-j", "2"])
        code, out, err = run(["decompile", "--realm", "EU", "--dry-run"])
        self.assertEqual(code, EXIT_OK, out + err)
        self.assertIn("Simulacao: 2 .pyc selecionados", out)
        self.assertEqual(run(["decompile", "--realm", "EU", "-j", "0"])[0], EXIT_USAGE)

    def test_all_spec_commands_exist(self):
        from wot_extractor.cli import PLANNED, build_parser
        self.assertEqual(PLANNED, {})  # todos os comandos do readme estao implementados
        sub = next(a for a in build_parser()._actions if a.dest == "command")
        for cmd in ("detect", "extract", "decompile", "gameface", "actionscript", "stubs", "update", "verify",
                    "report"):
            self.assertIn(cmd, sub.choices)
        for cmd in ("verify", "report"):  # sem manifesto: erro claro, nao "nao implementado"
            with self.subTest(cmd=cmd):
                code, _, err = run([cmd, "--realm", "EU", "--no-install"] if cmd == "verify" else [cmd, "--realm", "EU"])
                self.assertEqual(code, 1)
                self.assertIn("nao existe", err)


if __name__ == "__main__":
    unittest.main()
