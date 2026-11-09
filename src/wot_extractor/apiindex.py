"""Indice de pesquisa de APIs das arvores wot_src_<R> (comandos `index` e `search`).

Uma base SQLite com FTS5 por realm (so biblioteca padrao) em <saida>/wot_api_index_<R>.sqlite com:
  python    modulos, classes, funcoes, metodos, atributos e constantes (das descricoes dos stubs, fase F), com
            a assinatura verificada e ficheiro:linha no .py descompilado/original
  native    membros usados dos modulos sem codigo (BigWorld, ResMgr, ...), dos stubs
  as3       classes (catalogo, fase D) e metodos/propriedades dos .as descompilados pelo FFDec
  gameface  views (R.views oficial) e propriedades/comandos dos ViewModels ligados (ligacao PROVAVEL)
So le as saidas das fases; nao muda as arvores.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sqlite3
import time
from dataclasses import dataclass, field
from pathlib import Path

from .config import Config
from .extract.manifest import ManifestError, load_manifest
from .extract.writer import long_path

INDEX_VERSION = 1
DB_NAME = "wot_api_index_{realm}.sqlite"
_AS_FUNC = re.compile(r"^\s*((?:(?:public|private|protected|internal|override|static|final|native)\s+)*)"
                      r"function\s+(?:(get|set)\s+)?([A-Za-z_$][\w$]*)\s*\(([^)]*)\)\s*(?::\s*([\w.*<>]+))?", re.M)
_AS_VAR = re.compile(r"^\s*((?:(?:public|protected|internal|static)\s+)+)(var|const)\s+([A-Za-z_$][\w$]*)\s*:\s*([\w.*<>]+)",
                     re.M)
_NATIVE_LINE = re.compile(r"^(?:def\s+(\w+)\(|(\w+):\s*Any)(?:.*?#\s*(.*))?$")

SCHEMA = """
CREATE TABLE IF NOT EXISTS symbols(
  id INTEGER PRIMARY KEY, realm TEXT, kind TEXT, name TEXT, qualname TEXT, signature TEXT,
  parent TEXT, module TEXT, file TEXT, line INTEGER, doc TEXT, source TEXT);
CREATE INDEX IF NOT EXISTS symbols_realm ON symbols(realm);
CREATE INDEX IF NOT EXISTS symbols_name ON symbols(name);
CREATE VIRTUAL TABLE IF NOT EXISTS symbols_fts USING fts5(
  name, qualname, doc, content='symbols', content_rowid='id', tokenize="unicode61 tokenchars '_'");
