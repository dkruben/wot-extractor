"""RABCDAsm (abcexport + rabcdasm): desmontagem SEM PERDAS do bytecode AS3 em assembly AVM2 (.asasm).

Complementa o FFDec onde este nao reconstroi o codigo (linhas `§§`, metodos nao descompilados): o .asasm
mostra todas as instrucoes de cada metodo. E o formato usado pelo XVM para aplicar patches aos SWF.
As ferramentas so leem uma copia do SWF numa pasta temporaria; nada do SWF e executado.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

ENV_VAR = "WOT_EXTRACTOR_RABCDASM"


@dataclass
class Rabc:
    dir: Path

    @property
    def abcexport(self) -> Path:
        return self.dir / ("abcexport.exe" if os.name == "nt" else "abcexport")

    @property
    def rabcdasm(self) -> Path:
        return self.dir / ("rabcdasm.exe" if os.name == "nt" else "rabcdasm")

    def label(self) -> str:
        return "RABCDAsm"

    def to_dict(self) -> dict:
        return {"dir": str(self.dir), "abcexport": str(self.abcexport), "rabcdasm": str(self.rabcdasm)}


def _from(path: Path | str | None) -> Rabc | None:
    if not path:
        return None
    p = Path(path)
    if p.is_file():
        p = p.parent
    r = Rabc(p)
    return r if r.abcexport.is_file() and r.rabcdasm.is_file() else None


def find_rabcdasm(configured: Path | None = None) -> tuple[Rabc | None, str]:
    for cand in (configured, os.environ.get(ENV_VAR), shutil.which("rabcdasm")):
        r = _from(cand)
        if r:
            return r, ""
    return None, ("RABCDAsm nao encontrado (indique a pasta com abcexport/rabcdasm em [actionscript] rabcdasm, "
                  f"--rabcdasm ou {ENV_VAR})")


def _run(cmd: list[str], cwd: Path, timeout: float) -> tuple[int | None, str]:
    try:
        r = subprocess.run(cmd, cwd=str(cwd), capture_output=True, timeout=timeout, stdin=subprocess.DEVNULL,
                           creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    except subprocess.TimeoutExpired:
        return None, f"tempo limite de {timeout:.0f} s excedido"
    except OSError as exc:
        return None, f"{type(exc).__name__}: {exc}"
    return r.returncode, (r.stderr or r.stdout or b"").decode("utf-8", "replace")[-300:]


def disassemble(rabc: Rabc, swf_bytes: bytes, work: Path, timeout: float = 1800) -> tuple[list[Path], str, float]:
    """Desmonta todos os blocos ABC do SWF para `work`. Devolve (pastas <bloco>/, erro, segundos)."""
    t0 = time.perf_counter()
    if work.exists():
        shutil.rmtree(work, ignore_errors=True)
    work.mkdir(parents=True)
    swf = work / "movie.swf"
    swf.write_bytes(swf_bytes)
    rc, err = _run([str(rabc.abcexport), swf.name], work, timeout)
    swf.unlink(missing_ok=True)
    if rc != 0:
        return [], f"abcexport falhou ({rc}): {err.strip()}", time.perf_counter() - t0
    abcs = sorted(work.glob("movie-*.abc"), key=lambda p: int(p.stem.rsplit("-", 1)[1]))
    if not abcs:
        return [], "abcexport nao encontrou blocos ABC", time.perf_counter() - t0
    dirs = []
    for abc in abcs:
        rc, err = _run([str(rabc.rabcdasm), abc.name], work, timeout)
        abc.unlink(missing_ok=True)
        if rc != 0:
            return dirs, f"rabcdasm falhou em {abc.name} ({rc}): {err.strip()}", time.perf_counter() - t0
        d = work / abc.stem
        if d.is_dir():
            dirs.append(d)
    return dirs, "", time.perf_counter() - t0
