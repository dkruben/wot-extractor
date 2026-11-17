"""Validate an isolated CDN experiment; never publish a partial mirror."""
import argparse
import hashlib
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from wot_extractor.cdn_regions import CDN_REGIONS, require_region


def validate(output, evidence, realm):
    require_region(realm)
    output, evidence = Path(output), Path(evidence)
    marker = output / '.version_name'
    if not marker.is_file() or not marker.read_text().strip():
        raise RuntimeError('No version marker: the service may have no build')
    files = sorted((output / 'sources').rglob('*.py'))
    if len(files) < 100:
        raise RuntimeError('Expected at least 100 real decompiled modules')
    failed = [p for p in files if b'# Decompile failed :(' in p.read_bytes()]
    summary = {
        'realm': realm, 'version': marker.read_text().strip(),
        'profile': 'scripts package only; NOT a complete client mirror',
        'engine': 'unicum-gg/wot.build@1832f2ff545a2950867fa698296c92315752bf81',
        'python_modules': len(files), 'partial_or_failed': len(failed),
        'complete_without_failure_marker': len(files) - len(failed),
        'failed_modules': [p.relative_to(output).as_posix() for p in failed],
        'sha256': {p.relative_to(output).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                   for p in files},
    }
    evidence.mkdir(parents=True, exist_ok=True)
    (evidence / 'validation.json').write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    print('{}: {} modules, {} partial/failed, version {}'.format(realm, len(files), len(failed), summary['version']))
    if len(failed) > len(files) * 0.10:
        raise RuntimeError('More than 10% of decompilations are partial/failed')
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output', type=Path)
    parser.add_argument('evidence', type=Path)
    parser.add_argument('--realm', choices=list(CDN_REGIONS), required=True)
    args = parser.parse_args()
    validate(args.output, args.evidence, args.realm)
