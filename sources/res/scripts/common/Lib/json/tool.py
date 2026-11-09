# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/json/tool.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/json/tool.py
import sys, json

def main():
    if len(sys.argv) == 1:
        infile = sys.stdin
        outfile = sys.stdout
    elif len(sys.argv) == 2:
        infile = open(sys.argv[1], 'rb')
        outfile = sys.stdout
    elif len(sys.argv) == 3:
        infile = open(sys.argv[1], 'rb')
        outfile = open(sys.argv[2], 'wb')
    else:
        raise SystemExit(sys.argv[0] + ' [infile [outfile]]')
    with infile:
        try:
            obj = json.load(infile)
        except ValueError as e:
            raise SystemExit(e)

    with outfile:
        json.dump(obj, outfile, sort_keys=True, indent=4, separators=(',', ': '))
        outfile.write('\n')


if __name__ == '__main__':
    main()
