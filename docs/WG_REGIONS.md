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
