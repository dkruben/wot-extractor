# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/exchange/discount_info_tooltip_decorator.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/exchange/discount_info_tooltip_decorator.py
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.backport.backport_tooltip import DecoratedTooltipWindow
from gui.impl.lobby.exchange.discount_info_tooltip import DiscountInfoTooltip, LimitedDiscountInfoTooltip
from gui.impl.lobby.exchange.exchange_rates_helper import NEED_ITEMS_TYPE_TO_EXCHANGE_RATE
from gui.shared.tooltips import ToolTipBaseData

class DiscountInfoTooltipContentWindowData(ToolTipBaseData):

    def __init__(self, context):
        super(DiscountInfoTooltipContentWindowData, self).__init__(context, TOOLTIPS_CONSTANTS.EXCHANGE_RATE_DISCOUNT_INFO)

    def getDisplayableData(self, needItemsType, *args, **kwargs):
        exchangeType = NEED_ITEMS_TYPE_TO_EXCHANGE_RATE.get(needItemsType, None)
        return DecoratedTooltipWindow(DiscountInfoTooltip(exchangeType), useDecorator=False)


class LimitedDiscountInfoTooltipContentWindowData(ToolTipBaseData):

    def __init__(self, context):
        super(LimitedDiscountInfoTooltipContentWindowData, self).__init__(context, TOOLTIPS_CONSTANTS.EXCHANGE_RATE_LIMITED_DISCOUNT_INFO)

    def getDisplayableData(self, needItemsType, selectedExchangeAmount, *args, **kwargs):
        exchangeType = NEED_ITEMS_TYPE_TO_EXCHANGE_RATE.get(needItemsType, None)
        return DecoratedTooltipWindow(LimitedDiscountInfoTooltip(exchangeType, selectedExchangeAmount), useDecorator=False)
