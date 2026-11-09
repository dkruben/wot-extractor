# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/pickle_intern.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/pickle_intern.py
from __future__ import absolute_import
import pickle
from copy import deepcopy
from io import BytesIO
from past.builtins import intern
from struct_helpers import unpackByte
STR_LEN_FOR_INTERN = 20

class UnpicklerWithIntern(pickle.Unpickler, object):

    def __init__(self, file):
        super(UnpicklerWithIntern, self).__init__(file)
        self.dispatch = deepcopy(self.dispatch)
        self.dispatch[pickle.SHORT_BINSTRING] = UnpicklerWithIntern.load_short_binstring

    def load_short_binstring(self):
        str_len = unpackByte(self.read(1))
        obj = self.read(str_len)
        if len(obj) <= STR_LEN_FOR_INTERN:
            obj = intern(obj)
        self.append(obj)

    @classmethod
    def loads(cls, data):
        unpickler = cls(BytesIO(data))
        return unpickler.load()
