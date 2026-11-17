"""Generate an Actions matrix from the WG-only catalog (no dependencies)."""
import argparse
import json
import os
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from wot_extractor.cdn_regions import matrix

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--regions', default='ALL')
    args = parser.parse_args()
    result = json.dumps(matrix(args.regions), separators=(',', ':'))
    print(result)
    if os.environ.get('GITHUB_OUTPUT'):
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as target:
            target.write('matrix=' + result + '\n')
