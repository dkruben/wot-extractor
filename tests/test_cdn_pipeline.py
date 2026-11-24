import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
import zipfile
from unittest.mock import patch

from wot_extractor.cdn_acquire import active_packages, assemble, discover, import_package, safe_name, validate_package
from wot_extractor.cdn_pipeline import quality
from wot_extractor.cdn_publish import unpack


class IndependentPipelineTests(unittest.TestCase):
    def test_install_and_preload_are_never_flattened_together(self):
        metadata = b'<root><version>1</version><predefined_section><client_types><type id="sd"><client_parts><client_part id="client"/><client_part id="sdcontent"/><client_part id="locale"/></client_parts></type></client_types><default_language>en</default_language><chain_id>test</chain_id></predefined_section></root>'
        def item(part, start, end, name):
            return f'<patch><part>{part}</part><version_from>{start}</version_from><version_to>{end}</version_to><files><file><name>{name}</name><size>10</size></file></files><torrent><hash>hash</hash></torrent></patch>'
        active = ''.join(item(p, '0', '1', p + '.wgpkg') for p in ['client', 'sdcontent', 'locale'])
        future = item('client', '1', '2', 'future.wgpkg')
        response = f'<root><web_seeds><url>https://cdn.example/</url></web_seeds><version_name>active</version_name><patches_chain type="install">{active}</patches_chain><patches_chain type="preload">{future}</patches_chain></root>'.encode()
        with patch('urllib.request.urlopen', side_effect=[io.BytesIO(metadata), io.BytesIO(response)]):
            result = discover()
        self.assertTrue(result['release_ready'])
        self.assertEqual(result['chain_types'], ['install', 'preload'])
        self.assertEqual(result['chains']['client'][0]['to'], '1')
        self.assertNotIn('future.wgpkg', str(result['chains']))

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
        record.pop('decompiled')
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
