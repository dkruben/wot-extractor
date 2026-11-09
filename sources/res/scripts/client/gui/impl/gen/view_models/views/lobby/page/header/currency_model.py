# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/page/header/currency_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/page/header/currency_model.py
from frameworks.wulf import ViewModel

class CurrencyModel(ViewModel):
    __slots__ = ()
    STATUS_SYNCING = 'SYNCING'
    STATUS_NOT_AVAILABLE = 'NOT_AVAILABLE'
    STATUS_AVAILABLE = 'AVAILABLE'

    def __init__(self, properties=4, commands=0):
        super(CurrencyModel, self).__init__(properties=properties, commands=commands)

    def getValue(self):
        return self._getNumber(0)

    def setValue(self, value):
        self._setNumber(0, value)

    def getDiscount(self):
        return self._getNumber(1)

    def setDiscount(self, value):
        self._setNumber(1, value)

    def getStatus(self):
        return self._getString(2)

    def setStatus(self, value):
        self._setString(2, value)

    def getTooltipType(self):
        return self._getString(3)

    def setTooltipType(self, value):
        self._setString(3, value)

    def _initialize(self):
        super(CurrencyModel, self)._initialize()
        self._addNumberProperty('value', 0)
        self._addNumberProperty('discount', 0)
        self._addStringProperty('status', '')
        self._addStringProperty('tooltipType', '')
