"""Manifesto (estado da arvore extraida) e journal (retoma de execucoes
interrompidas)."""

from __future__ import annotations

import json
import os
import threading
from pathlib import Path

from ..logutil import get_logger
from .writer import long_path

log = get_logger("extract")


class ManifestError(Exception):
    pass


class StateLocked(ManifestError):
    """Outra execucao (extract/decompile) esta a usar a mesma arvore."""


class StateLock:
    """Bloqueio exclusivo de wot_src_<R>/.state/lock enquanto o manifesto e
    alterado. O sistema operativo liberta-o se o processo morrer."""

    def __init__(self, out_dir: Path):
        self.path = Path(out_dir) / ".state" / "lock"
        self._fh = None

    def __enter__(self) -> "StateLock":
        os.makedirs(long_path(self.path.parent), exist_ok=True)
        fh = open(long_path(self.path), "a+b")
        try:
            if os.name == "nt":
                import msvcrt
                fh.seek(0)
                msvcrt.locking(fh.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(fh.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError:
            fh.close()
            raise StateLocked(f"{self.path.parent.parent} esta a ser usada por outra execucao do wot-extractor") from None
        self._fh = fh
        return self

    def __exit__(self, *exc) -> None:
        fh, self._fh = self._fh, None
        if fh is None:
            return
        try:
            if os.name == "nt":
                import msvcrt
                fh.seek(0)
                msvcrt.locking(fh.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl
                fcntl.flock(fh.fileno(), fcntl.LOCK_UN)
        except OSError:
            pass
        fh.close()


def load_manifest(path: Path) -> dict | None:
    if not path.is_file():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        raise ManifestError(f"manifesto ilegivel ({path}): {exc}") from exc
    if not isinstance(data, dict) or not isinstance(data.get("entries"), dict):
        raise ManifestError(f"manifesto com formato inesperado: {path}")
    return data


class Journal:
    """Ficheiro JSON-lines com um registo por entrada concluida. Escrito so
    pela thread principal; flush periodico."""

    def __init__(self, path: Path, flush_every: int = 200):
        self.path = path
        self.flush_every = flush_every
        self._fh = None
        self._pending = 0
        self._lock = threading.Lock()

    def load(self) -> dict[str, dict]:
        records: dict[str, dict] = {}
        if not self.path.is_file():
            return records
        with open(long_path(self.path), "r", encoding="utf-8", errors="replace") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    rec = json.loads(line)
                except ValueError:
                    continue  # ultima linha truncada por interrupcao
                key = rec.get("key")
                if key:
                    records[key] = rec
        return records

    def write(self, rec: dict) -> None:
        with self._lock:
            if self._fh is None:
                os.makedirs(long_path(self.path.parent), exist_ok=True)
                self._fh = open(long_path(self.path), "a", encoding="utf-8")
            self._fh.write(json.dumps(rec, ensure_ascii=False, separators=(",", ":")) + "\n")
            self._pending += 1
            if self._pending >= self.flush_every:
                self._fh.flush()
                self._pending = 0

    def close(self) -> None:
        with self._lock:
            if self._fh is not None:
                self._fh.flush()
                os.fsync(self._fh.fileno())
                self._fh.close()
                self._fh = None

    def remove(self) -> None:
        self.close()
        try:
            os.remove(long_path(self.path))
        except OSError:
            pass
