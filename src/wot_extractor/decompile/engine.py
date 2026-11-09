"""Motor de descompilacao: le os .pyc ja extraidos (sources/), descompila-os
nos workers externos, valida o codigo e escreve o .py ao lado do .pyc.

Trabalha so sobre wot_src_<R>: nao precisa da instalacao do jogo. E
incremental (pelo SHA-256 do .pyc e pela cadeia de descompiladores), paralelo
e retomavel (journal), e nunca troca um resultado melhor por um pior.

Estados (por .pyc, no campo "decompiled" do manifesto):
  success      descompilado e validado pelo parser de Python 2.7, sem seccoes falhadas
  partial      ha codigo, mas com seccoes falhadas, erro do descompilador ou sintaxe invalida
  failed       nenhum codigo recuperado (erro, tempo limite, worker terminado)
  unsupported  versao de bytecode sem descompilador validado
O estado "unchanged" e apenas da execucao: o resultado anterior e reaproveitado.
"""

from __future__ import annotations

import base64
import fnmatch
import hashlib
import time
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .. import TOOL_NAME, __version__
from ..config import Config
from ..extract.manifest import Journal, ManifestError, StateLock, load_manifest
from ..extract.writer import existing_size, long_path, remove_file, save_json_atomic, write_atomic
from ..logutil import get_logger
from ..safety import resolve_within
from .backends import (BACKENDS, DEFAULT_CHAIN, BackendError, Toolchain, WorkerCrashed, WorkerPool,
                       WorkerTimeout, find_toolchain)

log = get_logger("decompile")

RANK = {"success": 3, "partial": 2, "failed": 1}
OK_ENTRY = frozenset({"extracted", "unchanged"})
ATTEMPTS_DIR = Path(".state") / "decompile" / "attempts"
JOURNAL_NAME = "decompile_journal.jsonl"
MAX_LISTED = 2000
DEFAULT_TIMEOUT = 120.0


@dataclass
class DecompileOptions:
    chain: tuple[str, ...] = DEFAULT_CHAIN
    jobs: int = 4
    timeout: float = DEFAULT_TIMEOUT
    force: bool = False
    retry: bool = False  # voltar a tentar partial/failed mesmo com a mesma cadeia
    globs: tuple[str, ...] = ()  # fnmatch sobre o caminho virtual ou a chave
    trees: frozenset[str] = frozenset()
    limit: int = 0  # 0 = sem limite (util para amostras)
    dry_run: bool = False
    python27: Path | None = None
    python3: Path | None = None


@dataclass
class DecompileResult:
    realm: str
    out_dir: Path
    started: str = ""
    elapsed: float = 0.0
    candidates: int = 0
    selected: int = 0
    to_process: int = 0
    limited: int = 0
    resumed: int = 0
    processed: Counter = field(default_factory=Counter)  # estado obtido nesta execucao
    unchanged: Counter = field(default_factory=Counter)  # estado reaproveitado
    totals: Counter = field(default_factory=Counter)  # estado final de todos os selecionados
    unsupported: list[dict] = field(default_factory=list)
    failures: list[dict] = field(default_factory=list)
    partials: list[dict] = field(default_factory=list)
    kept_previous: int = 0
    fallback_used: int = 0
    attempts_saved: int = 0
    stale_removed: int = 0
    timeouts: int = 0
    crashes: int = 0
    worker_restarts: int = 0
    lines_recovered: int = 0
    chain: list[dict] = field(default_factory=list)
    toolchain: dict = field(default_factory=dict)
    interrupted: bool = False
    dry_run: bool = False
    manifest_path: Path | None = None
    report_path: Path | None = None

    def to_report(self) -> dict:
        return {
            "tool": TOOL_NAME, "tool_version": __version__, "realm": self.realm,
            "started": self.started, "elapsed_s": round(self.elapsed, 2),
            "dry_run": self.dry_run, "interrupted": self.interrupted,
            "chain": self.chain, "toolchain": self.toolchain,
            "counts": {
                "candidates": self.candidates, "selected": self.selected, "to_process": self.to_process,
                "not_processed_due_to_limit": self.limited, "resumed_from_journal": self.resumed,
                "processed": dict(self.processed), "unchanged": dict(self.unchanged), "totals": dict(self.totals),
                "kept_previous": self.kept_previous, "fallback_used": self.fallback_used,
                "attempts_saved": self.attempts_saved, "stale_removed": self.stale_removed,
                "timeouts": self.timeouts, "worker_crashes": self.crashes, "worker_restarts": self.worker_restarts,
                "code_lines_recovered_now": self.lines_recovered,
            },
            "failed": self.failures[:MAX_LISTED],
            "partial": self.partials[:MAX_LISTED],
            "unsupported": self.unsupported[:MAX_LISTED],
        }


