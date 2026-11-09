# wot-extractor — notas de desenvolvimento

Especificação completa: [`readme.txt`](../readme.txt).

## Utilização

```powershell
.\wot-extractor.cmd detect                 # deteta EU e CT, com sondagem dos .pkg
.\wot-extractor.cmd detect --quick         # sem abrir os .pkg (instantâneo)
.\wot-extractor.cmd detect --realm EU --path "D:\Games\World_of_Tanks_EU"
.\wot-extractor.cmd detect --json relatorios\detect.json

.\wot-extractor.cmd extract                       # EU + CT, perfil dev, incremental
.\wot-extractor.cmd extract --realm EU --dry-run  # so planear
.\wot-extractor.cmd extract --realm EU --profile gui -j 8
.\wot-extractor.cmd extract --realm CT --ext .pyc,.xml --pkg "scripts*"
.\wot-extractor.cmd extract --realm EU --force    # reextrair tudo
.\wot-extractor.cmd extract --realm EU --prune    # apagar o que saiu do jogo (so se a execucao for consistente)

.\wot-extractor.cmd decompile                     # EU + CT: .pyc -> .py ao lado, incremental
.\wot-extractor.cmd decompile --realm EU --dry-run
.\wot-extractor.cmd decompile --realm EU --glob "scripts/client/gui/*" --limit 200
.\wot-extractor.cmd decompile --realm EU --retry  # voltar a tentar partial/failed
.\wot-extractor.cmd decompile --realm EU --backend uncompyle6-py3 --retry

.\wot-extractor.cmd actionscript                  # EU + CT: catalogo SWF + FFDec (codigo e recursos)
.\wot-extractor.cmd actionscript --realm EU --glob "*/battle*.swf" -j 6
.\wot-extractor.cmd actionscript --realm EU --no-ffdec   # so catalogo e declaracoes AS3
.\wot-extractor.cmd actionscript --realm EU --no-assets  # so codigo
.\wot-extractor.cmd gameface                      # EU + CT: JS/CSS formatados, views, ligacoes ao Python
.\wot-extractor.cmd gameface --realm EU --glob "*/lobby/crew/*"   # so uma parte
.\wot-extractor.cmd gameface --realm EU --no-format      # so analise (sem copias formatadas)
.\wot-extractor.cmd stubs                         # EU + CT: stubs .pyi em __stubs/ (precisa do Python 2.7)
.\wot-extractor.cmd stubs --realm EU --stdlib     # incluir a biblioteca padrao que o jogo traz
.\wot-extractor.cmd update                        # depois de uma atualizacao do jogo: todas as fases, incremental
.\wot-extractor.cmd update --realm CT --steps extract,decompile   # so alguns passos
.\wot-extractor.cmd verify                        # hashes, saidas, orfaos e se a instalacao mudou (so leitura)
.\wot-extractor.cmd verify --realm EU --quick     # so tamanhos
.\wot-extractor.cmd report                        # report.json + REPORT.md por realm
.\wot-extractor.cmd index                         # indice de APIs (wot_api_index_<R>.sqlite)
.\wot-extractor.cmd search BarracksView           # pesquisar classes/funcoes/metodos/views nos dois realms
.\wot-extractor.cmd search BigWorld.callback --exact --realm EU
.\wot-extractor.cmd search onLoading --kind method --limit 50
.\wot-extractor.cmd compare                       # EU -> CT: ficheiros, API Python, AS3, Gameface (compare/)
.\wot-extractor.cmd purge --dry-run               # o que nao e do jogo (arvore mods) seria retirado
.\wot-extractor.cmd purge --yes                   # retirar a arvore mods (a instalacao nao e tocada)
.\wot-extractor.cmd clean --dry-run               # o que ja foi processado e seria apagado de sources/
.\wot-extractor.cmd clean --yes                   # apagar .pyc descompilados, XML binarios, SWF processados, trabalho
.\wot-extractor.cmd actionscript --asasm all      # desmontagem .asasm de todos os SWF (omissao: so os partial)
py -3 -m unittest discover -s tests -t .          # testes
```

Alternativa: `py -3 -m pip install -e .` cria o comando `wot-extractor`.
Requer Python ≥ 3.11 (usa `tomllib`); a ferramenta só usa a biblioteca padrão. O `decompile` precisa de um
Python 2.7 com `uncompyle6` (aqui `F:\Python27`) e, para a alternativa, de `uncompyle6` no Python 3 atual.
O `stubs` usa o mesmo Python 2.7 do `decompile` (só para ler a árvore sintática; nada é executado).
O `gameface` usa o Node.js (`node --check`, só verificação de sintaxe, nunca executa) se estiver no PATH.
O `actionscript` usa o FFDec (aqui `C:\Program Files (x86)\FFDec`, v26.2.1) com Java, se existir; sem ele,
produz só o catálogo e as declarações AS3.

Códigos de saída: `0` ok · `1` falha (realm não encontrado, escrita bloqueada, extração inconsistente) · `2` uso/configuração · `3` comando ainda não implementado · `130` interrompido (retomável).

## Estrutura

