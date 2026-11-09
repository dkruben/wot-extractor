# wot-extractor — development notes

Overview and usage: [`README.md`](../README.md).

## Usage

```powershell
.\wot-extractor.cmd detect                 # detect EU and CT, probing the .pkg files
.\wot-extractor.cmd detect --quick         # without opening the .pkg files (instant)
.\wot-extractor.cmd detect --realm EU --path "D:\Games\World_of_Tanks_EU"
.\wot-extractor.cmd detect --json reports\detect.json

.\wot-extractor.cmd extract --tree res --tree res_mods   # EU + CT, dev profile, incremental (no third-party mods)
.\wot-extractor.cmd extract --realm EU --dry-run  # plan only
.\wot-extractor.cmd extract --realm EU --profile gui -j 8
.\wot-extractor.cmd extract --realm CT --ext .pyc,.xml --pkg "scripts*"
.\wot-extractor.cmd extract --realm EU --force    # re-extract everything
.\wot-extractor.cmd extract --realm EU --prune    # delete what left the game (only on a consistent run)

.\wot-extractor.cmd decompile                     # EU + CT: .pyc -> .py next to it, incremental
.\wot-extractor.cmd decompile --realm EU --dry-run
.\wot-extractor.cmd decompile --realm EU --glob "scripts/client/gui/*" --limit 200
.\wot-extractor.cmd decompile --realm EU --retry  # retry partial/failed
.\wot-extractor.cmd decompile --realm EU --backend uncompyle6-py3 --retry

.\wot-extractor.cmd actionscript                  # EU + CT: SWF catalog + FFDec (code and assets)
.\wot-extractor.cmd actionscript --realm EU --glob "*/battle*.swf" -j 6
.\wot-extractor.cmd actionscript --realm EU --no-ffdec   # catalog and AS3 declarations only
.\wot-extractor.cmd actionscript --realm EU --no-assets  # code only
.\wot-extractor.cmd actionscript --asasm all      # .asasm disassembly of every SWF (default: partial ones only)
.\wot-extractor.cmd gameface                      # EU + CT: formatted JS/CSS, views, links to Python
.\wot-extractor.cmd gameface --realm EU --glob "*/lobby/crew/*"   # a subset only
.\wot-extractor.cmd gameface --realm EU --no-format      # analysis only (no formatted copies)
.\wot-extractor.cmd stubs                         # EU + CT: .pyi stubs in __stubs/ (needs Python 2.7)
.\wot-extractor.cmd stubs --realm EU --stdlib     # include the standard library shipped with the game
.\wot-extractor.cmd update                        # after a game update: every phase, incremental
.\wot-extractor.cmd update --realm CT --steps extract,decompile   # some steps only
.\wot-extractor.cmd verify                        # hashes, outputs, orphans and install drift (read-only)
.\wot-extractor.cmd verify --realm EU --quick     # sizes only
.\wot-extractor.cmd report                        # report.json + REPORT.md per realm
.\wot-extractor.cmd index                         # API index (wot_api_index_<R>.sqlite)
.\wot-extractor.cmd search BarracksView           # search classes/functions/methods/views in both realms
.\wot-extractor.cmd search BigWorld.callback --exact --realm EU
.\wot-extractor.cmd search onLoading --kind method --limit 50
.\wot-extractor.cmd compare                       # EU -> CT: files, Python API, AS3, Gameface (compare/)
.\wot-extractor.cmd purge --dry-run               # what is not part of the game (mods tree) would be removed
.\wot-extractor.cmd purge --yes                   # remove the mods tree (the install is never touched)
.\wot-extractor.cmd clean --dry-run               # what was already processed and would be deleted from sources/
.\wot-extractor.cmd clean --yes                   # delete decompiled .pyc, binary XML, processed SWF, work files
py -3 -m unittest discover -s tests -t .          # tests
```

Alternative: `py -3 -m pip install -e .` creates the `wot-extractor` command.
Requires Python ≥ 3.11 (uses `tomllib`); the tool only uses the standard library. `decompile` needs a
Python 2.7 with `uncompyle6` (here `F:\Python27`) and, for the fallback, `uncompyle6` on the current Python 3.
`stubs` uses the same Python 2.7 as `decompile` (only to read the syntax tree; nothing is executed).
`gameface` uses Node.js (`node --check`, syntax check only, never executes) if it is on the PATH.
`actionscript` uses FFDec (here `C:\Program Files (x86)\FFDec`, v26.2.1) with Java, when available; without
it, it only produces the catalog and the AS3 declarations.

Exit codes: `0` ok · `1` failure (realm not found, blocked write, inconsistent extraction) · `2`
usage/configuration · `3` command not implemented yet · `130` interrupted (resumable).

## Layout

