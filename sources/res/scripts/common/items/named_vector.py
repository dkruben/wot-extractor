# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/named_vector.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/named_vector.py
from __future__ import absolute_import
from collections import defaultdict
from future.utils import iteritems
__all__ = ('NamedVector', )

class NamedVector(defaultdict):

    def __init__(self, default_factory=int, args=None):
        super(NamedVector, self).__init__(default_factory, args or [])

    def __add__(self, other):
        r = NamedVector(self.default_factory, iteritems(self))
        r += other
        return r

    def __iadd__(self, other):
        for k, v in iteritems(other):
            self[k] += v

        return self

    __radd__ = __add__

    def __sub__(self, other):
        r = NamedVector(self.default_factory, iteritems(self))
        r -= other
        return r

    def __isub__(self, other):
        for k, v in iteritems(other):
            self[k] -= v

        return self

    __rsub__ = __sub__
