"""Independent EU processing, quality gates and publication candidates."""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tarfile

from .actionscript.engine import ASOptions, run_actionscript
from .actionscript.ffdec import find_ffdec
from .cdn_acquire import assemble, digest, discover, safe_name
from .config import Config
from .decompile.engine import DecompileOptions, run_decompile
from .extract.writer import save_json_atomic, write_atomic
from .extract.xmldecode import run_decode_pass
from .gameface import GFOptions, find_node, run_gameface
from .stubs.engine import StubOptions, find_python27, run_stubs

POLICY = Path(__file__).with_name('data') / 'eu_quality_policy.json'
RANK = {'partial': 1, 'failed': 2, 'unsupported': 3}


def quality(manifest, reports, policy):
    problems, accepted = [], []
    for phase, report in reports.items():
        if report.get('interrupted') or report.get('counts', {}).get('not_processed_due_to_limit'):
            problems.append({'phase': phase, 'key': 'incomplete processing pass'})
    for key, record in manifest['entries'].items():
        for phase in ['decompiled', 'actionscript', 'decoded']:
            state = record.get(phase) or {}
            required = ((phase == 'decompiled' and record.get('category') == 'python_bytecode') or
                        (phase == 'actionscript' and record.get('category') == 'scaleform') or
                        (phase == 'decoded' and record.get('validation') == 'packed'))
            if required and state.get('status') not in {'success', 'extracted', *RANK}:
                problems.append({'phase': phase, 'key': key, 'status': 'missing processing result'})
            if state.get('status') not in RANK:
                continue
            issue = {'phase': phase, 'key': key, 'input_sha256': record['sha256'],
                     'status': state['status'], 'error': state.get('error', ''), 'output': state.get('output')}
            known = policy['known_issues'].get(phase + ':' + key)
            if known and known['input_sha256'] == issue['input_sha256'] and RANK[issue['status']] <= RANK[known['status']]:
                accepted.append(issue)
            else:
                problems.append(issue)
    minima = policy['minimum']
    measured = {'packages': manifest['acquisition']['package_count'],
                'python_modules': sum(r.get('category') == 'python_bytecode' for r in manifest['entries'].values()),
                'as3_classes': reports['actionscript']['counts']['unique_classes'],
                'gameface_views': reports['gameface']['counts']['views']}
    for name, minimum in minima.items():
        if measured[name] < minimum:
            problems.append({'phase': 'coverage', 'key': name, 'actual': measured[name], 'minimum': minimum})
    for phase in ['gameface', 'stubs']:
        counts = reports[phase]['counts']['totals']
        if counts.get('failed') or (phase == 'gameface' and counts.get('partial')):
            problems.append({'phase': phase, 'key': 'processing totals', 'counts': counts})
    return {'ready': not problems, 'measured': measured, 'accepted_known_issues': accepted,
            'blocking_issues': problems, 'policy': 'Exact reviewed input hashes; new or worse recovery blocks publication'}


def files_under(root):
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError('Symlinks are not publication files: ' + str(path))
        if path.is_file():
            yield path


def verify_work_integrity(out):
    marker = out / 'processing-integrity.json'
    if not marker.exists():
        return False
    try:
        for name, expected in json.loads(marker.read_text()).items():
            path = out / safe_name(name)
            if not path.is_file() or digest(path.read_bytes()) != expected:
                return False
        return True
    except (OSError, ValueError):
        return False


