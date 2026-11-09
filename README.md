# wot-extractor

Ferramenta em Python 3 (só biblioteca padrão) para extrair, descompilar e documentar o cliente do
**World of Tanks** (EU e Common Test) em árvores de fontes independentes, para análise, pesquisa de APIs e
desenvolvimento de mods Python, ActionScript/Scaleform e Gameface.

| Branch | Conteúdo |
|---|---|
| `main` | a ferramenta (este branch, licença MIT) |
| [`EU`](../../tree/EU) | cliente EU extraído e descompilado |
| [`CT`](../../tree/CT) | cliente Common Test extraído e descompilado |

O conteúdo dos branches `EU` e `CT` vem do cliente do jogo e pertence à Wargaming; é publicado apenas para
referência de desenvolvimento de mods. Ver [`docs/DESENVOLVIMENTO.md`](docs/DESENVOLVIMENTO.md) para todas as
decisões técnicas, resultados e limitações.

## O que faz

- `detect` — encontra as instalações (EU/CT), versão, realm e recursos.
- `extract` — extrai `res`, `res_mods` e `mods` (pacotes `.pkg`/`.wotmod` e ficheiros soltos) para
  `wot_src_<R>/sources`, com manifesto (SHA-256), validação e descodificação dos XML binários BigWorld.
- `decompile` — `.pyc` (Python 2.7) → `.py` com `uncompyle6`, validado pelo parser do Python 2.7.
- `actionscript` — SWF: catálogo, código AS3 (FFDec), recursos e desmontagem `.asasm` (RABCDAsm).
- `gameface` — HTML/CSS/JS formatados (verificados token a token e com `node --check`), webpack, views e
  ligações prováveis ao Python.
- `stubs` — stubs `.pyi` só com informação verificada no código (para VS Code/Pylance).
- `update` / `verify` / `report` — atualização incremental, verificação de integridade, relatório global.
- `index` / `search` / `compare` — índice de APIs (SQLite FTS5), pesquisa e comparação EU ↔ CT.
- `purge` / `clean` — retirar o que não é do jogo e apagar intermediários já processados.

A instalação do jogo é sempre só de leitura; nada extraído é executado.

## Requisitos

- Python ≥ 3.11 (Windows).
- Para `decompile`/`stubs`: Python 2.7 com `uncompyle6`.
- Opcionais: Java + [FFDec](https://github.com/jindrapetrik/jpexs-decompiler) (AS3), RABCDAsm (`.asasm`),
  Node.js (verificação do JS formatado).

## Uso

```powershell
.\wot-extractor.cmd detect
.\wot-extractor.cmd update                 # extrai/atualiza e processa tudo, EU e CT
.\wot-extractor.cmd search BarracksView
.\wot-extractor.cmd compare
py -3 -m unittest discover -s tests -t .   # testes
```

Configuração: copie `wot_extractor.example.toml` para `wot_extractor.toml`.
