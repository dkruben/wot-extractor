"""Motor do comando `stubs`: stubs Python (.pyi) em __stubs/ para autocompletar nas IDEs.

Fontes, por ordem de confianca:
  1. o codigo descompilado (fase C) ou original (.py de mods): arvore sintatica lida pelo Python 2.7;
  2. o bytecode, quando a descompilacao falhou ou o codigo nao e valido: nomes de classes/funcoes/parametros;
  3. modulos nativos (BigWorld, ResMgr, ...): so os membros que o codigo usa, sem assinaturas.

  __stubs/<modulo>.pyi | <pacote>/__init__.pyi    um por modulo importavel (scripts/client|common|client_common)
  __stubs/stubs_index.json                       modulo -> origem, estado, modo
  __stubs/README.md                              como usar no VS Code/Pylance

Estados (campo "stubs" de cada .pyc/.py no manifesto):
  success  a partir do codigo, sem omissoes
  partial  a partir do bytecode, ou com nomes omitidos (palavras reservadas em Python 3), ou stub regenerado
           sem docstrings
  failed   sem descricao (codigo e bytecode ilegiveis) ou stub invalido
"""

from __future__ import annotations

import base64
import fnmatch
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .. import TOOL_NAME, __version__
from ..config import Config
from ..decompile.backends import Interpreter, WorkerPool, WorkerProcess, python27_candidates
from ..extract.manifest import ManifestError, StateLock, load_manifest
from ..extract.writer import long_path, remove_file, save_json_atomic, write_atomic
from ..logutil import get_logger
from ..safety import resolve_within
from .render import RENDER_VERSION, render_module, render_native

log = get_logger("stubs")

STUBS_DIR = "__stubs"
WORKER = Path(__file__).with_name("_describe27.py")
DESCRIBER_VERSION = 2
OK_ENTRY = frozenset({"extracted", "unchanged"})
DESC_DIR = "stubs_desc"
MAX_LISTED = 2000
_SCRIPTS = re.compile(r"(?:^|/)scripts/(client|client_common|common)/(.+)$")
_LIB_PREFIXES = ("Lib/plat-win/", "Lib/lib-tk/", "Lib/site-packages/", "Lib/")
ROOT_ORDER = {"client": 0, "client_common": 1, "common": 2}


@dataclass
class StubOptions:
    jobs: int = 4
    timeout: float = 120.0
    stdlib: bool = False
    natives: bool = True
    force: bool = False
    globs: tuple[str, ...] = ()
    trees: frozenset[str] = frozenset()
    limit: int = 0
    dry_run: bool = False


@dataclass
class StubResult:
    realm: str
    out_dir: Path
    started: str = ""
    elapsed: float = 0.0
    candidates: int = 0
    selected: int = 0
    described: int = 0
    reused: int = 0
    limited: int = 0
    totals: Counter = field(default_factory=Counter)
    modes: Counter = field(default_factory=Counter)
    written: int = 0
    unchanged_files: int = 0
    removed: int = 0
    classes: int = 0
    functions: int = 0
    stdlib_skipped: int = 0
    shadowed: int = 0
    natives: list[str] = field(default_factory=list)
    problems: list[dict] = field(default_factory=list)
    interpreter: str = ""
    interrupted: bool = False
    dry_run: bool = False
    manifest_path: Path | None = None
    report_path: Path | None = None
    stubs_dir: Path | None = None

    def to_report(self) -> dict:
        return {
            "tool": TOOL_NAME, "tool_version": __version__, "realm": self.realm, "started": self.started,
            "elapsed_s": round(self.elapsed, 2), "dry_run": self.dry_run, "interrupted": self.interrupted,
            "interpreter": self.interpreter or None,
            "counts": {"candidates": self.candidates, "selected": self.selected, "described_now": self.described,
                       "descriptions_reused": self.reused, "not_processed_due_to_limit": self.limited,
                       "totals": dict(self.totals), "modes": dict(self.modes), "files_written": self.written,
                       "files_unchanged": self.unchanged_files, "stale_removed": self.removed,
                       "classes": self.classes, "functions": self.functions,
                       "stdlib_modules_skipped": self.stdlib_skipped, "shadowed_modules": self.shadowed,
                       "native_modules": len(self.natives)},
            "native_modules": self.natives,
            "not_fully_generated": self.problems[:MAX_LISTED],
            "note": "Stubs so com informacao verificada no codigo; tipos desconhecidos = Any.",
        }


