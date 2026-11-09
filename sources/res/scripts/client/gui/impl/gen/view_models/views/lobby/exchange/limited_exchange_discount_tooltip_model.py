# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/exchange/limited_exchange_discount_tooltip_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/views/lobby/exchange/limited_exchange_discount_tooltip_model.py
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.exchange.discount_presentation import DiscountPresentation
from gui.impl.gen.view_models.views.lobby.exchange.exchange_discount_tooltip_model import ExchangeDiscountTooltipModel

class LimitedExchangeDiscountTooltipModel(ExchangeDiscountTooltipModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(LimitedExchangeDiscountTooltipModel, self).__init__(properties=properties, commands=commands)

    def getDiscounts(self):
        return self._getArray(6)

    def setDiscounts(self, value):
        self._setArray(6, value)

    @staticmethod
    def getDiscountsType():
        return DiscountPresentation

    def getAllDiscountsLimitsAmount(self):
        return self._getNumber(7)

    def setAllDiscountsLimitsAmount(self, value):
        self._setNumber(7, value)

    def _initialize(self):
        super(LimitedExchangeDiscountTooltipModel, self)._initialize()
        self._addArrayProperty('discounts', Array())
        self._addNumberProperty('allDiscountsLimitsAmount', 0)
