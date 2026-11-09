# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgnc/wgnc_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgnc/wgnc_helpers.py
from debug_utils import LOG_ERROR

def parseSize(sizeStr):
    if sizeStr:
        try:
            size = tuple(map(int, sizeStr.split('x')))
            if len(size) != 2:
                return
        except ValueError:
            LOG_ERROR('Failed to parse size: %s' % sizeStr)
            size = None

    else:
        size = None
    return size
