# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/currency_value_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/currency_value_model.py
from enum import Enum
from frameworks.wulf import Array, ViewModel

class ValueModifiers(Enum):
    UNDEFINED = 'undefined'
    MUL = 'mul'
    ADD = 'add'
    SUB = 'sub'
    PROCENT = 'procent'
    SHOW_NEGATIVE_IMPACT = 'showNegativeImpact'


class CurrencyValueModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(CurrencyValueModel, self).__init__(properties=properties, commands=commands)

    def getCurrencyType(self):
        return self._getString(0)

    def setCurrencyType(self, value):
        self._setString(0, value)

    def getValue(self):
        return self._getReal(1)

    def setValue(self, value):
        self._setReal(1, value)

    def getIsShown(self):
        return self._getBool(2)

    def setIsShown(self, value):
        self._setBool(2, value)

    def getModifiers(self):
        return self._getArray(3)

    def setModifiers(self, value):
        self._setArray(3, value)

    @staticmethod
    def getModifiersType():
        return ValueModifiers

    def _initialize(self):
        super(CurrencyValueModel, self)._initialize()
        self._addStringProperty('currencyType', '')
        self._addRealProperty('value', 0.0)
        self._addBoolProperty('isShown', False)
        self._addArrayProperty('modifiers', Array())