# ------------------------------------------------------------------- funcoes puras

def output_rel(key: str, entries: dict) -> str:
    """Caminho do .py (relativo a wot_src_<R>) para o .pyc `key`: x.pyc -> x.py.
    Nunca coincide com um .py original extraido do jogo (passa a x.decompiled.py)."""
    rel = key[:-1] if key.endswith((".pyc", ".pyo")) else key + ".py"
    if rel in entries:
        rel = rel[:-3] + ".decompiled.py"
    return "sources/" + rel


def attempt_rel(key: str, backend: str) -> Path:
    return ATTEMPTS_DIR / backend / (key[:-1] if key.endswith((".pyc", ".pyo")) else key + ".py")


def header_line(key: str, label: str) -> str:
    text = f"# wot-extractor: codigo DESCOMPILADO de sources/{key} ({label}) - nao e o codigo original\n"
    return text.encode("ascii", "backslashreplace").decode("ascii")


def classify(resp: dict) -> tuple[str, str, str]:
    """(estado, validacao, erro) para uma resposta do worker (com syntax_error ja preenchido)."""
    if resp.get("status") == "failed" or "source" not in resp:
        return "failed", "", resp.get("error") or "sem resposta do descompilador"
    error = resp.get("error") or ""
    code_lines = resp.get("code_lines", 0)
    syntax = resp.get("syntax_error")
    validation = "valid" if not syntax else f"invalid: {syntax}"
    if code_lines == 0 and error:
        return "failed", "", error
    problems = []
    if error:
        problems.append(f"descompilador: {error}")
    if resp.get("markers"):
        problems.append(f"{resp['markers']} seccao(oes) nao descompilada(s)")
    if syntax:
        problems.append(f"sintaxe: {syntax}")
    if problems:
        return "partial", validation, "; ".join(problems)
    return "success", validation, ""


def _footer(status: str, error: str) -> bytes:
    if status == "success":
        return b""
    msg = f"\n# wot-extractor: AVISO - descompilacao {status}: {error}\n"
    return msg.encode("ascii", "backslashreplace")


def _selected(rec: dict, key: str, opts: DecompileOptions) -> bool:
    if rec.get("category") != "python_bytecode" or rec.get("status") not in OK_ENTRY:
        return False
    if opts.trees and rec.get("tree") not in opts.trees:
        return False
    if opts.globs:
        v = rec.get("virtual", "")
        return any(fnmatch.fnmatchcase(v, g) or fnmatch.fnmatchcase(key, g) for g in opts.globs)
    return True


def _reusable(prev: dict | None, rec: dict, out_dir: Path, sig: list[str], opts: DecompileOptions) -> bool:
    if opts.force or not prev or prev.get("status") not in RANK:
        return False
    if prev.get("input_sha256") != rec.get("sha256"):
        return False
    if prev.get("output"):
        if existing_size(out_dir / prev["output"]) != prev.get("size"):
            return False
    elif prev["status"] != "failed":
        return False
    if prev["status"] == "success":
        return True
    return not opts.retry and prev.get("chain") == sig


# ------------------------------------------------------------------- execucao

