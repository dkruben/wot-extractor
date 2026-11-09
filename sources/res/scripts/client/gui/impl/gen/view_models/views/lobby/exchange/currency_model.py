# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/exchange/currency_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/exchange/currency_model.py
from enum import Enum
from frameworks.wulf import ViewModel

class CurrencyType(Enum):
    CREDITS = 'credits'
    GOLD = 'gold'
    CRYSTAL = 'crystal'
    FREEXP = 'freeXP'


class CurrencyModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CurrencyModel, self).__init__(properties=properties, commands=commands)

    def getCurrencyType(self):
        return CurrencyType(self._getString(0))

    def setCurrencyType(self, value):
        self._setString(0, value.value)

    def getValue(self):
        return self._getNumber(1)

    def setValue(self, value):
        self._setNumber(1, value)

    def getTooltipId(self):
        return self._getNumber(2)

    def setTooltipId(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(CurrencyModel, self)._initialize()
        self._addStringProperty('currencyType', CurrencyType.GOLD.value)
        self._addNumberProperty('value', 0)
        self._addNumberProperty('tooltipId', 0)
