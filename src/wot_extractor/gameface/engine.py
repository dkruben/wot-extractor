"""Motor do comando `gameface`: recursos Gameface (HTML/CSS/JS, .unbound, TypeScript, assets) para
sources_gameface/.

  sources_gameface/js|css|html/<chave>   copias FORMATADAS dos ficheiros minificados (nao sao o original)
  sources_gameface/manifests/files/<chave>.json   analise de cada ficheiro (webpack, referencias...)
  sources_gameface/manifests/views/<R id>.json    cada view: ficheiros, dependencias, ligacoes ao Python
  sources_gameface/manifests/index.json           views, chunks, modulos webpack, .unbound, TypeScript
  sources_gameface/manifests/python_links.json    ligacoes PROVAVEIS view <-> Python/ViewModel
  sources_gameface/assets/index.json              imagens/fontes/json/... (ficam em sources/, nao duplicados)
  sources_gameface/VIEWS.md                       documentacao das views para desenvolvimento de mods

Estados (campo "gameface" de cada ficheiro no manifesto):
  success   lido e analisado; se minificado, formatado e verificado
  partial   analisado, mas a formatacao (ou a leitura do JS pelo lexer) falhou: so o original em sources/
  failed    nao foi possivel ler o ficheiro
"""

from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import posixpath
import shutil
import subprocess
import time
from collections import Counter
from concurrent.futures import FIRST_COMPLETED, ProcessPoolExecutor, wait
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from .. import TOOL_NAME, __version__
from ..config import Config
from ..extract.manifest import Journal, ManifestError, StateLock, load_manifest
from ..extract.writer import long_path, remove_tree, save_json_atomic, write_atomic
from ..formats.jsfmt import FORMATTER_VERSION
from ..logutil import get_logger
from ..safety import resolve_within
from . import pylinks
from .analyze import (ANALYZER_VERSION, GF_DIR, PROD, file_kind, outputs_of, process_file, prod_parts,
                      remove_outputs)

log = get_logger("gameface")

OK_ENTRY = frozenset({"extracted", "unchanged"})
JOURNAL_NAME = "gameface_journal.jsonl"
MAX_LISTED = 2000
LAYOUT_FILES = ("gui/gen_resources/gameface_layouts.json", "gui/gen_resources/unbound_layouts.json")


@dataclass
class GFOptions:
    jobs: int = 4
    format: bool = True
    use_node: bool = True
    links: bool = True
    force: bool = False
    retry: bool = False
    globs: tuple[str, ...] = ()
    trees: frozenset[str] = frozenset()
    limit: int = 0
    dry_run: bool = False


@dataclass
class GFResult:
    realm: str
    out_dir: Path
    started: str = ""
    elapsed: float = 0.0
    candidates: int = 0
    selected: int = 0
    to_process: int = 0
    limited: int = 0
    resumed: int = 0
    processed: Counter = field(default_factory=Counter)
    unchanged: Counter = field(default_factory=Counter)
    totals: Counter = field(default_factory=Counter)
    kinds: Counter = field(default_factory=Counter)
    formatted: int = 0
    node_checked: int = 0
    assets: int = 0
    views: int = 0
    links: Counter = field(default_factory=Counter)
    pyindex_cached: bool = False
    problems: list[dict] = field(default_factory=list)
    node: str = ""
    interrupted: bool = False
    dry_run: bool = False
    manifest_path: Path | None = None
    report_path: Path | None = None
    index_path: Path | None = None
    views_doc: Path | None = None

    def to_report(self) -> dict:
        return {
            "tool": TOOL_NAME, "tool_version": __version__, "realm": self.realm, "started": self.started,
            "elapsed_s": round(self.elapsed, 2), "dry_run": self.dry_run, "interrupted": self.interrupted,
            "node": self.node or None,
            "counts": {"candidates": self.candidates, "selected": self.selected, "to_process": self.to_process,
                       "not_processed_due_to_limit": self.limited, "resumed_from_journal": self.resumed,
                       "processed": dict(self.processed), "unchanged": dict(self.unchanged),
                       "totals": dict(self.totals), "kinds": dict(self.kinds), "formatted": self.formatted,
                       "node_checked_ok": self.node_checked, "assets": self.assets, "views": self.views,
                       "python_links": dict(self.links)},
            "not_fully_processed": self.problems[:MAX_LISTED],
            "note": "JavaScript/CSS formatado NAO e o codigo-fonte original; ligacoes ao Python sao PROVAVEIS.",
        }


