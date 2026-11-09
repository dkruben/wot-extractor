# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/uuid_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/uuid_utils.py
from __future__ import absolute_import
import os, random
from uuid import uuid1
_node = None

def _getNode():
    global _node
    if _node is not None:
        return _node
    else:
        _node = random.randrange(0, 4294967296L) << 16
        _node = _node | os.getpid() & 65535
        _node = _node | 1099511627776L
        return _node


def genUUID():
    return uuid1(_getNode())
