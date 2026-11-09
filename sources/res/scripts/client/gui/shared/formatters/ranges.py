# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/formatters/ranges.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/formatters/ranges.py
from __future__ import absolute_import
from builtins import range
from future.utils import lmap
from helpers import int2roman

def toRangeString(sequence, step=1, itemDelimiter=', ', rangeDelimiter='-'):
    return itemDelimiter.join(rangeDelimiter.join(item) for item in stringRanges(sequence, step))


def toRomanRangeString(sequence, step=1, itemDelimiter=', ', rangeDelimiter='-'):
    return itemDelimiter.join(rangeDelimiter.join(item) for item in romanStringRanges(sequence, step))


def stringRanges(sequence, step):
    for item in numberRanges(sequence, step):
        yield lmap(str, item)


def romanStringRanges(sequence, step):
    for item in numberRanges(sequence, step):
        yield lmap(int2roman, item)


def numberRanges(sequence, step):
    length = len(sequence)
    if length > 0:
        q = sorted(sequence)
        i = 0
        for j in range(1, length):
            if q[j] > step + q[j - 1]:
                if i == j - 1:
                    yield (
                     q[i],)
                else:
                    yield (
                     q[i], q[j - 1])
                i = j

        if i == length - 1:
            yield (
             q[i],)
        else:
            yield (
             q[i], q[-1])