# ------------------------------------------------------------------ selecao

def is_gameface(rec: dict) -> bool:
    v = "/" + (rec.get("virtual") or "")
    return rec.get("category") == "web" or "/gameface/" in v or v.startswith("/gui/unbound/")


def find_node(explicit: Path | None = None) -> tuple[str | None, str]:
    """(executavel, rotulo 'node vX') ou (None, motivo)."""
    cands = [str(explicit)] if explicit else []
    which = shutil.which("node")
    if which:
        cands.append(which)
    for c in cands:
        try:
            r = subprocess.run([c, "--version"], capture_output=True, text=True, timeout=30,
                               creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0))
        except (OSError, subprocess.TimeoutExpired):
            continue
        if r.returncode == 0 and r.stdout.strip().startswith("v"):
            return c, f"node {r.stdout.strip()}"
    return None, "node nao encontrado"


def _selected(rec: dict, key: str, opts: GFOptions) -> bool:
    if rec.get("status") not in OK_ENTRY or not is_gameface(rec):
        return False
    if opts.trees and rec.get("tree") not in opts.trees:
        return False
    if opts.globs:
        v = rec.get("virtual", "")
        return any(fnmatch.fnmatchcase(v, g) or fnmatch.fnmatchcase(key, g) for g in opts.globs)
    return True


def _tool_sig(node_label: str, opts: GFOptions) -> str:
    return f"gf{ANALYZER_VERSION}/fmt{FORMATTER_VERSION}/{node_label if opts.use_node else 'sem-node'}/format={int(opts.format)}"


def _reusable(prev: dict | None, rec: dict, out_dir: Path, sig: str, opts: GFOptions) -> bool:
    if opts.force or not prev or prev.get("status") not in ("success", "partial"):
        return False
    if prev.get("input_sha256") != rec.get("sha256") or prev.get("tool_sig") != sig:
        return False
    for rel in outputs_of({"gameface": prev}):
        if not os.path.exists(long_path(out_dir / rel)):
            return False
    return prev["status"] == "success" or not opts.retry


# ------------------------------------------------------------------ execucao

def run_gameface(cfg: Config, realm: str, options: GFOptions | None = None, progress=None,
                 node: str | None = None, node_label: str = "") -> GFResult:
    opts = options or GFOptions()
    t0 = time.perf_counter()
    out_dir = cfg.realm_output_dir(realm)
    manifest_path = out_dir / "manifest.json"
    res = GFResult(realm=realm, out_dir=out_dir, dry_run=opts.dry_run,
                   started=datetime.now(timezone.utc).isoformat(timespec="seconds"))
    if not manifest_path.is_file():
        raise ManifestError(f"{manifest_path} nao existe: corra primeiro 'extract --realm {realm}'")
    if not opts.use_node:
        node, node_label = None, ""
    res.node = node_label if node else ""
    if opts.dry_run:
        return _run(cfg, realm, opts, res, node, manifest_path, progress, t0)
    with StateLock(out_dir):
        return _run(cfg, realm, opts, res, node, manifest_path, progress, t0)


