import subprocess
import tempfile
import unittest
from pathlib import Path

from wot_extractor.publication import commit_publication, reference_tree


class PublicationTests(unittest.TestCase):
    def test_fresh_game_output_retains_the_manual_actions_entry_point(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            repo, source = root / 'repo', root / 'game'
            subprocess.run(['git', 'init', '-q', str(repo)], check=True)
            workflow = repo / '.github/workflows/cdn-regions.yml'
            workflow.parent.mkdir(parents=True)
            workflow.write_text('manual workflow')
            subprocess.run(['git', '-C', str(repo), 'add', '.'], check=True)
            subprocess.run(['git', '-C', str(repo), '-c', 'user.name=Test', '-c', 'user.email=test@example.com',
                            'commit', '-qm', 'Actions entry point'], check=True)
            source.mkdir()
            (source / 'README.md').write_text('fresh extraction')
            tree = reference_tree(repo / '.git', source)
            actual = subprocess.check_output(['git', '-C', str(repo), 'show', tree + ':.github/workflows/cdn-regions.yml'])
            self.assertEqual(actual, b'manual workflow')

    def test_migration_preserves_blobs_and_does_not_move_working_files(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            gitdir = root / '.git'
            for key, value in [('user.name', 'Test'), ('user.email', 'test@example.com')]:
                subprocess.run(['git', '-C', str(root), 'config', key, value], check=True)
            for name in ['__stubs/a.pyi', 'sources_as/scripts/a.as', 'sources/a.py', 'sources_gameface/a.js']:
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(name)
            subprocess.run(['git', '-C', str(root), 'add', '.'], check=True)
            subprocess.run(['git', '-C', str(root), 'commit', '-qm', 'Initial'], check=True)
            before = subprocess.check_output(['git', '-C', str(root), 'show', 'HEAD:__stubs/a.pyi'])
            index_before = (gitdir / 'index').read_bytes()
            self.assertEqual(commit_publication(gitdir, 'Reference layout'), 'commit')
            after = subprocess.check_output(['git', '-C', str(root), 'show', 'HEAD:_stubs/a.pyi'])
            self.assertEqual(before, after)
            self.assertEqual(index_before, (gitdir / 'index').read_bytes())
            self.assertTrue((root / '__stubs/a.pyi').is_file())
            self.assertEqual(commit_publication(gitdir, 'Again'), 'sem alteracoes')
            self.assertEqual(commit_publication(gitdir, 'Fresh snapshot', root), 'sem alteracoes')
            # A removed source must disappear from the next published tree.
            (root / 'sources/a.py').unlink()
            self.assertEqual(commit_publication(gitdir, 'Delete source', root), 'commit')
            names = subprocess.check_output(['git', '-C', str(root), 'ls-tree', '-r', '--name-only', 'HEAD']).decode()
            self.assertNotIn('sources/a.py', names)
            self.assertIn('sources_gameface/a.js', names)

    def test_conflicting_old_and_new_layouts_are_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            subprocess.run(['git', 'init', '-q', str(root)], check=True)
            for name in ['__stubs/a.pyi', '_stubs/a.pyi']:
                path = root / name
                path.parent.mkdir(exist_ok=True)
                path.write_text(name)
            with self.assertRaises(ValueError):
                reference_tree(root / '.git', root)