class _Runner:
    def __init__(self, tc: Toolchain, chain: list[str], jobs: int, timeout: float, cwd: Path):
        self.tc = tc
        self.chain = chain
        self.timeout = timeout
        self.pools: dict[str, WorkerPool] = {}
        for name in chain:
            role = BACKENDS[name].interpreter
            if role not in self.pools:
                self.pools[role] = WorkerPool(tc.for_backend(name), jobs, cwd)
        if "py27" not in self.pools:  # validacao
            self.pools["py27"] = WorkerPool(tc.py27, jobs, cwd)

    def close(self) -> int:
        restarts = sum(p.restarts for p in self.pools.values())
        for p in self.pools.values():
            p.close()
        return restarts

    def _call(self, role: str, req: dict) -> dict:
        try:
            return self.pools[role].call(req, self.timeout)
        except WorkerTimeout as exc:
            return {"status": "failed", "error": str(exc), "timeout": True}
        except WorkerCrashed as exc:
            return {"status": "failed", "error": str(exc), "crash": True}

    def run(self, key: str, rec: dict, path: Path) -> tuple[str, dict | None, list[dict], str]:
        """Executado numa thread. Devolve (chave, melhor tentativa, tentativas, erro de leitura)."""
        try:
            with open(long_path(path), "rb") as fh:
                data = fh.read()
        except OSError as exc:
            return key, None, [], f"leitura do .pyc extraido: {exc}"
        if rec.get("sha256") and hashlib.sha256(data).hexdigest() != rec["sha256"]:
            return key, None, [], "o .pyc em sources/ nao corresponde ao manifesto (corra 'extract' de novo)"
        b64 = base64.b64encode(data).decode("ascii")
        attempts: list[dict] = []
        best = None
        for name in self.chain:
            spec = BACKENDS[name]
            interp = self.tc.for_backend(name)
            label = interp.label()
            t0 = time.perf_counter()
            resp = self._call(spec.interpreter, {"op": "decompile", "id": 1, "name": rec.get("virtual") or key,
                                                 "data": b64, "validate": spec.interpreter == "py27",
                                                 "header": header_line(key, label)})
            if "source" in resp and spec.interpreter != "py27":
                v = self._call("py27", {"op": "validate", "id": 2, "name": rec.get("virtual") or key,
                                        "source": resp["source"]})
                resp["syntax_error"] = v.get("syntax_error") if v.get("status") != "failed" else \
                    f"validacao impossivel: {v.get('error')}"
            status, validation, error = classify(resp)
            att = {"backend": name, "tool": label, "status": status, "validation": validation, "error": error,
                   "markers": resp.get("markers", 0), "code_lines": resp.get("code_lines", 0),
                   "cookie": resp.get("cookie"), "elapsed": round(time.perf_counter() - t0, 3),
                   "timeout": bool(resp.get("timeout")), "crash": bool(resp.get("crash"))}
            if "source" in resp and status != "failed":
                att["source"] = base64.b64decode(resp["source"])
            attempts.append(att)
            if best is None or RANK[status] > RANK[best["status"]]:
                best = att
            if status == "success":
                break
        return key, best, attempts, ""


def _chain_sig(tc: Toolchain, chain: list[str]) -> list[str]:
    return [f"{n}={tc.for_backend(n).label()}" for n in chain]