```text
src/wot_extractor/
  cli.py            CLI (argparse)
  config.py         wot_extractor.toml opcional (ver wot_extractor.example.toml)
  constants.py      realms, magic numbers .pyc, categorias por extensão
  safety.py         path traversal, WriteGuard (bloqueio de escrita no jogo), limites de zip
  logutil.py
  detect/
    sources.py      candidatos: Game Center, registo do Windows, pesquisa limitada nos discos
    xmlinfo.py      version.xml, game_info.xml, app_type.xml, paths.xml
    install.py      inspeção de uma instalação (diretórios, pacotes, mods, inventário)
    pkgprobe.py     leitura do diretório central dos .pkg/.wotmod (sem extrair)
    detector.py     escolha de uma instalação por realm
  extract/
    plan.py         plano: enumeração, filtros/perfis, precedência, sombreamento, sobreposições por mods
    validate.py     validação do conteúdo (XML/JSON/.pyc/SWF), versionada (VALIDATOR_VERSION)
    writer.py       escrita atómica (tmp + replace), SHA-256, caminhos longos \\?\
    manifest.py     leitura do manifesto e journal JSON-lines (retoma)
    engine.py       execução incremental/paralela, manifest.json, relatórios, .version_name
    xmldecode.py    passo de descodificação dos XML binários (processos, incremental)
  formats/
    bwxml.py        descodificador do XML binário BigWorld (packed section)
    swf.py          leitor SWF (FWS/CWS/ZWS, limite de descompressão), tags, catálogo, .swc
    abc.py          leitor ABC (AVM2) completo: classes, assinaturas, declarações AS3
    jsfmt.py        lexer e formatador de JavaScript/CSS minificados (só espaços), verificação token a token
  gameface/
    analyze.py      um ficheiro: tipo, formatação, webpack, referências (corre em processos paralelos)
    pylinks.py      índice do Python descompilado e ligações prováveis view <-> Python/ViewModel
    engine.py       execução incremental, views, layouts oficiais, índices, VIEWS.md, gameface_report.json
  stubs/
    _describe27.py  worker Python 2.7: descreve um módulo pela AST ou, se falhar, pelo bytecode (marshal)
    render.py       escrita dos .pyi (só informação verificada) e validação pelo parser do Python 3
    engine.py       módulos importáveis, cache das descrições, módulos sem código, __stubs/, stubs_report.json
  maintenance/
    update.py       diferenças entre manifestos, filtros anteriores, update_report.json (a ordem dos passos é no cli)
    verify.py       verificação só de leitura: SHA-256, saídas derivadas, órfãos, CRC no .pkg da instalação
    report.py       relatório global por realm (report.json, REPORT.md)
  decompile/
    _worker.py      worker externo (Py2.7/Py3): unmarshal + uncompyle6 + validação compile(PyCF_ONLY_AST)
    backends.py     descompiladores, deteção dos interpretadores, processos de trabalho (timeout/reinício)
    engine.py       execução incremental/paralela/retomável, estados, manifesto, decompile_report.json
  actionscript/
    ffdec.py        deteção do FFDec/Java e exportação (uma JVM por SWF, tempo limite)
    rabcdasm.py     RABCDAsm (abcexport + rabcdasm): desmontagem .asasm sem perdas
    engine.py       catálogo, código, recursos, sources_as/catalog.json, actionscript_report.json
tests/              unittest; instalações falsas em pastas temporárias + testes só-leitura nos clientes reais
```

## Roadmap

| Fase | Conteúdo | Estado |
|---|---|---|
| A | Fundação, configuração, segurança, deteção, `detect` | concluída |
| B | `extract`: .pkg/.wotmod/res/res_mods → `wot_src_<R>/sources`, manifest com hashes, limites de segurança | concluída |
| B.2 | Descodificador de XML binário BigWorld → `sources_xml/` | concluída |
| C | `decompile`: .pyc 2.7 (uncompyle6 em `F:\Python27`), validação sintática com parser 2.7, estados | concluída |
| D | `actionscript`: catálogo SWF, código AS3 (FFDec) ou declarações, recursos incorporados | concluída |
| E | `gameface`: HTML/CSS/JS, bundles, formatação de minificados, ligações a Python (prováveis) | concluída |
| F | `stubs`: geração de `.pyi` a partir de informação verificável | concluída |
| G | `update` / `verify` / `report`: incremental, comparação de manifests, retoma | concluída |

## Decisões técnicas (fase A)

1. **Ordem das fontes de deteção**: `--path` (CLI) > `wot_extractor.toml` > preferências do Game Center
   (`%ProgramData%\Wargaming.net\GameCenter\preferences.xml`, `<working_dir>`) > registo
   (`Uninstall`, HKCU/HKLM, 32/64 bits) > pesquisa nos discos (só pastas com nome típico, profundidade ≤ 2).
   O registo tem entradas obsoletas (ex.: `F:\WorldOfTanks_CT\...`), que são rejeitadas por validação.
2. **Realm** lido de `version.xml <meta><realm>`, verificado contra `game_info.xml <id>` (WOT.EU.PRODUCTION).
   Realms fora do âmbito (NA) são listados, mas não selecionados.
3. **Escolha quando há várias instalações do mesmo realm**: disco preferido (EU→`D:`, CT→`C:`),
   depois a versão/build mais alta e depois a fonte mais forte. As restantes ficam registadas em `issues`.
4. **Versão**: `number` (`2.4.2.0`), `suffix` (`Common Test`), `build` (`995`); `folder_name` (`2.4.2.0 Common Test`)
   é o nome usado em `res_mods/` e `mods/`. A pasta efetiva vem do `paths.xml`.
5. **Pacotes ativos** = os listados no `paths.xml` cujo `type` inclui o `app_type` do cliente (sd/hd).
   A ordem do `paths.xml` é guardada (`load_order`) para modelar a precedência na fase B.
6. **Sondagem** lê apenas o diretório central dos zip e 4 bytes de no máximo 16 `.pyc` por contentor.
   Os `.pkg` reais são ZIP *stored* (sem compressão).
7. **Segurança**: nenhum ficheiro do jogo é aberto para escrita; `WriteGuard` recusa qualquer destino dentro de
   uma instalação (incluindo o `--json`); nomes de membros com `..`, caminhos absolutos, nomes reservados do
   Windows ou caracteres inválidos são assinalados; XML com DTD/entidades é recusado.

## Decisões técnicas (fase B)

1. **Árvore de saída** (`wot_src_<R>/`):
   - `sources/res/<caminho virtual>`: conteúdo dos `.pkg` ativos fundido com o `res/` solto, tal como o jogo
     o vê. Os HTML do Gameface continuam a encontrar os bundles de outro `gui-part`.
   - `sources/res_mods/<versão>/...` e `sources/mods/<versão>/<nome>.wotmod/<conteúdo>`: caminhos originais.
     Os `.wotmod` são expandidos numa pasta com o nome do arquivo; `mods/configs/...` é copiado.
   - `sources_as/`, `sources_gameface/` e `__stubs/` são criados vazios e preenchidos nas fases D, E e F.
     Separar o Gameface por tipo (html/css/js) partiria as referências relativas, por isso a fonte de
     verdade fica em `sources/res` e a fase E gera vistas/manifestos.
