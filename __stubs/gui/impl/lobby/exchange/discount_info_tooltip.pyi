# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/exchange/discount_info_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from exchange.personal_discounts_constants import ExchangeRateShowFormat as ExchangeRateShowFormat, ExchangeRate as ExchangeRate
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.exchange.exchange_discount_tooltip_model import ExchangeDiscountTooltipModel as ExchangeDiscountTooltipModel, CurrencyType as CurrencyType
from gui.impl.gen.view_models.views.lobby.exchange.limited_exchange_discount_tooltip_model import LimitedExchangeDiscountTooltipModel as LimitedExchangeDiscountTooltipModel
from gui.impl.lobby.exchange.exchange_rates_helper import EXCHANGE_RATE_NAME_TO_CURRENCIES as EXCHANGE_RATE_NAME_TO_CURRENCIES, MAX_SHOW_DISCOUNTS_INDEX as MAX_SHOW_DISCOUNTS_INDEX, fillAllDiscountsModel as fillAllDiscountsModel, getAllLimitedDiscountsAmount as getAllLimitedDiscountsAmount
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from typing import Optional as Optional
from exchange.personal_discounts_constants import ExchangeDiscountInfo as ExchangeDiscountInfo
from skeletons.gui.game_control import IExchangeRateWithDiscounts as IExchangeRateWithDiscounts
_logger: Any

class DiscountInfoTooltip(ViewImpl):
    __exchangeRateProvider: Any
    __exchangeType: Any
    def __init__(self, exchangeType, contentID=None, model=None, *args):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def exchangeRate(self):
        ...
    @property
    def discount(self):
        ...
    @property
    def defaultRate(self):
        ...
    @property
    def commonRate(self):
        ...
    @property
    def personalDiscountRate(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _update(self, model=None):
        ...
    def __updateData(self):
        ...

class LimitedDiscountInfoTooltip(DiscountInfoTooltip):
    __selectedGoldAmount: Any
    def __init__(self, exchangeType, selectedExchangeAmount, *args):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def commonRate(self):
        ...
    def _getListeners(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _update(self, model=None):
        ...
    def __updateSelectedAmount(self, event):
        ...
