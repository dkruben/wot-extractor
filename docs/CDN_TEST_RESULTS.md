# Real CDN experiment — 2026-11-17

Both extraction jobs ran successfully on GitHub-hosted Ubuntu 22.04, with no
installed game. A second GitHub run compiled the resulting modules with the
CPython 2.7.18 parser, without executing game code.

- [Real download, reconstruction and decompilation](https://github.com/dkruben/wot-extractor/actions/runs/44057785201)
- [Complete Python 2.7 syntax inspection](https://github.com/dkruben/wot-extractor/actions/runs/44060286568)

| Result | EU | CT |
| --- | --- | --- |
| WGUS version name | `2.4.1.5514` | `2.4.2.5518` |
| Total Python modules | 8,678 | 8,676 |
| Passed Python 2.7 syntax | 8,660 | 8,658 |
| Marked partial/failed by decompiler | 16 | 16 |
| Additional syntax errors | 2 | 2 |
| Full extraction job duration, including setup/upload | 7m 10s | 7m 42s |
| Compressed result artifact | 44,524,628 bytes | 45,041,402 bytes |

The extraction logs show one selected `scripts.pkg`, with a base compressed
block of about 22 MB, reconstructed through three relevant package deltas in
EU and one in CT. The generator also fetched archive metadata, root text/XML
and locale resources. The 22 MB figure is NOT the total network transfer, which
was not instrumented in this experiment.

Every Python module hash in each downloaded result artifact was checked against
its generated SHA-256 manifest. Passing syntax checks is not proof of semantic
equivalence to the original source.

The two extra syntax errors occur in both regions:

- `sources/res/scripts/common/persistent_data_cache_common/types.py`
- `sources/res/scripts/common/site-packages/typing-3.10.0.0/test_typing.py`

The syntax reports explicitly set `publication_ready` to `false`. The green
quality jobs mean the inspection completed successfully, not that the output
contains no incomplete files. The checker has a `--strict` mode that rejects
any incomplete output; it was also tested against valid Python 2 print syntax,
an invalid module and an explicitly marked partial module.

## What changed in the source branches

- `EU` remains the default branch, `CT` holds Common Test, `main` holds tooling.
- `__stubs/` became `_stubs/`.
- `sources_as/` became `sources-as3/`.
- `sources/`, decoded XML, Gameface and reports were preserved.
- Migration verified 81,358 files in EU and 69,184 in CT. All file blob IDs were
  preserved under the mapped paths, except README text updated for the names.
- The local working extraction folders were not moved. The local automatic
  publisher now uses the same publication mapping.

Migration commits:

- [EU](https://github.com/dkruben/wot-extractor/commit/f8afa0cba68e2299a8b89bf9d573c76834ac018c)
- [CT](https://github.com/dkruben/wot-extractor/commit/5c41810cc5e32813c5570172aa286bc88c0bb520)

## Scope and next production work

This experiment used the pinned external engine described in
[GITHUB_LAYOUT.md](GITHUB_LAYOUT.md). It did not replace the production
extractor or publish its incomplete output to EU/CT. It covers the scripts
package, not every mode, AS3 or Gameface; the source migration retained those
existing outputs.

Before enabling scheduled publication: integrate selective CDN acquisition with
the existing validated processing pipeline, test remaining package families,
persist incremental cache, define the policy for partial decompilations, and
observe a real preloading window. Neither test activates a publication schedule.
The default branch has no workflow files, so scheduled/manual default-branch
execution also needs an explicit orchestration arrangement; the experiment
branches were triggered by pushes instead.

Local validation: 162 unit tests passed, along with the standalone artifact
validator and Python 2.7 checker smoke tests. Existing unrelated local changes
were not included in the published tooling commits.
