# Gameface from the update CDN

The existing EU and CT source branches already retain `sources_gameface/`.
The additional `.github/workflows/cdn-gameface.yml` experiment validates producing
that folder on GitHub-hosted Linux from actual reconstructed CDN packages.

## Coverage

The initial profile selects the `client` part's `gui-part<N>.pkg` and
`scripts.pkg`. It imports Gameface, Unbound and the official view-layout JSON
resources. Game-mode packages are not included. The downloaded manifest records
the exact package list and scope rather than claiming a complete client mirror.

The resources are spread across GUI packages: all selected packages are
reconstructed before building the view/dependency index. Per-package imports
refuse conflicting versions of a virtual resource, mixed realms, symlinks and
paths escaping the output tree.

## Pipeline

1. A small adapter uses the separately checked-out `wot.build` archive API at
   the same pinned commit as the Python experiment. It resolves the real client
   chain, reads split-archive headers, downloads the selected package blocks and
   applies their binary patches in order.
2. `wot_extractor.cdn_gameface import` reads those packages as ZIP archives and
   creates our native extraction manifest, retaining originals under `sources/`.
3. Our existing `run_gameface` processor formats and analyses the resources into
   `sources_gameface/`, including `js/`, `css/`, `html/`, `manifests/` and
   `VIEWS.md`. Formatted JS/CSS is not original source code.
4. Formatting verification, Node syntax checks and SHA-256 of all original
   imports are checked. Partial or failed processing rejects the experiment.
   Generated Gameface files also receive a SHA-256 manifest.

Python links are deliberately not evaluated in this experiment: it does not
import the output of the separate Python-decompilation run. The report and
indices identify those links as not analysed.

## Artifacts and execution

The `cdn-gameface-EU` and `cdn-gameface-CT` artifacts include raw selected
resources, the generated folder, reports and logs. Nothing pushes to EU or CT.
The GitHub runner does all acquisition and processing; the user's PC is not
required for those jobs.

`evidence/cdn-transfer.json` records fetched HTTP response-body bytes and range
request count, including archive headers and repeated reads. Each range must
return HTTP 206 with the requested `Content-Range`. These are body-byte counts,
not TLS/network-interface traffic or the final output size. Downloading only
Gameface members still requires their containing outer compressed package
blocks, which can be much larger than the selected resources.

The experiment is triggered by code pushes to `automation/cdn-gameface`.
Like the Python experiment, it has no publication schedule and does not make
the complete CDN production pipeline ready.

## Local commands after package reconstruction

```sh
python -m wot_extractor.cdn_gameface import gui-part1.pkg output/wot_src_EU --realm EU --container res/packages/gui-part1.pkg
# Repeat the import for every package in the acquisition plan.
# cdn-gameface.json is written by the acquisition adapter.
python -m wot_extractor.cdn_gameface process output/wot_src_EU evidence --realm EU --jobs 2
```

## Real EU result — 2026-11-17

[The real workflow run](https://github.com/dkruben/wot-extractor/actions/runs/44061170889)
successfully generated EU version `2.4.1.5514`:

- 1,896 imported resources, including two view-layout JSON files.
- 1,854 processed successfully; no partial or failed processing.
- 665 JavaScript, 528 CSS, 454 HTML, 190 Unbound, 16 TypeScript and one typings file.
- 488 views; 511 formatted outputs and 511 successful Node checks.
- 2,857 files generated under `sources_gameface/`.
- 4,926,565,956 fetched response-body bytes over 37 exact-range requests
  plus two metadata requests.
- Acquisition/reconstruction: 3m 36s; processing: 30s; complete job: 4m 44s.

All raw and generated hashes were verified in the downloaded artifact. The
1,886 raw files also present in the existing local extracted tree had identical
SHA-256; the remaining ten imported files were not present in that comparison
tree. Existing published content was not replaced.

## Real CT result and final validation

The same run successfully generated CT version `2.4.2.5518`, with the same
1,896 imported resources, 1,854 successful processing results, 488 views and
2,857 generated files. There were no partial or failed processing results in
either region. Original and generated artifact hashes were checked for CT too.

| Measurement | EU | CT |
| --- | --- | --- |
| Fetched response-body bytes | 4,926,565,956 | 4,865,674,990 |
| Exact-range requests | 37 | 25 |
| Acquisition/reconstruction | 3m 36s | 9m 02s |
| Gameface processing | 30s | 30s |
| Complete GitHub job | 4m 44s | 10m 08s |

The acquisition cost is a cold-run measurement with no persistent package
cache. A future scheduled publisher should reuse unchanged input resources
and avoid reconstructing unchanged packages on every check.

All 165 local unit tests passed, including importer isolation/conflict checks
and a fixture processed through the real Gameface engine. The experiment
preserves the complete existing `sources_gameface` trees in EU and CT; its
base-GUI artifacts are not used to replace those trees or discard mode output.