```text
src/wot_extractor/
  cli.py            CLI (argparse)
  config.py         optional wot_extractor.toml (see wot_extractor.example.toml)
  constants.py      realms, .pyc magic numbers, categories by extension
  safety.py         path traversal, WriteGuard (blocks writes into the game), zip limits
  logutil.py
  apiindex.py       API index (SQLite FTS5) and search
  compare.py        realm comparison
  detect/
    sources.py      candidates: Game Center, Windows registry, bounded disk search
    xmlinfo.py      version.xml, game_info.xml, app_type.xml, paths.xml
    install.py      inspection of an install (directories, packages, mods, inventory)
    pkgprobe.py     reads the central directory of .pkg/.wotmod files (without extracting)
    detector.py     picks one install per realm
  extract/
    plan.py         plan: enumeration, filters/profiles, precedence, shadowing, overrides by mods
    validate.py     content validation (XML/JSON/.pyc/SWF), versioned (VALIDATOR_VERSION)
    writer.py       atomic writes (tmp + replace), SHA-256, \\?\ long paths
    manifest.py     manifest reading and JSON-lines journal (resume)
    engine.py       incremental/parallel run, manifest.json, reports, .version_name
    xmldecode.py    binary XML decoding pass (processes, incremental)
  formats/
    bwxml.py        BigWorld binary XML decoder (packed section)
    swf.py          SWF reader (FWS/CWS/ZWS, decompression limit), tags, catalog, .swc
    abc.py          full ABC (AVM2) reader: classes, signatures, AS3 declarations
    jsfmt.py        lexer and formatter for minified JavaScript/CSS (whitespace only), token-by-token check
  gameface/
    analyze.py      one file: kind, formatting, webpack, references (runs in parallel processes)
    pylinks.py      index of the decompiled Python and probable view <-> Python/ViewModel links
    engine.py       incremental run, views, official layouts, indexes, VIEWS.md, gameface_report.json
  stubs/
    _describe27.py  Python 2.7 worker: describes a module from its AST or, failing that, its bytecode (marshal)
    render.py       writes the .pyi files (verified information only), validated by the Python 3 parser
    engine.py       importable modules, description cache, no-code modules, __stubs/, stubs_report.json
  maintenance/
    update.py       manifest diffs, previous filters, update_report.json (step order lives in the cli)
    verify.py       read-only verification: SHA-256, derived outputs, orphans, CRC in the install's .pkg
    report.py       global report per realm (report.json, REPORT.md)
    purge.py        remove content that is not part of the game (mods tree)
    clean.py        delete already processed intermediates from sources/
  decompile/
    _worker.py      external worker (Py2.7/Py3): unmarshal + uncompyle6 + compile(PyCF_ONLY_AST) validation
    backends.py     decompilers, interpreter detection, worker processes (timeout/restart)
    engine.py       incremental/parallel/resumable run, states, manifest, decompile_report.json
  actionscript/
    ffdec.py        FFDec/Java detection and export (one JVM per SWF, timeout)
    rabcdasm.py     RABCDAsm (abcexport + rabcdasm): lossless .asasm disassembly
    engine.py       catalog, code, assets, sources_as/catalog.json, actionscript_report.json
tests/              unittest; fake installs in temporary folders + read-only tests against the real clients
```

## Roadmap

| Phase | Content | Status |
|---|---|---|
| A | Foundation, configuration, safety, detection, `detect` | done |
| B | `extract`: .pkg/.wotmod/res/res_mods → `wot_src_<R>/sources`, manifest with hashes, safety limits | done |
| B.2 | BigWorld binary XML decoder → `sources_xml/` | done |
| C | `decompile`: .pyc 2.7 (uncompyle6 on `F:\Python27`), syntax validation with the 2.7 parser, states | done |
| D | `actionscript`: SWF catalog, AS3 code (FFDec) or declarations, embedded assets | done |
| E | `gameface`: HTML/CSS/JS, bundles, formatting of minified files, links to Python (probable) | done |
| F | `stubs`: `.pyi` generation from verifiable information | done |
| G | `update` / `verify` / `report`: incremental, manifest comparison, resume | done |

## Technical decisions (phase A)

1. **Order of detection sources**: `--path` (CLI) > `wot_extractor.toml` > Game Center preferences
   (`%ProgramData%\Wargaming.net\GameCenter\preferences.xml`, `<working_dir>`) > registry
   (`Uninstall`, HKCU/HKLM, 32/64-bit) > disk search (only folders with typical names, depth ≤ 2).
   The registry contains stale entries (e.g. `F:\WorldOfTanks_CT\...`), which validation rejects.
2. **Realm** read from `version.xml <meta><realm>`, checked against `game_info.xml <id>` (WOT.EU.PRODUCTION).
   Out-of-scope realms (NA) are listed but not selected.
3. **Choice when there are several installs of the same realm**: preferred drive (EU→`D:`, CT→`C:`),
   then the highest version/build, then the strongest source. The others are recorded in `issues`.
4. **Version**: `number` (`2.4.2.0`), `suffix` (`Common Test`), `build` (`995`); `folder_name`
   (`2.4.2.0 Common Test`) is the name used in `res_mods/` and `mods/`. The effective folder comes from `paths.xml`.
5. **Active packages** = those listed in `paths.xml` whose `type` includes the client's `app_type` (sd/hd).
   The `paths.xml` order is stored (`load_order`) to model precedence in phase B.
6. **Probing** only reads the zip central directory and 4 bytes of at most 16 `.pyc` per container.
   The real `.pkg` files are *stored* ZIPs (no compression).
7. **Safety**: no game file is ever opened for writing; `WriteGuard` refuses any destination inside an
   install (including `--json`); member names with `..`, absolute paths, reserved Windows names or invalid
   characters are flagged; XML with DTD/entities is refused.

## Technical decisions (phase B)

