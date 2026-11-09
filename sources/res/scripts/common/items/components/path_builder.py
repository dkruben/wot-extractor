# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/components/path_builder.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/components/path_builder.py
from __future__ import absolute_import
import persistent_data_cache_common as pdc
__all__ = ('makeIndexes', 'makePath')
_SEPARATOR = '/'
_chains = []

def makeIndexes(path):
    global _chains
    chains = path.split(_SEPARATOR)
    for chain in chains:
        if chain not in _chains:
            yield len(_chains)
            _chains.append(chain)
        else:
            yield _chains.index(chain)


def makePath(*indexes):
    chains = []
    for index in indexes:
        chains.append(_chains[index])

    return _SEPARATOR.join(chains)


def init():
    global _chains
    _chains = pdc.load('path_builder', list)
