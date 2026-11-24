# Independent EU pipeline

The manual **EU source pipeline** workflow on the default `EU` branch calls
`eu-build.yml` on `main`. It supports `candidate/EU` and `EU`; publication is
optional and requires a successful quality gate. No schedule is enabled yet.

The builder has read-only repository access. It locks the official WGUS
installation chain, indexes its split archives, and acquires source-bearing
members of active SD packages. Audio packages are excluded. `preload` is kept
separate from `install`, including when both appear in the same response.
The active version cannot include preload patches.

The initial build reconstructs selected packages. Subsequent runs validate and
reuse content-addressed package caches; unchanged processing results also have
an integrity checkpoint. Corrupt cached files cause reacquisition or regeneration.
The current processor hash invalidates derived output when the code changes.

Own processors decode packed XML, decompile Python 2.7 and AS3, generate static
stubs, and process Gameface for active modes with probable Python links.
Python 2.7 tools run in a Docker container without network access. The separately
checked-out archive engine is pinned; no upstream source snapshot or stubs are
used as the source of this build.

`eu_quality_policy.json` permits only previously reviewed issues with exactly
matching input hashes and no worse recovery status. New failures, missing
processing results, interrupted passes, and unexpectedly low coverage block
publication. Incomplete Python output is named `.py.partial`, retaining `.pyc`.
Recovery limitations are included in `QUALITY.json`.

A separate job with write access verifies every candidate file, rechecks the
active WGUS fingerprint, preserves the branch's workflow entrypoints, and
checks that Git retained the artifact's exact bytes. The target must still be
at the head observed before building. Pushes never use force.

## Validation status

Local validation: 174 Python tests and four bounded-transfer Node tests passed
before the first complete run. The first complete EU run was started on
2026-11-24: [45472405901](https://github.com/dkruben/wot-extractor/actions/runs/45472405901).
Its target is `candidate/EU`, with publication conditional on validation.
Cold-build results, restored-cache reuse, production publication, and scheduling
must be confirmed from actual runs before claiming unattended operation complete.