1. **Output tree** (`wot_src_<R>/`):
   - `sources/res/<virtual path>`: content of the active `.pkg` files merged with the loose `res/`, as the game
     sees it. Gameface HTML files keep finding the bundles that live in another `gui-part`.
   - `sources/res_mods/<version>/...` and `sources/mods/<version>/<name>.wotmod/<content>`: original paths.
     `.wotmod` files are expanded into a folder named after the archive; `mods/configs/...` is copied.
   - `sources_as/`, `sources_gameface/` and `__stubs/` are created empty and filled by phases D, E and F.
     Splitting Gameface by type (html/css/js) would break relative references, so the source of truth stays in
     `sources/res` and phase E generates views/manifests.
2. **Precedence** (from `paths.xml`): `res_mods` → `mods` → packages in the listed order → `./res`. Inside
   `sources/res` the first occurrence wins; the losers are kept in `shadows`. `res` files that the game replaces
   with `res_mods`/`mods` are marked with `overridden_by` (81 in EU, mostly from RemoveFog).
3. **Profiles**: `dev` (default: pyc/py, xml/def, json, web, swf/swc, fonts, text + everything under
   `gui/gameface/`), `gui` (+ everything under `gui/`), `full` (everything). Extra filters: `--ext`, `--pkg`, `--tree`.
