# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/contents/exchange_content.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from exchange.personal_discounts_helper import getDiscountsRequiredForExchange as getDiscountsRequiredForExchange
from gui import SystemMessages as SystemMessages
from gui.game_control.exchange_rates_with_discounts import getCurrentTime as getCurrentTime
from gui.impl.auxiliary.exchanger import Exchanger as Exchanger
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.exchange_panel_model import ExchangePanelModel as ExchangePanelModel
from gui.impl.gen.view_models.common.price_item_model import PriceItemModel as PriceItemModel
from gui.impl.gen.view_models.views.lobby.exchange.currency_model import CurrencyType as CurrencyType
from gui.impl.lobby.exchange.currency_tab_view import getCurrencyValueFromType as getCurrencyValueFromType
from gui.impl.lobby.exchange.discount_info_tooltip import DiscountInfoTooltip as DiscountInfoTooltip, LimitedDiscountInfoTooltip as LimitedDiscountInfoTooltip
from gui.impl.lobby.exchange.discount_info_view import ExchangeDiscountView as ExchangeDiscountView
from gui.impl.lobby.exchange.exchange_rates_helper import getRateNameFromCurrencies as getRateNameFromCurrencies, handleUserValuesInput as handleUserValuesInput, showAllPersonalDiscountsWindow as showAllPersonalDiscountsWindow, handleAndRoundStepperInput as handleAndRoundStepperInput
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class ExchangeContentResult(Enum):
    IS_OK = 0
    SERVER_ERROR = 1
    INVALID_VALUE = 2

class ExchangeContent(ExchangeDiscountView):
    __fromItem: Any
    __toItem: Any
    __needItem: Any
    __exchanger: Any
    def __init__(self, fromItem, toItem, viewModel=None, needItem=0):
        ...
    def onLoading(self, *args, **kwargs):
        ...
    def update(self, needItem=0):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def exchange(self, callback=None):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _getAvailableGoldAmount(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _updateDiscountInfo(self, model=None):
        ...
    def __onOpenAllDiscountsWindow(self):
        ...
    def __onSelectedAmountChanged(self, event):
        ...
    def __updateTooltipInformation(self):
        ...
    def __validateCount(self):
        ...
    def __fillItemsModel(self, fromItemCount, toItemCount):
        ...
    def __fillRateModel(self, model):
        ...

class ExchangeMoneyInfo(object):
    __itemsCache: Any
    __walletController: Any
    _type: Any
    def __init__(self, currencyType=''):
        ...
    def isEnough(self, count):
        ...
    def getType(self):
        ...
    def isAvailable(self):
        ...
    def getMaxCount(self):
        ...
    def updateItemModel(self, viewModel, count):
        ...
