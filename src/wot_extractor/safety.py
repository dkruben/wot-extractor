"""Regras de seguranca: validacao de caminhos, protecao de escrita sobre as
instalacoes do jogo e limites para arquivos (.pkg/.wotmod/zip)."""

from __future__ import annotations

import os
import re
import zipfile
from dataclasses import dataclass
from pathlib import Path


class UnsafePathError(ValueError):
    """Nome de ficheiro/membro que poderia escapar da pasta de destino."""


class ProtectedPathError(PermissionError):
    """Tentativa de escrita dentro de uma instalacao do jogo."""


class ArchiveLimitError(ValueError):
    """Arquivo ou membro que excede os limites de seguranca."""


_WIN_RESERVED = {"CON", "PRN", "AUX", "NUL"} | {f"COM{i}" for i in range(1, 10)} | {f"LPT{i}" for i in range(1, 10)}
_BAD_CHARS = set('<>:"|?*')
_DRIVE_RE = re.compile(r"^[A-Za-z]:")


def normalize_member_name(name: str) -> str:
    """Valida um caminho relativo (ex.: nome de membro de um zip) e devolve a
    forma POSIX normalizada. Levanta UnsafePathError se for inseguro."""
    if not isinstance(name, str) or not name:
        raise UnsafePathError("nome vazio")
    if "\x00" in name:
        raise UnsafePathError(f"byte nulo no nome: {name!r}")
    n = name.replace("\\", "/")
    if n.startswith("/") or _DRIVE_RE.match(n):
        raise UnsafePathError(f"caminho absoluto: {name!r}")
    parts: list[str] = []
    for part in n.split("/"):
        if part in ("", "."):
            continue
        if part == "..":
            raise UnsafePathError(f"path traversal ('..'): {name!r}")
        if part.endswith((" ", ".")):
            raise UnsafePathError(f"componente termina em espaco/ponto: {name!r}")
        if any(c in _BAD_CHARS or ord(c) < 32 for c in part):
            raise UnsafePathError(f"caracter invalido: {name!r}")
        if part.split(".")[0].upper() in _WIN_RESERVED:
            raise UnsafePathError(f"nome reservado do Windows: {name!r}")
        parts.append(part)
    if not parts:
        raise UnsafePathError(f"caminho sem componentes: {name!r}")
    return "/".join(parts)


def is_within(path: Path, root: Path) -> bool:
    p, r = Path(path).resolve(), Path(root).resolve()
    return p == r or r in p.parents


def resolve_within(base: Path, relative: str) -> Path:
    """Junta `relative` a `base` garantindo (lexicalmente) que o resultado fica
    dentro de base. Nao usa Path.resolve() por ficheiro: no Windows o realpath
    tem corridas com pastas criadas em paralelo e e lento em arvores grandes.
    A seguranca vem de normalize_member_name (sem '..', absolutos ou drives);
    a pasta base em si e validada uma vez pelo WriteGuard."""
    rel = normalize_member_name(relative)
    base_a = os.path.abspath(str(base))
    target = os.path.normpath(os.path.join(base_a, *rel.split("/")))
    if os.path.normcase(os.path.commonpath([base_a, target])) != os.path.normcase(base_a):
        raise UnsafePathError(f"destino fora da pasta base: {relative!r}")
    return Path(target)


class WriteGuard:
    """Bloqueia qualquer escrita dentro das pastas protegidas (instalacoes)."""

    def __init__(self, protected_roots=()):
        self._roots: list[Path] = []
        for r in protected_roots:
            self.protect(r)

    @property
    def roots(self) -> tuple[Path, ...]:
        return tuple(self._roots)

    def protect(self, root: Path) -> None:
        r = Path(root).resolve()
        if r not in self._roots:
            self._roots.append(r)

    def check(self, path: Path) -> Path:
        p = Path(path).resolve()
        for r in self._roots:
            if is_within(p, r):
                raise ProtectedPathError(f"escrita bloqueada dentro da instalacao do jogo: {p} (protegido: {r})")
        return p

    def check_output_root(self, output_root: Path) -> Path:
        out = self.check(output_root)
        for r in self._roots:
            if is_within(r, out):
                raise ProtectedPathError(f"a pasta de saida {out} contem uma instalacao do jogo ({r})")
        return out


@dataclass(frozen=True)
class ArchiveLimits:
    max_entries: int = 500_000
    max_member_size: int = 4 * 1024**3        # 4 GiB por membro
    max_total_size: int = 256 * 1024**3       # 256 GiB por arquivo
    max_ratio: float = 200.0                  # descompactado/compactado (zip bomb)
    ratio_min_size: int = 1024 * 1024         # so aplica a ratio acima de 1 MiB


def check_archive_member(info: zipfile.ZipInfo, limits: ArchiveLimits = ArchiveLimits()) -> str:
    """Valida um membro; devolve o nome normalizado ou levanta excecao."""
    name = normalize_member_name(info.filename)
    if info.file_size > limits.max_member_size:
        raise ArchiveLimitError(f"membro demasiado grande ({info.file_size} B): {info.filename}")
    if info.compress_type != zipfile.ZIP_STORED and info.file_size >= limits.ratio_min_size:
        ratio = info.file_size / max(info.compress_size, 1)
        if ratio > limits.max_ratio:
            raise ArchiveLimitError(f"taxa de compressao suspeita ({ratio:.0f}x): {info.filename}")
    return name


def check_archive(zf: zipfile.ZipFile, limits: ArchiveLimits = ArchiveLimits()) -> None:
    """Valida os totais do arquivo (numero de entradas e tamanho total)."""
    infos = zf.infolist()
    if len(infos) > limits.max_entries:
        raise ArchiveLimitError(f"demasiadas entradas ({len(infos)})")
    total = sum(i.file_size for i in infos)
    if total > limits.max_total_size:
        raise ArchiveLimitError(f"tamanho total excessivo ({total} B)")
