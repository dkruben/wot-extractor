# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/exchange_rate_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/exchange_rate_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_discount_model import ExchangeRateDiscountModel

class ExchangeRateModel(ViewModel):
    __slots__ = ('onOpenAllDiscountsWindow', 'onSelectedValueUpdated')

    def __init__(self, properties=5, commands=2):
        super(ExchangeRateModel, self).__init__(properties=properties, commands=commands)

    @property
    def discount(self):
        return self._getViewModel(0)

    @staticmethod
    def getDiscountType():
        return ExchangeRateDiscountModel

    def getDefault(self):
        return self._getReal(1)

    def setDefault(self, value):
        self._setReal(1, value)

    def getMaxResourceAmountForExchange(self):
        return self._getNumber(2)

    def setMaxResourceAmountForExchange(self, value):
        self._setNumber(2, value)

    def getMaxGoldAmountForExchange(self):
        return self._getNumber(3)

    def setMaxGoldAmountForExchange(self, value):
        self._setNumber(3, value)

    def getAmountOfPersonalDiscounts(self):
        return self._getNumber(4)

    def setAmountOfPersonalDiscounts(self, value):
        self._setNumber(4, value)

    def _initialize(self):
        super(ExchangeRateModel, self)._initialize()
        self._addViewModelProperty('discount', ExchangeRateDiscountModel())
        self._addRealProperty('default', 0.0)
        self._addNumberProperty('maxResourceAmountForExchange', 0)
        self._addNumberProperty('maxGoldAmountForExchange', 1)
        self._addNumberProperty('amountOfPersonalDiscounts', 0)
        self.onOpenAllDiscountsWindow = self._addCommand('onOpenAllDiscountsWindow')
        self.onSelectedValueUpdated = self._addCommand('onSelectedValueUpdated')
