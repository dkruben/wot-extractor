# wot-extractor

A Python 3 tool (standard library only) that extracts, decompiles and documents the **World of Tanks** client
(EU and Common Test) into independent source trees, for analysis, API lookup and Python, ActionScript/Scaleform
and Gameface mod development.

| Branch | Content |
|---|---|
| `main` | the tool (this branch, MIT licence) |
| [`EU`](../../tree/EU) | EU client, extracted and decompiled |
| [`CT`](../../tree/CT) | Common Test client, extracted and decompiled |

The content of the `EU` and `CT` branches comes from the game client and belongs to Wargaming; it is published
only as a reference for mod development. See [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) for every technical
decision, result and limitation.

## What it does

- `detect` — finds the installs (EU/CT), version, realm and resources.
- `extract` — extracts `res`, `res_mods` and `mods` (`.pkg`/`.wotmod` packages and loose files) into
  `wot_src_<R>/sources`, with a manifest (SHA-256), validation and decoding of BigWorld binary XML.
- `decompile` — `.pyc` (Python 2.7) → `.py` with `uncompyle6`, validated by the Python 2.7 parser.
- `actionscript` — SWF: catalog, AS3 code (FFDec), assets and `.asasm` disassembly (RABCDAsm).
- `gameface` — formatted HTML/CSS/JS (verified token by token and with `node --check`), webpack, views and
  probable links to Python.
- `stubs` — `.pyi` stubs containing only information verified in the code (for VS Code/Pylance).
- `update` / `verify` / `report` — incremental update, integrity check, global report.
- `index` / `search` / `compare` — API index (SQLite FTS5), search and EU ↔ CT comparison.
- `purge` / `clean` — remove what is not part of the game and delete intermediates already processed.

The game install is always read-only; nothing extracted is ever executed.

## Requirements

- Python ≥ 3.11 (Windows).
- For `decompile`/`stubs`: Python 2.7 with `uncompyle6`.
- Optional: Java + [FFDec](https://github.com/jindrapetrik/jpexs-decompiler) (AS3), RABCDAsm (`.asasm`),
  Node.js (check of the formatted JS).

## Usage

```powershell
.\wot-extractor.cmd detect
.\wot-extractor.cmd update                 # extract/update and process everything, EU and CT
.\wot-extractor.cmd search BarracksView
.\wot-extractor.cmd compare
py -3 -m unittest discover -s tests -t .   # tests
```

Configuration: copy `wot_extractor.example.toml` to `wot_extractor.toml`.