def process(cache, code_hash, python27, python3, ffdec):
    cache = Path(cache).resolve()
    previous = cache / 'work/wot_src_EU'
    if previous.exists() and not verify_work_integrity(previous):
        if previous.parent != cache / 'work':
            raise ValueError('Unsafe processing reset')
        shutil.rmtree(previous)
    out = assemble(cache / 'plan.json', cache, code_hash)
    cfg = Config(project_root=cache / 'work', output_root=cache / 'work', python27=Path(python27).resolve(),
                 python3=Path(python3).resolve(), ffdec=Path(ffdec).resolve(), java_heap='4g')
    def progress(*args):
        done, total = args[:2]
        if done == total or done % 25 == 0:
            print('processing {}/{} {}'.format(done, total, str(args[2:])[:180]), flush=True)
    manifest = json.loads((out / 'manifest.json').read_text())
    print('Decoding packed XML', flush=True)
    decoded = run_decode_pass(manifest['entries'], manifest['entries'], out, jobs=2)
    save_json_atomic(out / 'manifest.json', manifest, indent=None)
    save_json_atomic(out / 'xml_report.json', decoded.to_dict())
    del manifest
    print('Decompiling and validating Python 2.7', flush=True)
    py = run_decompile(cfg, 'EU', DecompileOptions(jobs=2, python27=cfg.python27, python3=cfg.python3), progress=progress)
    if py.interrupted:
        raise RuntimeError('Python processing interrupted')
    ff, error = find_ffdec(cfg.ffdec, heap='4g')
    if ff is None:
        raise RuntimeError(error)
    print('Decompiling all active SWF/SWC, including game modes', flush=True)
    actionscript = run_actionscript(cfg, 'EU', ASOptions(jobs=2, heavy_jobs=1, assets=False, asasm='none'),
                                   progress=progress, ff=ff)
    if actionscript.interrupted:
        raise RuntimeError('AS3 processing interrupted')
    print('Building static Python and native-usage stubs', flush=True)
    interp, error = find_python27(cfg.python27, out)
    if interp is None:
        raise RuntimeError(error)
    stubs = run_stubs(cfg, 'EU', StubOptions(jobs=2), progress=progress, interp=interp, interp_label=interp.label())
    node, label = find_node()
    if not node:
        raise RuntimeError('Node is required')
    print('Processing Gameface for all active modes, with Python links', flush=True)
    gf = run_gameface(cfg, 'EU', GFOptions(jobs=2, links=True), progress=progress, node=node, node_label=label)
    reports = {'python': py.to_report(), 'actionscript': actionscript.to_report(), 'stubs': stubs.to_report(), 'gameface': gf.to_report()}
    manifest = json.loads((out / 'manifest.json').read_text())
    import polib
    for key, rec in manifest['entries'].items():
        source = out / 'sources' / key
        if digest(source.read_bytes()) != rec['sha256']:
            raise RuntimeError('Input was modified by processing: ' + key)
        if key.endswith('.mo'):
            relative = 'sources/' + key[:-3] + '.po'
            text = str(polib.mofile(str(source))).encode('utf-8')
            write_atomic(out / relative, text)
            rec['gettext'] = {'path': relative, 'sha256': digest(text)}
    policy = json.loads(POLICY.read_text(encoding='utf-8'))
    result = quality(manifest, reports, policy)
    save_json_atomic(out / 'manifest.json', manifest, indent=None)
    save_json_atomic(out / 'QUALITY.json', result)
    save_json_atomic(cache / 'quality.json', result)
    # Integrity checkpoints prevent corrupted processed output being reused.
    integrity = {}
    for directory in ['sources_as', 'sources_xml', 'sources_gameface', '__stubs']:
        for path in files_under(out / directory):
            integrity[path.relative_to(out).as_posix()] = digest(path.read_bytes())
    for rec in manifest['entries'].values():
        for state, field in [('decompiled', 'output'), ('gettext', 'path')]:
            name = (rec.get(state) or {}).get(field)
            if name and (out / name).is_file():
                integrity[name] = digest((out / name).read_bytes())
    save_json_atomic(out / 'processing-integrity.json', integrity, indent=None)
    print(json.dumps({'quality_ready': result['ready'], 'coverage': result['measured'],
                      'known_issues': len(result['accepted_known_issues']), 'new_issues': result['blocking_issues'][:20]}, indent=2), flush=True)
    return out, result


