# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/lobby/feature/purchase_dialog_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from collections import namedtuple as namedtuple
from advent_calendar.gui.impl.gen.view_models.views.lobby.purchase_dialog_model import PurchaseDialogModel as PurchaseDialogModel
from advent_calendar.gui.impl.lobby.feature.currency_provider import CurrencyProvider as CurrencyProvider, CurrencyInfo as CurrencyInfo
from advent_calendar.gui.impl.lobby.feature.tooltips.advent_calendar_simple_tooltip_view import AdventCalendarSimpleTooltip as AdventCalendarSimpleTooltip
from advent_calendar.skeletons import IAdventCalendarController as IAdventCalendarController
from gui.impl.gen import R as R
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.lobby.dialogs.full_screen_dialog_view import FullScreenDialogBaseView as FullScreenDialogBaseView, TViewModel as TViewModel
from gui.impl.pub.dialog_window import DialogButtons as DialogButtons
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from helpers import dependency as dependency
from skeletons.gui.game_control import IWalletController as IWalletController
from typing import Dict as Dict, List as List, Optional as Optional
from gui.impl.backport import TooltipData as TooltipData
_logger: Any
PurchaseData: Any

# base nao representavel no stub: ViewComponent[...]
class BasePurchaseDialogView(FullScreenDialogBaseView):
    _wallet: Any
    __adventController: Any
    _dayId: Any
    _price: Any
    _currencyProvider: Any
    _currency: Any
    _tooltips: Any
    def __init__(self, dayId, price, currencyProvider, layoutID, model):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _getAdditionalData(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _updatePrice(self, model=None):
        ...
    def _fillModel(self):
        ...
    def _setCurrency(self):
        ...
    def _onClose(self):
        ...
    def _onAccept(self):
        ...
    def __onWalletStatusChanged(self, *_):
        ...
    def __onBalanceUpdated(self):
        ...
    def __onSettingsChanged(self):
        ...

# base nao representavel no stub: BasePurchaseDialogView[...]
class PurchaseDialogView:
    def __init__(self, dayId, price, currencyProvider=None):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _fillModel(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _updatePrice(self, model=None):
        ...
