# GitHub publication and real CDN test

The repository opens on `EU`, like the reference `izeberg/wot-src` repository.
`CT` holds Common Test sources, `NA`, `ASIA` and `CN` hold attributed regional
reference snapshots with CDN Gameface, and `main` holds this extraction tool.
RU/Lesta branches are excluded. See [regional provenance and test results](WG_REGIONS.md).

## Published source branches

| Path | Content |
| --- | --- |
| `sources/` | Extracted game files and decompiled Python |
| `sources-as3/scripts/` | Decompiled ActionScript, retaining original SWF paths |
| `sources-as3/swf/` | SWF catalogues |
| `_stubs/` | Generated Python type stubs |
| `sources_xml/` | Decoded XML, retained as a separate output |
| `sources_gameface/` | Formatted Gameface and view analysis |
| `.version_name` | Existing client version marker |
| `REPORT.md` | Extraction report |

The main folder names match the reference. The AS3 hierarchy remains grouped
by original SWF to prevent collisions. XML and Gameface outputs are preserved;
this is not a byte-for-byte copy of the reference repository.

The local extractor still uses `__stubs` and `sources_as`. Publication maps them
using `wot_extractor.publication`, without moving those working files. It uses
an isolated Git index and refuses path collisions. Existing state, assets and
intermediate exclusions still apply to snapshots from the extractor.

To preview or commit a migration of already committed sources:

```powershell
python -m wot_extractor.publication --git-dir .publish/EU.git
python -m wot_extractor.publication --git-dir .publish/EU.git --apply
```

To publish a fresh extraction, pass `--source wot_src_EU`. These commands create
no push. Inspect the commit before sending it to the corresponding branch.
Source Git directories are used as publication object stores; ordinary status
against the old local folder names will show the layout difference. The
publisher builds a fresh isolated index instead of relying on that status.

## Real experiment on GitHub Actions

`.github/workflows/cdn-validation.yml` runs on pushes to
`automation/cdn-validation` and supports manual dispatch after it is available
on the default branch. EU and CT run sequentially on GitHub-hosted Linux.
The user's computer is not used by either job.

The experiment executes the external `unicum-gg/wot.build` engine at commit
`1832f2ff545a2950867fa698296c92315752bf81`, with `--only scripts`. Its code is
checked out separately and is not vendored into this project. This validates
CDN access, split 7z archives, package reconstruction and real Python
decompilation. Each job records generated files, per-module SHA-256 and the
number of decompiler failure markers as a seven-day workflow artifact.

At least 100 Python modules and at least 90% without a failure marker are
required. Absence of a marker does not guarantee semantic correctness.
The script-only result is NOT a complete source mirror: it does not validate
AS3, Gameface, every game mode, preloading or production publication.

The workflow has read-only repository permissions and no scheduled trigger;
it cannot replace EU or CT content. A production workflow needs separate
coverage and quality checks, reusable downloads, preloading validation and a
publication step before scheduling is enabled.

The default EU branch now has a small `cdn-regions.yml` dispatch entry point,
calling the implementation on `main`. It selects region(s) and Python/Gameface
profiles without replacing source content. This file is preserved when the
local publisher builds a fresh EU source snapshot.

The syntax check runs in a CPython 2.7.18 container on the GitHub runner. It
records unmarked syntax errors as well as the decompiler's explicit failures.
`cdn-quality.yml` can inspect the artifacts of an existing experiment without
repeating the downloads and decompilation. Its success means the inspection
finished; inspect `publication_ready` in `syntax.json` before publication.

See [the measured EU and CT results](CDN_TEST_RESULTS.md).