def export_candidate(cache, destination, discovery_path, code_hash):
    cache, destination = Path(cache).resolve(), Path(destination).resolve()
    if destination.exists():
        raise ValueError('Candidate destination must be new')
    out = cache / 'work/wot_src_EU'
    manifest = json.loads((out / 'manifest.json').read_text())
    review = json.loads((out / 'QUALITY.json').read_text())
    discovery = json.loads(Path(discovery_path).read_text())
    if manifest['acquisition']['fingerprint'] != discovery['fingerprint'] or not discovery['release_ready']:
        raise ValueError('Candidate does not match its locked active-release plan')
    destination.mkdir(parents=True)
    inputs, outputs, partials = {}, {}, {}
    def add(relative, source):
        safe_name(relative)
        if not source.is_file():
            raise ValueError('Missing publication output: ' + str(source))
        if relative in outputs:
            if outputs[relative] != digest(source.read_bytes()):
                raise ValueError('Conflicting publication path: ' + relative)
            return
        target = destination / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            os.link(source, target)
        except OSError:
            shutil.copyfile(source, target)
        outputs[relative] = digest(target.read_bytes())
    for key, rec in manifest['entries'].items():
        raw = out / 'sources' / key
        inputs[key] = rec['sha256']
        decoded, py, action = rec.get('decoded') or {}, rec.get('decompiled') or {}, rec.get('actionscript') or {}
        public_raw = 'sources/' + (rec['path'] if rec['tree'] == 'root' else key)
        if py.get('output'):
            name = py['output'] if py['status'] == 'success' else py['output'] + '.partial'
            add(name, out / py['output'])
            if py['status'] != 'success':
                partials[py['output']] = name
        if rec.get('gettext'):
            add(rec['gettext']['path'], out / rec['gettext']['path'])
        elif not (decoded.get('status') == 'success' or py.get('status') == 'success' or action.get('status') in ['success', 'extracted']):
            add(public_raw, raw)
    for source_dir, public_dir in [('sources_xml', 'sources_xml'), ('sources_as/scripts', 'sources-as3/scripts'),
                                   ('sources_as/swf', 'sources-as3/swf'), ('sources_gameface', 'sources_gameface'), ('__stubs', '_stubs')]:
        for path in files_under(out / source_dir):
            add(public_dir + '/' + path.relative_to(out / source_dir).as_posix(), path)
    if (out / 'sources_as/catalog.json').exists():
        add('sources-as3/catalog.json', out / 'sources_as/catalog.json')
    def rewrite(value):
        if isinstance(value, str):
            return partials.get(value, value.replace('sources_as/', 'sources-as3/').replace('__stubs/', '_stubs/'))
        if isinstance(value, list): return [rewrite(v) for v in value]
        if isinstance(value, dict): return {k: rewrite(v) for k, v in value.items()}
        return value
    # Metadata paths refer to the public layout. Source code is never rewritten.
    for name in list(outputs):
        if name.endswith('.json') and name.startswith(('sources-as3/', 'sources_gameface/', '_stubs/')):
            path = destination / name
            data = json.loads(path.read_text(encoding='utf-8'))
            path.unlink()  # break hardlink before changing generated metadata
            save_json_atomic(path, rewrite(data), indent=None)
            outputs[name] = digest(path.read_bytes())
    def text(name, data):
        write_atomic(destination / name, data.encode('utf-8'))
        outputs[name] = digest(data.encode('utf-8'))
    info = {'realm': 'EU', 'version': discovery['version'], 'independently_generated': True,
            'acquisition_fingerprint': discovery['fingerprint'], 'generator_code_hash': code_hash,
            'scope': manifest['acquisition']['scope'], 'packages': manifest['acquisition']['packages'],
            'quality': review, 'source_parts': ['client', 'sdcontent', 'locale'],
            'software_archive_engine': 'unicum-gg/wot.build@1832f2ff545a2950867fa698296c92315752bf81',
            'note': 'Game files came directly from the CDN. No source baseline or upstream stubs were imported.'}
    text('.version_name', discovery['version'] + '\n')
    text('.gitattributes', '* -text\n')
    text('BUILD_INFO.json', json.dumps(info, indent=2) + '\n')
    text('QUALITY.json', json.dumps(review, indent=2) + '\n')
    text('README.md', '# World of Tanks EU — ' + discovery['version'] + '\n\n'
         'Generated independently from the WG update CDN by [our pipeline](../../tree/main).\n\n'
         '`sources/`: client text and Python; `sources_xml/`: decoded packed XML; '
         '`sources-as3/`: decompiled SWF/SWC; `_stubs/`: static inferred API stubs; '
         '`sources_gameface/`: formatted UI, including active modes and probable Python links.\n\n'
         'Incomplete Python text has a `.py.partial` suffix and its original bytecode is retained. '
         'Known AS3 recovery limitations are recorded in `QUALITY.json` and the SWF catalogues. '
         'Formatted/decompiled files are not original source code; inferred stubs do not describe the entire native engine.\n\n'
         'This is an SD source-reference profile, excluding audio and HD texture-only packages. '
         'Game content belongs to its rights holders; the tooling MIT licence does not apply to it.\n')
    publication = {'schema': 1, 'files': outputs, 'input_hashes': inputs, 'file_count': len(outputs)}
    save_json_atomic(destination / 'PUBLICATION_MANIFEST.json', publication, indent=None)
    return publication


def verify_candidate(root):
    root = Path(root)
    manifest = json.loads((root / 'PUBLICATION_MANIFEST.json').read_text())
    actual = {p.relative_to(root).as_posix() for p in files_under(root)}
    if actual != set(manifest['files']) | {'PUBLICATION_MANIFEST.json'}:
        raise ValueError('Candidate has missing or unexpected files')
    allowed = {'sources', 'sources_xml', 'sources-as3', 'sources_gameface', '_stubs', '.version_name', '.gitattributes',
               'README.md', 'BUILD_INFO.json', 'QUALITY.json'}
    for name, expected in manifest['files'].items():
        safe_name(name)
        if name.split('/')[0] not in allowed or digest((root / name).read_bytes()) != expected:
            raise ValueError('Invalid candidate file: ' + name)
    info = json.loads((root / 'BUILD_INFO.json').read_text())
    if info['realm'] != 'EU' or not info['independently_generated']:
        raise ValueError('EU independent candidate required')
    if not info['quality']['ready']:
        raise ValueError('Quality gate rejected this candidate')
    return info


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('process'); p.add_argument('cache', type=Path); p.add_argument('--code-hash', required=True); p.add_argument('--python27', required=True); p.add_argument('--python3', required=True); p.add_argument('--ffdec', required=True)
    e = sub.add_parser('export'); e.add_argument('cache', type=Path); e.add_argument('destination', type=Path); e.add_argument('--discovery', required=True); e.add_argument('--code-hash', required=True)
    v = sub.add_parser('verify'); v.add_argument('root', type=Path)
    args = parser.parse_args()
    if args.command == 'process': process(args.cache, args.code_hash, args.python27, args.python3, args.ffdec)
    elif args.command == 'export': export_candidate(args.cache, args.destination, args.discovery, args.code_hash)
    else: print(json.dumps(verify_candidate(args.root)['quality']['measured']))