2. **Precedência** (do `paths.xml`): `res_mods` → `mods` → pacotes pela ordem listada → `./res`. Dentro de
   `sources/res` ganha a primeira ocorrência; as perdedoras ficam em `shadows`. Os ficheiros de `res` substituídos
   no jogo por `res_mods`/`mods` ficam marcados com `overridden_by` (81 no EU, sobretudo do RemoveFog).
3. **Perfis**: `dev` (omissão: pyc/py, xml/def, json, web, swf/swc, fontes, texto + tudo sob `gui/gameface/`),
   `gui` (+ tudo sob `gui/`), `full` (tudo). Filtros adicionais: `--ext`, `--pkg`, `--tree`.
4. **Incremental**: uma entrada está inalterada se a origem (contentor, membro, tamanho, CRC32 do zip ou
   mtime do ficheiro solto) coincidir com o manifesto e a cópia existir com o mesmo tamanho. Só se reescreve
   o que mudou. Execuções filtradas mantêm no manifesto as entradas fora do âmbito.
5. **Ficheiros que saíram do jogo**: ficam no manifesto com `status: removed` e não são apagados; só o
   `--prune` os apaga, e apenas se a execução for consistente.
6. **Consistência**: só sem falhas. Nesse caso escreve-se `.version_name` (nome da pasta da versão, ex.:
   `2.4.2.0 Common Test`). Em caso de falha, o `.version_name` anterior é mantido. O manifesto anterior é
   guardado em `.state/manifest.prev.json` e cada relatório fica em `.state/reports/extraction_<UTC>.json`.
7. **Retoma**: cada entrada concluída é escrita em `.state/journal.jsonl`. Se a execução for interrompida
   (Ctrl+C → código 130), a seguinte reaproveita o journal. Os ficheiros são escritos de forma atómica, por
   isso nunca fica um ficheiro meio escrito com o nome final.
8. **Integridade**: o `zipfile` verifica o CRC32 de cada membro lido; o SHA-256 é calculado durante a escrita
   e o tamanho é confirmado.
9. **Validação** (`validate.py`, versão no manifesto): XML → `packed` (binário BigWorld), `valid`,
   `valid_bigworld` (prefixos de tag não declarados, ex.: `<xmlns:xmlref>`) ou `invalid`; JSON → `valid`,
   `valid_jsonc` (comentários, ex.: tsconfig.json) ou `invalid`; `.pyc` → versão CPython; SWF → assinatura
   FWS/CWS/ZWS e versão; `.swc` → ZIP. Quando a versão do validador muda, as entradas inalteradas são
   revalidadas a partir da cópia extraída, sem reescrita.
