# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/details_price_block_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/tank_setup/dialogs/details_price_block_model.py
from frameworks.wulf import ViewModel

class DetailsPriceBlockModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(DetailsPriceBlockModel, self).__init__(properties=properties, commands=commands)

    def getCurrencyName(self):
        return self._getString(0)

    def setCurrencyName(self, value):
        self._setString(0, value)

    def getCountDevice(self):
        return self._getNumber(1)

    def setCountDevice(self, value):
        self._setNumber(1, value)

    def getPriceDevice(self):
        return self._getNumber(2)

    def setPriceDevice(self, value):
        self._setNumber(2, value)

    def _initialize(self):
        super(DetailsPriceBlockModel, self)._initialize()
        self._addStringProperty('currencyName', '')
        self._addNumberProperty('countDevice', 0)
        self._addNumberProperty('priceDevice', 0)
