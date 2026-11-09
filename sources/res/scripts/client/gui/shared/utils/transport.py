# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/transport.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/transport.py
from __future__ import absolute_import
import zlib
from future.moves import pickle
from debug_utils import LOG_ERROR

def z_dumps(obj, protocol=-1, level=1):
    return zlib.compress(pickle.dumps(obj, protocol), level)


def z_loads(value):
    try:
        result = zlib.decompress(value)
    except zlib.error:
        LOG_ERROR('Can not decompress value', value)
        return

    try:
        result = pickle.loads(result)
    except pickle.PickleError:
        LOG_ERROR('Can not unpickle value', value)
        result = None

    return result