4. **Incremental**: an entry is unchanged if its source (container, member, size, zip CRC32 or the loose
   file's mtime) matches the manifest and the copy exists with the same size. Only what changed is rewritten.
   Filtered runs keep out-of-scope entries in the manifest.
5. **Files that left the game**: they stay in the manifest with `status: removed` and are not deleted; only
   `--prune` deletes them, and only when the run is consistent.
6. **Consistency**: only without failures. In that case `.version_name` is written (the version folder name,
   e.g. `2.4.2.0 Common Test`). On failure the previous `.version_name` is kept. The previous manifest is saved
   in `.state/manifest.prev.json` and each report in `.state/reports/extraction_<UTC>.json`.
7. **Resume**: each finished entry is written to `.state/journal.jsonl`. If the run is interrupted
   (Ctrl+C → code 130) the next one reuses the journal. Files are written atomically, so a half-written file
   never carries the final name.
8. **Integrity**: `zipfile` checks the CRC32 of each member read; SHA-256 is computed while writing and the
   size is confirmed.
9. **Validation** (`validate.py`, version stored in the manifest): XML → `packed` (BigWorld binary), `valid`,
   `valid_bigworld` (undeclared tag prefixes, e.g. `<xmlns:xmlref>`) or `invalid`; JSON → `valid`,
   `valid_jsonc` (comments, e.g. tsconfig.json) or `invalid`; `.pyc` → CPython version; SWF → FWS/CWS/ZWS
   signature and version; `.swc` → ZIP. When the validator version changes, unchanged entries are revalidated
   from the extracted copy, without rewriting.
10. **Long paths**: writes use `\\?\` (on this PC `LongPathsEnabled` is 0). The report counts destinations
    longer than 259 characters (0 with the dev profile; possible with `full`).
11. **Safety**: `resolve_within` is lexical (no per-file `Path.resolve()`, which races on Windows with folders
    created in parallel); the `wot_src_<R>` folder is validated once by `WriteGuard`.

## Technical decisions (phase B.2 — BigWorld binary XML)

1. **Format** (documented in `formats/bwxml.py`): magic `45 4E A1 62`, 1 version byte, a dictionary of
   `\0`-terminated names, and a tree of elements with `uint32` descriptors (28 bits of block end + 4 bits of
   type). Types: 0 nested element, 1 string, 2 integer (0/1/2/4/8 B), 3 floats (12 floats = matrix
   `row0..row3`), 4 boolean, 5 binary (base64).
2. **Structural check**: each nested element must fill its block exactly and the file must be consumed
   completely. Trailing bytes → `partial`; any inconsistency → `failed`, with the technical message. Real result:
   **9949/9949 `success`** (EU 5171, CT 4778).
3. **Output**: `sources_xml/<tree>/<path>` (an extension of the specification's layout). The binary original in
   `sources/` is never modified (rule 3), and copy and original are clearly separated. Each copy starts with a
   comment identifying the original.
4. **Fidelity**: tags with a BigWorld prefix (`<xmlns:xmlref>`, `<xmlns:germany>`) are kept as they are, like
   in the game's text XML files (`valid_bigworld` validation). Only names invalid for any parser (e.g. starting
   with a digit) would be renamed with `_` (0 real cases). Floats use the shortest decimal representation that
   reproduces the float32 exactly, without exponent (`20`, not `2e+01`).
5. **Manifest**: a `decoded` field in each binary entry (`path`, `status`, `decoder`, `sha256`, `size`,
   `elements`, `validation`, warnings). `tool_versions.bwxml_decoder` records the decoder version.
6. **Incremental**: a file is only decoded again if the original changed, the copy is missing or
   `DECODER_VERSION` changed. Files that stop being binary lose their old copy; `--prune` also removes the copy.
7. **Consistency**: a decoding failure does **not** make the extraction inconsistent (the originals are
   correct), but it is listed in `xml_decode.failures` in the report.
8. **Performance**: ~215 MB of XML per realm. Runs in processes (`ProcessPoolExecutor`, `-j`); with 8
   processes it takes ~10 s. Below 64 files it runs serially. Can be disabled with `--no-decode-xml`.

## Technical decisions (phase C — .pyc decompilation)

1. **Where it runs**: the decompiler and the validation run in external interpreters (`decompile/_worker.py`,
   compatible with 2.7 and 3.x), with JSON-line requests. The worker does not open files: it receives the
   `.pyc` bytes and returns the `.py`, both base64-encoded. **Bytecode is never executed**: it is read with
   `xdis` (unmarshal), converted by `uncompyle6`, and the text is only parsed with `compile(..., ast.PyCF_ONLY_AST)`.
2. **Decompiler chain** (`--backend auto`): `uncompyle6` 3.9.2 on Python 2.7 (primary, the source is 2.7) and,
   when that is not `success`, `uncompyle6` 3.9.3 on Python 3. **Validation is always done by the Python 2.7
   parser**, never by Python 3's, so code that would only be valid in another version is never accepted.
3. **States** (the `decompiled` field of each `.pyc` in the manifest): `success` (no errors, no failed sections
   and valid 2.7 syntax), `partial` (there is code, but with failed sections `--- This code section failed: ---`,
   a decompiler error after producing text, or invalid syntax), `failed` (no code: error, timeout, worker
   died), `unsupported` (bytecode version without a validated decompiler; only 2.7 is supported, with no
   conversion of modern bytecode). `unchanged` is the run state for reused results. Each `partial`/`failed`
   carries the technical message (`error`) and the list of attempts (`attempts`).
4. **Output**: `sources/<tree>/<path>.py`, next to the `.pyc`, preserving modules and packages (rule 2 of the
   specification). The first line marks the file as **decompiled** and names the tool used; `partial` files
   have a warning at the end. If the game ships an original `.py` with the same name, it is never replaced: the
   decompiled code goes to `<name>.decompiled.py`. An encoding declaration is added (2nd line) only when there
   are non-ASCII bytes; it does not change Python 2 `str` literals.
5. **Attempts never lose results**: a worse result never replaces a better one for the same `.pyc`
   (`kept_previous`); attempts not chosen that produced code are kept in `.state/decompile/attempts/<backend>/`.
   `--retry` retries `partial`/`failed`; changing the chain (another uncompyle6 version) also retries them
   automatically.
6. **Incremental**: results are reused when the `.pyc` SHA-256 (`input_sha256`) and the written `.py` did not
   change. The `.pyc` read from `sources/` is checked against the manifest SHA-256. `extract` keeps the
   `decompiled` field of unchanged `.pyc` files and `--prune` also deletes the decompiled `.py`.
7. **Robustness**: one worker per thread (`-j`), per-file timeout (`--timeout`, default 120 s; the worker is
   restarted), 192 MB stack for uncompyle6's recursion, `.state/decompile_journal.jsonl` journal to resume after
   Ctrl+C, and a `.state/lock` lock so `extract` and `decompile` never change the same tree at the same time.
8. **Reports**: `decompile_report.json` (and a dated copy in `.state/reports/`) with counts, the chain and
   interpreters used, and the full list of `failed`/`partial`/`unsupported`; summary in `manifest.decompile`.
9. **Real result** (2026-11-08, `-j 8`, ~6 min per realm; second pass ~2 s):
   EU 12,392 `.pyc` → 12,373 `success`, 14 `partial`, 5 `failed`; CT 11,666 → 11,649 / 14 / 3; 0 `unsupported`.
   The Python 3 fallback solved 3 files per realm (2 with excessive recursion on 2.7, 1 timeout) and gave
   `partial` on 12 that 2.7 could not handle at all. Independent check: SHA-256 of every output equal to the
   manifest and 400 `success` files per realm accepted by Python 2.7's `compile()`.
10. **Interpreters**: `--python27`/`--python3`, `[decompile]` in `wot_extractor.toml`, the
   `WOT_EXTRACTOR_PY27` variable, the `py -2.7` launcher or the usual `X:\Python27` folders. Each one is probed
   (version and uncompyle6 presence) before use.

## Technical decisions (phase D — ActionScript/Scaleform)

1. **Own reader** (`formats/swf.py`, `formats/abc.py`, standard library only): decompresses FWS/CWS/ZWS with a
   512 MB limit, walks the tags and reads each ABC block **completely** (constants, methods, classes, scripts,
   bodies), with bounds checks and full-consumption checks. Never executes anything. It is used for the catalog,
   to verify what FFDec exported, and for the declarations when FFDec is not available.
2. **Catalog** `sources_as/swf/<key>.json`: header, compression, tags, ActionScript (as3/as2/none), classes
   (inheritance, interfaces), `SymbolClass`, `ExportAssets`, `ImportAssets2` (shared libraries), fonts, labels,
   warnings. Global index `sources_as/catalog.json` with **class → SWF(s)** that define it.
3. **Code** `sources_as/scripts/<key>/`: FFDec (`-export script`, `as` format) decompiles the full AS3. The
   output is checked: expected classes (from the ABC) without a file, methods with `Not decompiled due to ...`
   and `§§` lines (unreconstructed control flow) make the SWF `partial`. Without FFDec, or if it fails,
   **declarations** are written (package, class, inheritance, fields, constants, signatures and default values,
   all read from the ABC; empty bodies with the bytecode size), marked as such on the first line.
4. **Assets** `sources_as/assets/<key>/{images,fonts,sounds,binaryData,symbolClass}` via FFDec (PNG/JPEG, TTF,
   MP3/WAV, raw data, symbol→class map). The original SWF stays intact in `sources/`.
5. **States** (the `actionscript` field in the manifest): `success`, `partial`, `failed`, `extracted` (no code),
   `unsupported` (AS1/2 without a decompiler). With a technical `error` and counts (files, failed methods,
   missing classes, assets).
6. **Execution**: one JVM per SWF (`-j`, `-Xmx` from `java_heap`), those with the most ABC bytes first (the slow
   ones) and **at most `--heavy-jobs` (2) heavy SWFs** (ABC ≥ 2 MB: lobby, battle and variants) at the same
   time — with 6 in parallel the physical RAM ran out. Per-SWF timeout (`--timeout`, default 3600 s) also
   passed to FFDec as `-exportTimeout` (FFDec stops exporting at 1800 s by default, which left lobby and battle
   incomplete), plus per method/class limits inside FFDec. "Java out of memory" is detected in the log and
   reported in the error. The JVM runs in the temporary folder `.state/as_tmp` (the `hs_err_pid*.log` files do not
   pollute the project; the end of the log is kept in the manifest error). Moving into `sources_as/` tolerates
   transient Windows locks (retries; as a last resort copy and delete). Classes FFDec did not export get the
   ABC declarations; journal and lock as in `decompile`. Incremental by SWF SHA-256 and the tool signature
   (reader and FFDec versions); `--retry`/`--force`. `extract` keeps the state and `--prune` deletes the outputs
   of removed SWFs. `.swc`: the `library.swf` is read from inside the ZIP.
7. **Letter case**: NTFS is case-insensitive and WG's SWFs have packages such as `net.wg.data.VO` and
   `net.wg.data.vo` (battle, lobby): they end up in the same folder. The check of exported classes ignores
   case, declarations never replace an FFDec file, and the pairs are recorded in `case_collisions`.
8. **RABCDAsm** (the copy shipped with XVM in `xvm-master/src_build/bin/windows_i686/rabcdasm`, configured in
   `wot_extractor.toml`): disassembles the ABC into AVM2 assembly (`.asasm`) losslessly. Integrated — see
   "Improvements".
9. **Real results (2026-11-09, FFDec 26.2.1)**:

   | | SWF | success | extracted | partial | failed | .as files | assets | missing classes |
   |---|---|---|---|---|---|---|---|---|
   | EU | 817 | 780 | 26 | 11 | 0 | 45,269 | 14,950 | 0 |
   | CT | 760 | 727 | 26 | 7 | 0 | 35,458 | 13,912 | 0 |

   The `partial` ones are only 2 `§§` lines in one method of `BranderVehicle2dMarker` (vehicle markers), repeated
   in the battle SWFs and the `gui_battle` .swc. `sources_as` ≈ 750 MB per realm. Full run ~30–40 min per realm
   (`lobby.swf`, 4954 classes and 14 MB of ABC, takes ~25 min alone in FFDec); rerun without changes < 1 s.

## Technical decisions (phase E — Gameface)

1. **Selection**: `web` files (`.html/.css/.js/.mjs/.ts/.unbound`) and everything in `*/gui/gameface/` or
   `gui/unbound/`. Images, fonts, JSON and similar from those folders stay in `sources/` and are only indexed in
   `sources_gameface/assets/index.json` (not duplicated).
2. **Formatting** (`formats/jsfmt.py`, standard library only): a JavaScript lexer (strings, templates with nested
   `${}`, regex vs division — including the `)` of `if/for/while`, comments, `#private`) rewrites minified files
   adding **only** line breaks and indentation at safe points (after `{` and `;` outside parentheses, before `}`,
   between `}` and a new statement, between `},` of properties). It never removes an original line break
   (automatic semicolon insertion depends on them). Each result is **verified**: the lexer reads the copy back
   and the token sequence must be identical; with Node.js present, the copy must also pass `node --check` (if
   only the original passes, the copy is deleted and the file is `partial`). CSS is formatted and verified the
   same way. In HTML only minified inline scripts/styles that are not third-party libraries (`@license`) are
   formatted. Each copy starts with a header saying it is **not the original source code**.
