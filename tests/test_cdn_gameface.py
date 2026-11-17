import json
from pathlib import Path
import shutil
import tempfile
import unittest
import zipfile

from wot_extractor.cdn_gameface import import_package, process


class GamefaceImportTests(unittest.TestCase):
    def archive(self, root, name, files):
        target = root / name
        with zipfile.ZipFile(target, 'w') as archive:
            for path, content in files.items():
                archive.writestr(path, content)
        return target

    def test_import_selects_gameface_and_refuses_cross_package_conflicts(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            output = root / 'wot_src_EU'
            name = 'gui/gameface/_dist/production/lobby/Test/Test.js'
            first = self.archive(root, 'first.pkg', {name: 'const x=1;', 'gui/flash/a.swf': 'skip'})
            self.assertEqual(import_package(first, output, 'EU', 'gui-part1.pkg'), 1)
            self.assertFalse((output / 'sources/res/gui/flash/a.swf').exists())
            second = self.archive(root, 'second.pkg', {name: 'const x=2;'})
            with self.assertRaises(ValueError):
                import_package(second, output, 'EU', 'gui-part2.pkg')
            self.assertEqual((output / 'sources/res' / name).read_text(), 'const x=1;')
            with self.assertRaises(ValueError):
                import_package(first, output, 'CT', 'gui-part1.pkg')

    def test_package_traversal_is_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            archive = self.archive(root, 'bad.pkg', {'gui/gameface/../../../../escape.js': 'bad'})
            with self.assertRaises(ValueError):
                import_package(archive, root / 'wot_src_EU', 'EU', 'bad.pkg')
            self.assertFalse((root / 'escape.js').exists())

    @unittest.skipUnless(shutil.which('node'), 'Node is required')
    def test_real_processor_generates_views_without_changing_originals(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            output = root / 'wot_src_EU'
            prefix = 'gui/gameface/_dist/production/lobby/Test/'
            archive = self.archive(root, 'gui.pkg', {
                prefix + 'Test.js': 'const x=1;\n',
                prefix + 'Test.css': '.test { color: red; }\n',
                prefix + 'Test.html': '<html><head><link rel="stylesheet" href="Test.css"></head>'
                                      '<body><script src="Test.js"></script></body></html>',
            })
            import_package(archive, output, 'EU', 'gui.pkg')
            (output / 'cdn-gameface.json').write_text(json.dumps({
                'version': 'fixture', 'scope': 'base-gui test', 'packages': ['gui.pkg'],
            }))
            result = process(output, 'EU', root / 'evidence', jobs=1)
            self.assertEqual(result['counts']['views'], 1)
            self.assertTrue(result['all_original_hashes_preserved'])
            self.assertTrue((output / 'sources_gameface/VIEWS.md').is_file())
