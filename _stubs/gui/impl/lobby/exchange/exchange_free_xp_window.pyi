# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/exchange/exchange_free_xp_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui import GUI_NATIONS_ORDER_INDEX as GUI_NATIONS_ORDER_INDEX
from gui.impl.lobby.exchange.exchange_rates_helper import calculateMaxPossibleFreeXp as calculateMaxPossibleFreeXp, handleUserValuesInput as handleUserValuesInput, handleAndRoundStepperInput as handleAndRoundStepperInput
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.utils.decorators import adisp_process as adisp_process
from exchange.personal_discounts_constants import EXCHANGE_RATE_FREE_XP_NAME as EXCHANGE_RATE_FREE_XP_NAME
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_free_xp_model import ExchangeRateFreeXpModel as ExchangeRateFreeXpModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_vehicles_selection_model import ExchangeRateVehiclesSelectionModel as ExchangeRateVehiclesSelectionModel
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from gui.impl.lobby.exchange.base_exchange_window import BaseExchangeWindow as BaseExchangeWindow
from gui.shared.gui_items.processors.common import FreeXPExchanger as FreeXPExchanger
from gui.shop import showBuyGoldForXpWebOverlay as showBuyGoldForXpWebOverlay
from gui.veh_post_progression.models.progression import PostProgressionCompletion as PostProgressionCompletion
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class ExchangeFreeXPView(BaseExchangeWindow):
    __itemsCache: Any
    __xpSelectedForExchange: Any
    __selectedXpFromVehicles: Any
    _initValues: Any
    def __init__(self, layoutID, ctx=None, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _updateModel(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _setStepperValues(self, selectedGold, selectedCurrency, model=None):
        ...
    def _setMaxAmountForExchange(self, maxGold, maxResource, model):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _onSelectedValueChanged(self, params=None, model=None):
        ...
    # decorador original: @adisp_process(...)
    def _onExchange(self, data):
        ...
    @staticmethod
    def _goToGoldBuy(gold):
        ...
    def __updateVehiclesInfo(self, model=None):
        ...
    @staticmethod
    def __addVehicleAdditionalInfo(model, vehicle):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __onVehiclesSelectedChanged(self, event=None, vehiclesChanged=True, model=None):
        ...
    def __updateData(self, *args):
        ...

class ExchangeXPWindowDialog(ExchangeFreeXPView):
    __slots__: tuple
    _result: Any
    _exchangeAmount: Any
    def __init__(self, *args, **kwargs):
        ...
    def _processResult(self, result, exchangeAmount):
        ...
    def _goToGoldBuy(self, gold):
        ...
    def _getAdditionalData(self):
        ...
    def _setNotExchangedResult(self):
        ...

def getLevelOfFieldModification(vehicle):
    ...
