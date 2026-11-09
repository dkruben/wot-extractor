# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/exchange/base_exchange_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from exchange.personal_discounts_helper import getDiscountsRequiredForExchange as getDiscountsRequiredForExchange
from gui import SystemMessages as SystemMessages
from gui.game_control.exchange_rates_with_discounts import getCurrentTime as getCurrentTime
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.exchange.currency_model import CurrencyType as CurrencyType
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_base_model import ExchangeRateBaseModel as ExchangeRateBaseModel
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView
from gui.impl.common.components_presenter import ComponentsPresenterView as ComponentsPresenterView
from gui.impl.lobby.exchange.currency_tab_view import CurrenciesTabView as CurrenciesTabView, getCurrencyValueFromType as getCurrencyValueFromType
from gui.impl.lobby.exchange.discount_info_tooltip import DiscountInfoTooltip as DiscountInfoTooltip, LimitedDiscountInfoTooltip as LimitedDiscountInfoTooltip
from gui.impl.lobby.exchange.discount_info_view import ExchangeDiscountView as ExchangeDiscountView
from gui.impl.lobby.exchange.exchange_rates_helper import setDiscountViewed as setDiscountViewed, isDiscountViewed as isDiscountViewed, handleUserValuesInput as handleUserValuesInput, showAllPersonalDiscountsWindow as showAllPersonalDiscountsWindow, handleAndRoundStepperInput as handleAndRoundStepperInput
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController, IExchangeRatesWithDiscountsProvider as IExchangeRatesWithDiscountsProvider
from typing import Optional as Optional
from skeletons.gui.game_control import IExchangeRateWithDiscounts as IExchangeRateWithDiscounts

class BaseExchangeWindow(ComponentsPresenterView, FullScreenDialogBaseView):
    _wallet: Any
    __exchangeRatesProvider: Any
    __BLUR_INTENSITY = 0.8
    _initValues: Any
    __backgroundImage: Any
    __exchangeRateType: Any
    __blur: Any
    def __init__(self, settings, exchangeRateType, ctx=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def exchangeRate(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def _updateAllModel(self):
        ...
    def _updateModel(self, model=None):
        ...
    def _registerSubModels(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _onSelectedValueChanged(self, params=None, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _setStepperValues(self, selectedGold, selectedCurrency, model=None):
        ...
    def _onOpenAllDiscountsWindow(self):
        ...
    def _processResult(self, result, exchangeAmount):
        ...
    def _onExchange(self, event):
        ...
    def _setMaxAmountForExchange(self, maxGold, maxResource, model):
        ...
    def _getDiscountsRequiredForExchange(self, goldForExchange):
        ...
    def __setExchangeDiscountsInfo(self, model):
        ...
    def __onSelectedAmountChanged(self, params):
        ...
    def __updateData(self, *args):
        ...
    def __onClose(self):
        ...
