"""Comando `report`: relatorio global de um realm (todas as fases) em report.json e REPORT.md.

So le o manifesto e os relatorios de cada fase; distingue rigorosamente o que e original, extraido,
descodificado, descompilado, formatado, gerado (stubs) e parcialmente recuperado.
"""

from __future__ import annotations

import json
import os
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from .. import TOOL_NAME, __version__
from ..config import Config
from ..extract.manifest import ManifestError, load_manifest
from ..extract.writer import long_path, save_json_atomic, write_atomic

OK_ENTRY = frozenset({"extracted", "unchanged"})
TOP_PROBLEMS = 25

CONTENT = [
    ("sources/", "ORIGINAL files extracted from res and res_mods (exact copy, SHA-256 in the manifest); the .py files next "
                 "to the .pyc are DECOMPILED code (first line 'wot-extractor: codigo DESCOMPILADO'); processed .pyc/XML/SWF "
                 "may have been removed by `clean`"),
    ("sources_xml/", "BigWorld binary XML DECODED to text"),
    ("sources_as/", "SWF: catalog, AS3 code DECOMPILED by FFDec (or declarations only, marked), exported assets and "
                    ".asasm disassembly"),
    ("sources_gameface/", "FORMATTED JS/CSS/HTML (not the original source code), analyses, views and PROBABLE links "
                          "to Python (originals in sources/)"),
    ("__stubs/", ".pyi stubs GENERATED only from information verified in the code (Any = unknown)"),
]


