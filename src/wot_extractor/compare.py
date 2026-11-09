"""Comando `compare`: o que mudou entre dois realms (por omissao EU -> CT).

  ficheiros  por caminho (as pastas de versao de mods/ e res_mods/ sao normalizadas) e SHA-256: novos,
             removidos, alterados, por categoria
  Python     modulos, classes, funcoes, metodos, atributos e constantes novos/removidos e assinaturas alteradas
             (do indice de APIs, que vem das descricoes verificadas dos stubs)
  AS3        classes novas/removidas
  Gameface   views novas/removidas e propriedades/comandos dos ViewModels alterados
Resultado em <saida>/compare/compare_<A>_<B>.json e COMPARE_<A>_<B>.md. So leitura das arvores.
"""

from __future__ import annotations

import sqlite3
import time
from collections import Counter
from pathlib import Path

from .apiindex import build_index, db_path
from .config import Config
from .extract.manifest import ManifestError, load_manifest
from .extract.writer import save_json_atomic, write_atomic

OK_ENTRY = frozenset({"extracted", "unchanged"})
MAX_LISTED = 3000
MAX_PER_KIND = 1500  # listas da API limitadas por tipo (os totais sao sempre completos)
API_KINDS = ("module", "class", "function", "method", "attribute", "constant", "native")


def norm_key(key: str, rec: dict) -> str:
    """mods/<versao>/x.wotmod/... e res_mods/<versao>/... sem a pasta de versao (muda entre clientes)."""
    tree = rec.get("tree")
    if tree in ("mods", "res_mods"):
        parts = key.split("/", 2)
        if len(parts) == 3 and parts[1][:1].isdigit():
            return f"{parts[0]}/*/{parts[2]}"
    return key


def _files(manifest: dict) -> dict[str, tuple[str, str, str]]:
    out = {}
    for key, rec in manifest["entries"].items():
        if rec.get("status") in OK_ENTRY:
            out[norm_key(key, rec)] = (key, rec.get("sha256"), rec.get("category"))
    return out


def _symbols(con: sqlite3.Connection, realm: str, kinds) -> dict[tuple[str, str], str | None]:
    q = f"SELECT kind, qualname, signature FROM symbols WHERE realm=? AND kind IN ({','.join('?' * len(kinds))})"
    return {(k, qn): sig for k, qn, sig in con.execute(q, (realm, *kinds))}


def compare_realms(cfg: Config, a: str = "EU", b: str = "CT", refresh_index: bool = True) -> tuple[dict, Path, Path]:
    t0 = time.perf_counter()
    ma, mb = (load_manifest(cfg.realm_output_dir(r) / "manifest.json")
              if (cfg.realm_output_dir(r) / "manifest.json").is_file() else None for r in (a, b))
    if ma is None or mb is None:
        raise ManifestError(f"falta o manifesto de {a if ma is None else b}: corra primeiro 'extract'")
    if refresh_index:
        build_index(cfg, a)
        build_index(cfg, b)

    fa, fb = _files(ma), _files(mb)
    added = sorted(k for k in fb if k not in fa)
    removed = sorted(k for k in fa if k not in fb)
    changed = sorted(k for k in fa if k in fb and fa[k][1] != fb[k][1])
    by_cat = {"added": Counter(fb[k][2] for k in added), "removed": Counter(fa[k][2] for k in removed),
              "changed": Counter(fa[k][2] for k in changed)}

    for r in (a, b):
        if not db_path(cfg, r).is_file():
            raise ManifestError(f"{db_path(cfg, r)} nao existe: corra 'index' (ou compare sem --no-index)")
    con_a, con_b = sqlite3.connect(str(db_path(cfg, a))), sqlite3.connect(str(db_path(cfg, b)))
    try:
        sa, sb = _symbols(con_a, a, API_KINDS), _symbols(con_b, b, API_KINDS)
        ca, cb = _symbols(con_a, a, ("as3_class",)), _symbols(con_b, b, ("as3_class",))
        va = {qn: sig for (_, qn), sig in _symbols(con_a, a, ("view",)).items()}
        vb = {qn: sig for (_, qn), sig in _symbols(con_b, b, ("view",)).items()}
        vma = _symbols(con_a, a, ("vm_property", "vm_command"))
        vmb = _symbols(con_b, b, ("vm_property", "vm_command"))
    finally:
        con_a.close()
        con_b.close()

    def api_diff(x: dict, y: dict) -> dict:
        add = sorted(k for k in y if k not in x)
        rem = sorted(k for k in x if k not in y)
        sig = sorted(k for k in x if k in y and x[k] != y[k] and k[0] in ("function", "method", "class", "constant"))
        def cap(items):
            seen = Counter()
            out = []
            for k, n in items:
                seen[k] += 1
                if seen[k] <= MAX_PER_KIND:
                    out.append((k, n))
            return out
        return {"added": [{"kind": k, "name": n, "signature": y[(k, n)]} for k, n in cap(add)],
                "removed": [{"kind": k, "name": n, "signature": x[(k, n)]} for k, n in cap(rem)],
                "signature_changed": [{"kind": k, "name": n, "before": x[(k, n)], "after": y[(k, n)]}
                                      for k, n in cap(sig)],
                "counts": {"added": dict(Counter(k for k, _ in add)), "removed": dict(Counter(k for k, _ in rem)),
                           "signature_changed": dict(Counter(k for k, _ in sig))}}

    py = api_diff(sa, sb)
    as3 ={"added": sorted(n for (_, n) in cb.keys() - ca.keys()), "removed": sorted(n for (_, n) in ca.keys() - cb.keys())}
    vm = api_diff(vma, vmb)
    views = {"added": sorted(set(vb) - set(va)), "removed": sorted(set(va) - set(vb)),
             "view_model_changed": sorted(k for k in set(va) & set(vb) if va[k] != vb[k]),
             "vm_members_added": [x["name"] for x in vm["added"]], "vm_members_removed": [x["name"] for x in vm["removed"]]}
    result = {
        "realms": [a, b], "versions": {a: ma.get("version_name"), b: mb.get("version_name")},
        "generated": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "note": "Comparacao so com informacao verificada (SHA-256 e descricoes dos stubs); ligacoes Gameface<->Python "
                "continuam PROVAVEIS.",
        "files": {"counts": {"added": len(added), "removed": len(removed), "changed": len(changed),
                             "same": len(fa) - len(removed) - len(changed)},
                  "by_category": {k: dict(v.most_common()) for k, v in by_cat.items()},
                  "added": [fb[k][0] for k in added][:MAX_LISTED], "removed": [fa[k][0] for k in removed][:MAX_LISTED],
                  "changed": [fb[k][0] for k in changed][:MAX_LISTED]},
        "python_api": py,
        "as3_classes": {k: v[:MAX_LISTED] for k, v in as3.items()},
        "gameface": {k: v[:MAX_LISTED] for k, v in views.items()},
    }
    out = cfg.output_root / "compare"
    jp = out / f"compare_{a}_{b}.json"
    mp = out / f"COMPARE_{a}_{b}.md"
    save_json_atomic(jp, result)
    write_atomic(mp, _markdown(result).encode("utf-8"))
    result["elapsed_s"] = round(time.perf_counter() - t0, 1)
    return result, jp, mp


