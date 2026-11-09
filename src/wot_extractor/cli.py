"""Interface de linha de comandos: wot-extractor <comando> [opcoes]."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

from . import TOOL_NAME, __version__
from .config import ConfigError, load_config
from .constants import PROFILES, SUPPORTED_REALMS
from .detect import DetectionResult, detect
from .actionscript import ASOptions, ASResult, find_ffdec, run_actionscript
from .actionscript.rabcdasm import find_rabcdasm
from .gameface import GFOptions, GFResult, find_node, run_gameface
from .stubs import StubOptions, StubResult, find_python27, run_stubs
from .apiindex import build_index
from .apiindex import search as api_search
from .compare import compare_realms
from .maintenance import update as upd
from .maintenance.purge import run_purge
from .maintenance.clean import KINDS as CLEAN_KINDS
from .maintenance.clean import run_clean
from .maintenance.report import write_report
from .maintenance.update import STEPS as UPDATE_STEPS
from .maintenance.verify import VerifyOptions, run_verify
from .decompile import (BACKENDS, DEFAULT_CHAIN, BackendError, DecompileOptions, DecompileResult, find_toolchain,
                        run_decompile)
from .extract import ExtractOptions, ExtractResult, Filters, ManifestError, run_extract
from .extract.plan import TREES
from .logutil import setup_logging
from .safety import ProtectedPathError, WriteGuard

EXIT_INTERRUPTED = 130

EXIT_OK = 0
EXIT_FAIL = 1
EXIT_USAGE = 2
EXIT_NOT_IMPLEMENTED = 3

# Comandos previstos na especificacao e a fase em que serao implementados.
SEARCH_KINDS = ("module", "class", "function", "method", "attribute", "constant", "native", "as3_class",
                "as3_member", "view", "vm_property", "vm_command")
PLANNED = {
}


def _human(n: int) -> str:
    size = float(n)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.0f} {unit}" if unit == "B" else f"{size:.1f} {unit}"
        size /= 1024
    return f"{n} B"


def _realm_arg(value: str) -> str:
    v = value.upper()
    if v != "ALL" and v not in SUPPORTED_REALMS:
        raise argparse.ArgumentTypeError(f"realm invalido: {value} (use {', '.join(SUPPORTED_REALMS)} ou all)")
    return v


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog=TOOL_NAME, description="World of Tanks Source Extractor & Decompiler")
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    parser.add_argument("--config", type=Path, help="ficheiro TOML (por omissao: wot_extractor.toml na raiz)")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="mais detalhe (-v, -vv)")
    parser.add_argument("--log-file", type=Path, help="gravar log detalhado neste ficheiro")
    sub = parser.add_subparsers(dest="command", metavar="<comando>")

    p = sub.add_parser("detect", help="detetar instalacoes, realm, versao e recursos")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--path", type=Path, help="caminho manual da instalacao (exige --realm EU|CT)")
    p.add_argument("--quick", action="store_true", help="nao sondar o conteudo dos .pkg/.wotmod")
    p.add_argument("--no-system", action="store_true", help="ignorar Game Center, registo e pesquisa nos discos")
    p.add_argument("--json", type=Path, metavar="FICHEIRO", help="gravar o resultado completo em JSON")

    p = sub.add_parser("extract", help="extrair res/res_mods/mods para wot_src_<REALM>/sources")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--path", type=Path, help="caminho manual da instalacao (exige --realm EU|CT)")
    p.add_argument("--profile", choices=sorted(PROFILES), default="dev",
                   help="dev (codigo/UI, omissao), gui (+ tudo sob gui/), full (tudo)")
    p.add_argument("--ext", help="so estas extensoes, separadas por virgula (ex.: .pyc,.xml)")
    p.add_argument("--pkg", action="append", default=[], metavar="PADRAO",
                   help="so estes contentores .pkg/.wotmod (fnmatch, repetivel; ex.: 'gui-part*')")
    p.add_argument("--tree", action="append", choices=list(TREES), default=[], help="so estas arvores (repetivel)")
    p.add_argument("-j", "--jobs", type=int, default=min(8, os.cpu_count() or 4), help="threads de escrita")
    p.add_argument("--force", action="store_true", help="reextrair mesmo o que esta inalterado")
    p.add_argument("--dry-run", action="store_true", help="so planear e mostrar o que seria feito")
    p.add_argument("--prune", action="store_true",
                   help="apagar da arvore os ficheiros que ja nao existem no jogo (so se a execucao for consistente)")
    p.add_argument("--no-decode-xml", action="store_true",
                   help="nao gerar copias legiveis dos XML binarios BigWorld em sources_xml/")
    p.add_argument("--no-system", action="store_true", help="ignorar Game Center, registo e pesquisa nos discos")

    p = sub.add_parser("decompile", help="descompilar os .pyc extraidos para .py (ao lado do .pyc em sources/)")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--backend", choices=["auto", *BACKENDS], default="auto",
                   help="auto (omissao): uncompyle6 no Python 2.7 e, se nao der success, uncompyle6 no Python 3; "
                        "ou so o descompilador indicado")
    p.add_argument("--python27", type=Path, help="Python 2.7 com uncompyle6 (omissao: configuracao/detecao)")
    p.add_argument("--python3", type=Path, help="Python 3 com uncompyle6 para a alternativa (omissao: o atual)")
    p.add_argument("--glob", action="append", default=[], metavar="PADRAO",
                   help="so os .pyc cujo caminho virtual (ou chave) case com o padrao (fnmatch, repetivel; "
                        "ex.: 'scripts/client/gui/*')")
    p.add_argument("--tree", action="append", choices=list(TREES), default=[], help="so estas arvores (repetivel)")
    p.add_argument("--limit", type=int, default=0, help="processar no maximo N ficheiros (amostra)")
    p.add_argument("-j", "--jobs", type=int, default=min(8, os.cpu_count() or 4), help="workers em paralelo")
    p.add_argument("--timeout", type=float, help="tempo limite por ficheiro, em segundos (omissao: 120)")
    p.add_argument("--retry", action="store_true", help="voltar a tentar os resultados partial/failed")
    p.add_argument("--force", action="store_true",
                   help="descompilar tudo de novo (um resultado pior nunca substitui um melhor)")
    p.add_argument("--dry-run", action="store_true", help="so mostrar o que seria processado")

    p = sub.add_parser("actionscript", help="catalogar SWF, recuperar ActionScript e recursos para sources_as/")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--ffdec", type=Path, help="ffdec-cli.jar/ffdec.jar ou a pasta do FFDec (omissao: detecao)")
    p.add_argument("--java", type=Path, help="executavel java para o FFDec")
    p.add_argument("--no-ffdec", action="store_true",
                   help="nao usar o FFDec: so catalogo e declaracoes AS3 (sem corpos nem recursos)")
    p.add_argument("--no-assets", action="store_true", help="nao exportar imagens/fontes/sons/dados binarios")
    p.add_argument("--glob", action="append", default=[], metavar="PADRAO",
                   help="so os SWF cujo caminho virtual (ou chave) case com o padrao (fnmatch, repetivel)")
    p.add_argument("--tree", action="append", choices=list(TREES), default=[], help="so estas arvores (repetivel)")
    p.add_argument("--limit", type=int, default=0, help="processar no maximo N SWF (amostra)")
    p.add_argument("-j", "--jobs", type=int, default=min(6, os.cpu_count() or 4),
                   help="SWF em paralelo (uma JVM cada)")
    p.add_argument("--timeout", type=float, help="tempo limite por SWF em segundos (omissao: 3600)")
    p.add_argument("--rabcdasm", type=Path, help="pasta do RABCDAsm (abcexport/rabcdasm)")
    p.add_argument("--asasm", choices=["partial", "all", "none"], default="partial",
                   help="desmontagem .asasm pelo RABCDAsm: so SWF com falhas (omissao), todos, ou nenhum")
    p.add_argument("--heavy-jobs", type=int, default=2,
                   help="maximo de SWF com muito codigo (lobby/battle) em simultaneo; cada um usa varios GB")
    p.add_argument("--retry", action="store_true", help="voltar a tentar os resultados partial/failed")
    p.add_argument("--force", action="store_true", help="processar tudo de novo")
    p.add_argument("--dry-run", action="store_true", help="so mostrar o que seria processado")

    p = sub.add_parser("gameface", help="Gameface: formatar JS/CSS, analisar views e ligacoes ao Python (sources_gameface/)")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--node", type=Path, help="node.exe para verificar o JS formatado (omissao: PATH)")
    p.add_argument("--no-node", action="store_true", help="nao usar o node (so verificacao token a token)")
    p.add_argument("--no-format", action="store_true", help="nao criar copias formatadas (so analise)")
    p.add_argument("--no-links", action="store_true", help="nao procurar ligacoes ao Python")
    p.add_argument("--glob", action="append", default=[], metavar="PADRAO",
                   help="so os ficheiros cujo caminho virtual (ou chave) case com o padrao (fnmatch, repetivel)")
    p.add_argument("--tree", action="append", choices=list(TREES), default=[], help="so estas arvores (repetivel)")
    p.add_argument("--limit", type=int, default=0, help="processar no maximo N ficheiros (amostra)")
    p.add_argument("-j", "--jobs", type=int, default=min(8, os.cpu_count() or 4), help="processos em paralelo")
    p.add_argument("--retry", action="store_true", help="voltar a tentar os resultados partial/failed")
    p.add_argument("--force", action="store_true", help="processar tudo de novo")
    p.add_argument("--dry-run", action="store_true", help="so mostrar o que seria processado")

    p = sub.add_parser("stubs", help="gerar stubs Python (.pyi) em __stubs/ a partir do codigo verificavel")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--python27", type=Path, help="interpretador Python 2.7 (omissao: [decompile] python27 ou detecao)")
    p.add_argument("--stdlib", action="store_true", help="incluir a biblioteca padrao que o jogo traz (scripts/common/Lib)")
    p.add_argument("--no-natives", action="store_true", help="nao gerar stubs dos modulos nativos (BigWorld, ...)")
    p.add_argument("--glob", action="append", default=[], metavar="PADRAO",
                   help="so os ficheiros cujo caminho virtual (ou chave) case com o padrao (fnmatch, repetivel)")
    p.add_argument("--tree", action="append", choices=list(TREES), default=[], help="so estas arvores (repetivel)")
    p.add_argument("--limit", type=int, default=0, help="descrever no maximo N modulos novos (amostra)")
    p.add_argument("-j", "--jobs", type=int, default=min(6, os.cpu_count() or 4), help="interpretadores em paralelo")
    p.add_argument("--timeout", type=float, default=120.0, help="tempo limite por modulo em segundos")
    p.add_argument("--force", action="store_true", help="descrever tudo de novo (ignorar a cache)")
    p.add_argument("--dry-run", action="store_true", help="so mostrar o que seria processado")

    p = sub.add_parser("update", help="atualizar um realm apos uma atualizacao do jogo (todas as fases, incremental)")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--path", type=Path, help="caminho manual da instalacao (exige --realm EU|CT)")
    p.add_argument("--steps", default=",".join(UPDATE_STEPS),
                   help=f"passos a correr, por esta ordem (omissao: {','.join(UPDATE_STEPS)})")
    p.add_argument("--skip", action="append", default=[], choices=list(UPDATE_STEPS), help="saltar um passo (repetivel)")
    p.add_argument("--profile", choices=sorted(PROFILES),
                   help="perfil da extracao (omissao: o da extracao anterior, para nao marcar ficheiros como removidos)")
    p.add_argument("--prune", action="store_true",
                   help="apagar da arvore o que deixou de existir no jogo (so se a extracao for consistente)")
    p.add_argument("--retry", action="store_true", help="voltar a tentar os resultados partial/failed das fases")
    p.add_argument("-j", "--jobs", type=int, help="paralelismo para todos os passos (omissao: o de cada comando)")
    p.add_argument("--heavy-jobs", type=int, help="actionscript: SWF pesados em simultaneo")
    p.add_argument("--no-system", action="store_true", help="ignorar Game Center, registo e pesquisa nos discos")
    p.add_argument("--dry-run", action="store_true", help="so detetar e mostrar o que a extracao faria")

    p = sub.add_parser("verify", help="verificar a arvore (hashes, saidas, orfaos) e se a instalacao mudou")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--path", type=Path, help="caminho da instalacao a comparar (omissao: o do manifesto/detecao)")
    p.add_argument("--quick", action="store_true", help="so tamanhos (sem SHA-256)")
    p.add_argument("--no-install", action="store_true", help="nao comparar com a instalacao")
    p.add_argument("--no-derived", action="store_true", help="nao verificar as saidas das fases C-F")
    p.add_argument("--no-orphans", action="store_true", help="nao procurar ficheiros orfaos em sources/")
    p.add_argument("-j", "--jobs", type=int, default=min(8, os.cpu_count() or 4), help="threads de leitura")
    p.add_argument("--no-system", action="store_true", help="ignorar Game Center, registo e pesquisa nos discos")

    p = sub.add_parser("report", help="relatorio global do realm (report.json e REPORT.md)")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--no-sizes", action="store_true", help="nao calcular o tamanho das pastas")

    p = sub.add_parser("purge", help="retirar da arvore conteudo que nao e do jogo (omissao: a arvore mods)")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--tree", action="append", choices=list(TREES), default=[],
                   help="arvore a retirar (repetivel; omissao: mods)")
    p.add_argument("--glob", action="append", default=[], metavar="PADRAO",
                   help="retirar tambem as chaves que casem com o padrao (fnmatch)")
    p.add_argument("--dry-run", action="store_true", help="so mostrar o que seria retirado")
    p.add_argument("--yes", action="store_true", help="confirmar a remocao (obrigatorio sem --dry-run)")

    p = sub.add_parser("clean", help="apagar de sources/ o que ja foi processado (.pyc, XML binarios, SWF) e "
                                     "ficheiros de trabalho")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--only", action="append", default=[], choices=list(CLEAN_KINDS),
                   help="so este tipo (repetivel; omissao: todos)")
    p.add_argument("--keep", action="append", default=[], choices=list(CLEAN_KINDS), help="nao limpar este tipo")
    p.add_argument("--keep-reports", type=int, default=3, help="relatorios a manter por tipo em .state/reports")
    p.add_argument("--dry-run", action="store_true", help="so mostrar o que seria apagado")
    p.add_argument("--yes", action="store_true", help="confirmar (obrigatorio sem --dry-run)")

    p = sub.add_parser("index", help="construir o indice de pesquisa de APIs (wot_api_index.sqlite)")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--force", action="store_true", help="reconstruir mesmo sem alteracoes")

    p = sub.add_parser("search", help="pesquisar classes/funcoes/metodos/views no indice de APIs")
    p.add_argument("query", help="nome ou parte (ex.: BarracksView, onLoading, BigWorld.callback)")
    p.add_argument("--realm", type=_realm_arg, default="ALL", help="EU, CT ou all (omissao)")
    p.add_argument("--kind", action="append", default=[], choices=list(SEARCH_KINDS), help="so este tipo (repetivel)")
    p.add_argument("--exact", action="store_true", help="nome ou nome qualificado exato")
    p.add_argument("--limit", type=int, default=30, help="maximo de resultados (omissao: 30)")
    p.add_argument("--json", action="store_true", help="resultado em JSON")

    p = sub.add_parser("compare", help="comparar dois realms: ficheiros, API Python, AS3 e Gameface")
    p.add_argument("--from", dest="realm_a", type=_realm_arg, default="EU", help="realm de origem (omissao: EU)")
    p.add_argument("--to", dest="realm_b", type=_realm_arg, default="CT", help="realm de destino (omissao: CT)")
    p.add_argument("--no-index", action="store_true", help="nao atualizar o indice de APIs antes de comparar")

    for name, phase in PLANNED.items():
        sp = sub.add_parser(name, help=f"(ainda nao implementado - fase {phase})")
        sp.add_argument("--realm", type=_realm_arg, default="ALL")
    return parser


def main(argv: list[str] | None = None) -> int:
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(errors="replace")
        except (AttributeError, ValueError):
            pass
    parser = build_parser()
    args = parser.parse_args(argv)
    if not args.command:
        parser.print_help()
        return EXIT_USAGE
    setup_logging(args.verbose, args.log_file)
    try:
        cfg = load_config(args.config)
    except ConfigError as exc:
        print(f"Erro de configuracao: {exc}", file=sys.stderr)
        return EXIT_USAGE

    if args.command == "detect":
        return cmd_detect(args, cfg)
    if args.command == "extract":
        return cmd_extract(args, cfg)
    if args.command == "decompile":
        return cmd_decompile(args, cfg)
    if args.command == "actionscript":
        return cmd_actionscript(args, cfg)
    if args.command == "gameface":
        return cmd_gameface(args, cfg)
    if args.command == "stubs":
        return cmd_stubs(args, cfg)
    if args.command == "update":
        return cmd_update(args, cfg)
    if args.command == "verify":
        return cmd_verify(args, cfg)
    if args.command == "report":
        return cmd_report(args, cfg)
    if args.command == "index":
        return cmd_index(args, cfg)
    if args.command == "purge":
        return cmd_purge(args, cfg)
    if args.command == "clean":
        return cmd_clean(args, cfg)
    if args.command == "search":
        return cmd_search(args, cfg)
    if args.command == "compare":
        return cmd_compare(args, cfg)
    phase = PLANNED[args.command]
    print(f"O comando '{args.command}' ainda nao esta implementado (previsto para a fase {phase}).", file=sys.stderr)
    return EXIT_NOT_IMPLEMENTED


def cmd_detect(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    overrides = {}
    if args.path:
        if args.realm == "ALL":
            print("--path exige --realm EU ou --realm CT", file=sys.stderr)
            return EXIT_USAGE
        overrides[args.realm] = args.path
    t0 = time.perf_counter()
    result = detect(cfg, realms, overrides, deep=not args.quick, use_system=not args.no_system)
    elapsed = time.perf_counter() - t0
    print_detection(result, realms, elapsed)

    if args.json:
        guard = WriteGuard(i.path for i in result.installs)
        try:
            out = guard.check(args.json)
        except ProtectedPathError as exc:
            print(f"Erro: {exc}", file=sys.stderr)
            return EXIT_FAIL
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(result.to_dict(), indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nRelatorio JSON: {out}")
    return EXIT_OK if result.ok else EXIT_FAIL


def _parse_exts(value: str | None) -> frozenset[str]:
    if not value:
        return frozenset()
    exts = set()
    for part in value.split(","):
        part = part.strip().lower()
        if part:
            exts.add(part if part.startswith(".") else "." + part)
    return frozenset(exts)


class _Progress:
    def __init__(self, realm: str):
        self.realm = realm
        self.last = 0.0
        self.tty = sys.stderr.isatty()

    def __call__(self, done: int, total: int, written: int) -> None:
        now = time.perf_counter()
        if not self.tty or (now - self.last < 0.5 and done < total):
            return
        self.last = now
        sys.stderr.write(f"\r  [{self.realm}] {done}/{total} ficheiros, {_human(written)} escritos   ")
        if done >= total:
            sys.stderr.write("\n")
        sys.stderr.flush()


def cmd_extract(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    overrides = {}
    if args.path:
        if args.realm == "ALL":
            print("--path exige --realm EU ou --realm CT", file=sys.stderr)
            return EXIT_USAGE
        overrides[args.realm] = args.path
    if args.jobs < 1:
        print("--jobs deve ser >= 1", file=sys.stderr)
        return EXIT_USAGE
    filters = Filters(profile=args.profile, extensions=_parse_exts(args.ext), containers=tuple(args.pkg),
                      trees=frozenset(args.tree) if args.tree else frozenset(TREES))
    options = ExtractOptions(filters=filters, jobs=args.jobs, force=args.force, dry_run=args.dry_run, prune=args.prune,
                             decode_xml=not args.no_decode_xml)

    detection = detect(cfg, realms, overrides, deep=False, use_system=not args.no_system)
    code = EXIT_OK
    for realm in realms:
        inst = detection.selected.get(realm)
        if inst is None:
            print(f"[{realm}] instalacao nao encontrada: {detection.errors.get(realm, '?')}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        print(f"[{realm}] {inst.path} -> {cfg.realm_output_dir(realm)}  (versao {inst.version.folder_name}, perfil {args.profile})")
        try:
            result = run_extract(cfg, inst, options, progress=_Progress(realm))
        except (ManifestError, ProtectedPathError) as exc:
            print(f"[{realm}] Erro: {exc}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        except KeyboardInterrupt:
            print(f"\n[{realm}] Interrompido durante o planeamento; nada foi alterado.", file=sys.stderr)
            return EXIT_INTERRUPTED
        print_extraction(result)
        if result.interrupted:
            return EXIT_INTERRUPTED
        if not result.dry_run and not result.consistent:
            code = EXIT_FAIL
    return code


def print_extraction(r: ExtractResult) -> None:
    c = r.counts
    if r.dry_run:
        print(f"  Simulacao: {r.found} ficheiros encontrados, {r.selected} selecionados ({_human(r.selected_bytes)}), "
              f"{r.filtered_out} excluidos pelo perfil/filtros")
        print(f"  Seriam extraidos {r.to_extract}; inalterados {c.get('unchanged', 0)}; "
              f"recusados {len(r.failures)}; contentores ignorados {len(r.skipped_containers)}")
        print()
        return
    if r.interrupted:
        print(f"  INTERROMPIDO: {c.get('extracted', 0)} extraidos nesta execucao (journal guardado; volte a correr para retomar)\n")
        return
    print(f"  Encontrados {r.found} | selecionados {r.selected} ({_human(r.selected_bytes)}) | excluidos pelo perfil {r.filtered_out}")
    print(f"  Extraidos {c.get('extracted', 0)} ({_human(r.bytes_written)}) | inalterados {c.get('unchanged', 0)} | "
          f"falhas {r.failed_total} | removidos do jogo {len(r.removed)} (apagados {len(r.pruned)})"
          + (f" | retomados do journal {r.resumed}" if r.resumed else "")
          + (f" | revalidados {r.revalidated}" if r.revalidated else ""))
    for tree, cnt in sorted(r.by_tree.items()):
        print(f"    {tree:<9}: {dict(cnt)}")
    for cat, v in sorted(r.validation.items()):
        print(f"    validacao {cat:<16}: {dict(v)}")
    if r.xml is not None:
        x = r.xml
        print(f"  XML binario -> sources_xml: descodificados {x.decoded}, reaproveitados {x.reused} | "
              f"estado {dict(x.status)} | validacao {dict(x.validation)}"
              + (f" | copias obsoletas removidas {x.removed_stale}" if x.removed_stale else ""))
        for f in x.failures[:5]:
            print(f"  ! XML {f['key']}: {f['error']}")
    if r.overridden:
        print(f"  {len(r.overridden)} ficheiro(s) de res substituidos por res_mods/mods no jogo")
    if r.shadowed:
        print(f"  {r.shadowed} copia(s) sombreadas por pacotes de maior precedencia")
    if r.collisions:
        print(f"  ! {len(r.collisions)} colisao(oes) de caixa (ver relatorio)")
    if r.long_paths:
        print(f"  ! {r.long_paths} caminho(s) com mais de 259 caracteres: ferramentas sem suporte a caminhos "
              f"longos (Explorador, LongPathsEnabled=0) podem nao os abrir")
    for f in r.failures[:10]:
        print(f"  ! {f['key']}: {f['error']}")
    if len(r.failures) > 10:
        print(f"  ! ... mais {len(r.failures) - 10} falhas no relatorio")
    if r.previous_version and r.previous_version != r.version_name:
        print(f"  Versao anterior da arvore: {r.previous_version} -> {r.version_name}")
    state = "CONSISTENTE (.version_name atualizado)" if r.consistent else "INCONSISTENTE (.version_name mantido)"
    print(f"  Estado: {state}  [{r.elapsed:.1f} s]")
    print(f"  Manifesto: {r.manifest_path}\n  Relatorio: {r.report_path}\n")


class _DecProgress:
    def __init__(self, realm: str):
        self.realm = realm
        self.last = 0.0
        self.tty = sys.stderr.isatty()

    def __call__(self, done: int, total: int, counts) -> None:
        now = time.perf_counter()
        if not self.tty or (now - self.last < 0.5 and done < total):
            return
        self.last = now
        parts = ", ".join(f"{k} {v}" for k, v in sorted(counts.items()))
        sys.stderr.write(f"\r  [{self.realm}] {done}/{total} .pyc ({parts})   ")
        if done >= total:
            sys.stderr.write("\n")
        sys.stderr.flush()


def cmd_decompile(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    if args.jobs < 1 or args.limit < 0 or (args.timeout is not None and args.timeout <= 0):
        print("Use --jobs >= 1, --limit >= 0 e --timeout > 0", file=sys.stderr)
        return EXIT_USAGE
    chain = DEFAULT_CHAIN if args.backend == "auto" else (args.backend,)
    options = DecompileOptions(chain=tuple(chain), jobs=args.jobs,
                               timeout=args.timeout or cfg.decompile_timeout, force=args.force, retry=args.retry,
                               globs=tuple(args.glob), trees=frozenset(args.tree), limit=args.limit,
                               dry_run=args.dry_run, python27=args.python27 or cfg.python27,
                               python3=args.python3 or cfg.python3)
    toolchain = find_toolchain(options.python27, options.python3,
                               need_py3=any(BACKENDS[n].interpreter == "py3" for n in chain))
    for rej in toolchain.rejected:
        print(f"  (interpretador rejeitado: {rej.path}: {rej.error})", file=sys.stderr)
    code = EXIT_OK
    for realm in realms:
        print(f"[{realm}] {cfg.realm_output_dir(realm)}")
        try:
            result = run_decompile(cfg, realm, options, progress=_DecProgress(realm), toolchain=toolchain)
        except (ManifestError, BackendError, ProtectedPathError) as exc:
            print(f"[{realm}] Erro: {exc}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        except KeyboardInterrupt:
            print(f"\n[{realm}] Interrompido antes de comecar; nada foi alterado.", file=sys.stderr)
            return EXIT_INTERRUPTED
        print_decompile(result)
        if result.interrupted:
            return EXIT_INTERRUPTED
    # ficheiros partial/failed ficam no relatorio: nao sao erro da ferramenta
    return code


def print_decompile(r: DecompileResult) -> None:
    for c in r.chain:
        print(f"  Descompilador: {c['backend']:<15} {c['tool']}  ({c['path']})")
    if r.dry_run:
        print(f"  Simulacao: {r.selected} .pyc selecionados de {r.candidates}; seriam processados {r.to_process}; "
              f"reaproveitados {sum(r.unchanged.values())}; sem suporte {len(r.unsupported)}"
              + (f"; fora do limite {r.limited}" if r.limited else "") + "\n")
        return
    if r.interrupted:
        print(f"  INTERROMPIDO: {sum(r.processed.values())} processados nesta execucao "
              f"(journal guardado; volte a correr para retomar)\n")
        return
    print(f"  Selecionados {r.selected} de {r.candidates} | processados agora {r.to_process} {dict(r.processed)} | "
          f"reaproveitados {sum(r.unchanged.values())}" + (f" | retomados do journal {r.resumed}" if r.resumed else "")
          + (f" | fora do limite {r.limited}" if r.limited else ""))
    t = r.totals
    print(f"  Resultado: success {t.get('success', 0)} | partial {t.get('partial', 0)} | failed {t.get('failed', 0)} | "
          f"unsupported {t.get('unsupported', 0)} | linhas de codigo recuperadas agora {r.lines_recovered}")
    extra = []
    for label, n in (("alternativa usada", r.fallback_used), ("resultado anterior mantido", r.kept_previous),
                     ("tentativas guardadas", r.attempts_saved), ("tempo limite", r.timeouts),
                     ("workers terminados", r.crashes), (".py obsoletos removidos", r.stale_removed)):
        if n:
            extra.append(f"{label} {n}")
    if extra:
        print("  " + " | ".join(extra))
    for f in r.failures[:8]:
        print(f"  ! failed  {f['key']}: {f['error']}")
    for f in r.partials[:8]:
        print(f"  ~ partial {f['key']}: {f['error'][:160]}")
    more = len(r.failures) + len(r.partials) - min(8, len(r.failures)) - min(8, len(r.partials))
    if more > 0:
        print(f"  ... mais {more} no relatorio")
    print(f"  [{r.elapsed:.1f} s]  Manifesto: {r.manifest_path}\n  Relatorio: {r.report_path}\n")


def cmd_actionscript(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    if args.jobs < 1 or args.heavy_jobs < 1 or args.limit < 0 or (args.timeout is not None and args.timeout <= 0):
        print("Use --jobs >= 1, --heavy-jobs >= 1, --limit >= 0 e --timeout > 0", file=sys.stderr)
        return EXIT_USAGE
    options = ASOptions(jobs=args.jobs, timeout=args.timeout or cfg.actionscript_timeout,
                        use_ffdec=not args.no_ffdec, assets=not args.no_assets, force=args.force,
                        retry=args.retry, globs=tuple(args.glob), trees=frozenset(args.tree), limit=args.limit,
                        dry_run=args.dry_run, heavy_jobs=args.heavy_jobs, asasm=args.asasm)
    rabc_error = ""
    if args.asasm != "none":
        options.rabc, rabc_error = find_rabcdasm(args.rabcdasm or cfg.rabcdasm)
        if options.rabc is None:
            print(f"  (sem desmontagem .asasm: {rabc_error})")
    ff, ff_error = (None, "FFDec desativado (--no-ffdec)")
    if not args.no_ffdec:
        ff, ff_error = find_ffdec(args.ffdec or cfg.ffdec, args.java or cfg.java, cfg.java_heap)
    code = EXIT_OK
    for realm in realms:
        print(f"[{realm}] {cfg.realm_output_dir(realm)}")
        try:
            result = run_actionscript(cfg, realm, options, progress=_DecProgress(realm), ff=ff, ff_error=ff_error)
        except (ManifestError, ProtectedPathError) as exc:
            print(f"[{realm}] Erro: {exc}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        except KeyboardInterrupt:
            print(f"\n[{realm}] Interrompido antes de comecar; nada foi alterado.", file=sys.stderr)
            return EXIT_INTERRUPTED
        print_actionscript(result)
        if result.interrupted:
            return EXIT_INTERRUPTED
    return code


def cmd_stubs(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    if args.jobs < 1 or args.limit < 0 or args.timeout <= 0:
        print("Use --jobs >= 1, --limit >= 0 e --timeout > 0", file=sys.stderr)
        return EXIT_USAGE
    options = StubOptions(jobs=args.jobs, timeout=args.timeout, stdlib=args.stdlib, natives=not args.no_natives,
                          force=args.force, globs=tuple(args.glob), trees=frozenset(args.tree), limit=args.limit,
                          dry_run=args.dry_run)
    code = EXIT_OK
    interp, label = (None, "")
    for realm in realms:
        print(f"[{realm}] {cfg.realm_output_dir(realm)}")
        if interp is None and not args.dry_run:
            state = cfg.realm_output_dir(realm) / ".state"
            state.mkdir(parents=True, exist_ok=True)
            interp, label = find_python27(args.python27 or cfg.python27, state)
        try:
            result = run_stubs(cfg, realm, options, progress=_DecProgress(realm), interp=interp, interp_label=label)
        except (ManifestError, ProtectedPathError) as exc:
            print(f"[{realm}] Erro: {exc}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        except KeyboardInterrupt:
            print(f"\n[{realm}] Interrompido antes de comecar; nada foi alterado.", file=sys.stderr)
            return EXIT_INTERRUPTED
        print_stubs(result)
        if result.interrupted:
            return EXIT_INTERRUPTED
    return code


def print_stubs(r: StubResult) -> None:
    print(f"  Leitura do codigo: {r.interpreter or '(nao necessaria: tudo em cache)'}")
    if r.dry_run:
        print(f"  Simulacao: {r.selected} modulos selecionados de {r.candidates} ficheiros Python; seriam descritos "
              f"{r.described}; em cache {r.reused}" + (f"; fora do limite {r.limited}" if r.limited else "")
              + (f"; biblioteca padrao excluida {r.stdlib_skipped}" if r.stdlib_skipped else "") + "\n")
        return
    if r.interrupted:
        print(f"  INTERROMPIDO: {r.described} modulos descritos (guardados em cache; volte a correr para retomar)\n")
        return
    print(f"  Modulos {r.selected} (de {r.candidates} ficheiros; biblioteca padrao excluida {r.stdlib_skipped}; "
          f"sobrepostos {r.shadowed}) | descritos agora {r.described} | em cache {r.reused}"
          + (f" | fora do limite {r.limited}" if r.limited else ""))
    t = r.totals
    print(f"  Resultado: success {t.get('success', 0)} | partial {t.get('partial', 0)} | failed {t.get('failed', 0)}"
          f" | modos {dict(r.modes)} | classes {r.classes} | funcoes {r.functions}")
    print(f"  Ficheiros .pyi escritos {r.written} | iguais {r.unchanged_files} | antigos removidos {r.removed} | "
          f"nativos {len(r.natives)}: {', '.join(r.natives[:12])}{' ...' if len(r.natives) > 12 else ''}")
    for p in r.problems[:10]:
        print(f"  ~ {p['status']:<8} {p['module']}: {p['error'][:150]}")
    if len(r.problems) > 10:
        print(f"  ... mais {len(r.problems) - 10} no relatorio")
    print(f"  [{r.elapsed:.1f} s]  Stubs: {r.stubs_dir}\n  Relatorio: {r.report_path}\n")


def _sub_argv(args, argv: list[str]) -> list[str]:
    """Opcoes globais (config, log) repetidas nos subcomandos que o update corre."""
    pre = []
    if getattr(args, "config", None):
        pre += ["--config", str(args.config)]
    if getattr(args, "verbose", 0):
        pre += ["-" + "v" * args.verbose]
    if getattr(args, "log_file", None):
        pre += ["--log-file", str(args.log_file)]
    return pre + argv


def cmd_update(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    if args.path and args.realm == "ALL":
        print("--path exige --realm EU ou --realm CT", file=sys.stderr)
        return EXIT_USAGE
    steps = [s.strip() for s in args.steps.split(",") if s.strip()]
    bad = [s for s in steps if s not in UPDATE_STEPS]
    if bad or (args.jobs is not None and args.jobs < 1):
        print(f"Passos invalidos: {bad} (validos: {', '.join(UPDATE_STEPS)}); --jobs >= 1", file=sys.stderr)
        return EXIT_USAGE
    steps = [s for s in steps if s not in args.skip]
    detection = detect(cfg, realms, {args.realm: args.path} if args.path else {}, deep=False,
                       use_system=not args.no_system)
    code = EXIT_OK
    for realm in realms:
        out_dir = cfg.realm_output_dir(realm)
        inst = detection.selected.get(realm)
        if inst is None:
            print(f"[{realm}] instalacao nao encontrada: {detection.errors.get(realm, '?')}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        before, prev = upd.snapshot(out_dir / "manifest.json")
        try:
            extracted = (out_dir / ".version_name").read_text(encoding="utf-8").strip()
        except OSError:
            extracted = prev.get("version_name")
        installed = inst.version.folder_name
        if not prev:
            state = "primeira extracao"
        elif extracted != installed:
            state = f"NOVA VERSAO: {extracted} -> {installed}"
        else:
            state = f"mesma versao ({installed}): procurar ficheiros alterados"
        print(f"[{realm}] update: {inst.path} -> {out_dir}\n  {state}")
        filters = upd.previous_filters(prev) if prev else {"profile": "dev", "extensions": [], "containers": [],
                                                                 "trees": []}
        if args.profile:
            filters["profile"] = args.profile
        ex_argv = ["extract", "--realm", realm, "--profile", filters["profile"]]
        if args.path:
            ex_argv += ["--path", str(args.path)]
        if filters["extensions"]:
            ex_argv += ["--ext", ",".join(filters["extensions"])]
        for c in filters["containers"]:
            ex_argv += ["--pkg", c]
        if filters["trees"] and sorted(filters["trees"]) != sorted(TREES):
            for t in filters["trees"]:
                ex_argv += ["--tree", t]
        if args.no_system:
            ex_argv.append("--no-system")
        if args.jobs:
            ex_argv += ["-j", str(args.jobs)]
        if args.dry_run:
            print("  (simulacao: so a extracao e planeada; nada e escrito)")
            rc = main(_sub_argv(args, ex_argv + ["--dry-run"]))
            code = max(code, rc) if rc != EXIT_INTERRUPTED else rc
            continue
        report = {"realm": realm, "started": time.strftime("%Y-%m-%dT%H:%M:%S"), "installed_version": installed,
                  "previous_version": extracted, "state": state, "filters": filters, "steps": {}}
        t0 = time.perf_counter()
        stopped = None
        for step in steps:
            print(f"\n[{realm}] === {step} ===")
            if step == "extract":
                argv = ex_argv + (["--prune"] if args.prune else [])
            else:
                argv = [step, "--realm", realm] + (["--yes"] if step == "clean" else [])
                if args.jobs and step not in ("index", "clean"):
                    argv += ["-j", str(args.jobs)]
                if args.retry and step in ("decompile", "actionscript", "gameface"):
                    argv.append("--retry")
                if step == "actionscript" and args.heavy_jobs:
                    argv += ["--heavy-jobs", str(args.heavy_jobs)]
            s0 = time.perf_counter()
            rc = main(_sub_argv(args, argv))
            report["steps"][step] = {"exit_code": rc, "elapsed_s": round(time.perf_counter() - s0, 1)}
            if rc == EXIT_INTERRUPTED:
                stopped = f"{step} interrompido (volte a correr 'update' para retomar)"
                code = EXIT_INTERRUPTED
                break
            if step == "extract":
                after, now = upd.snapshot(out_dir / "manifest.json")
                report["diff"] = upd.diff(before, after)
                d = report["diff"]
                print(f"  Diferencas face a extracao anterior: novos {len(d['new'])} | alterados {len(d['changed'])} "
                      f"| removidos {len(d['removed'])}")
                if not now.get("consistent"):
                    stopped = "a extracao nao foi consistente: a versao nao avanca e as fases seguintes nao correm"
                    code = EXIT_FAIL
                    break
            elif rc not in (EXIT_OK,):
                code = max(code, EXIT_FAIL)  # continua: as outras fases nao dependem desta
                report["steps"][step]["note"] = "falhou; as fases seguintes correram na mesma"
        report["elapsed_s"] = round(time.perf_counter() - t0, 1)
        report["completed"] = stopped is None
        if stopped:
            report["stopped"] = stopped
            print(f"\n[{realm}] PARADO: {stopped}", file=sys.stderr)
        try:
            report["version_name_now"] = (out_dir / ".version_name").read_text(encoding="utf-8").strip()
        except OSError:
            report["version_name_now"] = None
        path = upd.save_report(out_dir, report)
        print(f"\n[{realm}] update {'concluido' if stopped is None else 'incompleto'}: versao na arvore "
              f"{report['version_name_now']} | {report['elapsed_s']} s | Relatorio: {path}\n")
    return code


def cmd_verify(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    if args.path and args.realm == "ALL":
        print("--path exige --realm EU ou --realm CT", file=sys.stderr)
        return EXIT_USAGE
    options = VerifyOptions(quick=args.quick, install=not args.no_install, derived=not args.no_derived,
                            orphans=not args.no_orphans, jobs=max(1, args.jobs))
    detection = None
    if options.install:
        detection = detect(cfg, realms, {args.realm: args.path} if args.path else {}, deep=False,
                           use_system=not args.no_system)
    code = EXIT_OK
    for realm in realms:
        print(f"[{realm}] verify {cfg.realm_output_dir(realm)}")
        inst = detection.selected.get(realm) if detection else None
        try:
            r = run_verify(cfg, realm, options, install_path=inst.path if inst else None,
                           installed_version=inst.version.folder_name if inst else None, progress=_DecProgress(realm))
        except ManifestError as exc:
            print(f"[{realm}] Erro: {exc}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        print_verify(r)
        if not r.integrity_ok:
            code = EXIT_FAIL
    return code


def print_verify(r) -> None:
    print(f"  Versao: manifesto {r.version_name} | .version_name {r.version_file} | instalada {r.installed_version or '?'}"
          f" | extracao consistente: {r.consistent}")
    print(f"  Ficheiros verificados {r.checked} ({_human(r.bytes_hashed)} com SHA-256) | saidas derivadas "
          f"{dict(r.derived)} | orfaos {len(r.orphans)}"
          + (f" | removidos do jogo ainda na arvore {len(r.removed_kept)} (update --prune apaga-os)" if r.removed_kept else ""))
    if r.problems:
        for kind, items in r.problems.items():
            print(f"  ! {kind}: {len(items)}  ex.: {items[0]}")
    for o in r.orphans[:5]:
        print(f"  ! orfao: {o}")
    print(f"  Integridade: {'OK' if r.integrity_ok else 'COM PROBLEMAS'}")
    if r.install_error:
        print(f"  Instalacao: {r.install_error}")
    else:
        print(f"  Instalacao: {r.install_checked} ficheiros comparados | alterados {len(r.install_changed)} | "
              f"em falta {len(r.install_missing)}")
    if r.update_needed:
        print("  -> O jogo mudou desde a extracao: corra 'update' para atualizar a arvore.")
    print(f"  [{r.elapsed:.1f} s]  Relatorio: {r.report_path}\n")


def cmd_report(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    code = EXIT_OK
    for realm in realms:
        try:
            r, jpath, mpath = write_report(cfg, realm, sizes=not args.no_sizes)
        except ManifestError as exc:
            print(f"[{realm}] Erro: {exc}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        p = r["phases"]
        print(f"[{realm}] {r['version_name']}  ({r['install_path']})")
        c = p["extract"].get("counts") or {}
        print(f"  Extracao: {c.get('selected')} ficheiros (de {c.get('found')}), falhas {c.get('failed')}, "
              f"consistente {p['extract']['consistent']}")
        for name in ("decompile", "actionscript", "gameface", "stubs"):
            ph = p[name]
            print(f"  {name:<12} {'nao executada' if not ph['done'] else ph['status']}"
                  + (f" | nao totalmente recuperados {ph['problems_total']}" if ph["done"] else ""))
        for cdir in r["content"]:
            if "files" in cdir:
                print(f"  {cdir['dir']:<18} {cdir['files']:>7} ficheiros {_human(cdir['bytes']):>10}")
        v = r.get("verify")
        print(f"  verify: " + (f"integridade {'OK' if v['integrity_ok'] else 'COM PROBLEMAS'}, atualizacao "
                                f"necessaria: {'sim' if v['update_needed'] else 'nao'} ({v['started']})" if v
                                else "ainda nao corrida"))
        print(f"  Relatorio: {jpath}\n  Resumo:    {mpath}\n")
    return code


def cmd_clean(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    if not args.dry_run and not args.yes:
        print("clean apaga ficheiros de sources/: use --dry-run para ver o que sai e --yes para confirmar",
              file=sys.stderr)
        return EXIT_USAGE
    kinds = set(args.only or CLEAN_KINDS) - set(args.keep)
    code = EXIT_OK
    for realm in realms:
        try:
            r = run_clean(cfg, realm, kinds, dry_run=args.dry_run, keep_reports=max(0, args.keep_reports))
        except ManifestError as exc:
            print(f"[{realm}] Erro: {exc}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        verb = "seriam apagados" if r.dry_run else "apagados"
        parts = [f"{k} {r.removed[k]} ({_human(r.freed[k])})" for k in ("pyc", "xml", "swf") if k in kinds]
        print(f"[{realm}] {verb}: " + " | ".join(parts)
              + (f" | trabalho .state {r.state_removed} ficheiros ({_human(r.state_freed)})" if "state" in kinds else ""))
        print(f"  ainda precisos (ficam): {dict(r.kept)} | ja limpos antes: {r.already}"
              + (f"\n  Relatorio: {r.report_path}" if r.report_path else ""))
    return code


def cmd_purge(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    trees = tuple(args.tree) if args.tree else (() if args.glob else ("mods",))
    if not args.dry_run and not args.yes:
        print("purge apaga ficheiros da arvore de saida: use --dry-run para ver a lista e --yes para confirmar",
              file=sys.stderr)
        return EXIT_USAGE
    code = EXIT_OK
    for realm in realms:
        try:
            r = run_purge(cfg, realm, trees, tuple(args.glob), dry_run=args.dry_run)
        except ManifestError as exc:
            print(f"[{realm}] Erro: {exc}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        groups = {}
        for k in r.keys:
            parts = k.split("/")
            g = "/".join(parts[:3])
            groups[g] = groups.get(g, 0) + 1
        verb = "seriam retiradas" if r.dry_run else "retiradas"
        print(f"[{realm}] {r.selected} entradas {verb} {r.by_tree}")
        for g, n in sorted(groups.items()):
            print(f"  {n:>5}  {g}")
        if not r.dry_run:
            print(f"  saidas apagadas {r.removed_files} | ficheiros de res que voltam a ser os efetivos {r.unshadowed}"
                  f"\n  Relatorio: {r.report_path}\n  -> corra 'update' (ou actionscript, gameface, stubs, index) "
                  "para atualizar os indices e as views")
    return code


def cmd_index(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    code = EXIT_OK
    for realm in realms:
        try:
            r = build_index(cfg, realm, force=args.force)
        except ManifestError as exc:
            print(f"[{realm}] Erro: {exc}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        state = "sem alteracoes (reaproveitado)" if r.skipped else "construido"
        print(f"[{realm}] indice {state}: {sum(r.counts.values())} simbolos {r.counts}  [{r.elapsed:.1f} s]\n"
              f"  {r.db}")
    return code


def cmd_search(args, cfg) -> int:
    realms = None if args.realm == "ALL" else [args.realm]
    try:
        rows = api_search(cfg, args.query, realms, args.kind or None, max(1, args.limit), args.exact)
    except ManifestError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return EXIT_FAIL
    if args.json:
        print(json.dumps(rows, ensure_ascii=False, indent=1))
        return EXIT_OK
    if not rows:
        print("Sem resultados.")
        return EXIT_OK
    for r in rows:
        loc = f"{r['file']}:{r['line']}" if r.get("line") else (r.get("file") or "")
        sig = r.get("signature") or ""
        print(f"[{r['realm']}] {r['kind']:<11} {r['qualname']}{sig if sig.startswith('(') else ''}")
        if sig and not sig.startswith("("):
            print(f"      {sig}")
        if r.get("doc"):
            print(f"      # {r['doc'][:150]}")
        print(f"      {loc}")
    return EXIT_OK


def cmd_compare(args, cfg) -> int:
    if args.realm_a == "ALL" or args.realm_b == "ALL" or args.realm_a == args.realm_b:
        print("Indique dois realms diferentes (--from EU --to CT)", file=sys.stderr)
        return EXIT_USAGE
    try:
        r, jp, mp = compare_realms(cfg, args.realm_a, args.realm_b, refresh_index=not args.no_index)
    except ManifestError as exc:
        print(f"Erro: {exc}", file=sys.stderr)
        return EXIT_FAIL
    f, py, g, c = r["files"], r["python_api"], r["gameface"], r["as3_classes"]
    print(f"{args.realm_a} {r['versions'][args.realm_a]} -> {args.realm_b} {r['versions'][args.realm_b]}")
    print(f"  Ficheiros: novos {f['counts']['added']} | removidos {f['counts']['removed']} | alterados "
          f"{f['counts']['changed']} | iguais {f['counts']['same']}")
    print(f"  API Python: novos {py['counts']['added']}\n              removidos {py['counts']['removed']}\n"
          f"              assinaturas alteradas {py['counts']['signature_changed']}")
    print(f"  AS3: classes novas {len(c['added'])} | removidas {len(c['removed'])}")
    print(f"  Gameface: views novas {len(g['added'])} | removidas {len(g['removed'])} | ViewModel mudou "
          f"{len(g['view_model_changed'])} | membros de VM novos/removidos {len(g['vm_members_added'])}/"
          f"{len(g['vm_members_removed'])}")
    print(f"  [{r['elapsed_s']} s]  {jp}\n  {mp}")
    return EXIT_OK


def cmd_gameface(args, cfg) -> int:
    realms = list(SUPPORTED_REALMS) if args.realm == "ALL" else [args.realm]
    if args.jobs < 1 or args.limit < 0:
        print("Use --jobs >= 1 e --limit >= 0", file=sys.stderr)
        return EXIT_USAGE
    options = GFOptions(jobs=args.jobs, format=not args.no_format, use_node=not args.no_node,
                        links=not args.no_links, force=args.force, retry=args.retry, globs=tuple(args.glob),
                        trees=frozenset(args.tree), limit=args.limit, dry_run=args.dry_run)
    node, node_label = (None, "")
    if not args.no_node:
        node, node_label = find_node(args.node or cfg.node)
    code = EXIT_OK
    for realm in realms:
        print(f"[{realm}] {cfg.realm_output_dir(realm)}")
        try:
            result = run_gameface(cfg, realm, options, progress=_DecProgress(realm), node=node, node_label=node_label)
        except (ManifestError, ProtectedPathError) as exc:
            print(f"[{realm}] Erro: {exc}", file=sys.stderr)
            code = EXIT_FAIL
            continue
        except KeyboardInterrupt:
            print(f"\n[{realm}] Interrompido antes de comecar; nada foi alterado.", file=sys.stderr)
            return EXIT_INTERRUPTED
        print_gameface(result, node_label)
        if result.interrupted:
            return EXIT_INTERRUPTED
    return code


def print_gameface(r: GFResult, node_label: str) -> None:
    print(f"  Verificacao do JS formatado: token a token" + (f" + {r.node} --check" if r.node else
                                                            f" (sem node: {node_label or 'desativado'})"))
    if r.dry_run:
        print(f"  Simulacao: {r.selected} ficheiros selecionados de {r.candidates}; seriam processados "
              f"{r.to_process}; reaproveitados {sum(r.unchanged.values())}"
              + (f"; fora do limite {r.limited}" if r.limited else "") + "\n")
        return
    if r.interrupted:
        print(f"  INTERROMPIDO: {sum(r.processed.values())} ficheiros processados (journal guardado; volte a "
              f"correr para retomar)\n")
        return
    print(f"  Selecionados {r.selected} de {r.candidates} | processados agora {r.to_process} {dict(r.processed)} | "
          f"reaproveitados {sum(r.unchanged.values())}" + (f" | retomados do journal {r.resumed}" if r.resumed else "")
          + (f" | fora do limite {r.limited}" if r.limited else ""))
    t = r.totals
    print(f"  Resultado: success {t.get('success', 0)} | partial {t.get('partial', 0)} | failed {t.get('failed', 0)}"
          f" | tipos {dict(r.kinds)}")
    print(f"  Formatados {r.formatted} (node ok {r.node_checked}) | views {r.views} | ligacoes ao Python "
          f"{dict(r.links)} | assets indexados {r.assets}" + (" | indice Python em cache" if r.pyindex_cached else ""))
    for p in r.problems[:10]:
        print(f"  ~ {p['status']:<8} {p['key']}: {p['error'][:160]}")
    if len(r.problems) > 10:
        print(f"  ... mais {len(r.problems) - 10} no relatorio")
    print(f"  [{r.elapsed:.1f} s]  Manifesto: {r.manifest_path}\n  Indice: {r.index_path}\n  Views: {r.views_doc}\n"
          f"  Relatorio: {r.report_path}\n")


def print_actionscript(r: ASResult) -> None:
    if r.tool:
        print(f"  Descompilador: FFDec {r.tool['version']}  ({r.tool['jar']}, java {r.tool['java']})")
    else:
        print(f"  Sem descompilador: {r.ffdec_error} -> so catalogo e declaracoes AS3")
    if r.dry_run:
        print(f"  Simulacao: {r.selected} SWF selecionados de {r.candidates}; seriam processados {r.to_process}; "
              f"reaproveitados {sum(r.unchanged.values())}" + (f"; fora do limite {r.limited}" if r.limited else "")
              + "\n")
        return
    if r.interrupted:
        print(f"  INTERROMPIDO: {sum(r.processed.values())} SWF processados (journal guardado; volte a correr "
              f"para retomar)\n")
        return
    print(f"  Selecionados {r.selected} de {r.candidates} | processados agora {r.to_process} {dict(r.processed)} | "
          f"reaproveitados {sum(r.unchanged.values())}" + (f" | retomados do journal {r.resumed}" if r.resumed else "")
          + (f" | fora do limite {r.limited}" if r.limited else ""))
    t = r.totals
    print(f"  Resultado: success {t.get('success', 0)} | extracted {t.get('extracted', 0)} | partial "
          f"{t.get('partial', 0)} | failed {t.get('failed', 0)} | unsupported {t.get('unsupported', 0)}")
    print(f"  ActionScript: {dict(r.code)} | classes {r.classes} ({r.unique_classes} distintas) | ficheiros .as "
          f"agora {r.scripts_files} | recursos agora {r.asset_files} | metodos nao descompilados {r.methods_failed}")
    if r.asasm_selected or r.asasm_done:
        print(f"  RABCDAsm (.asasm): {r.asasm_done} de {r.asasm_selected} SWF desmontados agora | ficheiros {r.asasm_files}")
    for p in r.problems[:10]:
        print(f"  ~ {p['status']:<8} {p['key']}: {p['error'][:160]}")
    if len(r.problems) > 10:
        print(f"  ... mais {len(r.problems) - 10} no relatorio")
    print(f"  [{r.elapsed:.1f} s]  Manifesto: {r.manifest_path}\n  Catalogo: {r.catalog_path}\n"
          f"  Relatorio: {r.report_path}\n")


def print_detection(result: DetectionResult, realms: list[str], elapsed: float) -> None:
    print(f"{TOOL_NAME} {__version__} - detecao ({elapsed:.1f} s)\n")
    for realm in realms:
        inst = result.selected.get(realm)
        print(f"[{realm}]")
        if inst is None:
            print(f"  NAO ENCONTRADO: {result.errors.get(realm, '?')}\n")
            continue
        v = inst.version
        print(f"  Instalacao : {inst.path}")
        print(f"  Fontes     : {', '.join(inst.sources)}")
        print(f"  Versao     : {v.number}{' ' + v.suffix if v.suffix else ''} (build #{v.build}, ramo {v.branch or '?'})")
        print(f"  Realm      : {inst.realm} (via {inst.realm_source})   cliente: {inst.app_type or '?'}")
        for key in ("res", "packages", "res_mods", "mods"):
            print(f"  {key:<11}: {inst.dirs.get(key) or '(em falta)'}")
        pk = inst.packages
        print(f"  Pacotes    : {pk.get('on_disk', 0)} no disco ({_human(pk.get('on_disk_bytes', 0))}), "
              f"{pk.get('active_for_app_type', 0)} ativos para '{inst.app_type}', "
              f"{len(pk.get('unlisted_on_disk', []))} fora do paths.xml")
        print(f"  Mods       : {len(inst.mods)} .wotmod; res_mods: {inst.res_mods.get('files', 0)} ficheiros")
        print(f"  res solto  : {inst.loose_res.get('files', 0)} ficheiros ({_human(inst.loose_res.get('bytes', 0))})")
        if inst.deep:
            for label, key in (("Jogo (.pkg)", "packages"), ("Mods", "mods")):
                c = inst.content.get(key, {})
                cats = c.get("categories", {})
                print(f"  {label}: {c.get('files', 0)} ficheiros | pyc {cats.get('python_bytecode', 0)} | "
                      f"swf {cats.get('scaleform', 0)} | gameface {c.get('gameface_entries', 0)} | "
                      f"xml {cats.get('xml', 0)} | json {cats.get('json', 0)} | web {cats.get('web', 0)}")
                if c.get("pyc_versions_sample"):
                    print(f"      bytecode (amostra): {c['pyc_versions_sample']}")
                holders = c.get("containers_with", {})
                if key == "packages" and holders:
                    print(f"      .pyc em: {', '.join(holders.get('python_bytecode', [])) or '-'}")
                    print(f"      .swf em: {', '.join(holders.get('scaleform', [])) or '-'}")
                    print(f"      Gameface em: {', '.join(holders.get('gameface', [])) or '-'}")
        for issue in inst.issues:
            print(f"  ! {issue}")
        print()
    others = [i for i in result.installs if i.realm not in realms]
    if others:
        print("Outras instalacoes (fora do ambito):")
        for i in others:
            print(f"  {i.realm:<3} {i.version_number:<10} {i.path}")
    if result.rejected:
        print(f"Candidatos rejeitados: {len(result.rejected)}")
        for i in result.rejected:
            print(f"  {i.path} [{', '.join(i.sources)}]: {'; '.join(i.issues)}")
