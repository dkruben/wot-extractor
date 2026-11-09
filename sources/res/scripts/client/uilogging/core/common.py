# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/core/common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/core/common.py
from __future__ import absolute_import
import typing
from enum import Enum
from future.moves.itertools import zip_longest
from helpers import getClientVersion

def getClientBuildVersion():
    return getClientVersion(force=False)


def grouper(iterable, batch):
    args = [
     iter(iterable)] * batch
    for parts in zip_longest(fillvalue=None, *args):
        yield [part for part in parts if part is not None]

    return


def convertEnum(value):
    if isinstance(value, Enum):
        return value.value
    if hasattr(value, '__enum__'):
        return int(value)
    return value
