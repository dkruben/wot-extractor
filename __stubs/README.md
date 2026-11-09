# Stubs Python (.pyi) do World of Tanks

Gerados pelo wot-extractor a partir do código descompilado (fase C), dos `.py` originais dos mods e,
quando a descompilação falhou, do bytecode. **Só contêm informação verificada no código**: nomes,
parâmetros, valores por omissão literais, docstrings, atributos atribuídos e o tipo de valores literais.
`Any` significa *desconhecido*. Os módulos nativos (C++) listam só os membros que o Python usa, com
`*args/**kwargs`, e terminam em `__getattr__` (lista incompleta).

Uso no VS Code (Pylance): em `settings.json` da pasta do mod,

```json
{ "python.analysis.stubPath": "<caminho>/wot_src_EU/__stubs" }
```

O código do jogo é Python 2.7; o Pylance analisa como Python 3, por isso podem aparecer avisos sobre
sintaxe Python 2 no código do mod — os stubs em si são Python 3 válido (verificado).

Módulos: 10199 (nativos: 69). Estado detalhado em `stubs_index.json`.
