# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/utils/data.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/utils/data.py
from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from frameworks.wulf import Array
T = typing.TypeVar('T')

def findIndexes(arr, predicate):
    return [idx for idx, item in enumerate(arr) if predicate(item)]


def findItems(arr, predicate):
    return [item for item in arr if predicate(item)]
