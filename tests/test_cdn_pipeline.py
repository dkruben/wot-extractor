import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
import zipfile

from wot_extractor.cdn_acquire import active_packages, assemble, import_package, safe_name, validate_package
from wot_extractor.cdn_pipeline import quality
from wot_extractor.cdn_publish import unpack


class IndependentPipelineTests(unittest.TestCase):
    def test_cache_verifies_bytes_and_preserves_package_precedence(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            for signature, content in [('first', b'first'), ('second', b'second')]:
                archive = root / (signature + '.pkg')
                with zipfile.ZipFile(archive, 'w') as z:
                    z.writestr('gui/example.xml', content)
                    z.writestr('vehicles/large.dds', b'ignored')
                import_package(archive, root / 'packages' / signature, signature, signature)
                self.assertTrue(validate_package(root / 'packages' / signature, signature))
            plan = {'realm': 'EU', 'packages': [{'name': s, 'fingerprint': s} for s in ['first', 'second']], 'loose': []}
            (root / 'plan.json').write_text(json.dumps(plan))
            out = assemble(root / 'plan.json', root, 'code')
            target = out / 'sources/res/gui/example.xml'
            self.assertEqual(target.read_bytes(), b'first')
            self.assertFalse((out / 'sources/res/vehicles/large.dds').exists())
            target.write_bytes(b'corruption')
            self.assertFalse(validate_package(root / 'packages/first', 'first'))

    def test_active_sd_inventory_excludes_hd_audio_and_keeps_order(self):
        with tempfile.TemporaryDirectory() as td:
            paths = Path(td) / 'paths.xml'
            paths.write_text('<root><Paths><Packages><Package type="sd">res/packages/scripts.pkg</Package><Package type="hd">res/packages/hd.pkg</Package><Package>res/packages/audioww.pkg</Package><Package>res/packages/scripts.pkg</Package></Packages></Paths></root>')
            self.assertEqual(active_packages(paths), ['res/packages/scripts.pkg'])

    def test_quality_rejects_changed_input_and_worsened_recovery(self):
        record = {'sha256': 'known', 'category': 'python_bytecode', 'decompiled': {'status': 'partial'}}
        manifest = {'entries': {'res/a.pyc': record}, 'acquisition': {'package_count': 1}}
        reports = {'actionscript': {'counts': {'unique_classes': 1}}, 'gameface': {'counts': {'views': 1, 'totals': {}}}, 'stubs': {'counts': {'totals': {}}}}
        policy = {'minimum': {'packages': 1}, 'known_issues': {'decompiled:res/a.pyc': {'input_sha256': 'known', 'status': 'partial'}}}
        self.assertTrue(quality(manifest, reports, policy)['ready'])
        record['sha256'] = 'new'
        self.assertFalse(quality(manifest, reports, policy)['ready'])
        record['sha256'] = 'known'
        record['decompiled']['status'] = 'failed'
        self.assertFalse(quality(manifest, reports, policy)['ready'])

    def test_artifact_rejects_traversal_and_links(self):
        for name, kind in [('../outside', tarfile.REGTYPE), ('link', tarfile.SYMTYPE)]:
            with tempfile.TemporaryDirectory() as td:
                root = Path(td)
                with tarfile.open(root / 'bad.tar.gz', 'w:gz') as tar:
                    member = tarfile.TarInfo(name)
                    member.type = kind
                    member.linkname = '../outside'
                    tar.addfile(member, io.BytesIO(b''))
                with self.assertRaises(ValueError):
                    unpack(root / 'bad.tar.gz', root / 'candidate')

    def test_paths_reject_windows_and_git_escapes(self):
        for name in ['../x', '/absolute', 'C:/x', 'a\\b', '.git/config', 'a/../b']:
            with self.assertRaises(ValueError):
                safe_name(name)
