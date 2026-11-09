"""Construcao do plano de extracao: enumera o conteudo de res (pacotes + res
solto), res_mods e mods, aplica filtros, resolve precedencia e sobreposicoes.
So leitura sobre a instalacao."""

from __future__ import annotations

import fnmatch
import os
import re
import zipfile
from dataclasses import dataclass, field
from pathlib import Path, PurePosixPath

from ..constants import PROFILE_PREFIXES, PROFILES
from ..detect.install import ClientInstall
from ..detect.pkgprobe import categorize
from ..safety import ArchiveLimitError, ArchiveLimits, UnsafePathError, check_archive, check_archive_member, normalize_member_name

TREES = ("res", "res_mods", "mods")
_VERSION_DIR_RE = re.compile(r"^\d+\.\d+")


@dataclass(frozen=True)
class Filters:
    profile: str = "dev"
    extensions: frozenset[str] = frozenset()   # ex.: {".pyc", ".xml"}; vazio = sem restricao
    containers: tuple[str, ...] = ()           # padroes fnmatch sobre o nome do .pkg/.wotmod
    trees: frozenset[str] = frozenset(TREES)

    def __post_init__(self):
        if self.profile not in PROFILES:
            raise ValueError(f"perfil desconhecido: {self.profile}")

    def accepts(self, tree: str, virtual: str, category: str, container_name: str, kind: str) -> bool:
        if tree not in self.trees:
            return False
        if self.containers:
            if kind != "zip" or not any(fnmatch.fnmatch(container_name.lower(), p.lower()) for p in self.containers):
                return False
        if self.extensions:
            ext = PurePosixPath(virtual or container_name).suffix.lower()
            if ext not in self.extensions:
                return False
        cats = PROFILES[self.profile]
        if cats is None:
            return True
        v = virtual.lower()
        if any(v.startswith(p) for p in PROFILE_PREFIXES[self.profile]):
            return True
        return category in cats

    def to_dict(self) -> dict:
        return {"profile": self.profile, "extensions": sorted(self.extensions),
                "containers": list(self.containers), "trees": sorted(self.trees)}


@dataclass
class Entry:
    tree: str                 # res | res_mods | mods
    path: str                 # caminho relativo dentro de sources/<tree>
    virtual: str              # caminho no sistema de ficheiros virtual do jogo ("" se nao aplicavel)
    kind: str                 # zip | file
    container: str            # relativo a instalacao (res/packages/x.pkg, mods/v/a.wotmod, res/text/a.mo)
    member: str               # nome do membro no zip ("" para ficheiros soltos)
    size: int
    category: str
    crc: int | None = None
    mtime_ns: int | None = None
    shadows: list[str] = field(default_factory=list)
    overridden_by: list[str] = field(default_factory=list)

    @property
    def key(self) -> str:
        return f"{self.tree}/{self.path}"

    @property
    def container_name(self) -> str:
        return self.container.rsplit("/", 1)[-1]

    def base_record(self) -> dict:
        rec = {"tree": self.tree, "path": self.path, "virtual": self.virtual, "category": self.category,
               "source": self.kind, "container": self.container, "size": self.size}
        if self.member:
            rec["member"] = self.member
        if self.crc is not None:
            rec["crc"] = self.crc
        if self.mtime_ns is not None:
            rec["mtime_ns"] = self.mtime_ns
        if self.shadows:
            rec["shadows"] = list(self.shadows)
        if self.overridden_by:
            rec["overridden_by"] = list(self.overridden_by)
        return rec

    def same_source(self, rec: dict) -> bool:
        """True se o registo anterior descreve exatamente a mesma origem."""
        return (rec.get("container") == self.container and rec.get("member", "") == self.member
                and rec.get("size") == self.size and rec.get("crc") == self.crc
                and rec.get("mtime_ns") == self.mtime_ns)


@dataclass
class Plan:
    entries: list[Entry] = field(default_factory=list)
    found: int = 0
    filtered_out: int = 0
    failures: list[dict] = field(default_factory=list)          # membros recusados (inseguros/limites)
    skipped_containers: list[dict] = field(default_factory=list)
    collisions: list[dict] = field(default_factory=list)        # mesmo caminho, caixa diferente
    containers: list[str] = field(default_factory=list)         # ordem de precedencia efetiva

    @property
    def selected_bytes(self) -> int:
        return sum(e.size for e in self.entries)


def _rel(install: Path, p: Path) -> str:
    return p.relative_to(install).as_posix()


def _walk(root: Path, exclude: set[str] = frozenset()):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if os.path.normcase(os.path.join(dirpath, d)) not in exclude)
        for fn in sorted(filenames):
            yield Path(dirpath) / fn


class _Tree:
    """Acumula entradas de uma arvore; a primeira ocorrencia ganha."""

    def __init__(self, plan: Plan):
        self.plan = plan
        self.by_lower: dict[str, Entry] = {}

    def add(self, e: Entry) -> None:
        low = e.path.lower()
        win = self.by_lower.get(low)
        if win is None:
            self.by_lower[low] = e
            self.plan.entries.append(e)
            return
        win.shadows.append(e.container)
        if win.path != e.path:
            self.plan.collisions.append({"tree": e.tree, "kept": win.path, "kept_from": win.container,
                                         "dropped": e.path, "dropped_from": e.container})


