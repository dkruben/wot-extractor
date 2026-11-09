"""Integracao com o JPEXS Free Flash Decompiler (FFDec), se estiver instalado.

O FFDec corre numa JVM separada, um processo por SWF, com tempo limite. So le
o SWF e escreve numa pasta temporaria dentro de wot_src_<R>/.state; o SWF nunca
e executado.
"""

from __future__ import annotations

import os
import re
import shutil
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path

from ..logutil import get_logger

log = get_logger("actionscript")

VERSION_RE = re.compile(r"Free Flash Decompiler v\.?\s*([\d.]+)")
# marcas que o FFDec deixa no codigo quando nao consegue descompilar
FAIL_MARKER = "Not decompiled due to"  # throw new IllegalOperationError("Not decompiled due to timeout/error")
UNSTRUCTURED_MARKER = "§§"  # "§§push", "§§goto": fluxo que nao foi reconstruido

ITEMS_SCRIPTS = "script"
ITEMS_ASSETS = "image,font,binaryData,sound,symbolClass"
FORMATS = "script:as,image:png_gif_jpeg,font:ttf,sound:mp3_wav"


@dataclass
class FFDec:
    java: Path
    jar: Path
    version: str
    heap: str = "4g"

    def label(self) -> str:
        return f"FFDec {self.version}"

    def to_dict(self) -> dict:
        return {"java": str(self.java), "jar": str(self.jar), "version": self.version, "heap": self.heap}


def _flags() -> int:
    return getattr(subprocess, "CREATE_NO_WINDOW", 0)


def jar_candidates(configured: Path | None = None) -> list[Path]:
    out: list[Path] = []
    roots = []
    for env in ("ProgramFiles(x86)", "ProgramFiles", "ProgramW6432"):
        v = os.environ.get(env)
        if v:
            roots.append(Path(v) / "FFDec")
    if os.environ.get("LOCALAPPDATA"):
        roots.append(Path(os.environ["LOCALAPPDATA"]) / "Programs" / "FFDec")
    for p in [configured, os.environ.get("WOT_EXTRACTOR_FFDEC") or None]:
        if p:
            p = Path(p)
            out.extend([p / "ffdec-cli.jar", p / "ffdec.jar"] if p.is_dir() else [p])
    for r in roots:
        out.extend([r / "ffdec-cli.jar", r / "ffdec.jar"])
    seen, res = set(), []
    for p in out:
        if p not in seen:
            seen.add(p)
            res.append(p)
    return res


def java_candidates(configured: Path | None = None) -> list[Path]:
    out = []
    if configured:
        out.append(Path(configured))
    if os.environ.get("JAVA_HOME"):
        out.append(Path(os.environ["JAVA_HOME"]) / "bin" / ("java.exe" if os.name == "nt" else "java"))
    w = shutil.which("java")
    if w:
        out.append(Path(w))
    return [p for p in out if p.is_file()]


def probe(java: Path, jar: Path, timeout: float = 90) -> str:
    """Versao do FFDec (texto vazio se nao responder como o FFDec)."""
    try:
        r = subprocess.run([str(java), "-Djava.awt.headless=true", "-jar", str(jar), "--help"], capture_output=True,
                           timeout=timeout, creationflags=_flags())
    except (OSError, subprocess.TimeoutExpired):
        return ""
    m = VERSION_RE.search((r.stdout + r.stderr).decode("utf-8", "replace"))
    return m.group(1) if m else ""


def find_ffdec(jar: Path | None = None, java: Path | None = None, heap: str = "4g") -> tuple[FFDec | None, str]:
    javas = java_candidates(java)
    if not javas:
        return None, "Java nao encontrado (necessario para o FFDec)"
    tried = []
    for j in jar_candidates(jar):
        if not j.is_file():
            continue
        v = probe(javas[0], j)
        if v:
            return FFDec(javas[0], j, v, heap), ""
        tried.append(str(j))
    if tried:
        return None, f"FFDec nao respondeu: {', '.join(tried)}"
    return None, "FFDec nao encontrado (indique-o com --ffdec ou [actionscript] ffdec)"


MEMORY_MARKERS = (b"insufficient memory for the Java Runtime", b"java.lang.OutOfMemoryError")
TIMEOUT_GRACE = 300  # s alem do -exportTimeout do FFDec antes de terminar o processo


@dataclass
class ExportRun:
    returncode: int | None
    elapsed: float
    timed_out: bool
    log_tail: str
    out_of_memory: bool = False


def export(ff: FFDec, swf: Path, out_dir: Path, items: str, timeout: float, method_timeout: int = 60,
           class_timeout: int = 600) -> ExportRun:
    out_dir.mkdir(parents=True, exist_ok=True)
    log_path = out_dir.parent / (out_dir.name + ".log")
    # -exportTimeout: o FFDec tem 1800 s por omissao e cortaria a exportacao dos SWF grandes a meio
    cmd = [str(ff.java), f"-Xmx{ff.heap}", "-Djava.awt.headless=true", "-jar", str(ff.jar),
           "-onerror", "ignore", "-timeout", str(method_timeout), "-exportFileTimeout", str(class_timeout),
           "-exportTimeout", str(int(timeout)), "-format", FORMATS, "-export", items, str(out_dir), str(swf)]
    t0 = time.perf_counter()
    timed_out = False
    with open(log_path, "wb") as logf:
        # cwd na pasta temporaria: relatorios hs_err_pid*.log da JVM nao vao parar ao projeto
        proc = subprocess.Popen(cmd, stdout=logf, stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL,
                                cwd=str(out_dir.parent), creationflags=_flags())
        try:
            rc = proc.wait(timeout=timeout + TIMEOUT_GRACE)
        except subprocess.TimeoutExpired:
            timed_out = True
            proc.kill()
            proc.wait()
            rc = None
    tail, oom = "", False
    try:
        with open(log_path, "rb") as fh:
            prev = b""
            while True:
                chunk = fh.read(1 << 20)
                if not chunk:
                    break
                if any(m in prev[-64:] + chunk for m in MEMORY_MARKERS):
                    oom = True
                prev = chunk
            fh.seek(max(0, os.path.getsize(log_path) - 4000))
            lines = [ln for ln in fh.read().decode("utf-8", "replace").splitlines() if ln.strip()]
            tail = "\n".join(lines[-8:])
    except OSError:
        pass
    return ExportRun(rc, time.perf_counter() - t0, timed_out, tail, oom)
