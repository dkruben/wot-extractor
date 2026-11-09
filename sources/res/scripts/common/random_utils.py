# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/random_utils.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/random_utils.py
from __future__ import absolute_import, division
import itertools, random
from bisect import bisect
from copy import deepcopy
from past.builtins import xrange
import typing

class wchoices(object):

    def __init__(self, elist, wlist=None):
        if not set(elist):
            raise IndexError
        evtLen = len(elist)
        norm = float(evtLen if wlist is None else sum(wlist[:evtLen]))
        self.welist = tuple(((i + 1 if wlist is None else sum(wlist[:i + 1])) / norm, elist[i]) for i in xrange(evtLen))
        return

    def nseq(self, count=1):
        return list(itertools.islice(self, count))

    def ncounts(self, count):
        data = sorted(self.nseq(count))
        return dict((k, len(list(g))) for k, g in itertools.groupby(data))

    def __iter__(self):
        welist = deepcopy(self.welist)

        def wrapper():
            for r in iter(random.random, -1):
                for w, e in welist:
                    if w > r:
                        yield e
                        break
                else:
                    raise LookupError('At least one option must be selected from %s' % welist)

        return wrapper()


def getValueWithDeviationInPercent(value, deviation):
    return value + value * (random.randint(-deviation, deviation) / 100.0)


def weighted_choice(seq, weights, customRandomModule=None):
    total = 0
    cum_weights = []
    for w in weights:
        total += w
        cum_weights.append(total)

    x = (customRandomModule.random() if customRandomModule is not None else random.random()) * total
    i = bisect(cum_weights, x)
    if i >= len(seq):
        i = len(seq) - 1
    return seq[i]