3. **Webpack 5**: from each bundle we read `__webpack_modules__` (id → line in the formatted copy), the chunks
   (`self.webpackChunkgameface.push([[ids],{modules}])`), the entry module and the required chunks
   (`__webpack_require__.O(void 0,[ids],()=>__webpack_require__(id))`). Module → files index.
4. **References** per file: `R.views.*` (child views), `R.strings/images/...`, `engine.call/on/trigger`,
   `viewEnv.*`, commands (`createCallback(..., "onX")`) and the property names/strings used.
5. **Views**: folders of `_dist/production` with an `.html` (including the `mono/.../main.html` + `bundle.js`
   ones) and the `.unbound` layouts. The **official id** comes from `gui/gen_resources/gameface_layouts.json` and
   `unbound_layouts.json` (one per feature: `res/<feature>/gui/gen_resources/`), which map `R.views.<id>` → file,
   with `entrance` and `impl`. Without an entry in those files the id is inferred from the folder and flagged.
   Files overridden by mods: the effective one and the existing ones are recorded.
6. **Links to Python — probable**: an index of the decompiled Python (`R.views.<id>` with file and line,
   `model=X`/`ViewComponent[X]`, generated ViewModels with properties and commands, including inheritance) and
   `coui://...html` paths in Python/XML/JSON. Per view: files that use the id, the ViewModel (from the `model=`
   in those files or by the `view_models/views/<path>/<name>_model.py` convention) and how many of its names
   appear in the view's JS and its chunks. Confidence: `provavel-forte` (references + ViewModel with ≥ 50% of the
   names in the JS, or a coui:// path referenced outside the layouts), `provavel`, `nao-encontrada`. Never
   "certain".
