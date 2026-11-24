# Complete regional updates

The **Update WG regional sources** manual workflow on the default `EU` branch
accepts `EU,CT,NA,ASIA,CN` or `ALL`. RU, PT_RU and Lesta are rejected by the
shared region catalog. Its default selection is `CT,NA,ASIA,CN`.

Each selected region gets a separate build, cache, evidence artifact, candidate
artifact, publication branch and concurrency lock. A region's failure does not
cancel the other regions. The full processing and publication checks documented
in [EU_PIPELINE.md](EU_PIPELINE.md) now also apply to these regional builds.
The shared reviewed recovery policy remains conservative: a new version with
different failing input hashes blocks publication until those failures are
reviewed; it is not automatically accepted as a known failure.

With `publish=true`, passing regions update their own source branches without
force-pushing. `warm_test=true` also requires a cached replay with zero packages
rebuilt and identical publication hashes. Existing branch contents remain in
place until the complete candidate passes. No periodic schedule is enabled.

## First complete multi-region update

On 2026-11-24 the official WGUS installation versions differed from the
published regional versions:

| Region | Official installation | Previously published marker |
| --- | --- | --- |
| CT | 2.4.2.5518 | 2.4.2.0 Common Test #996 |
| NA | 2.4.2.5523 | 2.4.1.5511 |
| ASIA | 2.4.2.5526 | 2.4.1.5513 |
| CN | 2.4.2.5525 | 2.4.1.5512 |

The [update run](https://github.com/dkruben/wot-extractor/actions/runs/45477680827)
was launched with all four regions, publication enabled and cached replay
required. Starting a run does not establish that the branches were updated;
its quality and publication jobs must succeed first.
