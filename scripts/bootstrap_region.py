"""Create a new regional source branch from a credited baseline and CDN evidence.

Creates a local root commit only. Never pushes or changes the baseline clone.
"""
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import subprocess
import sys
import tempfile
import time
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from wot_extractor.cdn_regions import require_region


def safe_path(name):
    value = PurePosixPath(name)
    if value.is_absolute() or '..' in value.parts or '.git' in value.parts or ':' in name or '\\' in name or '\n' in name or '\r' in name or str(value) != name:
        raise ValueError('Unsafe artifact path: ' + name)
    return value


def bootstrap(realm, baseline, artifact, git_dir, python_evidence, gameface_run, python_run):
    require_region(realm)
    baseline, git_dir = Path(baseline).resolve(), Path(git_dir).resolve()

    def upstream(*args):
        return subprocess.check_output(['git', '-C', str(baseline), *args])

    origin = upstream('remote', 'get-url', 'origin').decode().strip()
    if origin.rstrip('/').removesuffix('.git') != 'https://github.com/izeberg/wot-src':
        raise ValueError('Expected the explicitly credited izeberg/wot-src baseline')
    if upstream('status', '--porcelain', '--untracked-files=no').strip():
        raise ValueError('Baseline has tracked local changes; refusing to import it')
    upstream_commit = upstream('rev-parse', 'HEAD').decode().strip()
    upstream_tree = upstream('rev-parse', 'HEAD^{tree}').decode().strip()
    baseline_version = upstream('show', 'HEAD:.version_name').decode().strip()
    py = json.loads(Path(python_evidence).read_text(encoding='utf-8'))
    if py['realm'] != realm or py['version'] != baseline_version:
        raise ValueError('Python evidence does not match the baseline region/version')

    with zipfile.ZipFile(artifact) as archive:
        summary = json.loads(archive.read('evidence/gameface-validation.json'))
        if summary['realm'] != realm or summary['version'] != baseline_version:
            raise ValueError('Gameface artifact does not match the baseline region/version')
        if not summary['all_original_hashes_preserved'] or any(summary['counts']['totals'].get(k) for k in ['failed', 'partial']):
            raise ValueError('Gameface artifact did not pass integrity and processing checks')
        prefix = 'output/wot_src_' + realm + '/'
        manifest = json.loads(archive.read(prefix + 'manifest.json'))
        if manifest['realm'] != realm:
            raise ValueError('Wrong realm in the raw-resource manifest')
        payload = dict(summary['sha256'])
        if any(not name.startswith('sources_gameface/') for name in payload):
            raise ValueError('Unexpected generated artifact path')
        payload.update({'sources/' + key: record['sha256'] for key, record in manifest['entries'].items()})
        for name in payload:
            safe_path(name)

        git_dir.mkdir(parents=True, exist_ok=True)
        if not (git_dir / 'HEAD').exists():
            subprocess.run(['git', 'init', '--bare', '--initial-branch=' + realm, str(git_dir)], check=True, capture_output=True)

        def git(*args, data=None, env=None):
            return subprocess.run(['git', '--git-dir=' + str(git_dir), *args],
                                  input=data, env=env, check=True, capture_output=True).stdout

        head = subprocess.run(['git', '--git-dir=' + str(git_dir), 'rev-parse', '--verify', 'HEAD'], capture_output=True)
        if head.returncode == 0:
            raise ValueError('Publication repository already has a branch; bootstrap never overwrites it')
        git('config', 'core.autocrlf', 'false')
        git('config', 'core.safecrlf', 'false')

        # Transfer trees/blobs only: the baseline may be shallow. Starting a new
        # attributed root commit avoids pretending to own or pushing its history.
        pack = subprocess.Popen(['git', '-C', str(baseline), 'pack-objects', '--stdout', '--revs'],
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        index = subprocess.Popen(['git', '--git-dir=' + str(git_dir), 'index-pack', '--stdin'],
                                 stdin=pack.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        pack.stdout.close()
        pack.stdin.write((upstream_tree + '\n').encode())
        pack.stdin.close()
        _, index_error = index.communicate()
        pack_error = pack.stderr.read()
        pack.stderr.close()
        if pack.wait() or index.returncode:
            raise RuntimeError('Object transfer failed: ' + (pack_error + index_error).decode(errors='replace'))

        provenance = {
            'realm': realm, 'version': baseline_version,
            'reference_sources': {'repository': origin, 'commit': upstream_commit},
            'generated_here': {'scope': summary['scope'], 'gameface_counts': summary['counts'],
                               'all_original_hashes_preserved': True},
            'python_syntax_inspection': py,
            'gameface_run': gameface_run, 'python_run': python_run,
            'note': 'Python/AS3/reference stubs are an attributed upstream snapshot; Gameface base GUI was rebuilt from CDN. No claim of complete independent regeneration.',
        }
        readme = '''# World of Tanks {realm} — {version}

| Folder | Content |
| --- | --- |
| `sources/` | Reference client sources, plus original Gameface resources |
| `sources-as3/` | Decompiled ActionScript from the credited baseline |
| `_stubs/` | Reference engine stubs from the credited baseline |
| `sources_gameface/` | Formatted HTML/CSS/JS, resource indices and `VIEWS.md` |

Python/AS3/reference sources were initially imported from
[izeberg/wot-src at {commit}](https://github.com/izeberg/wot-src/commit/{commit}).
The existing baseline content is retained; it is not presented as independently
regenerated by this repository.

Gameface base GUI was reconstructed from the regional update CDN and processed
by [our tool](../../tree/main). Game-mode Gameface coverage and Python links
are not included in this first CDN profile. Formatted JS/CSS is not original
source code. See `BUILD_INFO.json` for provenance, quality limits and test runs.

Client content belongs to Wargaming and its respective rights holders; no MIT
licence from the tooling branch is granted for game files.
'''.format(realm=realm, version=baseline_version, commit=upstream_commit)

        with tempfile.TemporaryDirectory(prefix='wot-region-bootstrap-') as temporary:
            root = Path(temporary)
            env = dict(os.environ,
                       GIT_AUTHOR_NAME='dkruben', GIT_AUTHOR_EMAIL='20760582+dkruben@users.noreply.github.com',
                       GIT_COMMITTER_NAME='dkruben', GIT_COMMITTER_EMAIL='20760582+dkruben@users.noreply.github.com')
            seed = git('commit-tree', upstream_tree, data=b'Internal attributed baseline seed\n', env=env).decode().strip()
            temporary_ref = 'refs/wot-bootstrap/' + realm
            names = list(payload) + ['README.md', 'BUILD_INFO.json']
            # Stream blobs into one pack. Thousands of loose-object fsyncs are
            # expensive on Windows; fast-import also bypasses all text filters.
            marks = root / 'marks'
            importer = subprocess.Popen(['git', '--git-dir=' + str(git_dir), 'fast-import', '--quiet', '--done',
                                         '--export-marks=' + marks.as_posix()],
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            expected_git = {}
            try:
                for number, name in enumerate(names, 1):
                    if name == 'README.md':
                        data = readme.encode('utf-8')
                    elif name == 'BUILD_INFO.json':
                        data = (json.dumps(provenance, indent=2) + '\n').encode('utf-8')
                    else:
                        data = archive.read(prefix + name)
                        if hashlib.sha256(data).hexdigest() != payload[name]:
                            raise ValueError('Artifact SHA-256 mismatch: ' + name)
                    expected_git[number] = hashlib.sha1(('blob ' + str(len(data)) + '\0').encode() + data).hexdigest().encode()
                    importer.stdin.write(('blob\nmark :' + str(number) + '\ndata ' + str(len(data)) + '\n').encode())
                    importer.stdin.write(data)
                    importer.stdin.write(b'\n')
                message = b'Internal validated regional overlay\n'
                importer.stdin.write(('commit ' + temporary_ref + '\ncommitter dkruben <20760582+dkruben@users.noreply.github.com> ' + str(int(time.time())) + ' +0000\ndata ' + str(len(message)) + '\n').encode())
                importer.stdin.write(message)
                importer.stdin.write(('from ' + seed + '\n').encode())
                for number, name in enumerate(names, 1):
                    importer.stdin.write(('M 100644 :' + str(number) + ' ' + json.dumps(name, ensure_ascii=False) + '\n').encode('utf-8'))
                importer.stdin.write(b'\n')
                importer.stdin.write(b'done\n')
                importer.stdin.close()
                error = importer.stderr.read()
                importer.stderr.close()
                importer.stdout.read()
                importer.stdout.close()
                if importer.wait():
                    raise RuntimeError('Blob import failed: ' + error.decode(errors='replace'))
            except BaseException:
                if importer.poll() is None:
                    importer.kill()
                    importer.wait()
                for pipe in [importer.stdin, importer.stdout, importer.stderr]:
                    if pipe and not pipe.closed:
                        pipe.close()
                raise
            imported = {int(mark[1:]): blob for mark, blob in (row.split() for row in marks.read_bytes().splitlines())}
            if imported != expected_git:
                raise RuntimeError('Blob import did not preserve every artifact byte')
            # Fast-import updates trees lazily, without walking a 220k-file
            # index or re-writing every unchanged baseline directory.
            temporary_commit = git('rev-parse', temporary_ref).decode().strip()
            tree = git('rev-parse', temporary_ref + '^{tree}').decode().strip()
            def tree_entries(raw):
                return dict(row.split(b'\t', 1)[::-1] for row in raw.split(b'\0') if row)
            original = tree_entries(upstream('ls-tree', '-r', '-z', 'HEAD'))
            published = tree_entries(git('ls-tree', '-r', '-z', tree))
            overrides = {name.encode('utf-8') for name in names}
            if set(published) != set(original) | overrides:
                raise RuntimeError('Publication unexpectedly added or removed baseline paths')
            for number, name in enumerate(names, 1):
                if published[name.encode('utf-8')].split()[-1] != expected_git[number]:
                    raise RuntimeError('Publication changed artifact bytes: ' + name)
            for name, entry in original.items():
                if name not in overrides and published[name] != entry:
                    raise RuntimeError('Publication changed a baseline file: ' + name.decode('utf-8'))
            commit = git('commit-tree', tree, data=('v.' + baseline_version + ' — initial ' + realm + ' reference and CDN Gameface\n').encode('utf-8'), env=env).decode().strip()
            git('update-ref', 'refs/heads/' + realm, commit, '0' * 40)
            git('symbolic-ref', 'HEAD', 'refs/heads/' + realm)
            git('update-ref', '-d', temporary_ref, temporary_commit)
            git('config', 'remote.origin.url', 'https://github.com/dkruben/wot-extractor.git')
            git('config', 'remote.origin.fetch', '+refs/heads/*:refs/remotes/origin/*')
            print(json.dumps({'realm': realm, 'version': baseline_version, 'commit': commit,
                              'baseline': upstream_commit, 'gameface_files': len(summary['sha256'])}, indent=2))
            return commit


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--realm', required=True)
    parser.add_argument('--baseline', type=Path, required=True)
    parser.add_argument('--artifact', type=Path, required=True)
    parser.add_argument('--git-dir', type=Path, required=True)
    parser.add_argument('--python-evidence', type=Path, required=True)
    parser.add_argument('--gameface-run', required=True)
    parser.add_argument('--python-run', required=True)
    args = parser.parse_args()
    bootstrap(args.realm, args.baseline, args.artifact, args.git_dir, args.python_evidence, args.gameface_run, args.python_run)
