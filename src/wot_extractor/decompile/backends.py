"""Descompiladores disponiveis e processos de trabalho que os executam.

Cada backend corre num interpretador externo (o worker `_worker.py`), com
pedidos/respostas em linhas JSON. Um worker que exceda o tempo limite ou
termine inesperadamente e reiniciado e o ficheiro fica registado como falha.

Backends:
  uncompyle6      uncompyle6 a correr no Python 2.7 (primario para bytecode 2.7;
                  o mesmo interpretador valida o codigo com o parser de 2.7).
  uncompyle6-py3  uncompyle6 a correr no Python 3 (alternativa; o codigo e
                  validado pelo Python 2.7, nunca pelo parser de Python 3).
"""

from __future__ import annotations

import json
import os
import queue
import shutil
import subprocess
import sys
import threading
from dataclasses import dataclass, field
from pathlib import Path

from ..logutil import get_logger

log = get_logger("decompile")

WORKER_PATH = Path(__file__).with_name("_worker.py")
HELLO_TIMEOUT = 60.0


class BackendError(Exception):
    """Interpretador ou descompilador indisponivel."""


class WorkerTimeout(Exception):
    pass


class WorkerCrashed(Exception):
    pass


@dataclass(frozen=True)
class BackendSpec:
    name: str
    interpreter: str  # "py27" ou "py3"
    versions: frozenset[str]  # versoes de bytecode suportadas e validaveis
    description: str


BACKENDS: dict[str, BackendSpec] = {
    "uncompyle6": BackendSpec("uncompyle6", "py27", frozenset({"2.7"}),
                              "uncompyle6 no Python 2.7 (primario, validado pelo parser 2.7)"),
    "uncompyle6-py3": BackendSpec("uncompyle6-py3", "py3", frozenset({"2.7"}),
                                  "uncompyle6 no Python 3 (alternativa, validado pelo parser 2.7)"),
}
DEFAULT_CHAIN = ("uncompyle6", "uncompyle6-py3")


@dataclass
class Interpreter:
    role: str
    path: Path
    python: str = ""
    uncompyle6: str = ""
    xdis: str = ""
    error: str = ""

    @property
    def ok(self) -> bool:
        return not self.error and bool(self.uncompyle6)

    def label(self) -> str:
        return f"uncompyle6 {self.uncompyle6} / Python {self.python}"

    def to_dict(self) -> dict:
        return {"path": str(self.path), "python": self.python, "uncompyle6": self.uncompyle6,
                "xdis": self.xdis, "error": self.error}


# ------------------------------------------------------------------ processos

def _popen(interp: Path, cwd: Path, script: Path | None = None) -> subprocess.Popen:
    flags = getattr(subprocess, "CREATE_NO_WINDOW", 0)
    # -E ignora PYTHON* do ambiente; -B nao escreve .pyc. O cwd e uma pasta de
    # estado sem codigo, para nada ser importado por acidente a partir dela.
    return subprocess.Popen([str(interp), "-E", "-B", str(script or WORKER_PATH)], stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, cwd=str(cwd),
                            creationflags=flags)


class WorkerProcess:
    """Um interpretador externo com o worker carregado; um pedido de cada vez."""

    def __init__(self, interp: Path, cwd: Path, script: Path | None = None):
        self.interp = interp
        self.cwd = cwd
        self.script = script  # outro worker com o mesmo protocolo (ex.: stubs/_describe27.py)
        self.proc: subprocess.Popen | None = None
        self._q: queue.Queue = queue.Queue()
        self.restarts = 0

    def _reader(self, proc: subprocess.Popen, q: queue.Queue) -> None:
        try:
            for line in proc.stdout:
                q.put(line)
        except (OSError, ValueError):
            pass
        q.put(None)

    def start(self) -> None:
        self._q = queue.Queue()
        self.proc = _popen(self.interp, self.cwd, self.script)
        threading.Thread(target=self._reader, args=(self.proc, self._q), daemon=True).start()

    def kill(self) -> None:
        p, self.proc = self.proc, None
        if p is None:
            return
        try:
            p.kill()
            p.wait(timeout=10)
        except (OSError, subprocess.TimeoutExpired):
            pass
        for stream in (p.stdin, p.stdout):
            try:
                stream.close()
            except (OSError, AttributeError):
                pass

    def request(self, obj: dict, timeout: float) -> dict:
        if self.proc is None or self.proc.poll() is not None:
            if self.proc is not None:
                self.restarts += 1
            self.kill()
            self.start()
        try:
            self.proc.stdin.write((json.dumps(obj) + "\n").encode("ascii"))
            self.proc.stdin.flush()
        except OSError as exc:
            code = self.proc.poll()
            self.kill()
            raise WorkerCrashed(f"worker inacessivel ({exc}; codigo {code})") from exc
        try:
            line = self._q.get(timeout=timeout)
        except queue.Empty:
            self.kill()
            raise WorkerTimeout(f"tempo limite de {timeout:.0f} s excedido") from None
        if line is None:
            code = self.proc.wait() if self.proc else None
            self.kill()
            raise WorkerCrashed(f"o worker terminou inesperadamente (codigo {code})")
        try:
            return json.loads(line.decode("utf-8", "replace"))
        except ValueError as exc:
            self.kill()
            raise WorkerCrashed(f"resposta invalida do worker: {exc}") from exc

    def close(self) -> None:
        p = self.proc
        if p is None:
            return
        try:
            if p.poll() is None:
                p.stdin.write(b'{"op":"quit"}\n')
                p.stdin.flush()
                p.wait(timeout=5)
        except (OSError, subprocess.TimeoutExpired, ValueError):
            pass
        self.kill()


