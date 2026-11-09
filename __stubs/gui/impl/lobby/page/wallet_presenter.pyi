# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/page/wallet_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import itervalues as itervalues
from helpers.events_handler import EventsHandler as EventsHandler
from Event import Event as Event
from adisp import adisp_process as adisp_process
from constants import IS_SINGAPORE as IS_SINGAPORE
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyGoldUrl as getBuyGoldUrl
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.game_control.wallet import WalletController as WalletController
from gui.impl.gen.view_models.views.lobby.page.header.currency_model import CurrencyModel as CurrencyModel
from gui.impl.gen.view_models.views.lobby.page.header.wallet_model import WalletModel as WalletModel
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.shared import event_dispatcher as shared_events
from gui.shared.event_dispatcher import showShop as showShop
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController, IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class CurrencyStatusProvider(EventsHandler):
    _itemsCache: Any
    _wallet: Any
    _currencyType: Any
    onChanged: Any
    def __init__(self, currencyType):
        ...
    def initialize(self):
        ...
    def finalize(self):
        ...
    def getCurrencyType(self):
        ...
    def createModel(self):
        ...
    def fillModel(self, currencyModel):
        ...
    def doAction(self):
        ...
    def _changed(self, *args):
        ...
    def _getCallbacks(self):
        ...

class CrystalProvider(CurrencyStatusProvider):
    def __init__(self, currencyType=...):
        ...
    def fillModel(self, currencyModel):
        ...
    def doAction(self):
        ...
    def _getEvents(self):
        ...

class GoldProvider(CurrencyStatusProvider):
    _lobbyContext: Any
    def __init__(self, currencyType=...):
        ...
    def fillModel(self, currencyModel):
        ...
    # decorador original: @adisp_process
    def doAction(self):
        ...
    def _getEvents(self):
        ...

class CreditsProvider(CurrencyStatusProvider):
    _exchangeRates: Any
    def __init__(self, currencyType=...):
        ...
    def fillModel(self, currencyModel):
        ...
    def doAction(self):
        ...
    def _getEvents(self):
        ...

class FreeXpProvider(CurrencyStatusProvider):
    _exchangeRates: Any
    def __init__(self, currencyType=...):
        ...
    def fillModel(self, currencyModel):
        ...
    def doAction(self):
        ...
    def _getEvents(self):
        ...

# base nao representavel no stub: ViewComponent[...]
class WalletPresenter:
    _currencyProviders: Any
    def __init__(self, currencyStatusProviders=None, model=...):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __onCurrencyChanged(self, currencyType):
        ...
    def __onCurrenciesUpdate(self):
        ...
    def __onCurrencyAction(self, args):
        ...
