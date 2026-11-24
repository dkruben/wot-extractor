"""Locked WGUS plans and immutable source-package caches for the EU bot."""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import stat
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
import zipfile

from .cdn_regions import require_region
from .detect.pkgprobe import categorize
from .extract.writer import save_json_atomic, write_atomic

SCHEMA = 1
TEXT = {'.py', '.xml', '.def', '.txt', '.json', '.csv', '.js', '.mjs', '.css', '.html', '.htm',
        '.ts', '.unbound', '.po', '.proto', '.ini', '.cfg'}
CODE = {'.pyc', '.pyo', '.swf', '.swc', '.gfx', '.mo'}
PACKED = b'\x45\x4e\xa1\x62'


def digest(data):
    return hashlib.sha256(data).hexdigest()


def safe_name(name):
    path = PurePosixPath(name)
    if path.is_absolute() or '..' in path.parts or '.git' in path.parts or ':' in name or '\\' in name or '\0' in name or str(path) != name:
        raise ValueError('Unsafe CDN member: ' + name)
    return name


def discover(realm='EU'):
    target = require_region(realm)
    def request(endpoint, query):
        url = 'https://' + target['host'] + endpoint + '?' + urllib.parse.urlencode(query)
        with urllib.request.urlopen(url, timeout=45) as response:
            data = response.read(8 * 1024 * 1024 + 1)
        if len(data) > 8 * 1024 * 1024:
            raise ValueError('Unexpected WGUS response size')
        return ET.fromstring(data), data.decode('utf-8-sig')
    meta, metadata_xml = request('/api/v1/metadata/', {'guid': target['guid'], 'chain_id': 'unknown', 'protocol_version': '7.10'})
    pre = meta.find('predefined_section')
    if pre is None or meta.findtext('redirect_application_id'):
        raise ValueError('Unreviewed WGUS metadata redirect')
    types = pre.find('client_types')
    kind = next((t for t in types if t.get('id') == 'sd'), None)
    if kind is None:
        raise ValueError('No SD source profile advertised')
    query = {'game_id': target['guid'], 'protocol_version': '1.11', 'metadata_protocol_version': '7.10',
             'metadata_version': meta.findtext('version'), 'client_type': 'sd',
             'lang': pre.findtext('default_language'), 'chain_id': pre.findtext('chain_id'), 'game_installation': 'true'}
    for item in kind.findall('client_parts/client_part'):
        query[item.get('id') + '_current_version'] = '0'
    root, chain_xml = request('/api/v1/patches_chain/', query)
    if root.findtext('redirect_url'):
        raise ValueError('Unreviewed WGUS chain redirect')
    seeds = [e.text.strip() for e in root.findall('web_seeds/url') if e.text]
    if not seeds:
        raise ValueError('WGUS returned no download mirrors')
    chain_types = [e.get('type', '') for e in root.findall('patches_chain')]
    # Preload is a separate future chain, never part of the active installation.
    release_ready = chain_types.count('install') == 1 and set(chain_types) <= {'install', 'preload'} and root.findtext('meta_need_update', 'false').lower() == 'false'
    patches = []
    for p in root.findall("patches_chain[@type='install']/patch"):
        files = [{'name': safe_name(f.findtext('name').strip()), 'size': int(f.findtext('size'))} for f in p.findall('files/file')]
        patches.append({'part': p.findtext('part'), 'from': p.findtext('version_from'), 'to': p.findtext('version_to'),
                        'torrent': p.findtext('torrent/hash'), 'volumes': [{'url': seeds[0] + f['name'], 'size': f['size']} for f in files], 'files': files})
    chains = {}
    for part in ['client', 'sdcontent', 'locale']:
        choices = [p for p in patches if p['part'] == part]
        if not choices:
            raise ValueError('Missing source part: ' + part)
        by_from = {}
        for p in choices:
            if not p['from'] or p['from'] in by_from:
                raise ValueError('Ambiguous or missing version_from: ' + part)
            by_from[p['from']] = p
        ordered, current, visited = [], '0', set()
        while current in by_from:
            if current in visited:
                raise ValueError('Cyclic patch chain')
            visited.add(current)
            p = by_from[current]
            ordered.append(p)
            current = p['to']
        if not ordered or len(ordered) != len(choices):
            raise ValueError('Disconnected source chain: ' + part)
        chains[part] = ordered
    identity = {'schema': SCHEMA, 'realm': realm, 'guid': target['guid'], 'version': root.findtext('version_name'),
                'metadata': meta.findtext('version'), 'chains': [{k: v for k, v in p.items() if k != 'volumes'} for part in chains.values() for p in part]}
    return dict(identity, fingerprint=digest(json.dumps(identity, sort_keys=True).encode()), chains=chains,
                release_ready=release_ready, chain_types=chain_types, delay_preload=root.findtext('delay_preload'),
                metadata_xml=metadata_xml, chain_xml=chain_xml, host=target['host'])