def _markdown(r: dict) -> str:
    a, b = r["realms"]
    f = r["files"]
    py = r["python_api"]
    L = [f"# {a} ({r['versions'][a]}) → {b} ({r['versions'][b]})", "",
         f"Gerado em {r['generated']}. {r['note']}", "",
         "## Ficheiros", "",
         f"Novos {f['counts']['added']} · removidos {f['counts']['removed']} · alterados {f['counts']['changed']} · "
         f"iguais {f['counts']['same']}", "", "| Categoria | Novos | Removidos | Alterados |", "|---|---|---|---|"]
    cats = sorted(set().union(*[set(v) for v in f["by_category"].values()]))
    for c in cats:
        L.append(f"| {c} | {f['by_category']['added'].get(c, 0)} | {f['by_category']['removed'].get(c, 0)} | "
                 f"{f['by_category']['changed'].get(c, 0)} |")
    L += ["", "## API Python", "", f"Novos: {py['counts']['added']}", "", f"Removidos: {py['counts']['removed']}", "",
          f"Assinaturas alteradas: {py['counts']['signature_changed']}", ""]
    for title, items, fmt in (
            ("Módulos e classes novos", [x for x in py["added"] if x["kind"] in ("module", "class")],
             lambda x: f"- {x['kind']} `{x['name']}`"),
            ("Módulos e classes removidos", [x for x in py["removed"] if x["kind"] in ("module", "class")],
             lambda x: f"- {x['kind']} `{x['name']}`"),
            ("Assinaturas alteradas", py["signature_changed"],
             lambda x: f"- {x['kind']} `{x['name']}`: `{x['before']}` → `{x['after']}`")):
        L += [f"### {title}", ""]
        L += [fmt(x) for x in items[:300]] or ["- (nenhum)"]
        if len(items) > 300:
            L.append(f"- ... mais {len(items) - 300} (ver JSON)")
        L.append("")
    g = r["gameface"]
    L += ["## Gameface", "", f"Views novas: {len(g['added'])} · removidas: {len(g['removed'])} · ViewModel mudou: "
          f"{len(g['view_model_changed'])} · membros de ViewModels novos/removidos: {len(g['vm_members_added'])}/"
          f"{len(g['vm_members_removed'])}", ""]
    L += [f"- nova `{x}`" for x in g["added"][:200]] + [f"- removida `{x}`" for x in g["removed"][:200]]
    c = r["as3_classes"]
    L += ["", "## ActionScript", "", f"Classes novas: {len(c['added'])} · removidas: {len(c['removed'])}", ""]
    L += [f"- nova `{x}`" for x in c["added"][:200]] + [f"- removida `{x}`" for x in c["removed"][:200]]
    return "\n".join(L) + "\n"
