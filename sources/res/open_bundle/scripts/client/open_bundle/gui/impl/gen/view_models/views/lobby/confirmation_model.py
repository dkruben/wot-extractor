# wot-extractor: codigo DESCOMPILADO de sources/res/open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/confirmation_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: open_bundle/scripts/client/open_bundle/gui/impl/gen/view_models/views/lobby/confirmation_model.py
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class ConfirmationModel(ViewModel):
    __slots__ = ('confirm', 'cancel')

    def __init__(self, properties=4, commands=2):
        super(ConfirmationModel, self).__init__(properties=properties, commands=commands)

    @property
    def price(self):
        return self._getViewModel(0)

    @staticmethod
    def getPriceType():
        return PriceItemModel

    def getBundleType(self):
        return self._getString(1)

    def setBundleType(self, value):
        self._setString(1, value)

    def getBalance(self):
        return self._getArray(2)

    def setBalance(self, value):
        self._setArray(2, value)

    @staticmethod
    def getBalanceType():
        return PriceItemModel

    def getIsWalletAvailable(self):
        return self._getBool(3)

    def setIsWalletAvailable(self, value):
        self._setBool(3, value)

    def _initialize(self):
        super(ConfirmationModel, self)._initialize()
        self._addViewModelProperty('price', PriceItemModel())
        self._addStringProperty('bundleType', '')
        self._addArrayProperty('balance', Array())
        self._addBoolProperty('isWalletAvailable', True)
        self.confirm = self._addCommand('confirm')
        self.cancel = self._addCommand('cancel')
