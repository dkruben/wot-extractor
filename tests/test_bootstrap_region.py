import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
import zipfile

from scripts.bootstrap_region import bootstrap


class BootstrapTests(unittest.TestCase):
    def test_new_root_preserves_reference_sources_and_adds_only_validated_outputs(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            base = root / 'baseline'
            subprocess.run(['git', 'init', '-q', str(base)], check=True)
            subprocess.run(['git', '-C', str(base), 'remote', 'add', 'origin', 'https://github.com/izeberg/wot-src.git'], check=True)
            for name, content in {'.version_name': 'test-version', 'sources/mode.py': 'mode = 1',
                                  'sources-as3/a.as': 'AS3', '_stubs/a.pyi': 'stub', 'README.md': 'upstream',
                                  '.gitattributes': 'sources/** text eol=lf\nsources_gameface/** text eol=lf\n'}.items():
                target = base / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content)
            subprocess.run(['git', '-C', str(base), 'add', '.'], check=True)
            subprocess.run(['git', '-C', str(base), '-c', 'user.name=Test', '-c', 'user.email=test@example.com',
                            'commit', '-qm', 'Baseline'], check=True)
            raw, generated = b'<html>game</html>\r\n', b'view documentation\r\n'
            artifact = root / 'gameface.zip'
            summary = dict(realm='NA', version='test-version', scope='base-gui test',
                           all_original_hashes_preserved=True,
                           counts={'totals': {'success': 1}, 'views': 1},
                           sha256={'sources_gameface/VIEWS.md': hashlib.sha256(generated).hexdigest()})
            manifest = {'realm': 'NA', 'entries': {'res/gui/gameface/view.html': {'sha256': hashlib.sha256(raw).hexdigest()}}}
            with zipfile.ZipFile(artifact, 'w') as archive:
                archive.writestr('evidence/gameface-validation.json', json.dumps(summary))
                archive.writestr('output/wot_src_NA/manifest.json', json.dumps(manifest))
                archive.writestr('output/wot_src_NA/sources/res/gui/gameface/view.html', raw)
                archive.writestr('output/wot_src_NA/sources_gameface/VIEWS.md', generated)
            evidence = root / 'syntax.json'
            evidence.write_text(json.dumps({'realm': 'NA', 'version': 'test-version', 'passed': 100}))
            gitdir = root / 'NA.git'
            commit = bootstrap('NA', base, artifact, gitdir, evidence, 'test-gameface', 'test-python')
            def show(name):
                return subprocess.check_output(['git', '--git-dir=' + str(gitdir), 'show', 'HEAD:' + name])
            self.assertEqual(show('sources/mode.py'), b'mode = 1')
            self.assertEqual(show('sources-as3/a.as'), b'AS3')
            self.assertEqual(show('sources_gameface/VIEWS.md'), generated)
            self.assertEqual(show('sources/res/gui/gameface/view.html'), raw)
            parents = subprocess.check_output(['git', '--git-dir=' + str(gitdir), 'rev-list', '--parents', '-n1', commit]).split()
            self.assertEqual(len(parents), 1)
            self.assertEqual(subprocess.check_output(['git', '-C', str(base), 'status', '--porcelain']).strip(), b'')
            self.assertFalse((base / 'sources_gameface').exists())
            with self.assertRaises(ValueError):
                bootstrap('NA', base, artifact, gitdir, evidence, 'test', 'test')
