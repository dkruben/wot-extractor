# World of Tanks CT — v.2.4.2.0 Common Test #995

Cliente **CT** do World of Tanks (v.2.4.2.0 Common Test #995, sd) extraído e descompilado pelo
[wot-extractor](https://github.com/dkruben/wot-extractor) (branch `main`). Gerado automaticamente; cada commit
corresponde a uma versão do cliente.

| Pasta | Conteúdo |
|---|---|
| `sources/` | ficheiros do jogo (`res`, `res_mods`) com os caminhos originais; os `.py` são código **descompilado** dos `.pyc` (1.ª linha `wot-extractor: codigo DESCOMPILADO`) |
| `sources_xml/` | XML binários BigWorld **descodificados** para texto |
| `sources_as/scripts/` | código ActionScript 3 **descompilado** pelo FFDec (ou só declarações, assinaladas) |
| `sources_as/swf/` | catálogo de cada SWF (classes, símbolos, imports) e `catalog.json` (classe → SWF) |
| `sources_gameface/` | HTML/CSS/JS do Gameface **formatados** (não são o código-fonte original), análises e views (`VIEWS.md`) |
| `__stubs/` | stubs `.pyi` gerados só com informação verificada no código (para VS Code/Pylance: `python.analysis.stubPath`) |
| `REPORT.md` | resumo da extração: o que foi recuperado e o que ficou parcial |

Os `.pyc`, XML binários e SWF já processados não estão incluídos (ver `REPORT.md`). Os mods de terceiros não
estão incluídos.

**Todo o conteúdo pertence à Wargaming.net** e é publicado apenas como referência para o desenvolvimento de mods;
não é concedida nenhuma licença sobre ele.
