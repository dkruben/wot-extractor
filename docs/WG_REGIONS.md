# WG regional sources and CDN validation

The CDN target catalog is `src/wot_extractor/data/wg_realms.json`:

| Region | Application | Update server |
| --- | --- | --- |
| EU | `WOT.EU.PRODUCTION` | `wgus-woteu.wargaming.net` |
| CT | `WOT.CT.PRODUCTION` | `wgus-eu.wargaming.net` |
| NA | `WOT.NA.PRODUCTION` | `wgus-wotna.wargaming.net` |
| ASIA | `WOT.ASIA.PRODUCTION` | `wgus-wotasia.wargaming.net` |
| CN | `WOT.CN.PRODUCTION` | `wgus-cn360.wggames.cn` |

RU, PT_RU and Lesta targets are excluded. CN uses the regional 360 service.
This catalog controls the CDN jobs; it does not silently broaden Windows
installed-client detection/extraction support.

## Manual runs without changing test branches

The default EU source branch carries a small manual workflow entry point,
`Validate selected WG regions`. It calls the implementation on `main` and has
read-only repository permissions. Choose a comma-separated list or `ALL`, and
`python`, `gameface` or `both`. No scheduled publishing is enabled.

Example:

```sh
gh workflow run cdn-regions.yml --repo dkruben/wot-extractor --ref EU -f regions=NA,ASIA,CN -f kind=both
```

Region filtering is validated before the expensive jobs start. Each profile
creates per-region artifacts. Use a separate dispatch for retries to preserve
other successful runs and their artifacts.

## Regional branch bootstrap

The existing local `wot_src_NA`, `wot_src_ASIA` and `wot_src_CN` repositories
are shallow snapshots of `izeberg/wot-src`. Their initial commits match the
corresponding upstream regional branches, and their `.version_name` markers
match the service versions observed on 2026-11-17.

`scripts/bootstrap_region.py` creates a new attributed root commit from that
baseline, adding only hash-verified Gameface outputs and originals from a
successful CDN artifact of the SAME region/version. It preserves the baseline
Python, AS3 and reference stubs, records the upstream SHA and both test runs in
`BUILD_INFO.json`, and never pushes or overwrites an existing publication
branch. It does not alter the baseline clones or copy their shallow history.

These initial branches must not be described as complete independently
regenerated mirrors: Gameface currently covers base GUI only, Python links
are not analysed by that profile, and Python decompilation has documented
partial/syntax failures. The existing baseline content remains attributed.

## Regional CDN stalls

The first CN Gameface job reconstructed `gui-part1.pkg` but stalled while
reading the next large package block, reaching the job's 60-minute limit.
The downloader now reads ranges in 32 MiB pieces, requires exact HTTP 206
intervals and lengths, applies a 45-second request/body timeout, retries up to
three times, and retries the same versioned object over HTTPS when the original
HTTP edge stalls. It also rejects inconsistent object sizes between pieces.

Tests cover reassembly, truncated data, ignored ranges, inconsistent sizes and
a server that stalls after sending headers/partial data. Failed reads and
response-body bytes are reported in the artifact metrics. This prevents a
single unbounded read from silently occupying the whole job timeout.

## Real regional results — 2026-11-17

- [Python download, decompilation and syntax checks](https://github.com/dkruben/wot-extractor/actions/runs/44195860099)
- [Gameface with bounded range downloads](https://github.com/dkruben/wot-extractor/actions/runs/44196392534)
- [Manual region selector: CN Python run](https://github.com/dkruben/wot-extractor/actions/runs/44197758568)

| Result | NA | ASIA | CN |
| --- | --- | --- | --- |
| Version | `2.4.1.5511` | `2.4.1.5513` | `2.4.1.5512` |
| Python modules inspected | 8,678 | 8,678 | 8,678 |
| Python 2.7 syntax passed | 8,660 | 8,660 | 8,660 |
| Marked partial/failed | 16 | 16 | 16 |
| Additional Python syntax errors | 2 | 2 | 2 |
| Gameface processing succeeded | 1,854 | 1,854 | 1,854 |
| Gameface partial/failed | 0 | 0 | 0 |
| Views | 488 | 488 | 488 |
| Fetched response-body bytes (Gameface) | 4,926,455,910 | 4,926,506,465 | 4,991,941,150 |
| Failed/retried range reads | 0 | 0 | 3 |
| Gameface job duration | 4m 10s | 12m 18s | 12m 45s |

All three Gameface artifacts were checked against their original and generated
SHA-256 manifests. The CN job recovered from three failed reads and completed,
instead of remaining stuck on one large request. No Python incomplete modules
are hidden by the green workflow results: the syntax evidence explicitly
identifies the 18 non-complete modules per region.

The first NA staging import revealed Windows line-ending normalization. Its
unpublished staging commit was corrected before the first push. The bootstrap
now bypasses Git text filters, preserves CRLF bytes even when text attributes
request LF, and verifies that every untouched baseline object is retained.

## Published regional branches

| Branch | Initial reference commit | Publication commit |
| --- | --- | --- |
| [NA](https://github.com/dkruben/wot-extractor/tree/NA) | `izeberg/wot-src@152a09823c981ebded9dd9978ecd0072a53fde43` | `bc6f414deb9c45a9540066e075b35968a5dfb46f` |
| [ASIA](https://github.com/dkruben/wot-extractor/tree/ASIA) | `izeberg/wot-src@773da45244d66d04fa765dddc1b14e486c0b1733` | `faf519aa81cb67f4c174fda91bf5b15783c9ab1e` |
| [CN](https://github.com/dkruben/wot-extractor/tree/CN) | `izeberg/wot-src@94cb87342804d94f08079f6608890749cf5dd47d` | `c1ae7096adfbd1f508057b236541fdea42afe22a` |

Each branch contains `_stubs/`, `sources/`, `sources-as3/`,
`sources_gameface/`, the version marker, README and `BUILD_INFO.json`.
Baseline clones remain unchanged and still point to the upstream repository;
the independent local publication object stores are under `.publish/<R>.git`.

The initial import streams verified blobs into a pack and updates the baseline
trees lazily. It avoids normalizing text or repeatedly walking a 220k-file
Windows index. A regression test preserves raw CRLF even under LF attributes.
Validation included 169 Python unit tests, four range-fetch tests, complete
artifact hashes, preserved baseline object IDs and the real GitHub runs above.
The manual CN dispatch also completed successfully. The default branch remains
EU, and scheduled publication remains disabled.