def _add_zip(plan: Plan, tree: _Tree, install: Path, zpath: Path, filters: Filters, limits: ArchiveLimits,
             tree_name: str, out_prefix: str, strip_res: bool) -> None:
    container = _rel(install, zpath)
    try:
        with zipfile.ZipFile(zpath, "r") as zf:
            check_archive(zf, limits)
            infos = zf.infolist()
    except (zipfile.BadZipFile, OSError, ArchiveLimitError, ValueError) as exc:
        plan.skipped_containers.append({"container": container, "reason": f"{type(exc).__name__}: {exc}"})
        plan.failures.append({"key": container, "container": container, "error": f"contentor ilegivel/recusado: {exc}"})
        return
    plan.containers.append(container)
    for info in infos:
        if info.is_dir():
            continue
        plan.found += 1
        try:
            name = check_archive_member(info, limits)
        except (UnsafePathError, ArchiveLimitError) as exc:
            plan.failures.append({"key": f"{container}:{info.filename}", "container": container,
                                  "member": info.filename, "error": str(exc)})
            continue
        if strip_res:
            virtual = name[4:] if name.lower().startswith("res/") else ""
        else:
            virtual = name
        category = categorize(name)
        if not filters.accepts(tree_name, virtual, category, zpath.name, "zip"):
            plan.filtered_out += 1
            continue
        path = f"{out_prefix}/{name}" if out_prefix else name
        tree.add(Entry(tree_name, path, virtual, "zip", container, info.filename, info.file_size, category,
                       crc=info.CRC))


def _add_file(plan: Plan, tree: _Tree, install: Path, f: Path, filters: Filters, tree_name: str,
              path: str, virtual: str) -> None:
    plan.found += 1
    try:
        path = normalize_member_name(path)
        st = f.stat()
    except (UnsafePathError, OSError) as exc:
        plan.failures.append({"key": f"{tree_name}/{path}", "container": _rel(install, f), "error": str(exc)})
        return
    category = categorize(f.name)
    if not filters.accepts(tree_name, virtual, category, f.name, "file"):
        plan.filtered_out += 1
        return
    tree.add(Entry(tree_name, path, virtual, "file", _rel(install, f), "", st.st_size, category,
                   mtime_ns=st.st_mtime_ns))


def build_plan(install: ClientInstall, filters: Filters = Filters(),
               limits: ArchiveLimits = ArchiveLimits()) -> Plan:
    root = install.path
    plan = Plan()
    trees = {t: _Tree(plan) for t in TREES}

    # ---- res: pacotes ativos (ordem do paths.xml), depois res solto (./res e o ultimo caminho)
    if "res" in filters.trees and install.dirs.get("packages"):
        pkg_dir = Path(install.dirs["packages"])
        on_disk = {f.name.lower(): f for f in pkg_dir.glob("*.pkg")}
        order = install.packages.get("load_order") or sorted(f.name for f in on_disk.values())
        used = set()
        for name in order:
            f = on_disk.get(name.lower())
            if f is None or name.lower() in used:
                continue
            used.add(name.lower())
            if filters.containers and not any(fnmatch.fnmatch(f.name.lower(), p.lower()) for p in filters.containers):
                continue
            _add_zip(plan, trees["res"], root, f, filters, limits, "res", "", strip_res=False)
        for k, f in sorted(on_disk.items()):
            if k not in used:
                plan.skipped_containers.append({"container": _rel(root, f),
                                                "reason": "nao carregado por este cliente (fora do paths.xml ou tipo sd/hd)"})
    if "res" in filters.trees and install.dirs.get("res"):
        res_dir = Path(install.dirs["res"])
        exclude = {os.path.normcase(str(res_dir / "packages"))}
        for f in _walk(res_dir, exclude):
            rel = f.relative_to(res_dir).as_posix()
            _add_file(plan, trees["res"], root, f, filters, "res", rel, rel)

    # ---- res_mods: so a pasta da versao ativa, com o caminho relativo a res_mods/
    if "res_mods" in filters.trees and install.dirs.get("res_mods"):
        rm_dir = Path(install.dirs["res_mods"])
        rm_root = Path(install.dirs.get("res_mods_root") or rm_dir.parent)
        for f in _walk(rm_dir):
            _add_file(plan, trees["res_mods"], root, f, filters, "res_mods",
                      f.relative_to(rm_root).as_posix(), f.relative_to(rm_dir).as_posix())

    # ---- mods: pasta da versao ativa (.wotmod expandidos) + pastas nao-versao (configs/...)
    if "mods" in filters.trees and install.dirs.get("mods"):
        m_dir = Path(install.dirs["mods"])
        m_root = Path(install.dirs.get("mods_root") or m_dir.parent)
        for f in _walk(m_dir):
            rel = f.relative_to(m_root).as_posix()
            if f.suffix.lower() == ".wotmod":
                if filters.containers and not any(fnmatch.fnmatch(f.name.lower(), p.lower()) for p in filters.containers):
                    continue
                _add_zip(plan, trees["mods"], root, f, filters, limits, "mods", rel, strip_res=True)
            else:
                _add_file(plan, trees["mods"], root, f, filters, "mods", rel, "")
        for sub in sorted(p for p in m_root.iterdir() if p.is_dir()) if m_root.is_dir() else []:
            if _VERSION_DIR_RE.match(sub.name) or os.path.normcase(str(sub)) == os.path.normcase(str(m_dir)):
                continue
            for f in _walk(sub):
                _add_file(plan, trees["mods"], root, f, filters, "mods", f.relative_to(m_root).as_posix(), "")

    # ---- sobreposicoes: ficheiros de res substituidos por res_mods ou mods no jogo
    overrides: dict[str, list[str]] = {}
    for e in plan.entries:
        if e.tree in ("res_mods", "mods") and e.virtual:
            overrides.setdefault(e.virtual.lower(), []).append(f"{e.tree}:{e.container}")
    if overrides:
        for e in plan.entries:
            if e.tree == "res":
                hit = overrides.get(e.virtual.lower())
                if hit:
                    e.overridden_by = hit
    return plan
