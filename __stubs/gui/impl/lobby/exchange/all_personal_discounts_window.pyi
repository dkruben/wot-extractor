# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/exchange/all_personal_discounts_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from frameworks.wulf import WindowFlags as WindowFlags, WindowLayer as WindowLayer, ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_all_personal_discounts_model import ExchangeRateAllPersonalDiscountsModel as ExchangeRateAllPersonalDiscountsModel, CurrencyType as CurrencyType
from gui.impl.lobby.exchange.exchange_rates_helper import EXCHANGE_RATE_NAME_TO_CURRENCIES as EXCHANGE_RATE_NAME_TO_CURRENCIES, fillAllDiscountsModel as fillAllDiscountsModel, MAX_SHOW_DISCOUNTS_INDEX as MAX_SHOW_DISCOUNTS_INDEX, getAllLimitedDiscountsAmount as getAllLimitedDiscountsAmount
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from helpers import dependency as dependency
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from typing import Optional as Optional
from skeletons.gui.game_control import IExchangeRateWithDiscounts as IExchangeRateWithDiscounts
_logger: Any

class AllPersonalDiscountsView(ViewImpl):
    __exchangeRatesProvider: Any
    __selectedValue: Any
    __exchangeRateType: Any
    def __init__(self, layoutID, exchangeRateType, selectedValue=None):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def exchangeRate(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _updateModel(self, model=None):
        ...
    def __updateAllModel(self):
        ...
    def __createModel(self):
        ...
    def __updateDiscounts(self, model):
        ...
    def __getSelectedGold(self):
        ...
    def __onClose(self):
        ...

class AllPersonalDiscountsWindow(LobbyWindow):
    def __init__(self, layoutID, exchangeRateType, selectedValue):
        ...
