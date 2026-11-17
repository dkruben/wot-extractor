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
import zipfile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from wot_extractor.cdn_regions import require_region
from wot_extractor.extract.writer import write_atomic


def safe_path(name):
    value = PurePosixPath(name)
    if value.is_absolute() or '..' in value.parts or '.git' in value.parts or ':' in name or '\\' in name or str(value) != name:
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
            overlay = root / 'overlay'
            overlay.mkdir()
            env = dict(os.environ, GIT_INDEX_FILE=str(root / 'index'),
                       GIT_AUTHOR_NAME='dkruben', GIT_AUTHOR_EMAIL='20760582+dkruben@users.noreply.github.com',
                       GIT_COMMITTER_NAME='dkruben', GIT_COMMITTER_EMAIL='20760582+dkruben@users.noreply.github.com')
            git('read-tree', upstream_tree, env=env)
            for name, expected in payload.items():
                data = archive.read(prefix + name)
                if hashlib.sha256(data).hexdigest() != expected:
                    raise ValueError('Artifact SHA-256 mismatch: ' + name)
                write_atomic(overlay.joinpath(*safe_path(name).parts), data)
            write_atomic(overlay / 'README.md', readme.encode('utf-8'))
            write_atomic(overlay / 'BUILD_INFO.json', (json.dumps(provenance, indent=2) + '\n').encode('utf-8'))
            names = list(payload) + ['README.md', 'BUILD_INFO.json']
            git('--work-tree=' + str(overlay), 'add', '-f', '--pathspec-from-file=-', '--pathspec-file-nul',
                data=b''.join(n.encode('utf-8') + b'\0' for n in names), env=env)
            tree = git('write-tree', env=env).decode().strip()
            commit = git('commit-tree', tree, data=('v.' + baseline_version + ' — initial ' + realm + ' reference and CDN Gameface\n').encode('utf-8'), env=env).decode().strip()
            git('update-ref', 'refs/heads/' + realm, commit, '0' * 40)
            git('symbolic-ref', 'HEAD', 'refs/heads/' + realm)
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