# ------------------------------------------------------------------ modulos

def module_of(virtual: str) -> tuple[str, bool, str, bool] | None:
    """(modulo, e pacote, raiz scripts/<x>, e da biblioteca padrao) a partir do caminho virtual."""
    m = _SCRIPTS.search(virtual)
    if not m:
        return None
    root, rel = m.group(1), m.group(2)
    stdlib = False
    for p in _LIB_PREFIXES:
        if rel.startswith(p):
            rel = rel[len(p):]
            stdlib = True
            break
    for ext in (".pyc", ".pyo", ".py"):
        if rel.endswith(ext):
            rel = rel[: -len(ext)]
            break
    else:
        return None
    parts = rel.split("/")
    pkg = parts[-1] == "__init__"
    if pkg:
        parts = parts[:-1]
    if not parts or not all(p.isidentifier() for p in parts):
        return None
    return ".".join(parts), pkg, root, stdlib


def stub_rel(module: str, pkg: bool) -> str:
    parts = module.split(".")
    return f"{STUBS_DIR}/{'/'.join(parts)}/__init__.pyi" if pkg else f"{STUBS_DIR}/{'/'.join(parts)}.pyi"


def find_python27(configured: Path | None, cwd: Path) -> tuple[Interpreter | None, str]:
    for cand in python27_candidates(configured):
        w = WorkerProcess(cand, cwd, WORKER)
        try:
            r = w.request({"op": "hello"}, 30)
            if r.get("ok") and r.get("py2"):
                info = Interpreter("py27", cand)
                return info, f"Python {r.get('version')} ({cand})"
        except Exception:  # noqa: BLE001 - candidato invalido
            pass
        finally:
            w.close()
    return None, "Python 2.7 nao encontrado (indique-o em [decompile] python27)"


def _selected(rec: dict, key: str, opts: StubOptions) -> bool:
    if opts.trees and rec.get("tree") not in opts.trees:
        return False
    if opts.globs:
        v = rec.get("virtual", "")
        return any(fnmatch.fnmatchcase(v, g) or fnmatch.fnmatchcase(key, g) for g in opts.globs)
    return True


def _input_sig(rec: dict) -> str:
    d = rec.get("decompiled") or {}
    return f"{rec.get('sha256')}/{d.get('sha256') if d.get('status') in ('success', 'partial') else '-'}/d{DESCRIBER_VERSION}"


# ------------------------------------------------------------------ execucao