def active_packages(paths):
    root = ET.parse(paths).getroot()
    result = []
    for node in root.findall('./Paths/Packages/Package'):
        if 'sd' not in node.get('type', 'sd').split(','):
            continue
        name = safe_name(node.text.strip().removeprefix('./'))
        if not name.startswith('res/packages/') or not name.endswith('.pkg'):
            raise ValueError('Unexpected active package path')
        if not Path(name).name.lower().startswith('audioww'):
            result.append(name)
    if not result or 'res/packages/scripts.pkg' not in result:
        raise ValueError('Incomplete paths.xml package inventory')
    return list(dict.fromkeys(result))


def import_package(archive, destination, container, fingerprint):
    destination = Path(destination)
    if destination.exists():
        raise ValueError('Cache destination must be new')
    destination.mkdir(parents=True)
    records = {}
    with zipfile.ZipFile(archive) as z:
        for member in z.infolist():
            if member.is_dir():
                continue
            name = safe_name(member.filename)
            if stat.S_ISLNK(member.external_attr >> 16):
                raise ValueError('Package symlinks are not source inputs')
            ext = PurePosixPath(name).suffix.lower()
            with z.open(member) as source:
                head = source.read(4)
                is_packed = head == PACKED
                wanted = is_packed or ext in TEXT | CODE or '/gameface/' in '/' + name or '/gui/unbound/' in '/' + name
                if not wanted:
                    continue
                data = head + source.read()
            category = categorize(name)
            record = {'tree': 'res', 'path': name, 'virtual': name, 'source': 'cdn', 'container': container,
                      'member': name, 'size': len(data), 'sha256': digest(data), 'category': 'xml' if is_packed else category,
                      'status': 'extracted'}
            if is_packed:
                record['validation'] = 'packed'
            if ext in {'.pyc', '.pyo'}:
                if head != b'\x03\xf3\r\n':
                    raise ValueError('Unexpected bytecode version: ' + name)
                record['info'] = {'pyc_version': '2.7'}
            write_atomic(destination / 'files' / name, data)
            records['res/' + name] = record
    save_json_atomic(destination / 'package.json', {'schema': SCHEMA, 'fingerprint': fingerprint, 'container': container, 'entries': records})
    print(container, 'cached source members:', len(records), flush=True)


def validate_package(destination, fingerprint):
    destination = Path(destination)
    try:
        manifest = json.loads((destination / 'package.json').read_text())
        if manifest['schema'] != SCHEMA or manifest['fingerprint'] != fingerprint:
            return False
        for key, record in manifest['entries'].items():
            if key != 'res/' + record['path'] or record['tree'] != 'res':
                return False
            path = destination / 'files' / safe_name(record['path'])
            if not path.is_file() or digest(path.read_bytes()) != record['sha256']:
                return False
        return True
    except (OSError, ValueError, KeyError):
        return False


