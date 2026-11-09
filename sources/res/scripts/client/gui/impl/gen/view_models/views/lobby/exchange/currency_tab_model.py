# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/exchange/currency_tab_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/exchange/currency_tab_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.exchange.currency_model import CurrencyModel

class CurrencyTabModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CurrencyTabModel, self).__init__(properties=properties, commands=commands)

    def getCurrencies(self):
        return self._getArray(0)

    def setCurrencies(self, value):
        self._setArray(0, value)

    @staticmethod
    def getCurrenciesType():
        return CurrencyModel

    def getIsWalletAvailable(self):
        return self._getBool(1)

    def setIsWalletAvailable(self, value):
        self._setBool(1, value)

    def _initialize(self):
        super(CurrencyTabModel, self)._initialize()
        self._addArrayProperty('currencies', Array())
        self._addBoolProperty('isWalletAvailable', True)