7. **Outputs**: `sources_gameface/{js,css,html}/<key>` (formatted copies), `manifests/files/<key>.json`
   (analysis), `manifests/views/<R id>.json`, `manifests/index.json`, `manifests/python_links.json`,
   `assets/index.json`, `VIEWS.md` (table of views for mod development) and `gameface_report.json`. State in the
   manifest (the `gameface` field): `success`/`partial`/`failed`. Incremental by SHA-256 and signature
   (analyzer/formatter and node versions); the Python index is cached (`.state/gameface_pyindex.json`) until the
   extraction or the decompilation changes. Parallel processes (`-j`).
8. **Real results (2026-11-09)**:

   | | files | success | partial | formatted (node ok) | views (official id) | strong / probable / not found |
   |---|---|---|---|---|---|---|
   | EU | 2937 | 2937 | 0 | 754 (754) | 713 (713) | 303 / 324 / 86 |
   | CT | 2741 | 2741 | 0 | 700 (700) | 668 (668) | 285 / 304 / 79 |

   ~35 s per realm (the first time includes the Python index, ~3 min on CT); rerun without changes ~3 s. 81 EU
   layouts have no file (development demo views, not shipped).

## Technical decisions (phase F — stubs)

1. **Modules**: each `.pyc`/`.py` in `scripts/client`, `scripts/client_common` or `scripts/common` (from `res`,
   the features `res/<feature>/` and mods) gives the corresponding importable module (`__init__` → package).
   Files overridden by mods are left out (the effective one counts); with the same name in two roots, the
   package wins, then `client` > `client_common` > `common`. The standard library shipped with the game
   (`scripts/common/Lib`) is only included with `--stdlib` (IDEs have their own).