def _load(path: Path) -> dict | None:
    try:
        return json.loads(Path(long_path(path)).read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return None


def _dir_size(path: Path) -> tuple[int, int]:
    total = files = 0
    for dirpath, _, names in os.walk(long_path(path)):
        for n in names:
            try:
                total += os.stat(os.path.join(dirpath, n)).st_size
                files += 1
            except OSError:
                pass
    return files, total


def build_report(cfg: Config, realm: str, sizes: bool = True) -> dict:
    out_dir = cfg.realm_output_dir(realm)
    manifest_path = out_dir / "manifest.json"
    if not manifest_path.is_file():
        raise ManifestError(f"{manifest_path} nao existe: corra primeiro 'extract --realm {realm}'")
    m = load_manifest(manifest_path)
    entries: dict[str, dict] = m["entries"]
    live = {k: r for k, r in entries.items() if r.get("status") in OK_ENTRY}

    cats = Counter(r.get("category") for r in live.values())
    trees = Counter(r.get("tree") for r in live.values())
    validation = Counter(f"{r.get('category')}:{r.get('validation')}" for r in live.values() if r.get("validation"))

    def phase_counts(field: str, cat: str | None = None) -> Counter:
        c = Counter()
        for r in live.values():
            if cat and r.get("category") != cat:
                continue
            v = r.get(field)
            if isinstance(v, dict):
                c[v.get("status", "?")] += 1
            elif cat:
                c["nao processado"] += 1
        return c

    def problems(field: str) -> list[dict]:
        out = []
        for k, r in sorted(live.items()):
            v = r.get(field)
            if isinstance(v, dict) and v.get("status") not in ("success", "extracted", "native", None):
                out.append({"key": k, "status": v.get("status"), "error": (v.get("error") or "")[:300]})
        return out

    decoded = Counter((r.get("decoded") or {}).get("status") for r in live.values() if r.get("decoded"))
    cleaned = Counter(r.get("category") for r in live.values() if r.get("cleaned"))
    phases = {
        "extract": {"date": m.get("extraction_date"), "consistent": m.get("consistent"), "counts": m.get("counts"),
                    "filters": m.get("filters"), "by_category": dict(cats.most_common()), "by_tree": dict(trees),
                    "validation": dict(validation.most_common()), "xml_decoded": dict(decoded),
                    "cleaned": dict(cleaned), "clean": m.get("clean")},
        "decompile": {"summary": m.get("decompile"), "status": dict(phase_counts("decompiled", "python_bytecode")),
                      "problems": problems("decompiled")},
        "actionscript": {"summary": m.get("actionscript"), "status": dict(phase_counts("actionscript", "scaleform")),
                         "problems": problems("actionscript")},
        "gameface": {"summary": m.get("gameface"), "status": dict(phase_counts("gameface")),
                     "problems": problems("gameface")},
        "stubs": {"summary": {k: v for k, v in (m.get("stubs") or {}).items() if k != "outputs"},
                  "status": dict(phase_counts("stubs")), "problems": problems("stubs")},
    }
    for name in ("decompile", "actionscript", "gameface", "stubs"):
        phases[name]["problems_total"] = len(phases[name]["problems"])
        phases[name]["problems"] = phases[name]["problems"][:TOP_PROBLEMS]
        phases[name]["done"] = bool(m.get(name))

    verify = _load(out_dir / "verify_report.json")
    content = []
    for rel, desc in CONTENT:
        item = {"dir": rel, "content": desc}
        if sizes and (out_dir / rel).exists():
            item["files"], item["bytes"] = _dir_size(out_dir / rel)
        content.append(item)
    try:
        version_file = (out_dir / ".version_name").read_text(encoding="utf-8").strip()
    except OSError:
        version_file = None
    return {
        "tool": TOOL_NAME, "tool_version": __version__,
        "generated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "realm": realm, "version_name": m.get("version_name"), "version_file": version_file,
        "game_version": m.get("game_version"), "install_path": m.get("install_path"), "app_type": m.get("app_type"),
        "tool_versions": m.get("tool_versions"),
        "phases": phases,
        "verify": {k: verify.get(k) for k in ("started", "integrity_ok", "update_needed", "counts")} if verify else None,
        "content": content,
    }


def _h(n: int | None) -> str:
    if n is None:
        return "-"
    for unit in ("B", "KB", "MB", "GB"):
        if n < 1024:
            return f"{n:.0f} {unit}"
        n /= 1024
    return f"{n:.1f} TB"


def to_markdown(r: dict) -> str:
    p = r["phases"]
    ex = p["extract"]
    L = [f"# wot-extractor — {r['realm']} report ({r['version_name']})", "",
         f"Generated {r['generated']} · install `{r['install_path']}` ({r.get('app_type')}) · "
         f"`.version_name` = {r['version_file']}", "",
         "## Folder contents", "", "| Folder | What it is | Files | Size |", "|---|---|---|---|"]
    for c in r["content"]:
        L.append(f"| `{c['dir']}` | {c['content']} | {c.get('files', '-')} | {_h(c.get('bytes'))} |")
    counts = ex.get("counts") or {}
    L += ["", "## Phases", "",
          f"- **Extraction** ({ex['date']}, consistent: {ex['consistent']}): {counts.get('selected')} files out of "
          f"{counts.get('found')} found, success {counts.get('success')}, failures {counts.get('failed')}. "
          f"Binary XML decoded: {ex['xml_decoded']}."
          + (f" Removed from `sources/` by `clean` (already processed; marked in the manifest): {ex['cleaned']}."
             if ex.get("cleaned") else "")]
    labels = {"decompile": "Python decompilation (.pyc 2.7)", "actionscript": "ActionScript/SWF",
              "gameface": "Gameface", "stubs": ".pyi stubs"}
    for name, label in labels.items():
        ph = p[name]
        if not ph["done"]:
            L.append(f"- **{label}**: not run.")
            continue
        summ = ph.get("summary") or {}
        extra = ""
        if name == "gameface":
            extra = f" Views: {summ.get('views')}; links to Python (probable): {summ.get('python_links')}."
        if name == "stubs":
            extra = (f" Classes {summ.get('classes')}, functions {summ.get('functions')}, modules without code "
                     f"{len(summ.get('natives') or [])}.")
        L.append(f"- **{label}** ({summ.get('date')}): {ph['status']}. Not fully recovered: "
                 f"{ph['problems_total']}.{extra}")
    v = r.get("verify")
    L += ["", "## Verification", ""]
    if v:
        c = v.get("counts") or {}
        L.append(f"Last `verify` ({v['started']}): integrity {'OK' if v['integrity_ok'] else 'PROBLEMS FOUND'}; "
                 f"{c.get('files_checked')} files checked; update needed: "
                 f"{'yes' if v['update_needed'] else 'no'}.")
    else:
        L.append("`verify` has not been run yet.")
    L += ["", "## Not fully recovered (first ones per phase)", ""]
    for name, label in labels.items():
        items = p[name]["problems"]
        if not items:
            continue
        L.append(f"### {label}")
        L.append("")
        for it in items:
            L.append(f"- `{it['key']}` — {it['status']}: {it['error'][:160]}")
        if p[name]["problems_total"] > len(items):
            L.append(f"- ... {p[name]['problems_total'] - len(items)} more (see report.json / the phase report)")
        L.append("")
    L += ["## Tool versions", "", "```", json.dumps(r.get("tool_versions"), ensure_ascii=False, indent=1),
          "```", ""]
    return "\n".join(L)


def write_report(cfg: Config, realm: str, sizes: bool = True) -> tuple[dict, Path, Path]:
    r = build_report(cfg, realm, sizes)
    out_dir = cfg.realm_output_dir(realm)
    save_json_atomic(out_dir / "report.json", r)
    write_atomic(out_dir / "REPORT.md", to_markdown(r).encode("utf-8"))
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    save_json_atomic(out_dir / ".state" / "reports" / f"report_{stamp}.json", r)
    return r, out_dir / "report.json", out_dir / "REPORT.md"