def run_decompile(cfg: Config, realm: str, options: DecompileOptions | None = None, progress=None,
                  toolchain: Toolchain | None = None) -> DecompileResult:
    opts = options or DecompileOptions()
    t0 = time.perf_counter()
    out_dir = cfg.realm_output_dir(realm)
    manifest_path = out_dir / "manifest.json"
    res = DecompileResult(realm=realm, out_dir=out_dir, dry_run=opts.dry_run,
                          started=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    if not manifest_path.is_file():
        raise ManifestError(f"{manifest_path} nao existe: corra primeiro 'extract --realm {realm}'")
    for name in opts.chain:
        if name not in BACKENDS:
            raise BackendError(f"descompilador desconhecido: {name}")

    tc = toolchain or find_toolchain(opts.python27, opts.python3,
                                     need_py3=any(BACKENDS[n].interpreter == "py3" for n in opts.chain),
                                     cwd=out_dir if out_dir.is_dir() else None)
    res.toolchain = tc.to_dict()
    if tc.py27 is None:
        raise BackendError("Python 2.7 com uncompyle6 nao encontrado (necessario para descompilar e validar "
                           "bytecode 2.7). Indique-o com --python27 ou [decompile] python27 no wot_extractor.toml.")
    chain = [n for n in opts.chain if tc.for_backend(n) is not None]
    for n in opts.chain:
        if n not in chain:
            log.warning("Descompilador %s indisponivel (interpretador em falta); a continuar sem ele.", n)
    if not chain:
        raise BackendError("nenhum descompilador disponivel")
    res.chain = [{"backend": n, "tool": tc.for_backend(n).label(), "path": str(tc.for_backend(n).path)} for n in chain]
    sig = _chain_sig(tc, chain)
    versions = set().union(*(BACKENDS[n].versions for n in chain))

    lock = StateLock(out_dir) if not opts.dry_run else None
    if lock:
        lock.__enter__()
    try:
        return _run_locked(cfg, realm, opts, res, tc, chain, sig, versions, manifest_path, progress, t0)
    finally:
        if lock:
            lock.__exit__(None, None, None)


def _run_locked(cfg, realm, opts, res, tc, chain, sig, versions, manifest_path, progress, t0) -> DecompileResult:
    out_dir = res.out_dir
    manifest = load_manifest(manifest_path)
    if manifest.get("realm") != realm:
        raise ManifestError(f"{manifest_path} pertence ao realm {manifest.get('realm')}, nao a {realm}")
    entries: dict[str, dict] = manifest["entries"]
    state_dir = out_dir / ".state"
    journal = Journal(state_dir / JOURNAL_NAME)
    resumed = {k: r.get("decompiled") for k, r in journal.load().items() if r.get("decompiled")}
    res.resumed = len(resumed)

    results: dict[str, dict] = {}  # chave -> novo registo "decompiled"
    todo: list[str] = []
    for key, rec in entries.items():
        if rec.get("category") == "python_bytecode" and rec.get("status") in OK_ENTRY:
            res.candidates += 1
        if not _selected(rec, key, opts):
            continue
        res.selected += 1
        ver = (rec.get("info") or {}).get("pyc_version", "?")
        if ver not in versions:
            results[key] = {"status": "unsupported", "bytecode": ver, "input_sha256": rec.get("sha256"),
                            "error": f"bytecode {ver}: sem descompilador validado para esta versao "
                                     f"(suportadas: {', '.join(sorted(versions))})"}
            res.unsupported.append({"key": key, "bytecode": ver})
            continue
        prev = resumed.get(key) or rec.get("decompiled")
        if _reusable(prev, rec, out_dir, sig, opts) or (
                rec.get("cleaned") and prev and prev.get("input_sha256") == rec.get("sha256")):
            res.unchanged[prev["status"]] += 1
            results[key] = prev
            continue
        todo.append(key)
    # os maiores primeiro: melhor distribuicao entre workers
    todo.sort(key=lambda k: -(entries[k].get("size") or 0))
    if opts.limit and len(todo) > opts.limit:
        res.limited = len(todo) - opts.limit
        todo = sorted(sorted(todo)[:opts.limit], key=lambda k: -(entries[k].get("size") or 0))
    res.to_process = len(todo)

    if opts.dry_run:
        res.elapsed = time.perf_counter() - t0
        return res

    runner = _Runner(tc, chain, opts.jobs, opts.timeout, state_dir)
    done = 0
    total = len(todo)

    def handle(key: str, best: dict | None, attempts: list[dict], read_error: str) -> None:
        rec = entries[key]
        prev = resumed.get(key) or rec.get("decompiled")
        out_rel = output_rel(key, entries)
        dest = resolve_within(out_dir, out_rel)
        if best is None:
            new = {"status": "failed", "error": read_error, "input_sha256": rec.get("sha256"), "chain": sig,
                   "attempts": []}
        else:
            new = {"status": best["status"], "backend": best["backend"], "tool": best["tool"],
                   "input_sha256": rec.get("sha256"), "chain": sig, "validation": best["validation"] or None,
                   "error": best["error"] or None, "markers": best["markers"] or None,
                   "code_lines": best["code_lines"], "elapsed": round(sum(a["elapsed"] for a in attempts), 3),
                   "attempts": [{k: a[k] for k in ("backend", "tool", "status", "error")} for a in attempts]}
            if best["backend"] != chain[0]:
                res.fallback_used += 1
        for a in attempts:
            res.timeouts += a["timeout"]
            res.crashes += a["crash"]

        keep_prev = (prev and prev.get("status") in RANK and prev.get("input_sha256") == rec.get("sha256")
                     and RANK[prev["status"]] > RANK[new["status"]]
                     and (not prev.get("output") or existing_size(out_dir / prev["output"]) == prev.get("size")))
        if keep_prev:
            kept = dict(prev)
            kept["kept_previous"] = True
            kept["last_attempts"] = new.get("attempts", [])
            new = kept
            res.kept_previous += 1
        elif best is not None and "source" in best:
            body = best["source"] + _footer(best["status"], best["error"])
            size, sha = write_atomic(dest, body)
            new.update(output=out_rel, size=size, sha256=sha)
            res.lines_recovered += best["code_lines"]
        else:
            # sem codigo: nao deixar um .py antigo (de outra versao do .pyc) a parecer atual
            if prev and prev.get("output") == out_rel and remove_file(dest):
                res.stale_removed += 1
        for a in attempts:
            if "source" in a and (a is not best or keep_prev):
                write_atomic(resolve_within(out_dir, attempt_rel(key, a["backend"]).as_posix()), a["source"])
                res.attempts_saved += 1
        new = {k: v for k, v in new.items() if v is not None}
        results[key] = new
        res.processed[new["status"] if not keep_prev else "kept_previous"] += 1
        journal.write({"key": key, "decompiled": new})

    try:
        with ThreadPoolExecutor(max_workers=max(1, opts.jobs), thread_name_prefix="decompile") as ex:
            inflight = set()
            it = iter(todo)
            try:
                while True:
                    while len(inflight) < max(1, opts.jobs) * 2:
                        key = next(it, None)
                        if key is None:
                            break
                        src = resolve_within(out_dir / "sources", key)
                        inflight.add(ex.submit(runner.run, key, entries[key], src))
                    if not inflight:
                        break
                    finished, inflight = wait(inflight, return_when=FIRST_COMPLETED)
                    for f in finished:
                        handle(*f.result())
                        done += 1
                    if progress:
                        progress(done, total, res.processed)
            except KeyboardInterrupt:
                res.interrupted = True
                for f in inflight:
                    f.cancel()
                runner.close()
                ex.shutdown(wait=True, cancel_futures=True)
    finally:
        res.worker_restarts = runner.close()
        journal.close()

    if res.interrupted:
        res.elapsed = time.perf_counter() - t0
        log.warning("Descompilacao interrompida: %d resultados no journal; volte a correr para retomar.", done)
        return res

    # ---- totais e listas (todos os selecionados, incluindo os reaproveitados)
    for key, d in sorted(results.items()):
        st = d["status"]
        res.totals[st] += 1
        if st == "failed":
            res.failures.append({"key": key, "error": d.get("error", "")})
        elif st == "partial":
            res.partials.append({"key": key, "error": d.get("error", ""), "output": d.get("output")})

    # ---- manifesto
    for key, d in results.items():
        entries[key]["decompiled"] = d
    overall = Counter()
    for rec in entries.values():
        if rec.get("category") == "python_bytecode" and rec.get("status") in OK_ENTRY:
            overall[(rec.get("decompiled") or {}).get("status", "not_processed")] += 1
    now = datetime.now(timezone.utc)
    manifest["decompile"] = {"date": now.isoformat(timespec="seconds"), "chain": res.chain,
                             "counts": dict(overall)}
    manifest.setdefault("tool_versions", {})["decompile"] = sig
    write_atomic(state_dir / "manifest.prev.json", manifest_path.read_bytes())
    save_json_atomic(manifest_path, manifest, indent=None)
    res.manifest_path = manifest_path
    res.elapsed = time.perf_counter() - t0
    report = res.to_report()
    report["manifest_counts"] = dict(overall)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    save_json_atomic(state_dir / "reports" / f"decompile_{stamp}.json", report)
    save_json_atomic(out_dir / "decompile_report.json", report)
    res.report_path = out_dir / "decompile_report.json"
    journal.remove()
    return res