CREATE TABLE IF NOT EXISTS meta(realm TEXT PRIMARY KEY, version TEXT, built TEXT, sig TEXT, counts TEXT);
"""


@dataclass
class IndexResult:
    realm: str
    db: Path
    skipped: bool = False
    counts: dict = field(default_factory=dict)
    elapsed: float = 0.0
    version: str = ""


def db_path(cfg: Config, realm: str) -> Path:
    return cfg.output_root / DB_NAME.format(realm=realm.upper())


def _connect(path: Path) -> sqlite3.Connection:
    con = sqlite3.connect(str(path))
    con.executescript(SCHEMA)
    return con


def _sig(manifest: dict, out_dir: Path) -> str:
    """Assinatura do CONTEUDO que o indice le (nao das datas: reexecutar uma fase sem mudancas nao o refaz)."""
    h = hashlib.sha1(f"{INDEX_VERSION}|{(manifest.get('stubs') or {}).get('natives')}".encode())
    for key in sorted(manifest["entries"]):
        r = manifest["entries"][key]
        if r.get("status") not in ("extracted", "unchanged"):
            continue
        s, a, g = r.get("stubs") or {}, r.get("actionscript") or {}, r.get("gameface") or {}
        if s or a or g:
            h.update(f"{key}|{s.get('input_sig')}|{s.get('status')}|{a.get('input_sha256')}|{a.get('tool_sig')}|"
                     f"{g.get('input_sha256')}|{g.get('tool_sig')};".encode())
    for rel in ("sources_gameface/manifests/python_links.json", "sources_gameface/manifests/index.json"):
        try:
            h.update(Path(long_path(out_dir / rel)).read_bytes())
        except OSError:
            pass
    return h.hexdigest()


def _signature(fn: dict) -> str:
    parts = []
    for i, a in enumerate(fn.get("args", [])):
        name = a.get("name") or a.get("tuple") or f"__p{i}"
        parts.append(f"{name}={a.get('default') or '...'}" if a.get("has_default") else name)
    if fn.get("vararg"):
        parts.append("*" + fn["vararg"])
    if fn.get("kwarg"):
        parts.append("**" + fn["kwarg"])
    return "(" + ", ".join(parts) + ")"


def _first_line(doc: str | None) -> str | None:
    if not doc:
        return None
    return doc.strip().split("\n", 1)[0][:300]


def _python_rows(realm: str, out_dir: Path, manifest: dict):
    entries = manifest["entries"]
    desc_dir = out_dir / ".state" / "stubs_desc"
    for key, rec in sorted(entries.items()):
        s = rec.get("stubs") or {}
        if not s.get("module") or s.get("status") == "failed":
            continue
        try:
            d = json.loads(Path(long_path(desc_dir / (key + ".json"))).read_text(encoding="utf-8"))["desc"]
        except (OSError, ValueError, KeyError):
            continue
        if not d.get("ok"):
            continue
        module = s["module"]
        dec = rec.get("decompiled") or {}
        file = dec.get("output") if dec.get("output") else f"sources/{key}"
        src = "bytecode" if d.get("mode") == "bytecode" else "codigo"
        yield (realm, "module", module.rsplit(".", 1)[-1], module, None, None, module, file, 1,
               _first_line(d.get("doc")), src)
        for a in d.get("assigns", []):
            yield (realm, "constant", a["name"], f"{module}.{a['name']}", a.get("value") or a.get("kind"), None,
                   module, file, None, None, src)
        for f in d.get("functions", []):
            yield (realm, "function", f["name"], f"{module}.{f['name']}", _signature(f), None, module, file,
                   f.get("line"), _first_line(f.get("doc")), src)
        stack = [(c, module) for c in d.get("classes", [])]
        while stack:
            c, parent = stack.pop()
            q = f"{parent}.{c['name']}"
            bases = ", ".join(b.get("src") or "?" for b in c.get("bases", []))
            yield (realm, "class", c["name"], q, f"({bases})" if bases else None, parent, module, file, c.get("line"),
                   _first_line(c.get("doc")), src)
            for m in c.get("methods", []):
                deco = " ".join("@" + x for x in m.get("decorators", []) if x in ("property", "staticmethod",
                                                                                      "classmethod"))
                yield (realm, "method", m["name"], f"{q}.{m['name']}", (deco + " " if deco else "") + _signature(m),
                       q, module, file, m.get("line"), _first_line(m.get("doc")), src)
            names = set()
            for a in c.get("attrs", []):
                names.add(a["name"])
                yield (realm, "attribute", a["name"], f"{q}.{a['name']}", a.get("value") or a.get("kind"), q,
                       module, file, None, None, src)
            for n in c.get("instance_attrs", []):
                if n not in names:
                    yield (realm, "attribute", n, f"{q}.{n}", "self." + n, q, module, file, None, None, src)
            stack += [(k, q) for k in c.get("classes", [])]


def _native_rows(realm: str, out_dir: Path, manifest: dict):
    for mod in (manifest.get("stubs") or {}).get("natives", []):
        rel = f"__stubs/{mod}.pyi"
        try:
            lines = Path(long_path(out_dir / rel)).read_text(encoding="utf-8").splitlines()
        except OSError:
            continue
        yield (realm, "module", mod, mod, None, None, mod, rel, 1, "modulo sem codigo no cliente (nativo ou ausente)",
               "nativo")
        for i, line in enumerate(lines, 1):
            m = _NATIVE_LINE.match(line)
            if not m or (m.group(1) or m.group(2)) == "__getattr__":
                continue
            name = m.group(1) or m.group(2)
            yield (realm, "native", name, f"{mod}.{name}", "(*args, **kwargs)" if m.group(1) else None, mod, mod, rel,
                   i, m.group(3), "nativo")


def _line_counter(text: str):
    """Numero da linha de uma posicao, para posicoes crescentes (sem recontar desde o inicio)."""
    state = {"pos": 0, "line": 1}

    def at(pos: int) -> int:
        state["line"] += text.count("\n", state["pos"], pos)
        state["pos"] = pos
        return state["line"]
    return at


def _as3_members(name: str, key: str, rel: str, text: str, realm: str):
    rows = []
    for m in _AS_FUNC.finditer(text):
        mods = " ".join(m.group(1).split())
        acc = (m.group(2) + " ") if m.group(2) else ""
        ret = f" : {m.group(5)}" if m.group(5) else ""
        rows.append((m.start(), (realm, "as3_member", m.group(3), f"{name}.{m.group(3)}",
                                 f"{mods} {acc}function({' '.join(m.group(4).split())}){ret}".strip(), name, key, rel)))
    for m in _AS_VAR.finditer(text):
        rows.append((m.start(), (realm, "as3_member", m.group(3), f"{name}.{m.group(3)}",
                                 f"{' '.join(m.group(1).split())} {m.group(2)} : {m.group(4)}", name, key, rel)))
    rows.sort(key=lambda x: x[0])
    at = _line_counter(text)
    for pos, r in rows:
        yield r + (at(pos), None, "as3")


def _as3_rows(realm: str, out_dir: Path, manifest: dict):
    members_done: set[str] = set()  # a mesma classe existe em varios SWF: membros indexados uma vez
    for key, rec in sorted(manifest["entries"].items()):
        a = rec.get("actionscript") or {}
        if not a.get("catalog") or rec.get("overridden_by"):
            continue
        try:
            cat = json.loads(Path(long_path(out_dir / a["catalog"])).read_text(encoding="utf-8"))
        except (OSError, ValueError):
            continue
        sdir = (a.get("scripts") or {}).get("dir")
        for c in cat.get("classes", []):
            if c.get("private"):
                continue
            name = c["name"]
            rel = f"{sdir}/{name.replace('.', '/')}.as" if sdir else None
            ext = c.get("extends")
            yield (realm, "as3_class", name.rsplit(".", 1)[-1], name, f"extends {ext}" if ext else None,
                   name.rpartition(".")[0], key, rel, None, None, "as3")
            if not rel or name in members_done:
                continue
            try:
                text = Path(long_path(out_dir / rel)).read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            members_done.add(name)
            yield from _as3_members(name, key, rel, text, realm)


def _gameface_rows(realm: str, out_dir: Path):
    gf = out_dir / "sources_gameface" / "manifests"
    try:
        links = json.loads(Path(long_path(gf / "python_links.json")).read_text(encoding="utf-8"))["links"]
        index = json.loads(Path(long_path(gf / "index.json")).read_text(encoding="utf-8"))["views"]
    except (OSError, ValueError, KeyError):
        return
    for rid, v in sorted(index.items()):
        full = v.get("rid") or f"R.views.{rid}"
        link = links.get(rid) or {}
        vm = link.get("view_model") or {}
        main = next((f for f in v.get("files", []) if f.endswith((".html", ".unbound"))), (v.get("files") or [None])[0])
        yield (realm, "view", rid.rsplit(".", 1)[-1], full, f"impl={v.get('impl')}; VM={vm.get('class')}",
               None, None, f"sources/{main}" if main else None, None,
               f"ligacao ao Python: {link.get('confidence')}", "gameface")
        for p, t in vm.get("properties", []):
            yield (realm, "vm_property", p, f"{vm['class']}.{p}", t, vm["class"], full, vm.get("file"), None,
                   f"ViewModel de {full} (provavel)", "gameface")
        for c in vm.get("commands", []):
            yield (realm, "vm_command", c, f"{vm['class']}.{c}", "command", vm["class"], full, vm.get("file"), None,
                   f"ViewModel de {full} (provavel)", "gameface")


def build_index(cfg: Config, realm: str, force: bool = False) -> IndexResult:
    t0 = time.perf_counter()
    out_dir = cfg.realm_output_dir(realm)
    mpath = out_dir / "manifest.json"
    if not mpath.is_file():
        raise ManifestError(f"{mpath} nao existe: corra primeiro 'extract --realm {realm}'")
    manifest = load_manifest(mpath)
    res = IndexResult(realm=realm, db=db_path(cfg, realm), version=manifest.get("version_name") or "")
    sig = _sig(manifest, out_dir)
    if res.db.is_file() and not force:
        con = sqlite3.connect(str(res.db))
        try:
            row = con.execute("SELECT sig, counts FROM meta WHERE realm=?", (realm,)).fetchone()
        except sqlite3.Error:
            row = None
        finally:
            con.close()
        if row and row[0] == sig:
            res.skipped = True
            res.counts = json.loads(row[1])
            res.elapsed = time.perf_counter() - t0
            return res
    tmp = res.db.with_suffix(".tmp")  # base nova; troca atomica no fim (a antiga continua usavel ate la)
    tmp.unlink(missing_ok=True)
    con = _connect(tmp)
    try:
        con.execute("PRAGMA journal_mode=OFF")
        con.execute("PRAGMA synchronous=OFF")
        counts: dict[str, int] = {}
        insert = ("INSERT INTO symbols(realm, kind, name, qualname, signature, parent, module, file, line, doc, source)"
                  " VALUES (?,?,?,?,?,?,?,?,?,?,?)")
        for gen in (_python_rows(realm, out_dir, manifest), _native_rows(realm, out_dir, manifest),
                    _as3_rows(realm, out_dir, manifest), _gameface_rows(realm, out_dir)):
            batch = []
            for r in gen:
                batch.append(r)
                counts[r[1]] = counts.get(r[1], 0) + 1
                if len(batch) >= 5000:
                    con.executemany(insert, batch)
                    batch.clear()
            if batch:
                con.executemany(insert, batch)
        con.execute("INSERT INTO symbols_fts(symbols_fts) VALUES ('rebuild')")
        con.execute("INSERT OR REPLACE INTO meta VALUES (?,?,?,?,?)",
                    (realm, manifest.get("version_name"), time.strftime("%Y-%m-%dT%H:%M:%S"), sig, json.dumps(counts)))
        con.commit()
        res.counts = counts
    finally:
        con.close()
    os.replace(tmp, res.db)
    res.elapsed = time.perf_counter() - t0
    return res


def _fts_query(q: str) -> str:
    terms = [t for t in re.split(r"[^\w]+", q) if t]
    return " ".join(f'"{t}"*' for t in terms)


def search(cfg: Config, query: str, realms: list[str] | None = None, kinds: list[str] | None = None,
           limit: int = 30, exact: bool = False) -> list[dict]:
    from .constants import SUPPORTED_REALMS
    paths = [db_path(cfg, r) for r in (realms or SUPPORTED_REALMS) if db_path(cfg, r).is_file()]
    if not paths:
        raise ManifestError(f"{db_path(cfg, (realms or ['EU'])[0])} nao existe: corra primeiro 'index'")
    rows: list[dict] = []
    for p in paths:
        rows += _search_db(p, query, kinds, limit, exact)
    last = query.rsplit(".", 1)[-1]
    rows.sort(key=lambda r: (r["name"] != last, r["qualname"] != query, r.get("score") or 0, len(r["qualname"]),
                             r["realm"]))
    return rows[:limit]


def _search_db(path: Path, query: str, kinds: list[str] | None, limit: int, exact: bool) -> list[dict]:
    realms = None
    con = sqlite3.connect(str(path))
    con.row_factory = sqlite3.Row
    try:
        where, params = [], []
        if realms:
            where.append(f"s.realm IN ({','.join('?' * len(realms))})")
            params += realms
        if kinds:
            where.append(f"s.kind IN ({','.join('?' * len(kinds))})")
            params += kinds
        if exact:
            sql = "SELECT s.* FROM symbols s WHERE (s.name = ? OR s.qualname = ?)"
            p = [query, query]
        else:
            fq = _fts_query(query)
            if not fq:
                return []
            sql = ("SELECT s.*, bm25(symbols_fts, 10.0, 3.0, 1.0) AS score FROM symbols_fts "
                   "JOIN symbols s ON s.id = symbols_fts.rowid WHERE symbols_fts MATCH ?")
            p = [fq]
        if where:
            sql += " AND " + " AND ".join(where)
        last = query.rsplit(".", 1)[-1]
        order = " ORDER BY (s.name = ?) DESC, (s.qualname = ?) DESC" + ("" if exact else ", score") + \
                ", length(s.qualname) LIMIT ?"
        rows = con.execute(sql + order, p + params + [last, query, limit]).fetchall()
        return [dict(r) for r in rows]
    finally:
        con.close()
