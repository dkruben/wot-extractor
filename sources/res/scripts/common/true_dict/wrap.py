# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/true_dict/wrap.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/true_dict/wrap.py
from __future__ import absolute_import
from typing import Any
from .core import TrueDict
FixedDict = Any

class MemberProxy(object):

    def __init__(self, memberName):
        self.memberName = memberName

    def __get__(self, inst, owner):
        return inst.fixedDict[self.memberName]

    def __set__(self, inst, value):
        inst.fixedDict[self.memberName] = value

    def __delete__(self, inst):
        raise NotImplementedError(self.memberName)


class TrueDictWrapped(TrueDict):
    keysProxy = MemberProxy('keys')
    valuesProxy = MemberProxy('values')

    def __init__(self, fixedDict):
        self.fixedDict = fixedDict
        super(TrueDictWrapped, self).__init__(self.keysProxy, self.valuesProxy)


class TrueDictConverter(object):

    def createObjFromDict(self, fixedDict):
        return TrueDictWrapped(fixedDict)

    def getDictFromObj(self, obj):
        if isinstance(obj, TrueDictWrapped):
            return obj.fixedDict
        if isinstance(obj, TrueDict):
            return {'keys': (list(obj.iter_keys())), 'values': (list(obj.iter_values()))}
        if isinstance(obj, dict):
            if set(obj.keys()) == {'keys', 'values'}:
                return obj
        raise TypeError('TrueDictConverter: cannot convert %r to a FIXED_DICT' % (type(obj),))

    def isSameType(self, obj):
        if isinstance(obj, TrueDict):
            return True
        if isinstance(obj, dict):
            return set(obj.keys()) == {'keys', 'values'}
        return False


instance = TrueDictConverter()
