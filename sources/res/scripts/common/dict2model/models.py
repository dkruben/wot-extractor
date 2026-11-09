# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/dict2model/models.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/dict2model/models.py
from __future__ import absolute_import
import typing
from itertools import chain

class Model(object):
    __slots__ = ()

    def __init__(self, *args, **kwargs):
        super(Model, self).__init__()

    def toDict(self):
        slots = set(chain.from_iterable(getattr(cls, '__slots__', tuple()) for cls in self.__class__.__mro__))
        return {attr: getattr(self, attr) for attr in slots if hasattr(self, attr)}

    def _reprArgs(self):
        return ''

    def __repr__(self):
        return ('<{}({})>').format(self.__class__.__name__, self._reprArgs() or str(self.toDict()))