def assemble(plan_path, cache_root, code_hash):
    plan = json.loads(Path(plan_path).read_text())
    cache_root = Path(cache_root).resolve()
    out = cache_root / 'work' / ('wot_src_' + plan['realm'])
    old = json.loads((out / 'manifest.json').read_text()) if (out / 'manifest.json').exists() else {'entries': {}}
    if old.get('generator_code_hash') != code_hash and out.exists():
        if out.parent != cache_root / 'work' or not out.name.startswith('wot_src_'):
            raise ValueError('Unsafe processing-cache reset')
        shutil.rmtree(out)
        old = {'entries': {}}
    out.mkdir(parents=True, exist_ok=True)
    desired = {}
    for package in plan['packages']:
        directory = cache_root / 'packages' / package['fingerprint']
        if not validate_package(directory, package['fingerprint']):
            raise ValueError('Invalid cached package: ' + package['name'])
        records = json.loads((directory / 'package.json').read_text())['entries']
        for key, record in records.items():
            desired.setdefault(key, (record, directory / 'files' / record['path']))
    for item in plan['loose']:
        path = Path(item['path'])
        data = path.read_bytes()
        name = safe_name(item['name'])
        tree, sep, relative = name.partition('/')
        if tree != 'res' or not sep:
            tree, relative = 'root', name
        key = tree + '/' + relative
        desired.setdefault(key, ({'tree': tree, 'path': relative, 'virtual': relative, 'category': categorize(relative),
                                  'source': 'cdn', 'container': item['name'], 'size': len(data), 'sha256': digest(data), 'status': 'extracted'}, path))
    # Retire removed inputs and their derived outputs before reusing any state.
    for key, record in old['entries'].items():
        if key in desired:
            continue
        paths = ['sources/' + key, (record.get('decoded') or {}).get('path'), (record.get('decompiled') or {}).get('output')]
        gf = record.get('gameface') or {}
        paths += [gf.get('formatted'), gf.get('analysis'), 'sources_as/scripts/' + key,
                  'sources_as/swf/' + key + '.json', 'sources_as/assets/' + key]
        for relative in filter(None, paths):
            target = out / safe_name(relative)
            if target.is_dir():
                shutil.rmtree(target)
            elif target.exists():
                target.unlink()
    entries = {}
    for key, (record, source) in desired.items():
        previous = old['entries'].get(key, {})
        rec = dict(copy.deepcopy(previous), **copy.deepcopy(record))
        rec['status'] = 'unchanged' if previous.get('sha256') == rec['sha256'] else 'extracted'
        destination = out / 'sources' / key
        if not destination.is_file() or previous.get('sha256') != rec['sha256'] or digest(destination.read_bytes()) != rec['sha256']:
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.unlink(missing_ok=True)
            try:
                os.link(source, destination)
            except OSError:
                shutil.copyfile(source, destination)
        entries[key] = rec
    manifest = {'realm': plan['realm'], 'entries': entries, 'generator_code_hash': code_hash,
                'origin': 'direct WGUS/CDN acquisition', 'acquisition': plan}
    save_json_atomic(out / 'manifest.json', manifest, indent=None)
    return out


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    d = sub.add_parser('discover'); d.add_argument('output', type=Path)
    a = sub.add_parser('active'); a.add_argument('paths', type=Path)
    i = sub.add_parser('import'); i.add_argument('archive', type=Path); i.add_argument('destination', type=Path); i.add_argument('--container', required=True); i.add_argument('--fingerprint', required=True)
    v = sub.add_parser('validate'); v.add_argument('destination', type=Path); v.add_argument('--fingerprint', required=True)
    args = parser.parse_args()
    if args.command == 'discover':
        result = discover(); save_json_atomic(args.output, result)
        print(json.dumps({k: result[k] for k in ['realm', 'version', 'fingerprint', 'release_ready']}))
    elif args.command == 'active': print(json.dumps(active_packages(args.paths)))
    elif args.command == 'import': import_package(args.archive, args.destination, args.container, args.fingerprint)
    elif args.command == 'validate': sys_exit = 0 if validate_package(args.destination, args.fingerprint) else 1; raise SystemExit(sys_exit)