def _run(cfg, realm, opts, res, node, manifest_path, progress, t0) -> GFResult:
    out_dir = res.out_dir
    manifest = load_manifest(manifest_path)
    if manifest.get("realm") != realm:
        raise ManifestError(f"{manifest_path} pertence ao realm {manifest.get('realm')}, nao a {realm}")
    entries: dict[str, dict] = manifest["entries"]
    state_dir = out_dir / ".state"
    journal = Journal(state_dir / JOURNAL_NAME)
    resumed = {k: r.get("gameface") for k, r in journal.load().items() if r.get("gameface")}
    res.resumed = len(resumed)
    sig = _tool_sig(res.node, opts)

    results: dict[str, dict] = {}
    todo: list[str] = []
    for key, rec in entries.items():
        if rec.get("status") in OK_ENTRY and is_gameface(rec):
            res.candidates += 1
        if not _selected(rec, key, opts):
            continue
        kind = file_kind(rec.get("virtual") or key)
        if kind == "asset":
            continue  # indexados no fim, sem processamento
        res.selected += 1
        prev = resumed.get(key) or rec.get("gameface")
        if _reusable(prev, rec, out_dir, sig, opts):
            res.unchanged[prev["status"]] += 1
            results[key] = prev
            continue
        todo.append(key)
    if opts.limit and len(todo) > opts.limit:
        res.limited = len(todo) - opts.limit
        todo = sorted(todo)[:opts.limit]
    todo.sort(key=lambda k: -(entries[k].get("size") or 0))  # os maiores primeiro
    res.to_process = len(todo)
    if opts.dry_run:
        res.elapsed = time.perf_counter() - t0
        return res

    (out_dir / GF_DIR).mkdir(parents=True, exist_ok=True)
    done = 0

    def make_job(key: str) -> dict:
        rec = entries[key]
        prev = resumed.get(key) or rec.get("gameface")
        if prev:
            remove_outputs(out_dir, {"gameface": prev})
        return {"key": key, "src": str(resolve_within(out_dir / "sources", key)), "out_dir": str(out_dir),
                "kind": file_kind(rec.get("virtual") or key), "format": opts.format, "node": node}

    def record(key: str, new: dict) -> None:
        nonlocal done
        new["input_sha256"] = entries[key].get("sha256")
        new["tool_sig"] = sig
        results[key] = new
        journal.write({"key": key, "gameface": new})
        res.processed[new["status"]] += 1
        done += 1

    try:
        with ProcessPoolExecutor(max_workers=max(1, opts.jobs)) as ex:
            pending = iter(todo)
            inflight: dict = {}
            try:
                while True:
                    while len(inflight) < max(1, opts.jobs) * 2:
                        key = next(pending, None)
                        if key is None:
                            break
                        inflight[ex.submit(process_file, make_job(key))] = key
                    if not inflight:
                        break
                    finished, _ = wait(list(inflight), return_when=FIRST_COMPLETED)
                    for f in finished:
                        key = inflight.pop(f)
                        try:
                            new = f.result()
                        except Exception as exc:  # erro inesperado no processo de trabalho
                            new = {"status": "failed", "kind": file_kind(entries[key].get("virtual") or key),
                                   "error": f"{type(exc).__name__}: {exc}"}
                        record(key, new)
                    if progress:
                        progress(done, len(todo), res.processed)
            except KeyboardInterrupt:
                res.interrupted = True
                for f in inflight:
                    f.cancel()
                ex.shutdown(wait=True, cancel_futures=True)
    finally:
        journal.close()
    if res.interrupted:
        res.elapsed = time.perf_counter() - t0
        return res

    for key, g in sorted(results.items()):
        entries[key]["gameface"] = g
    for key, rec in entries.items():
        g = rec.get("gameface")
        if not g or rec.get("status") not in OK_ENTRY:
            continue
        res.totals[g["status"]] += 1
        res.kinds[g.get("kind", "?")] += 1
        if g.get("formatted"):
            res.formatted += 1
        if (g.get("verify") or {}).get("node") == "ok":
            res.node_checked += 1
        if g["status"] != "success":
            res.problems.append({"key": key, "status": g["status"], "error": g.get("error", "")})

    # agregados: views, ligacoes, indices e documentacao (sempre recalculados a partir das analises)
    pyindex = None
    if opts.links:  # sem 'decompile' ficam so os .py originais (mods) e os XML/JSON
        # conteudo das fontes do indice (Python descompilado, .py, XML/JSON), nao a data da extracao
        h = hashlib.sha1(f"{pylinks.PYINDEX_VERSION}".encode())
        for key in sorted(entries):
            r = entries[key]
            if r.get("category") in ("python_bytecode", "python_source", "xml", "json") and r.get("status") in OK_ENTRY:
                h.update(f"{key}={r.get('sha256')}/{(r.get('decompiled') or {}).get('sha256')};".encode())
        psig = h.hexdigest()
        pyindex, res.pyindex_cached = pylinks.load_or_build(out_dir, state_dir, entries, psig)
    agg = _aggregate(out_dir, entries, pyindex)
    res.views = len(agg["views"])
    res.assets = agg["assets"]
    res.links = Counter(v.get("link", {}).get("confidence", "sem-analise") for v in agg["views"].values())
    res.index_path = out_dir / GF_DIR / "manifests" / "index.json"
    res.views_doc = out_dir / GF_DIR / "VIEWS.md"

    now = datetime.now(timezone.utc)
    manifest["gameface"] = {"date": now.isoformat(timespec="seconds"), "tool_sig": sig, "node": res.node or None,
                            "counts": dict(res.totals), "views": res.views, "python_links": dict(res.links)}
    manifest.setdefault("tool_versions", {})["gameface"] = sig
    write_atomic(state_dir / "manifest.prev.json", manifest_path.read_bytes())
    save_json_atomic(manifest_path, manifest, indent=None)
    res.manifest_path = manifest_path
    res.elapsed = time.perf_counter() - t0
    report = res.to_report()
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    save_json_atomic(state_dir / "reports" / f"gameface_{stamp}.json", report)
    save_json_atomic(out_dir / "gameface_report.json", report)
    res.report_path = out_dir / "gameface_report.json"
    journal.remove()
    return res


