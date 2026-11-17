"""Run with CPython 2.7: compile generated modules without executing them."""
from __future__ import print_function

import argparse
import json
import os
import sys


def check(output, evidence):
    if sys.version_info[:2] != (2, 7):
        raise RuntimeError('This check requires Python 2.7')
    with open(os.path.join(evidence, 'validation.json')) as source:
        report = json.load(source)
    marked = set(report['failed_modules'])
    errors, passed = [], 0
    for name in sorted(report['sha256']):
        if name in marked:
            continue
        path = os.path.join(output, *name.split('/'))
        with open(path, 'rb') as source:
            content = source.read()
        try:
            compile(content, name, 'exec', 0, True)
            passed += 1
        except (SyntaxError, ValueError, TypeError) as exc:
            errors.append({'file': name, 'error': str(exc)})
    summary = {
        'realm': report['realm'], 'version': report['version'],
        'parser': sys.version, 'passed': passed, 'syntax_errors': errors,
        'marked_partial_or_failed': len(marked),
        'publication_ready': not errors and not marked,
    }
    with open(os.path.join(evidence, 'syntax.json'), 'w') as target:
        json.dump(summary, target, indent=2)
        target.write('\n')
    print('{}: {} valid, {} syntax errors, {} already marked partial/failed'.format(
        report['realm'], passed, len(errors), len(marked)))
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('output')
    parser.add_argument('evidence')
    parser.add_argument('--strict', action='store_true', help='Reject any incomplete module')
    args = parser.parse_args()
    summary = check(args.output, args.evidence)
    if args.strict and not summary['publication_ready']:
        sys.exit(1)