2. **Reading**: a **Python 2.7** worker (the game code is Python 2) reads the syntax tree with
   `compile(..., PyCF_ONLY_AST, dont_inherit=True)` — nothing is executed. If the decompiled code is not valid or
   the decompilation failed, it reads the **bytecode** (`marshal`): class and function names, parameters,
   `*args/**kwargs`, how many parameters have default values (from the parent's `MAKE_FUNCTION`), imports and
   assigned names. Unreadable bytecode (obfuscated mods) → `failed`.
3. **What goes into the stub** (verifiable only): imports (re-exported with `as`, as at runtime; Python 2 implicit
   relative imports become `from . import x` when the sibling module exists), classes with simple bases and
   `metaclass` (from `__metaclass__`), `property/staticmethod/classmethod/abstractmethod/x.setter` decorators (the
   others stay as comments: they may change the signature), methods and functions with parameter names and
   literal default values (others as `...`), docstrings (up to 30 lines), class attributes, instance attributes
   assigned with `self.x = ...`, module constants with the literal value (`X = 5`) or the literal's type
   (`X: tuple`). Everything else is `Any`, meaning *unknown*; return and parameter types are never written. The
   last definition with the same name wins. Names that are Python 3 keywords (e.g. `async`) are omitted and
   listed. Stubs from bytecode end with `def __getattr__(name) -> Any` (incomplete stub).
4. **No-code modules** (engine natives such as `BigWorld`, `ResMgr`, `Math`, `GUI`, or modules missing from the
   client): only the members the Python code uses, with `*args/**kwargs` and a comment describing the observed
   usage (how many calls, how many positional arguments, keywords, imports). The 2.7 and Python 3 standard
   libraries and implicit relative imports are excluded.
5. **Validation**: every `.pyi` goes through the Python 3 parser; if it fails it is regenerated without
   docstrings and, as a last resort, a minimal stub marked `failed` is written.
6. **Incremental**: descriptions are cached (`.state/stubs_desc/`) by the input signature (SHA-256 of the `.pyc`
   and of the decompiled `.py`); only `.pyi` files that change are rewritten; those of modules that disappeared
   are deleted. Without changes (same modules, inputs and versions) the run ends immediately.
7. **Usage**: VS Code/Pylance `python.analysis.stubPath` pointing to `wot_src_EU/__stubs` (see
   `__stubs/README.md`); index in `__stubs/stubs_index.json`.
8. **Real results (2026-11-09)**:

   | | modules | success | partial (bytecode) | failed | classes | functions | no-code modules |
   |---|---|---|---|---|---|---|---|
   | EU | 11,169 | 11,151 | 16 | 2 | 21,152 | 128,442 | 71 |
   | CT | 10,446 | 10,430 | 16 | 0 | 20,110 | 123,621 | 70 |

   The 2 EU `failed` were two obfuscated `.pyc` files from third-party mods. Every `.pyi` passes the Python 3
   parser. ~4 min per realm the first time; rerun without changes < 1 s; with `--force` the result is identical.

## Technical decisions (phase G — update, verify, report)

1. **`update`** = the normal commands, in order, through the same CLI parser (same defaults): detection of the
   installed version vs `.version_name` (first extraction / same version / NEW VERSION), `extract` with the
   **same filters as the previous extraction** (profile, extensions, packages, trees — a different profile would
   mark files as removed), differences against the previous manifest by SHA-256 (new, changed, removed), then
   `decompile`, `actionscript`, `gameface`, `stubs`, `index` and `clean` (each one only reprocesses what
   changed). If the extraction is not consistent the update **stops**: the version does not advance (`extract`
   only writes `.version_name` on a consistent run) and nothing is deleted. A later phase that fails does not
   prevent the others. `--prune` only on request. `update_report.json` + `.state/reports/update_<date>.json` (the
   previous ones are kept). `--steps`, `--skip`, `--retry`, `-j`, `--heavy-jobs`, `--dry-run`. Interrupted → run
   it again.
2. **`verify`** (read-only; only writes `verify_report.json`): `.version_name` = manifest and a consistent
   extraction; each `sources/` file with the manifest size and SHA-256 (`--quick`: size only); outputs of phases
   C–F (SHA-256 of decompiled `.py` and decoded XML; existence of the rest and of the `.pyi` files); orphan files
   in `sources/` (files removed from the game but kept without `--prune`, and files deleted by `clean`, are
   counted separately); and the **install**: installed version and, per file, CRC/size in the `.pkg`/`.wotmod`
   central directory (without decompressing) or size/date of loose files → `update_needed`. Exit code 1 only for
   integrity problems (an outdated tree is not corruption).
3. **`report`**: combines the manifest, the phase reports and the last `verify` into `report.json` and
   `REPORT.md`: version, install, state of each phase, files not fully recovered (the first 25 per phase), tool
   versions, and a table of **what each folder contains** — originals (`sources/`), decoded (`sources_xml/`),
   decompiled (`.py` in `sources/`, AS3 in `sources_as/`), formatted (`sources_gameface/`, not the original) and
   generated (`__stubs/`) — with file counts and sizes.
4. **Real results (2026-11-09)**: `verify` EU 22,122 files (845 MB) with SHA-256 OK, every output present,
   0 orphans, install unchanged (110 s). `verify` CT detected **339 files changed in the install** (the rebuilt
   `driftkings.wotmod` and mod settings changed while playing, same version); `update` CT extracted 9 new + 334
   changed, decompiled only 307 `.pyc`, 2 SWF, 10 Gameface files, described 307 modules (7 `.pyi` changed),
   141 s; afterwards `verify` reported the install unchanged. `update` without changes: ~45 s (the extraction
   has to read the 538,689 files/members of the install).

## Improvements after phase G (2026-11-09)

1. **RABCDAsm in `actionscript`**: a separate step after FFDec, so FFDec's results are not invalidated.
   `--asasm partial` (default: `partial` SWFs only), `all` or `none`. A copy of the SWF (or the `library.swf` of
   the `.swc`) in a temporary folder goes through `abcexport` and `rabcdasm`; the `<block>/` folders go to
   `sources_as/asasm/<key>/`. In the manifest (`actionscript.asasm`): folder, blocks, files and, for each `.as`
   with `§§` lines, the matching `.class.asasm` (RABCDAsm renames colliding folders, e.g. `vo_`). Incremental by
   SWF SHA-256. Configuration: `[actionscript] rabcdasm`, `--rabcdasm` or `WOT_EXTRACTOR_RABCDASM`. Real: EU 11
   SWF (31,053 + 732 files), CT 7 (18,496); the `§§` in `BranderVehicle2dMarker.as` points to
   `movie-0/net/wg/gui/battle/views/vehicleMarkers/BranderVehicle2dMarker.class.asasm`.
2. **API index** (`index`, `search`; `apiindex.py`): one SQLite FTS5 database per realm
   (`wot_api_index_<R>.sqlite` in the output folder), built into a new file and swapped in at the end. Content:
   Python modules, classes, functions, methods (with the verified signature), attributes and constants (from the
   stub descriptions, with file:line in the decompiled `.py`), members of no-code modules, AS3 classes (catalog)
   and AS3 methods/properties (from FFDec's `.as` files, once per class), Gameface views and ViewModel
   properties/commands (probable link). Prefix search in names, qualified names and the first line of
   docstrings; `--exact`, `--kind`, `--realm`, `--json`. Content-based signature (rerunning a phase without
   changes does not rebuild it). Also a step of `update`. Real: EU 521,201 symbols, CT 498,234, ~15 s per realm.
3. **Realm comparison** (`compare`; `compare.py`): files by path (version folders of `mods/` and `res_mods/`
   normalized) and SHA-256; Python API (new, removed, changed signatures) from the index; AS3 classes; Gameface
   views and ViewModel members. `compare/compare_<A>_<B>.json` and `COMPARE_<A>_<B>.md` (API lists capped at 1500
   per kind; totals are complete). Real EU 2.4.1.1 → CT 2.4.2.0: files +179 / −1639 / ~1425; Python modules +86 /
   −805 (mostly the `halloween` and `fort_rush` events, absent from CT); 24 changed signatures; views +8
   (advent_calendar) / −53; ~4 s.
4. **`purge`** (`maintenance/purge.py`): removes from `wot_src_<R>` content that is not part of the game — by
   default the `mods` tree (every `.wotmod` and `mods/configs` is third-party). Deletes the file in `sources/` and
   every derived output (XML, `.py`, AS3/asasm, Gameface, `.pyi`, caches), removes the entries from the manifest,
   clears the `overridden_by` marks (the `res` files become the effective ones again) and removes the tree from
   the manifest filters, so `update` does not extract it again. Requires `--yes` (or `--dry-run`). The install is
   never touched; recover with `extract --tree mods`. **2026-11-09**: on request, the mods were removed from both
   realms (driftkings, Driftkings.RemoveFog, poliroid modslistapi/replaysmanager, openwg gameface,
   mods/configs/driftkings): EU 765 entries / 1961 outputs, CT 705 / 1850. Note: a manual `extract` without
   `--tree` uses every tree and brings `mods` back (`update` does not, because it reuses the manifest filters).
5. **`clean`** (`maintenance/clean.py`; also the last step of `update`): deletes from `sources/` what already has
   a processed form — `.pyc` with `success` decompilation (and the `.py` present), binary XML with a `success`
   copy in `sources_xml/`, `.swf/.swc` with `success`/`extracted` state and a catalog — and work files in
   `.state/` (decompilation attempts, actionscript temporaries, the Gameface Python index cache, `.tmp`, old
   reports — 3 per kind are kept). Kept: `partial`/`failed` `.pyc` and `partial` SWFs (needed for `--retry`, stubs
   from bytecode and RABCDAsm) and `.state/stubs_desc` (source of the API index and of `compare`). Each deleted
   file is marked `cleaned` in the manifest: the extraction treats it as unchanged while its source does not
   change (no re-extraction), `decompile`/`actionscript`/XML decoding reuse the results, `verify` counts it
   separately. If the game changes the file, it is extracted and processed again and `update` cleans it again
   at the end. `--only`/`--keep pyc|xml|swf|state`, `--dry-run`, `--yes`. Limitation: a cleaned item cannot be
   force-reprocessed (`--force`) without re-extracting (`extract --force`).
6. **Publishing** (2026-11-09): public repository `dkruben/wot-extractor` — `main` holds the tool (MIT);
   branches `EU` and `CT` hold the extracted trees (one commit per client version, like izeberg/wot-src), each
   built from its own git dir `.publish/<R>.git` whose work tree is `wot_src_<R>`. Excluded from the branches:
   `.state/`, `sources_as/assets/`, `sources_as/asasm/` and the root `*.json` files.

## Facts verified on the clients (2026-11-08)

- EU `D:\Games\World_of_Tanks_EU`: 2.4.1.1 #993, hd, 229 pkgs (94 GB).
- CT `C:\Games\World_of_Tanks_CT`: 2.4.2.0 Common Test #995, sd, 126 pkgs (58 GB).
- Every sampled `.pyc` is CPython 2.7 (magic `03f30d0a`). There are `.pyc` files in `scripts.pkg` and in the game
  mode packages (comp7, frontline, story_mode, ...), not only in `scripts.pkg`.
- SWF in `gui-part1..4.pkg` and in mode packages; Gameface in `gui/gameface/_dist/production` (gui-part1..4).
- The client merges the packages into a virtual file system (e.g. an HTML file in gui-part2 references a bundle
  in gui-part4). Extraction must resolve by virtual path, not by archive.

## Known limitations

- The disk search does not walk the whole disk; installs in folders without a typical name need manual
  configuration.
- The magic number table only covers CPython 2.7 and 3.6–3.13; others show up as `unknown:<n>`.
- The `sources_xml/` copies are an interpretation: element order and structure are preserved, but the formatting
  (indentation, whitespace around values) is not that of the text XML the binary was built from, which cannot be
  recovered. Byte-for-byte conversion back to binary is not guaranteed.
- Type 5 (binary) fields appear as base64; the meaning of those blobs is not interpreted.
- Junctions/symbolic links created by hand inside `wot_src_<R>` are not detected (path validation is lexical).
- Packages not loaded by the client (outside `paths.xml` or of the other sd/hd type) are not extracted; they are
  listed in `skipped_containers`.
- `.wotmod` files of other versions (`mods/<other version>/`) are not extracted.
- Decompilation: `success` means valid 2.7 syntax without failed sections, not guaranteed semantic equivalence
  with the original (uncompyle6 may, rarely, rebuild a valid construct incorrectly). Original local variable
  names, comments and formatting cannot be recovered. Only 2.7 bytecode is supported.
- Index/comparison: only as good as the phases feeding them (without `stubs` there is no Python API; AS3 methods
  only come from FFDec's `.as` files). An AS3 class present in several SWFs has its members indexed once.
  The comparison counts changes in a constant's literal value as a "changed signature".
- Maintenance: `verify` compares loose files by size and date (like `extract`), so a file rewritten with the same
  content shows up as changed until the next `update` (which recognizes it by SHA-256). `update` does not detect
  new files in the install without running the extraction (the extraction is what enumerates everything).
- Stubs: signatures come from the decompiled code; unknown decorators (e.g. `adisp_process`, `wg_async`) may
  change the real signature and are only kept as comments. There are no types (not even return types), only
  `Any`. No-code modules only list the members that are used. Pylance analyzes as Python 3.
- Gameface: the formatted copy **is not the original source code** (shortened names and removed comments stay
  lost); verification only guarantees the tokens are the same. Links to Python are probable; views used through
  dynamically built paths show up as `nao-encontrada`. Only the TypeScript in
  `gui/gameface/scripts/migration-ui/src` and `@types` is original code.
- ActionScript: FFDec is an external tool; its output is not validated by an AS3 compiler, only by the failure
  marks FFDec itself leaves and by the ABC class list. Declarations (without FFDec) have no bodies. Scaleform
  external assets (tags 1000+) are only cataloged (they do not exist in the current clients).
- Decompiled `.py` files live next to the `.pyc` in `sources/`; they are told apart by the first line and the
  manifest. If `extract` updates a `.pyc`, the old `.py` stays until the next `decompile` run.