def run_stubs(cfg: Config, realm: str, options: StubOptions | None = None, progress=None,
              interp: Interpreter | None = None, interp_label: str = "") -> StubResult:
    opts = options or StubOptions()
    t0 = time.perf_counter()
    out_dir = cfg.realm_output_dir(realm)
    manifest_path = out_dir / "manifest.json"
    res = StubResult(realm=realm, out_dir=out_dir, dry_run=opts.dry_run, interpreter=interp_label,
                     started=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    if not manifest_path.is_file():
        raise ManifestError(f"{manifest_path} nao existe: corra primeiro 'extract --realm {realm}'")
    if opts.dry_run:
        return _run(cfg, realm, opts, res, interp, manifest_path, progress, t0)
    with StateLock(out_dir):
        return _run(cfg, realm, opts, res, interp, manifest_path, progress, t0)


def _collect(entries: dict, opts: StubOptions, res: StubResult) -> dict[str, dict]:
    """modulo -> {key, pkg, root, source(rel), pyc(rel)}; o ficheiro efetivo e a raiz mais prioritaria."""
    mods: dict[str, dict] = {}
    for key, rec in sorted(entries.items()):
        cat = rec.get("category")
        if cat not in ("python_bytecode", "python_source") or rec.get("status") not in OK_ENTRY:
            continue
        info = module_of(rec.get("virtual") or "")
        if not info:
            continue
        res.candidates += 1
        module, pkg, root, stdlib = info
        if stdlib and not opts.stdlib:
            res.stdlib_skipped += 1
            continue
        if rec.get("overridden_by") or not _selected(rec, key, opts):
            continue
        d = rec.get("decompiled") or {}
        src = d.get("output") if cat == "python_bytecode" and d.get("status") in ("success", "partial") else (
            f"sources/{key}" if cat == "python_source" else None)
        item = {"key": key, "module": module, "pkg": pkg, "root": root, "source": src,
                "pyc": f"sources/{key}" if cat == "python_bytecode" else None,
                "decompile_status": d.get("status"), "sig": _input_sig(rec)}
        prev = mods.get(module)
        if prev is not None:
            res.shadowed += 1
            # pacote > modulo com o mesmo nome; depois scripts/client > client_common > common; depois .py > .pyc
            better = (item["pkg"], -ROOT_ORDER[item["root"]], item["source"] is not None) > \
                     (prev["pkg"], -ROOT_ORDER[prev["root"]], prev["source"] is not None)
            if not better:
                continue
        mods[module] = item
    return mods


def _run(cfg, realm, opts, res, interp, manifest_path, progress, t0) -> StubResult:
    out_dir = res.out_dir
    manifest = load_manifest(manifest_path)
    if manifest.get("realm") != realm:
        raise ManifestError(f"{manifest_path} pertence ao realm {manifest.get('realm')}, nao a {realm}")
    entries: dict[str, dict] = manifest["entries"]
    state_dir = out_dir / ".state"
    mods = _collect(entries, opts, res)
    res.selected = len(mods)
    desc_dir = state_dir / DESC_DIR

    # nada mudou desde a ultima execucao (mesmos modulos, entradas e versoes): nao ha nada a refazer
    h = hashlib.sha1(f"d{DESCRIBER_VERSION}/r{RENDER_VERSION}/{opts.natives}/{opts.stdlib}/{opts.globs}/"
                     f"{sorted(opts.trees)}".encode())
    for module in sorted(mods):
        h.update(f"{module}={mods[module]['sig']};".encode())
    ctx_sig = h.hexdigest()
    prev = manifest.get("stubs") or {}
    if not opts.force and not opts.limit and prev.get("ctx_sig") == ctx_sig and all(
            os.path.exists(long_path(out_dir / rel)) for rel in prev.get("outputs", [])[:: max(1, len(mods) // 200)]):
        res.reused = len(mods)
        res.totals = Counter(prev.get("counts", {}))
        res.natives = list(prev.get("natives", []))
        res.modes = Counter(prev.get("modes", {}))
        res.classes, res.functions = prev.get("classes", 0), prev.get("functions", 0)
        res.unchanged_files = len(prev.get("outputs", []))
        res.stubs_dir = out_dir / STUBS_DIR
        res.report_path = out_dir / "stubs_report.json"
        res.manifest_path = manifest_path
        readme = _readme(res, len(prev.get("outputs", []))).encode("utf-8")  # texto pode mudar entre versoes
        try:
            same = Path(long_path(out_dir / STUBS_DIR / "README.md")).read_bytes() == readme
        except OSError:
            same = False
        if not same and not opts.dry_run:
            write_atomic(out_dir / STUBS_DIR / "README.md", readme)
        res.elapsed = time.perf_counter() - t0
        return res

    def desc_path(key: str) -> Path:
        return resolve_within(desc_dir, key + ".json")

    todo, cached = [], {}
    for module, item in mods.items():
        if not opts.force:
            try:
                d = json.loads(Path(long_path(desc_path(item["key"]))).read_text(encoding="utf-8"))
                if d.get("sig") == item["sig"]:
                    cached[module] = d["desc"]
                    continue
            except (OSError, ValueError):
                pass
        todo.append(module)
    if opts.limit and len(todo) > opts.limit:
        res.limited = len(todo) - opts.limit
        todo = sorted(todo)[:opts.limit]
    res.reused = len(cached)
    if opts.dry_run:
        res.described = len(todo)
        res.elapsed = time.perf_counter() - t0
        return res
    if todo and interp is None:
        raise ManifestError("os stubs precisam do Python 2.7 (o codigo do jogo e Python 2): " + (res.interpreter or
                                                                                                "nao encontrado"))
    descs: dict[str, dict] = dict(cached)
    known = sorted({m.split(".")[0] for m in mods} | {m.split(".")[0] for m in _all_modules(entries)})
    pool = WorkerPool(interp, opts.jobs, state_dir, WORKER) if todo else None
    done = 0
    try:
        if pool is not None:
            def describe(module: str) -> tuple[str, dict]:
                item = mods[module]
                # a lista de modulos com codigo vai em cada pedido (sobrevive a reinicios do worker)
                req = {"op": "describe", "id": 1, "name": item["source"] or item["pyc"], "known": known}
                for k in ("source", "pyc"):
                    if item[k]:
                        try:
                            with open(long_path(out_dir / item[k]), "rb") as fh:
                                req[k] = base64.b64encode(fh.read()).decode("ascii")
                        except OSError:
                            pass
                try:
                    r = pool.call(req, opts.timeout)
                except Exception as exc:  # noqa: BLE001 - timeout/crash do worker
                    r = {"ok": False, "error": f"{type(exc).__name__}: {exc}"}
                return module, r

            with ThreadPoolExecutor(max_workers=max(1, opts.jobs)) as ex:
                try:
                    for module, r in ex.map(describe, todo):
                        item = mods[module]
                        desc = r if r.get("ok") else {"ok": False, "error": r.get("error")}
                        descs[module] = desc
                        write_atomic(desc_path(item["key"]),
                                     json.dumps({"sig": item["sig"], "desc": desc}, ensure_ascii=False,
                                                separators=(",", ":")).encode("utf-8"))
                        done += 1
                        res.described += 1
                        if progress:
                            progress(done, len(todo), Counter({"descritos": done}))
                except KeyboardInterrupt:
                    res.interrupted = True
                    ex.shutdown(wait=False, cancel_futures=True)
    finally:
        if pool is not None:
            pool.close()
    if res.interrupted:
        res.elapsed = time.perf_counter() - t0
        return res

    stdlib_names: set[str] = set()
    native_usage: dict[str, dict] = {}
    if opts.natives and interp is not None:
        native_usage = _native_usage(descs, set(known), mods, set(_all_modules(entries)))
        if native_usage:
            w = WorkerProcess(interp.path, state_dir, WORKER)
            try:
                r = w.request({"op": "stdlib", "names": sorted(native_usage)}, opts.timeout)
                stdlib_names = set(r.get("stdlib", []))
            finally:
                w.close()
        # biblioteca padrao do 2.7 e tambem a do Python 3 (importada em blocos try de compatibilidade)
        py3_std = set(getattr(sys, "stdlib_module_names", ()))
        native_usage = {k: v for k, v in native_usage.items() if k not in stdlib_names and k not in py3_std}

    outputs = _write_all(out_dir, manifest, entries, mods, descs, native_usage, res)
    now = datetime.now(timezone.utc)
    manifest["stubs"] = {"date": now.isoformat(timespec="seconds"), "interpreter": res.interpreter or None,
                         "counts": dict(res.totals), "natives": res.natives, "modes": dict(res.modes),
                         "classes": res.classes, "functions": res.functions,
                         "tool_sig": f"d{DESCRIBER_VERSION}/r{RENDER_VERSION}", "outputs": outputs,
                         "ctx_sig": ctx_sig if not res.interrupted and not opts.limit else None}
    manifest.setdefault("tool_versions", {})["stubs"] = f"d{DESCRIBER_VERSION}/r{RENDER_VERSION}"
    write_atomic(state_dir / "manifest.prev.json", manifest_path.read_bytes())
    save_json_atomic(manifest_path, manifest, indent=None)
    res.manifest_path = manifest_path
    res.elapsed = time.perf_counter() - t0
    report = res.to_report()
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    save_json_atomic(state_dir / "reports" / f"stubs_{stamp}.json", report)
    save_json_atomic(out_dir / "stubs_report.json", report)
    res.report_path = out_dir / "stubs_report.json"
    res.stubs_dir = out_dir / STUBS_DIR
    return res


def _all_modules(entries: dict) -> list[str]:
    out = []
    for rec in entries.values():
        if rec.get("category") in ("python_bytecode", "python_source"):
            info = module_of(rec.get("virtual") or "")
            if info:
                out.append(info[0])
    return out


def _native_usage(descs: dict, known: set[str], mods: dict, all_modules: set[str]) -> dict[str, dict]:
    usage: dict[str, dict] = {}
    files: Counter = Counter()
    for module, desc in descs.items():
        if not desc.get("ok"):
            continue
        item = mods.get(module) or {}
        package = module if item.get("pkg") else module.rpartition(".")[0]
        relative_ok = package and "absolute_import" not in (desc.get("future") or [])

        def sibling(name: str) -> bool:  # import relativo implicito do Python 2: <pacote>.<nome> existe
            return bool(relative_ok) and f"{package}.{name.split('.')[0]}" in all_modules

        seen = set()
        for mod, members in (desc.get("native_usage") or {}).items():
            top = mod.split(".")[0]
            if top in known or "." in mod or sibling(mod):
                continue
            seen.add(mod)
            u = usage.setdefault(mod, {})
            for name, (uses, calls, mn, mx, kws) in members.items():
                m = u.setdefault(name, {"uses": 0, "calls": 0, "min": None, "max": None, "kw": set(), "imported": 0})
                m["uses"] += uses
                m["calls"] += calls
                if mn is not None:
                    m["min"] = mn if m["min"] is None else min(m["min"], mn)
                    m["max"] = mx if m["max"] is None else max(m["max"], mx)
                m["kw"].update(kws)
        for mod, names in (desc.get("native_from") or {}).items():
            if mod.split(".")[0] in known or "." in mod or sibling(mod):
                continue
            seen.add(mod)
            u = usage.setdefault(mod, {})
            for name in names:
                m = u.setdefault(name, {"uses": 0, "calls": 0, "min": None, "max": None, "kw": set(), "imported": 0})
                m["imported"] += 1
        for mod in seen:
            files[mod] += 1
    for mod, u in usage.items():
        u["__files__"] = files[mod]
    return usage


def _write_all(out_dir: Path, manifest: dict, entries: dict, mods: dict, descs: dict, natives: dict,
               res: StubResult) -> list[str]:
    all_modules = set(_all_modules(entries)) | set(natives)
    produced: set[str] = set()
    index = {}

    def write_if_changed(rel: str, text: str) -> None:
        path = out_dir / rel
        data = text.encode("utf-8")
        try:
            if Path(long_path(path)).read_bytes() == data:
                res.unchanged_files += 1
                produced.add(rel)
                return
        except OSError:
            pass
        write_atomic(path, data)
        res.written += 1
        produced.add(rel)

    for module, item in sorted(mods.items()):
        desc = descs.get(module) or {"ok": False, "error": "sem descricao"}
        rel = stub_rel(module, item["pkg"])
        source = item["source"] or item["pyc"]
        rec: dict = {"module": module, "output": rel, "input_sig": item["sig"], "tool": f"r{RENDER_VERSION}"}
        if desc.get("ok"):
            text, stats = render_module(desc, module, item["pkg"], source, all_modules.__contains__)
            mode = desc.get("mode")
            problems = []
            if mode == "bytecode":
                problems.append("gerado do bytecode" + (f" ({desc['ast_error']})" if desc.get("ast_error") else
                                                        " (sem codigo descompilado)"))
            if stats["omitted"]:
                problems.append(f"{len(stats['omitted'])} nome(s) omitido(s)")
            if stats["error"]:
                problems.append(stats["error"])
            status = "failed" if stats["failed"] else ("partial" if problems else "success")
            rec.update(status=status, mode=mode, classes=stats["classes"], functions=stats["functions"])
            if problems:
                rec["error"] = "; ".join(problems)
            res.classes += stats["classes"]
            res.functions += stats["functions"]
            res.modes[mode] += 1
        else:
            text = None
            rec.update(status="failed", error=desc.get("error") or "sem descricao")
        if text is not None:
            write_if_changed(rel, text)
        res.totals[rec["status"]] += 1
        if rec["status"] != "success":
            res.problems.append({"key": item["key"], "module": module, "status": rec["status"],
                                 "error": rec.get("error", "")})
        entries[item["key"]]["stubs"] = rec
        index[module] = {"source": source, "key": item["key"], "status": rec["status"], "mode": rec.get("mode"),
                         "stub": rel}

    for mod, members in sorted(natives.items()):
        files = members.pop("__files__", 0)
        if not mod.isidentifier():
            continue
        rel = f"{STUBS_DIR}/{mod}.pyi"
        if rel in produced:
            continue
        write_if_changed(rel, render_native(mod, members, files))
        res.natives.append(mod)
        index[mod] = {"source": None, "status": "native", "stub": rel, "members": len(members), "files": files}

    # stubs antigos que ja nao correspondem a nenhum modulo
    previous = set((manifest.get("stubs") or {}).get("outputs", []))
    for rel in sorted(previous - produced):
        if rel.startswith(STUBS_DIR + "/") and rel.endswith(".pyi"):
            res.removed += remove_file(resolve_within(out_dir, rel))
    save_json_atomic(out_dir / STUBS_DIR / "stubs_index.json",
                     {"tool": TOOL_NAME, "tool_version": __version__,
                      "note": "Stubs so com informacao verificada; 'native' = modulo C++ sem codigo (membros usados).",
                      "modules": index})
    write_atomic(out_dir / STUBS_DIR / "README.md", _readme(res, len(index)).encode("utf-8"))
    return sorted(produced)


def _readme(res: StubResult, n: int) -> str:
    return "\n".join([
        "# World of Tanks Python stubs (.pyi)",
        "",
        "Generated by wot-extractor from the decompiled code (phase C), the original `.py` files and, when the",
        "decompilation failed, the bytecode. **They only contain information verified in the code**: names,",
        "parameters, literal default values, docstrings, assigned attributes and the type of literal values.",
        "`Any` means *unknown*. Modules without code in the client (engine natives) only list the members the Python",
        "code uses, with `*args/**kwargs`, and end with `__getattr__` (incomplete list).",
        "",
        "Usage in VS Code (Pylance): in the `settings.json` of your mod folder,",
        "",
        "```json",
        '{ "python.analysis.stubPath": "<path>/wot_src_EU/__stubs" }',
        "```",
        "",
        "The game code is Python 2.7; Pylance analyzes as Python 3, so warnings about Python 2 syntax may show",
        "up in your mod code — the stubs themselves are valid Python 3 (verified).",
        "",
        f"Modules: {n} (without code: {len(res.natives)}). Detailed state in `stubs_index.json`.",
        "",
    ])
