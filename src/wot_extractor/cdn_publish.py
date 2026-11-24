"""Verify a source artifact and fast-forward a single explicitly selected branch."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
import tarfile

from .cdn_acquire import discover, safe_name
from .cdn_pipeline import verify_candidate
from .cdn_regions import require_region


def unpack(archive, destination):
    destination = Path(destination)
    if destination.exists():
        raise ValueError('Extraction destination must be new')
    destination.mkdir(parents=True)
    with tarfile.open(archive, 'r:gz') as tar:
        seen = set()
        for member in tar:
            name = member.name.removeprefix('./')
            if name in ('', '.') and member.isdir():
                continue
            safe_name(name)
            if name in seen or not (member.isfile() or member.isdir()):
                raise ValueError('Duplicate or non-regular artifact member: ' + name)
            seen.add(name)
            target = destination / name
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
            else:
                target.parent.mkdir(parents=True, exist_ok=True)
                with tar.extractfile(member) as source, target.open('xb') as output:
                    shutil.copyfileobj(source, output)
    return verify_candidate(destination)


def publish(archive, workspace, branch, repository, expected_head):
    realm = branch.removeprefix('candidate/')
    require_region(realm)
    if branch not in (realm, 'candidate/' + realm) or not re.fullmatch(r'[\w.-]+/[\w.-]+', repository):
        raise ValueError('Only catalogued WG regional branches are supported')
    workspace = Path(workspace).resolve()
    if workspace.exists():
        raise ValueError('Publication workspace must be new')
    workspace.mkdir(parents=True)
    candidate = workspace / 'candidate'
    info = unpack(archive, candidate)
    if info['realm'] != realm:
        raise ValueError('Artifact region does not match the target branch')
    current = discover(realm)
    if not current['release_ready'] or current['fingerprint'] != info['acquisition_fingerprint']:
        raise ValueError('WG active installation changed during the build; rebuild required')
    checkout = workspace / 'checkout'
    checkout.mkdir()
    def git(*args):
        return subprocess.check_output(['git', '-c', 'core.autocrlf=false', '-C', str(checkout), *args], text=True).strip()
    git('init')
    git('remote', 'add', 'origin', 'https://github.com/' + repository + '.git')
    remote = git('ls-remote', 'origin', 'refs/heads/' + branch)
    actual = remote.split()[0] if remote else ''
    if actual != expected_head:
        raise ValueError('Publication branch changed during the build; refusing to overwrite')
    if actual:
        git('fetch', '--depth=1', 'origin', 'refs/heads/' + branch)
        git('checkout', '-b', 'publication', 'FETCH_HEAD')
    else:
        git('checkout', '--orphan', 'publication')
    # Preserve workflow entrypoints from the target, replace its source snapshot.
    for item in checkout.iterdir():
        if item.name in ('.git', '.github'):
            continue
        if item.is_dir() and not item.is_symlink():
            shutil.rmtree(item)
        else:
            item.unlink()
    for item in candidate.iterdir():
        target = checkout / item.name
        if item.is_dir():
            shutil.copytree(item, target)
        else:
            shutil.copyfile(item, target)
    git('add', '-f', '-A')
    # Git must retain the verified bytes, including CRLF in game originals.
    expected = json.loads((candidate / 'PUBLICATION_MANIFEST.json').read_text())['files']
    import hashlib
    staged = {}
    for item in git('ls-files', '--stage', '-z').split('\0'):
        if item:
            metadata, name = item.split('\t', 1)
            staged[name] = metadata.split()[1]
    for name in expected:
        data = (candidate / name).read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if blob != staged.get(name):
            raise ValueError('Git altered verified file bytes: ' + name)
    if not git('diff', '--cached', '--name-only'):
        print('Verified source snapshot is already published')
        return
    git('config', 'user.name', 'github-actions[bot]')
    git('config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com')
    git('commit', '-m', 'Generate ' + realm + ' sources ' + info['version'] + ' directly from WG CDN')
    git('push', 'origin', 'HEAD:refs/heads/' + branch)
    print('Published', branch, git('rev-parse', 'HEAD'))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('archive', type=Path)
    parser.add_argument('workspace', type=Path)
    parser.add_argument('--branch', required=True)
    parser.add_argument('--repository', required=True)
    parser.add_argument('--expected-head', default='')
    args = parser.parse_args()
    publish(args.archive, args.workspace, args.branch, args.repository, args.expected_head)