# ------------------------------------------------------------------ agregacao

def _load_analysis(out_dir: Path, rel: str) -> dict:
    try:
        return json.loads(Path(long_path(out_dir / rel)).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def _effective(keys: list[str], entries: dict) -> str:
    """O ficheiro que o jogo usa (os outros estao sobrepostos por res_mods/mods)."""
    live = [k for k in keys if not entries[k].get("overridden_by")]
    return (live or keys)[0]


def _aggregate(out_dir: Path, entries: dict, pyindex: dict | None) -> dict:
    gf = out_dir / GF_DIR
    by_virtual: dict[str, list[str]] = {}
    analyses: dict[str, dict] = {}
    assets = []
    unbound, ts = [], []
    for key, rec in sorted(entries.items()):
        if rec.get("status") not in OK_ENTRY or not is_gameface(rec):
            continue
        v = rec.get("virtual") or ""
        kind = file_kind(v or key)
        if kind == "asset":
            assets.append({"key": key, "source": f"sources/{key}", "virtual": v, "category": rec.get("category"),
                           "size": rec.get("size")})
            continue
        g = rec.get("gameface") or {}
        if not g.get("analysis"):
            continue
        by_virtual.setdefault(v, []).append(key)
        analyses[key] = _load_analysis(out_dir, g["analysis"])
        if kind == "unbound":
            a = analyses[key]
            unbound.append({"key": key, "defs": a.get("defs", []), "generated_from": a.get("generated_from")})
        elif kind in ("ts_source", "typings"):
            a = analyses[key]
            ts.append({"key": key, "kind": kind, "exports": a.get("exports", []), "imports": a.get("imports", [])})

    # chunks do webpack: (prefixo antes de _dist, nome do chunk global, id) -> chaves
    chunk_files: dict[tuple, list[str]] = {}
    modules: dict[str, list] = {}
    for key, a in analyses.items():
        wp = a.get("webpack")
        if not wp:
            continue
        v = entries[key].get("virtual") or ""
        root = v.split(PROD.lstrip("/"), 1)[0] if PROD.lstrip("/") in v else ""
        for cid in wp.get("chunk_ids", []):
            chunk_files.setdefault((root, wp.get("chunk_name"), cid), []).append(key)
        lines = wp.get("module_lines", {})
        for mid in wp.get("module_ids", []):
            modules.setdefault(f"{root}{mid}" if root else mid, []).append([key, lines.get(mid)])

    # mapeamento oficial R.views -> ficheiro (gui/gen_resources/*_layouts.json de cada feature)
    layouts: dict[str, dict] = {}
    for key, rec in sorted(entries.items()):
        v = rec.get("virtual") or ""
        if rec.get("status") not in OK_ENTRY or rec.get("overridden_by") or not v.endswith(LAYOUT_FILES):
            continue
        try:
            data = json.loads(Path(long_path(out_dir / "sources" / key)).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        for it in data if isinstance(data, list) else []:
            if not isinstance(it, dict) or not it.get("id") or not it.get("path"):
                continue
            path = it["path"]
            if path.lower().startswith("coui://"):
                path = path[7:]
            params = it.get("parameters") or {}
            layouts[path.lower()] = {"id": it["id"], "impl": params.get("impl"), "entrance": params.get("entrance"),
                                     "file": f"sources/{key}", "path": path}

    # views: pastas de _dist/production com um .html, e layouts .unbound
    view_dirs: dict[str, dict] = {}
    for v, keys in by_virtual.items():
        pp = prod_parts(v)
        if not pp:
            continue
        feature, parts = pp
        if len(parts) < 2 or parts[0] in ("lib", "chunks") or "chunks" in parts[:-1]:
            continue
        vdir = v.rsplit("/", 1)[0]
        d = view_dirs.setdefault(vdir, {"feature": feature, "parts": parts[:-1], "files": {}, "impl": "gameface"})
        d["files"][parts[-1]] = keys
    for path, lay in layouts.items():
        if lay["impl"] == "unbound" and path in {k.lower() for k in by_virtual}:
            real = next(k for k in by_virtual if k.lower() == path)
            vdir, name = real.rsplit("/", 1)
            view_dirs.setdefault(real, {"feature": None, "parts": [], "files": {name: by_virtual[real]},
                                        "impl": "unbound", "dir": vdir})
    used_layouts: set[str] = set()
    views: dict[str, dict] = {}
    for vdir, d in sorted(view_dirs.items()):
        if d["impl"] == "gameface" and not any(n.lower().endswith((".html", ".htm")) for n in d["files"]):
            continue
        feature, parts = d["feature"], d["parts"]
        files = []
        js_names: set[str] = set()
        deps: set[str] = set()
        engine, r_views, commands = set(), set(), set()
        for name, keys in sorted(d["files"].items()):
            eff = _effective(keys, entries)
            files.append({"name": name, "effective": eff, "all": keys,
                          "formatted": (entries[eff].get("gameface") or {}).get("formatted")})
            a = analyses.get(eff, {})
            js_names.update(a.get("names", []))
            engine.update(a.get("engine", []))
            r_views.update(a.get("r_views", []))
            commands.update(a.get("commands", []))
            base = posixpath.dirname(entries[eff].get("virtual") or "")
            for ref in a.get("scripts", []) + a.get("stylesheets", []):
                deps.add(posixpath.normpath(posixpath.join(base, ref)))
            wp = a.get("webpack") or {}
            root = vdir.split(PROD.lstrip("/"), 1)[0] if PROD.lstrip("/") in vdir else ""
            for cid in wp.get("requires_chunks", []):
                for ck in chunk_files.get((root, "webpackChunkgameface", cid), []) or \
                        [k for (r, _, c), ks in chunk_files.items() if r == root and c == cid for k in ks]:
                    deps.add(entries[ck].get("virtual") or ck)
        main_files = [entries[f["effective"]].get("virtual") or "" for f in files
                      if f["name"].lower().endswith((".html", ".htm", ".unbound"))]
        lay = next((layouts[m.lower()] for m in main_files if m.lower() in layouts), None)
        if lay:
            used_layouts.add(lay["path"].lower())
            full = lay["id"]
            source = f"{lay['file']} (mapeamento oficial)"
        else:
            full = "R.views." + ".".join(([feature.replace("/", ".")] if feature else []) + parts)
            source = "convencao pela pasta (sem entrada nos *_layouts.json)"
        rid = full[len("R.views."):] if full.startswith("R.views.") else full
        dep_list = []
        for target in sorted(deps):
            keys = by_virtual.get(target)
            dep_list.append({"virtual": target, "key": _effective(keys, entries) if keys else None})
            if keys and "/lib/" not in target:  # bibliotecas de terceiros nao contam para a cobertura
                js_names.update(analyses.get(_effective(keys, entries), {}).get("names", []))
        view = {"rid": full, "rid_source": source, "impl": d["impl"], "entrance": (lay or {}).get("entrance"),
                "dir": d.get("dir", vdir), "feature": feature, "files": files, "dependencies": dep_list,
                "engine": sorted(engine), "child_views": sorted(r_views), "commands": sorted(commands)}
        if pyindex is not None:
            view["link"] = pylinks.link_view(pyindex, rid, feature, parts or rid.split("."), js_names, main_files)
        views[rid] = view
    missing_layouts = sorted(lay["id"] for p, lay in layouts.items() if p not in used_layouts)

    mdir = gf / "manifests"
    remove_tree(mdir / "views")
    for rid, view in views.items():
        save_json_atomic(resolve_within(mdir / "views", rid + ".json"), view)
    index = {
        "tool": TOOL_NAME, "tool_version": __version__,
        "note": "JS/CSS formatados NAO sao o codigo-fonte original; ligacoes ao Python sao PROVAVEIS.",
        "views": {rid: {"rid": v["rid"], "official_id": "mapeamento oficial" in v["rid_source"], "impl": v["impl"],
                        "dir": v["dir"], "files": [f["effective"] for f in v["files"]],
                        "confidence": v.get("link", {}).get("confidence"),
                        "view_model": ((v.get("link") or {}).get("view_model") or {}).get("class")}
                  for rid, v in views.items()},
        "chunks": {f"{r}|{n}|{c}": ks for (r, n, c), ks in sorted(chunk_files.items(), key=lambda x: str(x[0]))},
        "webpack_modules": modules,
        "layouts_without_files": missing_layouts,
        "unbound": unbound,
        "typescript": ts,
    }
    save_json_atomic(mdir / "index.json", index, indent=None)
    save_json_atomic(mdir / "python_links.json",
                     {"note": "O id R.views de cada view vem dos gui/gen_resources/*_layouts.json (mapeamento "
                              "oficial do jogo). As ligacoes ao Python (que classes/ViewModels usam a view) sao "
                              "PROVAVEIS: deduzidas pelas referencias R.views no Python descompilado e pelo ViewModel.",
                      "links": {rid: v["link"] for rid, v in views.items() if "link" in v}})
    save_json_atomic(gf / "assets" / "index.json",
                     {"note": "Os assets ficam em sources/ (nao sao duplicados).", "assets": assets})
    write_atomic(gf / "VIEWS.md", _views_markdown(views, len(assets), unbound, ts).encode("utf-8"))
    return {"views": views, "assets": len(assets)}


def _views_markdown(views: dict, n_assets: int, unbound: list, ts: list) -> str:
    lines = [
        "# Gameface views",
        "",
        "Generated by wot-extractor. **The JavaScript/CSS formatted in `js/` and `css/` is not the original source code**",
        "(webpack shortened names and removed comments; only whitespace and line breaks were added).",
        "Each view's `R.views` id comes from the official mapping `gui/gen_resources/*_layouts.json` (marked with *",
        "when there is none and it was inferred from the folder). The links to Python (classes that use the view and",
        "its ViewModel) are **probable**: inferred from `R.views` references in the decompiled Python and the ViewModel.",
        "",
        f"Views: {len(views)} · .unbound files: {len(unbound)} · TypeScript: {len(ts)} · indexed assets: {n_assets}",
        "",
        "| R.views | Confidence | ViewModel | VM names in the JS | Python |",
        "|---|---|---|---|---|",
    ]
    for rid, v in sorted(views.items()):
        link = v.get("link") or {}
        vm = link.get("view_model") or {}
        cov = vm.get("coverage") or {}
        pyf = link.get("python_files") or []
        star = "" if "mapeamento oficial" in v["rid_source"] else " *"
        lines.append(f"| `{v['rid']}`{star} | {link.get('confidence', '-')} | {vm.get('class', '-')} | "
                     f"{str(cov.get('found')) + '/' + str(cov.get('total')) if cov else '-'} | "
                     f"{('`' + pyf[0].replace('sources/', '') + '`') if pyf else '-'}"
                     f"{' (+' + str(len(pyf) - 1) + ')' if len(pyf) > 1 else ''} |")
    lines += ["", "Details of each view (files, dependencies, `engine.*` events, commands, ViewModel properties",
              "missing from the JS) in `manifests/views/<R.views>.json`.", ""]
    return "\n".join(lines)