10. **Caminhos longos**: a escrita usa `\\?\` (neste PC o `LongPathsEnabled` está a 0). O relatório conta os
    destinos com mais de 259 caracteres (0 no perfil dev; possível no perfil `full`).
11. **Segurança**: o `resolve_within` é lexical (sem `Path.resolve()` por ficheiro, que tem corridas no
    Windows com pastas criadas em paralelo); a pasta `wot_src_<R>` é validada uma vez pelo `WriteGuard`.

## Decisões técnicas (fase B.2 — XML binário BigWorld)

1. **Formato** (documentado em `formats/bwxml.py`): magic `45 4E A1 62`, 1 byte de versão, dicionário de
   nomes terminados em `\0`, e uma árvore de elementos com descritores `uint32` (28 bits de fim de bloco +
   4 bits de tipo). Tipos: 0 elemento aninhado, 1 string, 2 inteiro (0/1/2/4/8 B), 3 floats (12 floats =
   matriz `row0..row3`), 4 booleano, 5 binário (base64).
2. **Verificação estrutural**: cada elemento aninhado tem de ocupar exatamente o seu bloco e o ficheiro tem de
   ser consumido por completo. Bytes a mais no fim → `partial`; qualquer incoerência → `failed`, com a
   mensagem técnica. Resultado real: **9949/9949 `success`** (EU 5171, CT 4778).
3. **Saída**: `sources_xml/<árvore>/<caminho>` (extensão à estrutura da especificação). O original binário em
   `sources/` nunca é alterado (regra 3), e cópia e original ficam claramente separados. Cada cópia começa
   com um comentário que identifica o original.
4. **Fidelidade**: as tags com prefixo BigWorld (`<xmlns:xmlref>`, `<xmlns:germany>`) ficam tal como estão,
   como nos XML de texto do jogo (validação `valid_bigworld`). Só nomes inválidos para qualquer parser (ex.:
   começados por dígito) seriam renomeados com `_` (0 casos reais). Os floats usam a representação decimal mais
   curta que reproduz exatamente o float32, sem expoente (`20`, não `2e+01`).
5. **Manifesto**: campo `decoded` em cada entrada binária (`path`, `status`, `decoder`, `sha256`, `size`,
   `elements`, `validation`, avisos). `tool_versions.bwxml_decoder` regista a versão do descodificador.
6. **Incremental**: só se volta a descodificar se o original mudou, se a cópia faltar ou se `DECODER_VERSION`
   mudar. Os ficheiros que deixam de ser binários perdem a cópia antiga; o `--prune` também remove a cópia.
7. **Consistência**: uma falha de descodificação **não** torna a extração inconsistente (os originais estão
   corretos), mas fica em `xml_decode.failures` no relatório.
8. **Desempenho**: ~215 MB de XML por realm. Corre em processos (`ProcessPoolExecutor`, `-j`); com 8
   processos leva ~10 s. Abaixo de 64 ficheiros corre em série. Desativável com `--no-decode-xml`.

## Decisões técnicas (fase C — descompilação dos .pyc)

1. **Onde corre**: o descompilador e a validação correm em interpretadores externos (`decompile/_worker.py`,
   compatível com 2.7 e 3.x), com pedidos em linhas JSON. O worker não abre ficheiros: recebe os bytes do
   `.pyc` e devolve o `.py`, ambos em base64. **O bytecode nunca é executado**: é lido com `xdis` (unmarshal),
   convertido pelo `uncompyle6` e o texto só é analisado com `compile(..., ast.PyCF_ONLY_AST)`.
2. **Cadeia de descompiladores** (`--backend auto`): `uncompyle6` 3.9.2 no Python 2.7 (primário, a origem é 2.7)
   e, se não der `success`, `uncompyle6` 3.9.3 no Python 3. **A validação é sempre feita pelo parser do
   Python 2.7**, nunca pelo de Python 3, para não aceitar código que só seria válido noutra versão.
3. **Estados** (campo `decompiled` de cada `.pyc` no manifesto): `success` (sem erros, sem secções falhadas e
   sintaxe 2.7 válida), `partial` (há código, mas com secções falhadas `--- This code section failed: ---`,
   erro do descompilador depois de gerar o texto, ou sintaxe inválida), `failed` (nenhum código: erro, tempo
   limite, worker terminado), `unsupported` (versão de bytecode sem descompilador validado; só 2.7 é suportado,
   sem conversões de bytecode moderno). `unchanged` é o estado da execução para resultados reaproveitados.
   Cada `partial`/`failed` tem a mensagem técnica (`error`) e a lista de tentativas (`attempts`).
4. **Saída**: `sources/<árvore>/<caminho>.py`, ao lado do `.pyc`, preservando módulos e packages (regra 2 da
   especificação). A 1.ª linha identifica o ficheiro como **descompilado** e a ferramenta usada; os `partial`
   têm um aviso no fim. Se o jogo trouxer um `.py` original com o mesmo nome, esse nunca é substituído: a
   descompilação vai para `<nome>.decompiled.py`. A declaração de codificação é acrescentada (2.ª linha) só
   quando há bytes não-ASCII; não altera os literais `str` de Python 2.
5. **Tentativas sem perder resultados**: um resultado pior nunca substitui um melhor para o mesmo `.pyc`
   (`kept_previous`); as tentativas não escolhidas que produziram código ficam em
   `.state/decompile/attempts/<backend>/`. `--retry` volta a tentar `partial`/`failed`; mudar a cadeia (outra
   versão do uncompyle6) também os volta a tentar automaticamente.
6. **Incremental**: reaproveita quando o SHA-256 do `.pyc` (`input_sha256`) e o `.py` escrito não mudaram.
   O `.pyc` lido de `sources/` é verificado contra o SHA-256 do manifesto. O `extract` preserva o campo
   `decompiled` dos `.pyc` inalterados e o `--prune` apaga também o `.py` descompilado.
7. **Robustez**: um worker por thread (`-j`), tempo limite por ficheiro (`--timeout`, omissão 120 s; o worker é
   reiniciado), pilha de 192 MB para a recursão do uncompyle6, journal `.state/decompile_journal.jsonl` para
   retomar após Ctrl+C, e bloqueio `.state/lock` para `extract` e `decompile` não alterarem a mesma árvore
   ao mesmo tempo.
8. **Relatórios**: `decompile_report.json` (e cópia datada em `.state/reports/`) com contagens, cadeia e
   interpretadores usados e a lista completa de `failed`/`partial`/`unsupported`; resumo em `manifest.decompile`.
9. **Resultado real** (2026-11-08, `-j 8`, ~6 min por realm; segunda passagem ~2 s):
   EU 12 392 `.pyc` → 12 373 `success`, 14 `partial`, 5 `failed`; CT 11 666 → 11 649 / 14 / 3; 0 `unsupported`.
   A alternativa em Python 3 resolveu 3 ficheiros por realm (2 com recursão excessiva no 2.7, 1 com tempo
   limite) e deu `partial` em 12 que o 2.7 não conseguia de todo. Verificação independente: SHA-256 de todas
   as saídas igual ao manifesto e 400 `success` por realm aceites pelo `compile()` do Python 2.7.
10. **Interpretadores**: `--python27`/`--python3`, `[decompile]` no `wot_extractor.toml`, variável
   `WOT_EXTRACTOR_PY27`, lançador `py -2.7` ou pastas habituais `X:\Python27`. Cada um é sondado (versão e
   presença do uncompyle6) antes de ser usado.

## Decisões técnicas (fase D — ActionScript/Scaleform)

1. **Leitor próprio** (`formats/swf.py`, `formats/abc.py`, só biblioteca padrão): descomprime FWS/CWS/ZWS com
   limite de 512 MB, percorre as tags e lê **por completo** cada bloco ABC (constantes, métodos, classes,
   scripts, corpos), com verificação de limites e de consumo total. Nunca executa nada. Serve para o
   catálogo, para verificar o que o FFDec exportou e para as declarações quando não há FFDec.
2. **Catálogo** `sources_as/swf/<chave>.json`: cabeçalho, compressão, tags, ActionScript (as3/as2/none),
   classes (herança, interfaces), `SymbolClass`, `ExportAssets`, `ImportAssets2` (bibliotecas partilhadas),
   fontes, etiquetas, avisos. Índice global `sources_as/catalog.json` com **classe → SWF(s)** que a definem.
3. **Código** `sources_as/scripts/<chave>/`: o FFDec (`-export script`, formato `as`) descompila o AS3 completo.
   A saída é verificada: classes esperadas (pelo ABC) sem ficheiro, métodos com
   `Not decompiled due to ...` e linhas `§§` (fluxo não reconstruído) tornam o SWF `partial`. Sem FFDec, ou se
   este falhar, ficam **declarações** (pacote, classe, herança, campos, constantes, assinaturas e valores por
   omissão, tudo lido do ABC; corpos vazios com o tamanho do bytecode), marcadas como tal na 1.ª linha.
4. **Recursos** `sources_as/assets/<chave>/{images,fonts,sounds,binaryData,symbolClass}` pelo FFDec (PNG/JPEG,
   TTF, MP3/WAV, dados em bruto, mapa símbolo→classe). O SWF original continua intacto em `sources/`.
5. **Estados** (campo `actionscript` do manifesto): `success`, `partial`, `failed`, `extracted` (sem código),
   `unsupported` (AS1/2 sem descompilador). Com `error` técnico e contagens (ficheiros, métodos falhados,
   classes em falta, recursos).
6. **Execução**: uma JVM por SWF (`-j`, `-Xmx` em `java_heap`), primeiro os que têm mais bytes de ABC (os
   lentos) e **no máximo `--heavy-jobs` (2) SWF pesados** (ABC ≥ 2 MB: lobby, battle e variantes) em
   simultâneo — com 6 em paralelo a RAM física esgotou-se. Tempo limite por SWF (`--timeout`, omissão 3600 s)
   passado também ao FFDec como `-exportTimeout` (o FFDec corta a exportação aos 1800 s por omissão, o que
   deixava o lobby e os battle incompletos), e por método/classe no próprio FFDec. "Java sem memória" é
   detetado no registo e indicado no erro. A JVM corre na pasta temporária `.state/as_tmp` (os
   `hs_err_pid*.log` não poluem o projeto; o fim do registo fica no erro do manifesto). Mover para `sources_as/` tolera bloqueios temporários do Windows (novas
   tentativas; por fim copia e apaga). As classes que o FFDec não exportou ficam com as declarações do ABC;
   journal e bloqueio como no `decompile`. Incremental pelo SHA-256 do SWF e pela assinatura das ferramentas
   (versões do leitor e do FFDec); `--retry`/`--force`. O `extract` preserva o estado e o `--prune` apaga as
   saídas dos SWF removidos. `.swc`: o `library.swf` é lido de dentro do ZIP.
7. **Maiúsculas/minúsculas**: o NTFS não as distingue e os SWF da WG têm pacotes como `net.wg.data.VO` e
   `net.wg.data.vo` (battle, lobby): ficam na mesma pasta. A verificação das classes exportadas ignora a
   caixa, as declarações nunca substituem um ficheiro do FFDec, e os pares ficam em `case_collisions`.
8. **RABCDAsm** (o que vem com o XVM em `xvm-master/src_build/bin/windows_i686/rabcdasm`, configurado em
   `wot_extractor.toml`): desmonta o ABC em assembly AVM2 (`.asasm`) sem perdas. Integrado — ver "Melhorias".
9. **Resultados reais (2026-11-09, FFDec 26.2.1)**:

   | | SWF | success | extracted | partial | failed | ficheiros .as | recursos | classes em falta |
   |---|---|---|---|---|---|---|---|---|
   | EU | 817 | 780 | 26 | 11 | 0 | 45 269 | 14 950 | 0 |
   | CT | 760 | 727 | 26 | 7 | 0 | 35 458 | 13 912 | 0 |

   Os `partial` são só 2 linhas `§§` num método de `BranderVehicle2dMarker` (marcadores de veículos), repetido
   nos SWF de batalha e no `gui_battle` .swc. `sources_as` ≈ 750 MB por realm. Execução completa ~30–40 min
   por realm (o `lobby.swf`, 4954 classes e 14 MB de ABC, leva ~25 min sozinho no FFDec); reexecução sem
   alterações < 1 s.

## Decisões técnicas (fase E — Gameface)

1. **Seleção**: os ficheiros `web` (`.html/.css/.js/.mjs/.ts/.unbound`) e tudo o que está em `*/gui/gameface/`
   ou `gui/unbound/`. Imagens, fontes, JSON e afins dessas pastas ficam em `sources/` e são só indexados em
   `sources_gameface/assets/index.json` (não são duplicados).
2. **Formatação** (`formats/jsfmt.py`, só biblioteca padrão): um lexer de JavaScript (strings, templates com
   `${}` aninhados, regex vs divisão — incluindo o `)` de `if/for/while`, comentários, `#privado`) reescreve
   os ficheiros minificados acrescentando **só** quebras de linha e indentação em pontos seguros (depois de
   `{` e `;` fora de parênteses, antes de `}`, entre `}` e uma nova instrução, entre `},` de propriedades).
   Nunca remove uma quebra de linha original (a inserção automática de `;` depende delas). Cada resultado é
   **verificado**: o lexer volta a ler a cópia e a sequência de tokens tem de ser idêntica; com o Node.js
   presente, a cópia passa também no `node --check` (se só o original passar, a cópia é apagada e o ficheiro
   fica `partial`). O CSS é formatado e verificado da mesma forma. No HTML só são formatados os scripts/estilos
   inline minificados que não sejam bibliotecas de terceiros (`@license`). Cada cópia começa com um cabeçalho
   a dizer que **não é o código-fonte original**.
