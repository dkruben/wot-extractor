"""Import Gameface resources from rebuilt CDN packages and run our processor."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import stat
import zipfile

from .config import Config
from .cdn_regions import CDN_REGIONS, require_region
from .extract.writer import save_json_atomic
from .gameface import GFOptions, find_node, run_gameface

LAYOUTS = {'gui/gen_resources/gameface_layouts.json', 'gui/gen_resources/unbound_layouts.json'}


def wanted_member(name: str) -> bool:
    return '/gameface/' in '/' + name or name.startswith('gui/unbound/') or name in LAYOUTS


def import_package(archive: Path, output: Path, realm: str, container: str) -> int:
    require_region(realm)
    output = output.resolve()
    manifest_path = output / 'manifest.json'
    manifest = json.loads(manifest_path.read_text(encoding='utf-8')) if manifest_path.exists() else {
        'realm': realm, 'entries': {}, 'origin': 'selective CDN package reconstruction',
    }
    if manifest.get('realm') != realm:
        raise ValueError('Refusing to mix realms in a Gameface output')
    entries = manifest['entries']
    selected = 0
    with zipfile.ZipFile(archive) as source:
        for member in source.infolist():
            if member.is_dir():
                continue
            name = member.filename.replace('\\', '/')
            if not wanted_member(name):
                continue
            virtual = PurePosixPath(name)
            if virtual.is_absolute() or '..' in virtual.parts or ':' in name or str(virtual) != name:
                raise ValueError(f'Unsafe package member: {name}')
            if stat.S_ISLNK(member.external_attr >> 16):
                raise ValueError(f'Refusing package symlink: {name}')
            key = 'res/' + name
            target = output / 'sources' / key
            data = source.read(member)
            digest = hashlib.sha256(data).hexdigest()
            previous = entries.get(key)
            if previous and previous['sha256'] != digest:
                raise ValueError(f'Conflicting resources across packages: {name}')
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            entries[key] = {
                'tree': 'res', 'path': name, 'virtual': name,
                'category': 'json' if name in LAYOUTS else 'web',
                'source': 'zip', 'container': container, 'member': name,
                'size': len(data), 'crc': member.CRC, 'status': 'extracted', 'sha256': digest,
            }
            selected += 1
    save_json_atomic(manifest_path, manifest)
    print(f'{container}: imported {selected} Gameface/layout resources', flush=True)
    return selected


def process(output: Path, realm: str, evidence: Path, jobs: int = 2) -> dict:
    require_region(realm)
    output = output.resolve()
    if output.name != 'wot_src_' + realm:
        raise ValueError('Expected an isolated wot_src_<REALM> directory')
    cfg = Config(project_root=output.parent, output_root=output.parent)
    node, label = find_node()
    if not node:
        raise RuntimeError('Node is required for the real Gameface validation')

    def progress(done, total, counts):
        if done == total or done % 50 == 0:
            print(f'Gameface: {done}/{total} {dict(counts)}', flush=True)

    result = run_gameface(cfg, realm, GFOptions(jobs=jobs, links=False),
                          node=node, node_label=label, progress=progress)
    if result.interrupted or result.totals.get('failed') or result.totals.get('partial'):
        raise RuntimeError(f'Incomplete Gameface processing: {dict(result.totals)}')
    if not result.views or any(not result.kinds.get(k) for k in ['js', 'css', 'html']):
        raise RuntimeError('Expected real views and JavaScript, CSS and HTML resources')
    manifest = json.loads((output / 'manifest.json').read_text(encoding='utf-8'))
    for key, record in manifest['entries'].items():
        actual = hashlib.sha256((output / 'sources' / key).read_bytes()).hexdigest()
        if actual != record['sha256']:
            raise RuntimeError(f'Original source changed while formatting: {key}')
    files = sorted(p for p in (output / 'sources_gameface').rglob('*') if p.is_file())
    acquisition = json.loads((output / 'cdn-gameface.json').read_text(encoding='utf-8'))
    summary = {
        'realm': realm, 'version': acquisition['version'], 'scope': acquisition['scope'],
        'packages': acquisition['packages'], 'counts': result.to_report()['counts'],
        'python_links': 'not evaluated: Python package output was not imported in this test',
        'all_original_hashes_preserved': True,
        'sha256': {p.relative_to(output).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in files},
        'note': 'Formatted JavaScript/CSS is not original source code. Base GUI coverage only.',
    }
    evidence.mkdir(parents=True, exist_ok=True)
    save_json_atomic(evidence / 'gameface-validation.json', summary)
    print(json.dumps({k: v for k, v in summary.items() if k != 'sha256'}, indent=2), flush=True)
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    imp = sub.add_parser('import')
    imp.add_argument('archive', type=Path)
    imp.add_argument('output', type=Path)
    imp.add_argument('--container', required=True)
    imp.add_argument('--realm', choices=list(CDN_REGIONS), required=True)
    run = sub.add_parser('process')
    run.add_argument('output', type=Path)
    run.add_argument('evidence', type=Path)
    run.add_argument('--realm', choices=list(CDN_REGIONS), required=True)
    run.add_argument('--jobs', type=int, default=2)
    args = parser.parse_args()
    if args.command == 'import':
        import_package(args.archive, args.output, args.realm, args.container)
    else:
        process(args.output, args.realm, args.evidence, args.jobs)
