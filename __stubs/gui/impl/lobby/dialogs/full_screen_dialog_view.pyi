# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/full_screen_dialog_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import WindowLayer as WindowLayer
from gui.impl import backport as backport
from gui.impl.auxiliary.tooltips.simple_tooltip import createSimpleTooltip as createSimpleTooltip
from gui.impl.backport.backport_tooltip import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.dialogs.dialog_template_utils import getCurrencyTooltipAlias as getCurrencyTooltipAlias
from gui.impl.dialogs.sub_views.top_right.money_balance import NO_WGM_TOOLTIP_DATA as NO_WGM_TOOLTIP_DATA
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.format_resource_string_arg_model import FormatResourceStringArgModel as FormatResourceStringArgModel
from gui.impl.gen.view_models.views.dialogs.sub_views.currency_view_model import CurrencyType as CurrencyType
from gui.impl.gen.view_models.windows.full_screen_dialog_window_model import FullScreenDialogWindowModel as FullScreenDialogWindowModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.dialog_window import DialogResult as DialogResult, DialogButtons as DialogButtons, DialogFlags as DialogFlags
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.shared.money import Currency as Currency
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from py2to3 import patched_typing as patched_typing
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from wg_async import AsyncScope as AsyncScope, AsyncEvent as AsyncEvent, wg_await as wg_await, wg_async as wg_async, BrokenPromiseError as BrokenPromiseError, AsyncReturn as AsyncReturn
from frameworks import wulf as wulf
TViewModel: Any
_logger: Any

class FullScreenDialogBaseView(ViewImpl):
    __slots__: tuple
    BLUEPRINTS_CONVERSION = 'blueprintsConversion'
    __scope: Any
    __event: Any
    __result: Any
    def __init__(self, *args, **kwargs):
        ...
    # decorador original: @wg_async
    def wait(self):
        ...
    def _getAdditionalData(self):
        ...
    def _finalize(self):
        ...
    def _setResult(self, result):
        ...
    def stopWaiting(self, result):
        ...

# base nao representavel no stub: patched_typing.Generic[...]
class FullScreenDialogView(FullScreenDialogBaseView):
    __slots__: tuple
    _itemsCache: Any
    _stats: Any
    def __init__(self, settings):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTip(self, event):
        ...
    def _initialize(self):
        ...
    def _onInventoryResync(self, *args, **kwargs):
        ...
    def _setBaseParams(self, model):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def _onAcceptClicked(self):
        ...
    def _onAccept(self):
        ...
    def _onCancelClicked(self):
        ...
    def _onCancel(self):
        ...
    def _onExitClicked(self):
        ...
    def _setTitleArgs(self, arrModel, frmtArgs):
        ...
    def __setStats(self, model):
        ...
    def __createCurrencyTooltip(self, event, currency):
        ...

class FullScreenDialogWindowWrapper(LobbyWindow):
    __slots__: tuple
    __gui: Any
    __NOTIFICATIONS_LOCK_KEY = 'FullScreenDialogLockKey'
    _wrappedView: Any
    _blur: Any
    _doBlur: Any
    def __init__(self, wrappedView, parent=None, doBlur=True, layer=...):
        ...
    def _initialize(self):
        ...
    def wait(self):
        ...
    def stopWaiting(self, result):
        ...
    @classmethod
    def createIfNotExist(cls, layoutID, wrappedViewClass, parent=None, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __makeNotificationLockKey(self):
        ...