3. **Webpack 5**: de cada bundle lê-se `__webpack_modules__` (id → linha na cópia formatada), os chunks
   (`self.webpackChunkgameface.push([[ids],{módulos}])`), o módulo de entrada e os chunks exigidos
   (`__webpack_require__.O(void 0,[ids],()=>__webpack_require__(id))`). Índice módulo → ficheiros.
4. **Referências** por ficheiro: `R.views.*` (views filhas), `R.strings/images/...`, `engine.call/on/trigger`,
   `viewEnv.*`, comandos (`createCallback(..., "onX")`) e os nomes de propriedades/strings usados.
5. **Views**: pastas de `_dist/production` com um `.html` (incluindo as `mono/.../main.html` + `bundle.js`) e os
   layouts `.unbound`. O **id oficial** vem de `gui/gen_resources/gameface_layouts.json` e `unbound_layouts.json`
   (um por feature: `res/<feature>/gui/gen_resources/`), que mapeiam `R.views.<id>` → ficheiro, com `entrance` e
   `impl`. Sem entrada nesses ficheiros, o id é deduzido pela pasta e assinalado. Ficheiros sobrepostos por
   mods: fica registado qual é o efetivo e quais existem.
6. **Ligações ao Python — prováveis**: índice do Python descompilado (`R.views.<id>` com ficheiro e linha,
   `model=X`/`ViewComponent[X]`, ViewModels gerados com propriedades e comandos, incluindo herança) e caminhos
   `coui://...html` em Python/XML/JSON. Por view: ficheiros que usam o id, o ViewModel (pelo `model=` desses
   ficheiros ou pela convenção `view_models/views/<caminho>/<nome>_model.py`) e quantos dos seus nomes aparecem
   no JS da view e dos seus chunks. Confiança: `provavel-forte` (referências + ViewModel com ≥ 50% dos nomes no
   JS, ou caminho coui:// referido fora dos layouts), `provavel`, `nao-encontrada`. Nunca "certa".
7. **Saídas**: `sources_gameface/{js,css,html}/<chave>` (cópias formatadas), `manifests/files/<chave>.json`
   (análise), `manifests/views/<R id>.json`, `manifests/index.json`, `manifests/python_links.json`,
   `assets/index.json`, `VIEWS.md` (tabela das views para desenvolvimento de mods) e `gameface_report.json`.
   Estado no manifesto (campo `gameface`): `success`/`partial`/`failed`. Incremental pelo SHA-256 e pela
   assinatura (versões do analisador/formatador e do node); o índice do Python fica em cache
   (`.state/gameface_pyindex.json`) até mudar a extração ou a descompilação. Processos paralelos (`-j`).
8. **Resultados reais (2026-11-09)**:

   | | ficheiros | success | partial | formatados (node ok) | views (id oficial) | forte / provável / não encontrada |
   |---|---|---|---|---|---|---|
   | EU | 2937 | 2937 | 0 | 754 (754) | 713 (713) | 303 / 324 / 86 |
   | CT | 2741 | 2741 | 0 | 700 (700) | 668 (668) | 285 / 304 / 79 |

   ~35 s por realm (a 1.ª vez inclui o índice do Python, ~3 min no CT); reexecução sem alterações ~3 s. 81
   layouts do EU não têm ficheiro (views de demonstração de desenvolvimento, não distribuídas).

## Decisões técnicas (fase F — stubs)

1. **Módulos**: cada `.pyc`/`.py` em `scripts/client`, `scripts/client_common` ou `scripts/common` (de `res`,
   das features `res/<feature>/` e dos mods) dá o módulo importável correspondente (`__init__` → pacote). Os
   ficheiros sobrepostos por mods ficam de fora (conta o efetivo); com o mesmo nome em duas raízes, ganha o
   pacote e depois `client` > `client_common` > `common`. A biblioteca padrão que o jogo traz
   (`scripts/common/Lib`) só entra com `--stdlib` (as IDEs têm a sua).
2. **Leitura**: um worker no **Python 2.7** (o código do jogo é Python 2) lê a árvore sintática com
   `compile(..., PyCF_ONLY_AST, dont_inherit=True)` — nada é executado. Se o código descompilado não for válido
   ou a descompilação tiver falhado, lê o **bytecode** (`marshal`): nomes de classes, funções, parâmetros,
   `*args/**kwargs`, quantos parâmetros têm valor por omissão (pelo `MAKE_FUNCTION` do pai), imports e nomes
   atribuídos. Bytecode ilegível (mods ofuscados) → `failed`.
3. **O que entra no stub** (só verificável): imports (reexportados com `as`, como em tempo de execução; os
   imports relativos implícitos do Python 2 tornam-se `from . import x` quando o módulo irmão existe), classes
   com bases simples e `metaclass` (de `__metaclass__`), decoradores `property/staticmethod/classmethod/
   abstractmethod/x.setter` (os outros ficam em comentário: podem mudar a assinatura), métodos e funções com
   os nomes dos parâmetros e valores por omissão literais (os outros como `...`), docstrings (até 30 linhas),
   atributos de classe, atributos de instância atribuídos com `self.x = ...`, constantes de módulo com o
   valor literal (`X = 5`) ou o tipo do literal (`X: tuple`). O resto é `Any`, que significa *desconhecido*;
   nunca são escritos tipos de retorno nem de parâmetros. A última definição com o mesmo nome prevalece.
   Nomes que são palavras reservadas em Python 3 (ex.: `async`) são omitidos e listados. Stubs do bytecode
   terminam em `def __getattr__(name) -> Any` (stub incompleto).
4. **Módulos sem código** (nativos do motor como `BigWorld`, `ResMgr`, `Math`, `GUI`, ou ausentes do
   cliente): só os membros que o Python usa, com `*args/**kwargs` e um comentário com o uso observado
   (quantas chamadas, quantos argumentos posicionais, keywords, imports). Excluem-se a biblioteca padrão do
   2.7 e do Python 3 e os imports relativos implícitos.
5. **Validação**: cada `.pyi` passa pelo parser do Python 3; se falhar, é regenerado sem docstrings e, em
   último caso, fica um stub mínimo marcado `failed`.
6. **Incremental**: as descrições ficam em cache (`.state/stubs_desc/`) pela assinatura da entrada (SHA-256
   do `.pyc` e do `.py` descompilado); só são reescritos os `.pyi` que mudam; os de módulos que desapareceram
   são apagados. Sem alterações (mesmos módulos, entradas e versões) a execução termina logo.
7. **Uso**: `python.analysis.stubPath` do VS Code/Pylance a apontar para `wot_src_EU/__stubs`
   (ver `__stubs/README.md`); índice em `__stubs/stubs_index.json`.
8. **Resultados reais (2026-11-09)**:

   | | módulos | success | partial (bytecode) | failed | classes | funções | módulos sem código |
   |---|---|---|---|---|---|---|---|
   | EU | 11 169 | 11 151 | 16 | 2 | 21 152 | 128 442 | 71 |
   | CT | 10 446 | 10 430 | 16 | 0 | 20 110 | 123 621 | 70 |

   Os `failed` do EU são dois `.pyc` ofuscados de mods de terceiros. Todos os `.pyi` passam no parser do Python 3.
   ~4 min por realm na 1.ª vez; reexecução sem alterações < 1 s; com `--force` o resultado é idêntico.

## Decisões técnicas (fase G — update, verify, report)

1. **`update`** = os comandos normais, por ordem, através do mesmo parser da CLI (mesmas opções por omissão):
   deteção da versão instalada vs `.version_name` (primeira extração / mesma versão / NOVA VERSÃO), `extract`
   com os **mesmos filtros da extração anterior** (perfil, extensões, pacotes, árvores — um perfil diferente
   marcaria ficheiros como removidos), diferenças face ao manifesto anterior por SHA-256 (novos, alterados,
   removidos), e depois `decompile`, `actionscript`, `gameface`, `stubs` (cada um só reprocessa o que mudou).
   Se a extração não for consistente o update **para**: a versão não avança (o `extract` só escreve
   `.version_name` numa execução consistente) e nada é apagado. Uma fase seguinte que falhe não impede as
   outras. `--prune` só a pedido. `update_report.json` + `.state/reports/update_<data>.json` (os anteriores
   ficam). `--steps`, `--skip`, `--retry`, `-j`, `--heavy-jobs`, `--dry-run`. Interrompido → volta a correr.
2. **`verify`** (só leitura; escreve apenas `verify_report.json`): `.version_name` = manifesto e extração
   consistente; cada ficheiro de `sources/` com o tamanho e o SHA-256 do manifesto (`--quick`: só tamanho);
   saídas das fases C–F (SHA-256 dos `.py` descompilados e dos XML descodificados; existência das restantes e
   dos `.pyi`); ficheiros órfãos em `sources/` (os removidos do jogo mas mantidos sem `--prune` são contados à
   parte); e a **instalação**: versão instalada e, por ficheiro, CRC/tamanho no diretório central do
   `.pkg`/`.wotmod` (sem descomprimir) ou tamanho/data dos ficheiros soltos → `update_needed`. Código de saída 1
   só para problemas de integridade (uma árvore desatualizada não é corrupção).
3. **`report`**: junta manifesto, relatórios das fases e a última `verify` em `report.json` e `REPORT.md`:
   versão, instalação, estado de cada fase, ficheiros não totalmente recuperados (os primeiros 25 por fase),
   versões das ferramentas e uma tabela do **conteúdo de cada pasta** — originais (`sources/`), descodificados
   (`sources_xml/`), descompilados (`.py` em `sources/`, AS3 em `sources_as/`), formatados
   (`sources_gameface/`, não são o original) e gerados (`__stubs/`) — com número de ficheiros e tamanho.
4. **Resultados reais (2026-11-09)**: `verify` EU 22 122 ficheiros (845 MB) com SHA-256 OK, todas as saídas
   presentes, 0 órfãos, instalação igual (110 s). `verify` CT detetou **339 ficheiros alterados na instalação**
   (o `driftkings.wotmod` reconstruído e configurações do mod alteradas ao jogar, mesma versão); o `update` CT
   extraiu 9 novos + 334 alterados, descompilou só 307 `.pyc`, 2 SWF, 10 ficheiros Gameface, descreveu 307
   módulos (7 `.pyi` mudaram), 141 s; a seguir a `verify` deu a instalação igual. `update` sem alterações: ~45 s
   (a extração tem de ler os 538 689 ficheiros/membros da instalação).

## Melhorias após a fase G (2026-11-09)

1. **RABCDAsm no `actionscript`**: passo à parte, depois do FFDec, para não invalidar os resultados deste.
   `--asasm partial` (omissão: só os SWF `partial`), `all` ou `none`. Uma cópia do SWF (ou o `library.swf` do
   `.swc`) numa pasta temporária passa por `abcexport` e `rabcdasm`; as pastas `<bloco>/` vão para
   `sources_as/asasm/<chave>/`. No manifesto (`actionscript.asasm`): pasta, blocos, ficheiros e, para cada `.as`
   com linhas `§§`, o `.class.asasm` correspondente (o RABCDAsm renomeia pastas que colidem, ex.: `vo_`).
   Incremental pelo SHA-256 do SWF. Configuração: `[actionscript] rabcdasm`, `--rabcdasm` ou
   `WOT_EXTRACTOR_RABCDASM`. Real: EU 11 SWF (31 053 + 732 ficheiros), CT 7 (18 496); o `§§` de
   `BranderVehicle2dMarker.as` aponta para `movie-0/net/wg/gui/battle/views/vehicleMarkers/BranderVehicle2dMarker.class.asasm`.
2. **Índice de APIs** (`index`, `search`; `apiindex.py`): uma base SQLite FTS5 por realm
   (`wot_api_index_<R>.sqlite` na pasta de saída), construída num ficheiro novo e trocada no fim. Conteúdo:
   módulos, classes, funções, métodos (com a assinatura verificada), atributos e constantes do Python (das
   descrições dos stubs, com ficheiro:linha no `.py` descompilado), membros dos módulos sem código, classes AS3
   (catálogo) e métodos/propriedades AS3 (dos `.as` do FFDec, uma vez por classe), views Gameface e
   propriedades/comandos dos ViewModels (ligação provável). Pesquisa por prefixo nos nomes, nomes qualificados e
   1.ª linha das docstrings; `--exact`, `--kind`, `--realm`, `--json`. Assinatura pelo conteúdo (reexecutar uma
   fase sem mudanças não o reconstrói). Também é o último passo do `update`. Real: EU 521 201 símbolos, CT 498 234,
   ~15 s por realm.
3. **Comparação de realms** (`compare`; `compare.py`): ficheiros por caminho (pastas de versão de `mods/` e
   `res_mods/` normalizadas) e SHA-256; API Python (novos, removidos, assinaturas alteradas) a partir do índice;
   classes AS3; views Gameface e membros dos ViewModels. `compare/compare_<A>_<B>.json` e `COMPARE_<A>_<B>.md`
   (listas da API limitadas a 1500 por tipo; totais completos). Real EU 2.4.1.1 → CT 2.4.2.0: ficheiros +179 /
   −1639 / ~1425; módulos Python +86 / −805 (sobretudo os eventos `halloween` e `fort_rush`, ausentes no CT);
   24 assinaturas alteradas; views +8 (advent_calendar) / −53; ~4 s.

4. **`purge`** (`maintenance/purge.py`): retira de `wot_src_<R>` conteúdo que não é do jogo — por omissão a
   árvore `mods` (todos os `.wotmod` e `mods/configs` são de terceiros). Apaga o ficheiro em `sources/` e todas
   as saídas derivadas (XML, `.py`, AS3/asasm, Gameface, `.pyi`, caches), tira as entradas do manifesto, limpa as
   marcas `overridden_by` (os ficheiros de `res` voltam a ser os efetivos) e retira a árvore dos filtros do
   manifesto, para o `update` não a voltar a extrair. Exige `--yes` (ou `--dry-run`). A instalação não é tocada;
   recupera-se com `extract --tree mods`. **2026-11-09**: a pedido, foram retirados os mods de ambos os realms
   (driftkings, Driftkings.RemoveFog, poliroid modslistapi/replaysmanager, openwg gameface, mods/configs/driftkings):
   EU 765 entradas / 1961 saídas, CT 705 / 1850. Atenção: um `extract` manual sem `--tree` usa todas as árvores e
   volta a trazer `mods` (o `update` não, porque reutiliza os filtros do manifesto).

5. **`clean`** (`maintenance/clean.py`; também o último passo do `update`): apaga de `sources/` o que já tem
   forma processada — `.pyc` com descompilação `success` (e o `.py` presente), XML binários com a cópia
   `success` em `sources_xml/`, `.swf/.swc` com estado `success`/`extracted` e catálogo — e ficheiros de trabalho
   em `.state/` (tentativas de descompilação, temporários do actionscript, cache do índice Python do Gameface,
   `.tmp`, relatórios antigos — ficam 3 por tipo). Ficam os `.pyc` partial/failed e os SWF partial (precisos para
   `--retry`, stubs pelo bytecode e RABCDAsm) e `.state/stubs_desc` (fonte do índice de APIs e do `compare`).
   Cada ficheiro apagado fica marcado `cleaned` no manifesto: a extração considera-o inalterado enquanto a origem
   não mudar (não reextrai), `decompile`/`actionscript`/descodificação de XML reaproveitam os resultados, a
   `verify` conta-o à parte. Se o jogo mudar o ficheiro, é extraído e processado de novo e o `update` volta a
   limpá-lo no fim. `--only`/`--keep pyc|xml|swf|state`, `--dry-run`, `--yes`. Limitação: com o ficheiro limpo
   não se pode forçar o reprocessamento (`--force`) sem reextrair (`extract --force`).

## Factos verificados nos clientes (2026-11-08)

- EU `D:\Games\World_of_Tanks_EU`: 2.4.1.1 #993, hd, 229 pkgs (94 GB).
- CT `C:\Games\World_of_Tanks_CT`: 2.4.2.0 Common Test #995, sd, 126 pkgs (58 GB).
- Todos os `.pyc` amostrados são CPython 2.7 (magic `03f30d0a`). Existem `.pyc` em `scripts.pkg` e em
  pacotes de modos de jogo (comp7, frontline, story_mode, ...), não só em `scripts.pkg`.
- SWF em `gui-part1..4.pkg` e em pacotes de modos; Gameface em `gui/gameface/_dist/production` (gui-part1..4).
- O cliente junta os pacotes num sistema de ficheiros virtual (ex.: um HTML do gui-part2 referencia um
  bundle no gui-part4). A extração deve resolver por caminho virtual e não por arquivo.

## Limitações conhecidas

- A pesquisa nos discos não percorre o disco inteiro; instalações em pastas sem nome típico exigem
  configuração manual.
- A tabela de magic numbers só cobre CPython 2.7 e 3.6–3.13; os outros aparecem como `unknown:<n>`.
- As cópias de `sources_xml/` são uma interpretação: a ordem e a estrutura dos elementos são preservadas,
  mas a formatação (indentação, espaços à volta dos valores) não é a do XML de texto que originou o binário,
  que não é recuperável. Não se garante a reconversão byte a byte para binário.
- Os campos de tipo 5 (binário) aparecem em base64; o significado desses blobs não é interpretado.
- Junctions/links simbólicos criados à mão dentro de `wot_src_<R>` não são detetados (a validação de caminhos
  é lexical).
- Pacotes não carregados pelo cliente (fora do `paths.xml` ou de outro tipo sd/hd) não são extraídos; ficam
  listados em `skipped_containers`.
- Os `.wotmod` de outras versões (`mods/<outra versão>/`) não são extraídos.
- Descompilação: `success` significa sintaxe 2.7 válida sem secções falhadas, não equivalência semântica
  garantida com o original (o uncompyle6 pode, raramente, reconstruir mal uma construção válida). Os nomes
  de variáveis locais, comentários e formatação originais não são recuperáveis. Só bytecode 2.7 é suportado.
- Índice/comparação: só tão bons como as fases que os alimentam (sem `stubs` não há API Python; métodos AS3
  só dos `.as` do FFDec). Uma classe AS3 presente em vários SWF tem os membros indexados uma vez. A comparação
  de constantes conta mudanças de valor literal como "assinatura alterada".
- Manutenção: a `verify` compara ficheiros soltos por tamanho e data (como o `extract`), por isso um ficheiro
  reescrito com o mesmo conteúdo aparece como alterado até ao próximo `update` (que o reconhece pelo SHA-256).
  O `update` não deteta ficheiros novos na instalação sem correr a extração (é ela que enumera tudo).
- Stubs: as assinaturas vêm do código descompilado; decoradores desconhecidos (ex.: `adisp_process`,
  `wg_async`) podem alterar a assinatura real e ficam só em comentário. Não há tipos (nem de retorno), só
  `Any`. Os módulos sem código listam apenas os membros usados. O Pylance analisa como Python 3.
- Gameface: a cópia formatada **não é o código-fonte original** (nomes encurtados e comentários perdidos
  continuam perdidos); a verificação garante só que os tokens são os mesmos. As ligações ao Python são
  prováveis; views usadas por caminhos construídos dinamicamente aparecem como `nao-encontrada`. Só o
  TypeScript em `gui/gameface/scripts/migration-ui/src` e `@types` é código original.
- ActionScript: o FFDec é uma ferramenta externa; a sua saída não é validada por um compilador AS3, só pelas
  marcas de falha que o próprio FFDec deixa e pela lista de classes do ABC. As declarações (sem FFDec) não têm
  corpos. Os recursos externos Scaleform (tags 1000+) só são catalogados (não existem nos clientes atuais).
- Os `.py` descompilados ficam ao lado dos `.pyc` em `sources/`; a distinção faz-se pela 1.ª linha e pelo
  manifesto. Se o `extract` atualizar um `.pyc`, o `.py` antigo fica até à próxima execução de `decompile`.