class WorkerPool:
    """Conjunto de workers para um interpretador; arranque preguicoso."""

    def __init__(self, interp: Interpreter, size: int, cwd: Path, script: Path | None = None):
        self.interp = interp
        self.size = max(1, size)
        self.cwd = cwd
        self.script = script
        self._idle: queue.LifoQueue = queue.LifoQueue()
        self._created = 0
        self._all: list[WorkerProcess] = []
        self._lock = threading.Lock()
        self._closed = False

    def _acquire(self) -> WorkerProcess:
        try:
            return self._idle.get_nowait()
        except queue.Empty:
            pass
        with self._lock:
            if self._closed:
                raise BackendError("pool fechada")
            if self._created < self.size:
                self._created += 1
                w = WorkerProcess(self.interp.path, self.cwd, self.script)
                self._all.append(w)
                return w
        return self._idle.get()

    def call(self, obj: dict, timeout: float) -> dict:
        w = self._acquire()
        try:
            return w.request(obj, timeout)
        finally:
            self._idle.put(w)

    @property
    def restarts(self) -> int:
        return sum(w.restarts for w in self._all)

    def close(self) -> None:
        with self._lock:
            self._closed = True
            workers = list(self._all)
        for w in workers:
            w.close()


# ------------------------------------------------------------- interpretadores

def probe_interpreter(role: str, path: Path, cwd: Path | None = None) -> Interpreter:
    info = Interpreter(role, Path(path))
    if not Path(path).is_file():
        info.error = "ficheiro nao encontrado"
        return info
    w = WorkerProcess(Path(path), Path(cwd or Path.cwd()))
    try:
        resp = w.request({"op": "hello"}, HELLO_TIMEOUT)
    except (WorkerTimeout, WorkerCrashed, OSError) as exc:
        info.error = f"o interpretador nao arrancou o worker: {exc}"
        return info
    finally:
        w.close()
    info.python = resp.get("python", "")
    info.uncompyle6 = resp.get("uncompyle6", "")
    info.xdis = resp.get("xdis", "")
    if resp.get("error"):
        info.error = resp["error"]
    elif role == "py27" and not info.python.startswith("2.7"):
        info.error = f"esperado Python 2.7, encontrado {info.python}"
    elif role == "py3" and not info.python.startswith("3."):
        info.error = f"esperado Python 3, encontrado {info.python}"
    return info


def _py_launcher(tag: str) -> Path | None:
    exe = shutil.which("py")
    if not exe:
        return None
    try:
        out = subprocess.run([exe, tag, "-c", "import sys; print(sys.executable)"], capture_output=True,
                             timeout=20, creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
    except (OSError, subprocess.TimeoutExpired):
        return None
    if out.returncode != 0:
        return None
    p = Path(out.stdout.decode("utf-8", "replace").strip())
    return p if p.is_file() else None


def python27_candidates(configured: Path | None = None) -> list[Path]:
    """Ordem: configuracao, WOT_EXTRACTOR_PY27, lancador `py -2.7`, pastas habituais."""
    seen: list[Path] = []

    def add(p):
        if p and Path(p) not in seen:
            seen.append(Path(p))

    add(configured)
    add(os.environ.get("WOT_EXTRACTOR_PY27") or None)
    add(_py_launcher("-2.7"))
    local = os.environ.get("LOCALAPPDATA")
    if local:
        add(Path(local) / "Programs" / "Python" / "Python27" / "python.exe")
    if os.name == "nt":
        for letter in "CDEFGH":
            for sub in ("Python27", r"Program Files\Python27", r"Program Files (x86)\Python27"):
                p = Path(f"{letter}:\\") / sub / "python.exe"
                if p.is_file():
                    add(p)
    return [p for p in seen if p.is_file()] + [p for p in seen if not p.is_file() and p == configured]


@dataclass
class Toolchain:
    py27: Interpreter | None = None
    py3: Interpreter | None = None
    rejected: list[Interpreter] = field(default_factory=list)

    def for_backend(self, name: str) -> Interpreter | None:
        role = BACKENDS[name].interpreter
        return self.py27 if role == "py27" else self.py3

    def to_dict(self) -> dict:
        return {"python27": self.py27.to_dict() if self.py27 else None,
                "python3": self.py3.to_dict() if self.py3 else None,
                "rejected": [i.to_dict() for i in self.rejected]}


def find_toolchain(python27: Path | None = None, python3: Path | None = None, need_py3: bool = True,
                   cwd: Path | None = None) -> Toolchain:
    tc = Toolchain()
    for cand in python27_candidates(python27):
        info = probe_interpreter("py27", cand, cwd)
        if info.ok:
            tc.py27 = info
            break
        tc.rejected.append(info)
    if need_py3:
        info = probe_interpreter("py3", Path(python3 or sys.executable), cwd)
        if info.ok:
            tc.py3 = info
        else:
            tc.rejected.append(info)
    return tc
