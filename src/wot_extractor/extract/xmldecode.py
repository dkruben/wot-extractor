"""Passo de descodificacao dos XML binarios BigWorld extraidos:
sources/<arvore>/<caminho>  ->  sources_xml/<arvore>/<caminho>.

O original nunca e alterado. Corre em processos (trabalho de CPU) e e
incremental: so descodifica o que mudou ou quando DECODER_VERSION muda."""

from __future__ import annotations

from collections import Counter
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures.process import BrokenProcessPool
from dataclasses import dataclass, field
from pathlib import Path

from ..formats.bwxml import DECODER_VERSION, PackedXmlError, decode_packed_xml
from ..safety import resolve_within
from .validate import validate_xml
from .writer import existing_size, long_path, remove_file, write_atomic

XML_DIR = "sources_xml"
MIN_PARALLEL = 64
OK_DECODED = frozenset({"success", "partial"})


def _header(original_rel: str) -> bytes:
    return (f"<!-- Copia descodificada (XML binario BigWorld) gerada pelo wot-extractor. "
            f"Original: {original_rel} -->\n").encode("utf-8")


def decode_file(job: tuple[str, str, str, str]) -> tuple[str, dict]:
    """Executado num processo de trabalho. job = (chave, origem, destino, origem_relativa)."""
    key, src, dest, src_rel = job
    info: dict = {"path": f"{XML_DIR}/{key}", "decoder": DECODER_VERSION}
    try:
        with open(long_path(src), "rb") as fh:
            data = fh.read()
        r = decode_packed_xml(data)
        text = _header(src_rel) + r.to_text().encode("utf-8")
        size, sha = write_atomic(Path(dest), text)
        info.update(status=r.status, sha256=sha, size=size, elements=r.elements, validation=validate_xml(text))
        if r.warnings:
            info["warnings"] = r.warnings[:5]
        for k in ("renamed_tags", "non_utf8_strings", "escaped_strings", "trailing_bytes"):
            v = getattr(r, k)
            if v:
                info[k] = v
    except PackedXmlError as exc:
        info.update(status="failed", error=f"formato: {exc}")
    except Exception as exc:  # regista e continua
        info.update(status="failed", error=f"{type(exc).__name__}: {exc}")
    return key, info


@dataclass
class DecodeStats:
    decoded: int = 0
    reused: int = 0
    removed_stale: int = 0
    status: Counter = field(default_factory=Counter)
    validation: Counter = field(default_factory=Counter)
    failures: list[dict] = field(default_factory=list)
    parallel: bool = False

    def to_dict(self, limit: int = 500) -> dict:
        return {"decoder_version": DECODER_VERSION, "decoded_now": self.decoded, "reused": self.reused,
                "stale_removed": self.removed_stale, "status": dict(self.status),
                "validation": dict(self.validation), "parallel": self.parallel,
                "failures": self.failures[:limit]}


def run_decode_pass(records: dict[str, dict], known: dict[str, dict], out_dir: Path, jobs: int,
                    ok_statuses=frozenset({"extracted", "unchanged"})) -> DecodeStats:
    stats = DecodeStats()
    sources_dir = out_dir / "sources"
    xml_dir = out_dir / XML_DIR
    todo: list[tuple[str, str, str, str]] = []
    for key, rec in records.items():
        if rec.get("status") not in ok_statuses:
            continue
        dest = resolve_within(xml_dir / rec["tree"], rec["path"])
        if rec.get("validation") != "packed":
            # deixou de ser binario: remove a copia descodificada antiga
            if (known.get(key) or {}).get("decoded") and remove_file(dest):
                stats.removed_stale += 1
            rec.pop("decoded", None)
            continue
        d = rec.get("decoded")
        if (rec["status"] == "unchanged" and d and (d.get("decoder") == DECODER_VERSION or rec.get("cleaned"))
                and d.get("status") in OK_DECODED and existing_size(dest) == d.get("size")):
            stats.reused += 1
            stats.status[d["status"]] += 1
            if d.get("validation"):
                stats.validation[d["validation"].split(":")[0]] += 1
            continue
        src = resolve_within(sources_dir / rec["tree"], rec["path"])
        todo.append((key, str(src), str(dest), f"sources/{key}"))

    results: list[tuple[str, dict]] = []
    if len(todo) >= MIN_PARALLEL and jobs > 1:
        try:
            with ProcessPoolExecutor(max_workers=jobs) as ex:
                chunk = max(1, len(todo) // (jobs * 8))
                results = list(ex.map(decode_file, todo, chunksize=chunk))
            stats.parallel = True
        except (BrokenProcessPool, OSError):
            results = []
    if not stats.parallel:
        results = [decode_file(job) for job in todo]

    for key, info in results:
        records[key]["decoded"] = info
        stats.decoded += 1
        stats.status[info["status"]] += 1
        if info.get("validation"):
            stats.validation[info["validation"].split(":")[0]] += 1
        if info["status"] == "failed":
            stats.failures.append({"key": key, "error": info.get("error", "")})
    return stats
