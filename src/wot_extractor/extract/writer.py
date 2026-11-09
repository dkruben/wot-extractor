"""Escrita atomica de ficheiros (tmp + replace) com hash SHA-256 e suporte a
caminhos longos do Windows."""

from __future__ import annotations

import hashlib
import json
import os
import threading
from pathlib import Path

CHUNK = 1024 * 1024


def long_path(p: Path | str) -> str:
    """Prefixo \\\\?\\ no Windows para caminhos acima de 260 caracteres."""
    s = os.path.abspath(str(p))
    if os.name != "nt" or s.startswith("\\\\?\\"):
        return s
    if s.startswith("\\\\"):
        return "\\\\?\\UNC\\" + s[2:]
    return "\\\\?\\" + s


def existing_size(p: Path) -> int | None:
    try:
        return os.stat(long_path(p)).st_size
    except OSError:
        return None


def write_atomic(dest: Path, source) -> tuple[int, str]:
    """Escreve `source` (bytes ou objeto com .read) em `dest`. Devolve (tamanho, sha256)."""
    os.makedirs(long_path(dest.parent), exist_ok=True)
    tmp = dest.with_name(f"{dest.name}.{os.getpid()}.{threading.get_ident()}.part~")
    h = hashlib.sha256()
    size = 0
    try:
        with open(long_path(tmp), "wb") as out:
            if isinstance(source, (bytes, bytearray, memoryview)):
                h.update(source)
                out.write(source)
                size = len(source)
            else:
                while True:
                    chunk = source.read(CHUNK)
                    if not chunk:
                        break
                    h.update(chunk)
                    out.write(chunk)
                    size += len(chunk)
        os.replace(long_path(tmp), long_path(dest))
    except BaseException:
        try:
            os.remove(long_path(tmp))
        except OSError:
            pass
        raise
    return size, h.hexdigest()


def save_json_atomic(path: Path, data, indent: int | None = 2) -> None:
    text = json.dumps(data, indent=indent, ensure_ascii=False, separators=None if indent else (",", ":"))
    write_atomic(path, text.encode("utf-8"))


def remove_file(p: Path) -> bool:
    try:
        os.remove(long_path(p))
        return True
    except OSError:
        return False


def remove_tree(p: Path) -> bool:
    """Apaga uma pasta (com caminhos longos). Devolve True se existia."""
    import shutil
    lp = long_path(p)
    if not os.path.isdir(lp):
        return False
    shutil.rmtree(lp, ignore_errors=True)
    return True
