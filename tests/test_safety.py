import tempfile
import unittest
import zipfile
from pathlib import Path

from wot_extractor.safety import (ArchiveLimitError, ArchiveLimits, ProtectedPathError, UnsafePathError,
                                  WriteGuard, check_archive, check_archive_member, is_within,
                                  normalize_member_name, resolve_within)

from .helpers import make_zip


class NormalizeTests(unittest.TestCase):
    def test_valid_names(self):
        self.assertEqual(normalize_member_name("scripts/client/gui/a.pyc"), "scripts/client/gui/a.pyc")
        self.assertEqual(normalize_member_name("res\\gui\\./flash//x.swf"), "res/gui/flash/x.swf")
        self.assertEqual(normalize_member_name("2.4.2.0 Common Test/readme.txt"), "2.4.2.0 Common Test/readme.txt")

    def test_rejects_unsafe(self):
        bad = ["", "../x", "a/../../x", "/etc/passwd", "\\\\server\\share\\x", "C:/Windows/x", "c:x",
               "a/\x00b", "a/CON", "a/nul.txt", "a/b.", "a/b ", "a/b?c", "a/b:c", "./"]
        for name in bad:
            with self.subTest(name=name):
                with self.assertRaises(UnsafePathError):
                    normalize_member_name(name)

    def test_resolve_within(self):
        with tempfile.TemporaryDirectory() as td:
            base = Path(td)
            self.assertEqual(resolve_within(base, "a/b.txt").resolve(), (base / "a" / "b.txt").resolve())
            with self.assertRaises(UnsafePathError):
                resolve_within(base, "../escape.txt")


class GuardTests(unittest.TestCase):
    def test_blocks_writes_inside_install(self):
        with tempfile.TemporaryDirectory() as td:
            game = Path(td) / "World_of_Tanks_EU"
            game.mkdir()
            guard = WriteGuard([game])
            with self.assertRaises(ProtectedPathError):
                guard.check(game / "res" / "x.txt")
            with self.assertRaises(ProtectedPathError):
                guard.check(game)
            # caminho com caixa diferente (Windows) tambem e bloqueado
            with self.assertRaises(ProtectedPathError):
                guard.check(Path(str(game).upper()) / "a")
            self.assertEqual(guard.check(Path(td) / "out" / "x"), (Path(td) / "out" / "x").resolve())

    def test_output_root_cannot_contain_install(self):
        with tempfile.TemporaryDirectory() as td:
            game = Path(td) / "games" / "wot"
            game.mkdir(parents=True)
            guard = WriteGuard([game])
            with self.assertRaises(ProtectedPathError):
                guard.check_output_root(Path(td))
            guard.check_output_root(Path(td) / "wot_src")

    def test_is_within(self):
        self.assertTrue(is_within(Path("C:/a/b"), Path("C:/a")))
        self.assertFalse(is_within(Path("C:/ab"), Path("C:/a")))


class ArchiveLimitTests(unittest.TestCase):
    def test_member_limits(self):
        info = zipfile.ZipInfo("a/b.bin")
        info.file_size = 10
        self.assertEqual(check_archive_member(info), "a/b.bin")
        info.file_size = 11
        with self.assertRaises(ArchiveLimitError):
            check_archive_member(info, ArchiveLimits(max_member_size=10))

    def test_ratio_limit(self):
        info = zipfile.ZipInfo("bomb.bin")
        info.compress_type = zipfile.ZIP_DEFLATED
        info.file_size = 100 * 1024 * 1024
        info.compress_size = 1024
        with self.assertRaises(ArchiveLimitError):
            check_archive_member(info)
        info.compress_type = zipfile.ZIP_STORED  # stored nao tem ratio
        check_archive_member(info)

    def test_traversal_member(self):
        with self.assertRaises(UnsafePathError):
            check_archive_member(zipfile.ZipInfo("../../evil.py"))

    def test_archive_totals(self):
        with tempfile.TemporaryDirectory() as td:
            p = make_zip(Path(td) / "x.zip", {f"f{i}.txt": b"abc" for i in range(5)})
            with zipfile.ZipFile(p) as zf:
                check_archive(zf)
                with self.assertRaises(ArchiveLimitError):
                    check_archive(zf, ArchiveLimits(max_entries=4))
                with self.assertRaises(ArchiveLimitError):
                    check_archive(zf, ArchiveLimits(max_total_size=10))


if __name__ == "__main__":
    unittest.main()
