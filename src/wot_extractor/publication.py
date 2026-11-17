"""Publish the reference layout without moving the extractor's working files."""
from __future__ import annotations

import os
from pathlib import Path
import subprocess
import tempfile


def public_path(path: bytes) -> bytes:
    root, sep, rest = path.partition(b'/')
    root = {b'__stubs': b'_stubs', b'sources_as': b'sources-as3'}.get(root, root)
    return root + sep + rest


def _git(git_dir, *args, env=None, data=None):
    return subprocess.run(['git', f'--git-dir={Path(git_dir).resolve()}', *args],
                          input=data, env=env, check=True, capture_output=True).stdout


def reference_tree(git_dir: Path, source: Path | None = None) -> str:
    """Map HEAD, or a fresh source snapshot, through an isolated Git index.

    The real index and working files are never renamed or overwritten.
    """
    with tempfile.TemporaryDirectory(prefix='wot-publication-') as td:
        env = dict(os.environ, GIT_INDEX_FILE=str(Path(td) / 'index'))
        if source is None:
            _git(git_dir, 'read-tree', 'HEAD', env=env)
        else:
            _git(git_dir, 'read-tree', '--empty', env=env)
            _git(git_dir, f'--work-tree={source.resolve()}', 'add', '-A', '--', '.', env=env)
        entries = _git(git_dir, 'ls-files', '--stage', '-z', env=env).split(b'\0')
        mapped, seen = [], set()
        for entry in entries:
            if not entry:
                continue
            header, path = entry.split(b'\t', 1)
            target = public_path(path)
            if target in seen:
                raise ValueError(f'Publication path collision: {target!r}')
            seen.add(target)
            if target == b'README.md':
                mode, blob, stage = header.split()
                content = _git(git_dir, 'cat-file', 'blob', blob.decode())
                content = content.replace(b'__stubs/', b'_stubs/').replace(b'sources_as/', b'sources-as3/')
                blob = _git(git_dir, 'hash-object', '-w', '--stdin', data=content).strip()
                header = b' '.join((mode, blob, stage))
            mapped.append(header + b'\t' + target + b'\0')
        _git(git_dir, 'read-tree', '--empty', env=env)
        _git(git_dir, 'update-index', '-z', '--index-info', env=env, data=b''.join(mapped))
        return _git(git_dir, 'write-tree', env=env).decode().strip()


def commit_publication(git_dir: Path, message: str, source: Path | None = None) -> str:
    head = subprocess.run(['git', f'--git-dir={git_dir.resolve()}', 'rev-parse', '--verify', 'HEAD'],
                          capture_output=True, text=True)
    parent = head.stdout.strip() if head.returncode == 0 else None
    tree = reference_tree(git_dir, source)
    if parent and tree == _git(git_dir, 'rev-parse', 'HEAD^{tree}').decode().strip():
        return 'sem alteracoes'
    args = ['commit-tree', tree]
    if parent:
        args += ['-p', parent]
    commit = _git(git_dir, *args, data=(message + '\n').encode('utf-8')).decode().strip()
    _git(git_dir, 'update-ref', '-m', message.splitlines()[0], 'HEAD', commit,
         parent or '0' * 40)
    return 'commit'


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--git-dir', type=Path, required=True)
    parser.add_argument('--source', type=Path, help='Optional fresh extraction; default: migrate HEAD only')
    parser.add_argument('--apply', action='store_true', help='Create a local commit; never pushes')
    args = parser.parse_args()
    if args.apply:
        print(commit_publication(args.git_dir, 'Align source folders with the wot-src reference layout', args.source))
    else:
        print('Preview tree:', reference_tree(args.git_dir, args.source))
