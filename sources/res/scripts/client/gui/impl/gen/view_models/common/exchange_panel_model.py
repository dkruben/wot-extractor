# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/gen/view_models/common/exchange_panel_model.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/gen/view_models/common/exchange_panel_model.py
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.exchange_rate_model import ExchangeRateModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel

class ExchangePanelModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ExchangePanelModel, self).__init__(properties=properties, commands=commands)

    @property
    def fromItem(self):
        return self._getViewModel(0)

    @staticmethod
    def getFromItemType():
        return PriceItemModel

    @property
    def toItem(self):
        return self._getViewModel(1)

    @staticmethod
    def getToItemType():
        return PriceItemModel

    @property
    def exchangeRate(self):
        return self._getViewModel(2)

    @staticmethod
    def getExchangeRateType():
        return ExchangeRateModel

    def _initialize(self):
        super(ExchangePanelModel, self)._initialize()
        self._addViewModelProperty('fromItem', PriceItemModel())
        self._addViewModelProperty('toItem', PriceItemModel())
        self._addViewModelProperty('exchangeRate', ExchangeRateModel())
