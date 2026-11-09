"""Ligacoes PROVAVEIS entre views Gameface e o Python descompilado.

O cliente resolve `R.views.<caminho>` para a pasta `gui/gameface/_dist/production/<caminho>/` (ou
`<feature>/gui/gameface/...` para `R.views.<feature>.<caminho>`) dentro do motor; esse mapeamento nao esta
em nenhum ficheiro extraido. Por isso as ligacoes sao deduzidas por convencao e evidencias:
  1. ficheiros Python que usam `R.views.<id>` (classe da view, estados, menus...);
  2. o ViewModel passado nesses ficheiros (`model=XViewModel()`), ou o da convencao de nomes
     `gui/impl/gen/view_models/views/<caminho>/<nome_em_snake>_model.py`;
  3. quantas propriedades/comandos desse ViewModel aparecem no JavaScript da view.
Nunca sao apresentadas como certas.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

from ..extract.writer import long_path, save_json_atomic

PYINDEX_VERSION = 2
MAX_REFS = 30

_RVIEWS = re.compile(r"R\.views\.([A-Za-z_][\w.]*)")
_VM_PROP = re.compile(r"self\._add(\w+?)Property\(\s*'(\w+)'")
_VM_CMD = re.compile(r"self\._addCommand\(\s*'(\w+)'")
_CLASS = re.compile(r"^class\s+(\w+)\(([\w., ]*)\):", re.M)
_MODEL_KW = re.compile(r"\bmodel\s*=\s*(\w+)|ViewComponent\[(\w+)\]")
_COUI = re.compile(r"coui://([^\s\"'<>]+?\.html?)\b", re.I)
_CAMEL = re.compile(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])")


def snake(name: str) -> str:
    return _CAMEL.sub("_", name).lower()


def python_files(entries: dict) -> list[str]:
    """Caminhos (relativos a wot_src_<R>) dos .py (descompilados e fontes originais) e dos XML/JSON de
    configuracao (nestes so se procuram caminhos coui://...html)."""
    out = []
    for key, rec in entries.items():
        cat = rec.get("category")
        if cat == "python_bytecode":
            d = rec.get("decompiled") or {}
            if d.get("output") and d.get("status") in ("success", "partial"):
                out.append(d["output"])
        elif cat == "python_source" and key.endswith(".py"):
            out.append(f"sources/{key}")
        elif cat == "xml":
            d = rec.get("decoded") or {}
            out.append(d["path"] if d.get("path") else f"sources/{key}")
        elif cat == "json":
            out.append(f"sources/{key}")
    return sorted(out)


def build_index(out_dir: Path, files: list[str]) -> dict:
    refs: dict[str, list] = {}
    coui: dict[str, list] = {}
    models_in: dict[str, list[str]] = {}
    vms: dict[str, dict] = {}
    vm_by_class: dict[str, list[str]] = {}
    for rel in files:
        try:
            with open(long_path(out_dir / rel), "r", encoding="utf-8", errors="replace") as fh:
                text = fh.read()
        except OSError:
            continue
        if "coui://" in text:
            for m in _COUI.finditer(text):
                lst = coui.setdefault(m.group(1).lower(), [])
                if len(lst) < MAX_REFS:
                    lst.append([rel, text.count("\n", 0, m.start()) + 1])
        if not rel.endswith(".py"):
            continue
        if "R.views." in text:
            found = False
            line, last = 1, 0
            for m in _RVIEWS.finditer(text):
                rid = m.group(1)
                line += text.count("\n", last, m.start())
                last = m.start()
                lst = refs.setdefault(rid, [])
                if len(lst) < MAX_REFS:
                    lst.append([rel, line])
                found = True
            if found:
                models = sorted({a or b for a, b in _MODEL_KW.findall(text)})
                if models:
                    models_in[rel] = models
        if "/view_models/" in rel and ("_addCommand(" in text or "Property(" in text):
            classes = _CLASS.findall(text)
            if not classes:
                continue
            # o ViewModel (os ficheiros gerados podem ter enums/constantes antes da classe)
            cls, base = next((c for c in classes if c[0].endswith("Model")), classes[-1])
            vms[rel] = {"class": cls, "base": base.split(",")[0].strip(),
                        "properties": [[n, t] for t, n in _VM_PROP.findall(text)],
                        "commands": _VM_CMD.findall(text)}
            vm_by_class.setdefault(cls, []).append(rel)
    return {"version": PYINDEX_VERSION, "files": len(files), "refs": refs, "coui": coui, "models_in": models_in,
            "view_models": vms, "vm_by_class": vm_by_class}


def load_or_build(out_dir: Path, state_dir: Path, entries: dict, sig: str) -> tuple[dict, bool]:
    """Indice em cache (.state/gameface_pyindex.json) enquanto a assinatura (decompile) nao mudar."""
    path = state_dir / "gameface_pyindex.json"
    try:
        data = json.loads(Path(long_path(path)).read_text(encoding="utf-8"))
        if data.get("sig") == sig and data.get("version") == PYINDEX_VERSION:
            return data, True
    except (OSError, ValueError):
        pass
    data = build_index(out_dir, python_files(entries))
    data["sig"] = sig
    save_json_atomic(path, data, indent=None)
    return data, False


def _vm_full(index: dict, rel: str) -> dict:
    """ViewModel com as propriedades/comandos herdados de outros ViewModels conhecidos."""
    vms = index["view_models"]
    props, cmds, chain = [], [], []
    seen = set()
    cur = rel
    while cur and cur not in seen and len(chain) < 8:
        seen.add(cur)
        vm = vms.get(cur)
        if not vm:
            break
        chain.append(vm["class"])
        props += vm["properties"]
        cmds += vm["commands"]
        base = vm.get("base") or ""
        nxt = index["vm_by_class"].get(base.rsplit(".", 1)[-1], [])
        cur = nxt[0] if len(nxt) == 1 else None
    return {"file": rel, "class": vms[rel]["class"], "chain": chain, "properties": props, "commands": cmds}


def _prefer(cands: list[str], feature: str | None) -> list[str]:
    if not cands:
        return []
    if feature:
        same = [c for c in cands if f"/{feature}/" in c]
        if same:
            return same
    core = [c for c in cands if "/res/scripts/client/" in c]
    return core or cands


def link_view(index: dict, rid: str, feature: str | None, view_parts: list[str], js_names: set[str],
              html_virtuals: list[str] = ()) -> dict:
    """rid: id sem 'R.views.' (ex.: lobby.crew.BarracksView); view_parts: caminho relativo a production/;
    html_virtuals: caminhos virtuais dos .html da view (procurados como coui://...)."""
    refs = index["refs"].get(rid, [])
    evidence = []
    if refs:
        evidence.append(f"{len(refs)} referencia(s) R.views.{rid} no Python")
    coui = []
    for hv in html_virtuals:
        # os *_layouts.json sao o mapeamento id -> ficheiro, nao uma utilizacao da view
        coui += [r for r in index.get("coui", {}).get(hv.lower(), []) if "/gen_resources/" not in r[0]]
    if coui:
        evidence.append(f"caminho coui:// do HTML referido em {len(coui)} sitio(s) (referencia direta)")
    # ViewModel: pelo model=X() nos ficheiros que usam o id, senao pela convencao de nomes
    vm_files: list[str] = []
    for rel, _ in refs:
        for cls in index["models_in"].get(rel, []):
            vm_files += index["vm_by_class"].get(cls, [])
    vm_files = _prefer(sorted(set(vm_files)), feature)
    how = "model=... no Python da view" if vm_files else ""
    if not vm_files and view_parts:
        suffix = "/view_models/views/" + "/".join(view_parts[:-1] + [snake(view_parts[-1]) + "_model.py"])
        vm_files = _prefer([f for f in index["view_models"] if f.endswith(suffix)], feature)
        how = "convencao de nomes" if vm_files else ""
    view_model = None
    if len(vm_files) >= 1:
        vm = _vm_full(index, vm_files[0])
        props = [p for p, _ in vm["properties"]]
        names = props + vm["commands"]
        found = sorted({x for x in names if x in js_names})
        missing = sorted({x for x in names if x not in js_names})
        vm["coverage"] = {"found": len(found), "total": len(set(names)), "missing": missing[:50]}
        vm["found_by"] = how
        if len(vm_files) > 1:
            vm["other_candidates"] = vm_files[1:6]
        view_model = vm
        evidence.append(f"ViewModel {vm['class']} ({how}): {len(found)}/{len(set(names))} nomes no JS")
    cov = view_model["coverage"] if view_model else None
    if coui or (refs and view_model and cov["total"] and cov["found"] * 2 >= cov["total"]):
        confidence = "provavel-forte"
    elif refs or view_model:
        confidence = "provavel"
    else:
        confidence = "nao-encontrada"
    py_files = sorted({rel for rel, _ in refs})
    return {"rid": f"R.views.{rid}", "confidence": confidence, "evidence": evidence,
            "python_refs": refs[:MAX_REFS], "python_files": py_files[:MAX_REFS], "coui_refs": coui[:MAX_REFS],
            "view_model": view_model}
