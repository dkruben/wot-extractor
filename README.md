# wot-extractor

A Python 3 tool that extracts, decompiles and documents the **World of Tanks** client
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
- `updates` — consults WGUS for available patch chains without downloading or applying patches.
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
py -3.11 -m pip install -e .           # install the CLI and the WGUS dependency
.\wot-extractor.cmd detect
.\wot-extractor.cmd updates --realm EU
.\wot-extractor.cmd update                 # extract/update and process everything, EU and CT
.\wot-extractor.cmd search BarracksView
.\wot-extractor.cmd compare
py -3 -m unittest discover -s tests -t .   # tests
```

Configuration: copy `wot_extractor.example.toml` to `wot_extractor.toml`.
The `updates` command requires an internet connection to `wgus-woteu.wargaming.net`. It only reports
patch chains; it does not download or apply them.

## GitHub layout and CDN validation

The repository opens on `EU`; `CT` contains Common Test sources and `main`
contains the tool. Published branches use `sources/`, `sources-as3/` and
`_stubs/`, with the decoded XML and Gameface outputs retained separately.
Local extraction folders keep their existing names; the publication layer
maps them when building commits.

See [GitHub publication and the real CDN test](docs/GITHUB_LAYOUT.md).
The isolated Actions experiment downloads and decompiles the actual EU and CT
scripts package without an installed game. It saves artifacts and never
overwrites the published source branches.

[The real EU and CT experiment](docs/CDN_TEST_RESULTS.md) completed on GitHub
on 2026-11-17. The download path worked; the syntax inspection identified
incomplete modules, so scheduled production publication remains disabled.

[The Gameface CDN experiment](docs/CDN_GAMEFACE.md) additionally reconstructs
base GUI packages and runs our existing processor to generate
`sources_gameface/` on GitHub, with formatting and original-file integrity checks.
