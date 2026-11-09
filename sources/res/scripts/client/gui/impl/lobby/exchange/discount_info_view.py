# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/exchange/discount_info_view.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/exchange/discount_info_view.py
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_discount_model import DiscountType, ShowFormat
from gui.impl.common.components_presenter import BaseSubModelViewWithToolTips
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel
from helpers import dependency
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider

class ExchangeDiscountView(BaseSubModelViewWithToolTips):
    __exchangeRatesProvider = dependency.descriptor(IExchangeRatesWithDiscountsProvider)

    def __init__(self, exchangeType, *args, **kwargs):
        self.__exchangeType = exchangeType
        super(ExchangeDiscountView, self).__init__(*args, **kwargs)

    def initialize(self, *args, **kwargs):
        self._updateDiscountInfo()
        super(ExchangeDiscountView, self).initialize()

    def getViewModel(self):
        return self._viewModel

    @property
    def _exchangeRate(self):
        return self.__exchangeRatesProvider.get(self.__exchangeType)

    def _addListeners(self):
        self._exchangeRate.onUpdated += self._updateDiscountInfo

    def _removeListeners(self):
        self._exchangeRate.onUpdated -= self._updateDiscountInfo

    def _getDiscountInfo(self):
        return self._exchangeRate.discountInfo

    @replaceNoneKwargsModel
    def _updateDiscountInfo(self, model=None):
        self.__setDiscountInfo(model)

    def __setDiscountInfo(self, model):
        discount = self._getDiscountInfo()
        if discount is None:
            return model.setIsDiscountAvailable(False)
        else:
            discountType = DiscountType(discount.discountType.value)
            model.setIsDiscountAvailable(True)
            model.setDiscountType(discountType)
            model.exchangeRate.setGoldRateValue(discount.goldRateValue)
            model.exchangeRate.setResourceRateValue(discount.resourceRateValue)
            model.setShowFormat(ShowFormat(discount.showFormat.value))
            model.setAmountOfDiscount(0 if discountType == DiscountType.UNLIMITED else discount.amountOfDiscount)
            model.setDiscountLifetime(discount.discountLifetime)
            model.setDiscountPercent(self._exchangeRate.exchangeDiscountPercent)
            return
