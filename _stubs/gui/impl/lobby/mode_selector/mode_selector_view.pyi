# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mode_selector/mode_selector_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import typing as typing
import adisp as adisp
from constants import QUEUE_TYPE as QUEUE_TYPE
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags, WindowLayer as WindowLayer, ViewStatus as ViewStatus
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl import backport as backport
from gui.impl.auxiliary.tooltips.simple_tooltip import createSimpleTooltip as createSimpleTooltip, createSimpleIconTooltip as createSimpleIconTooltip
from gui.impl.backport.backport_tooltip import createAndLoadBackportTooltipWindow as createAndLoadBackportTooltipWindow
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.mode_selector.mode_selector_model import ModeSelectorModel as ModeSelectorModel
from gui.impl.gen.view_models.views.lobby.mode_selector.tooltips.mode_selector_tooltips_constants import ModeSelectorTooltipsConstants as ModeSelectorTooltipsConstants
from gui.impl.lobby.battle_pass.tooltips.battle_pass_completed_tooltip_view import BattlePassCompletedTooltipView as BattlePassCompletedTooltipView
from gui.impl.lobby.battle_pass.tooltips.battle_pass_in_progress_tooltip_view import BattlePassInProgressTooltipView as BattlePassInProgressTooltipView
from gui.impl.lobby.mode_selector.items import saveBattlePassStateForItems as saveBattlePassStateForItems
from gui.impl.lobby.mode_selector.mode_selector_data_provider import ModeSelectorDataProvider as ModeSelectorDataProvider
from gui.impl.lobby.mode_selector.sound_constants import MODE_SELECTOR_SOUND_SPACE as MODE_SELECTOR_SOUND_SPACE
from gui.impl.lobby.mode_selector.tooltips.simply_format_tooltip import SimplyFormatTooltipView as SimplyFormatTooltipView
from gui.impl.lobby.winback.popovers.winback_leave_mode_popover_view import WinbackLeaveModePopoverView as WinbackLeaveModePopoverView
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.tooltip_window import SimpleTooltipContent as SimpleTooltipContent
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import FullscreenModeSelectorEvent as FullscreenModeSelectorEvent, ModeSubSelectorEvent as ModeSubSelectorEvent, LoadViewEvent as LoadViewEvent
from gui.shared.system_factory import registerModeSelectorTooltips as registerModeSelectorTooltips, collectModeSelectorTooltips as collectModeSelectorTooltips
from gui.shared.view_helpers.blur_manager import CachedBlur as CachedBlur
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IWinbackController as IWinbackController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from wg_async import wg_await as wg_await, await_callback as await_callback, wg_async as wg_async, BrokenPromiseError as BrokenPromiseError, forwardAsFuture as forwardAsFuture
from typing import Optional as Optional, Callable as Callable
from gui.Scaleform.framework.application import AppEntry as AppEntry
from frameworks.wulf import View as View, ViewEvent as ViewEvent, Window as Window
from gui.Scaleform.managers import GameInputMgr as GameInputMgr
_logger: Any
_BACKGROUND_ALPHA = 0.7
_R_SIMPLE_TOOLTIP = R.views.common.tooltip_window.simple_tooltip_content.SimpleTooltipContent
_R_BACKPORT_TOOLTIP = R.views.common.tooltip_window.backport_tooltip_content.BackportTooltipContent
_SIMPLE_TOOLTIPS_KEY = 'simpleTooltipIds'
_CONTENT_TOOLTIPS_KEY = 'contentTooltipsMap'
_SIMPLE_TOOLTIP_IDS: list

class ModeSelectorView(ViewImpl):
    _COMMON_SOUND_SPACE = MODE_SELECTOR_SOUND_SPACE
    __appLoader: Any
    __lobbyContext: Any
    __gui: Any
    __winbackController: Any
    layoutID: Any
    _areWidgetsVisible = False
    __dataProvider: Any
    __blur: Any
    __prevOptimizationEnabled: Any
    __savedBackgroundAlpha: Any
    __isClickProcessing: Any
    __isGraphicsRestored: Any
    __subSelectorCallback: Any
    __isContentVisible: Any
    __tooltipConstants: Any
    def __init__(self, layoutId, provider=None, subSelectorCallback=None):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def inputManager(self):
        ...
    def createToolTip(self, event):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createPopOverContent(self, event):
        ...
    def refresh(self):
        ...
    def close(self):
        ...
    def _onLoading(self):
        ...
    def _initialize(self):
        ...
    def _onLoaded(self):
        ...
    def _finalize(self):
        ...
    def __restoreGraphics(self):
        ...
    def __dataProviderListChangeHandler(self):
        ...
    def __updateViewModel(self, vm):
        ...
    def __updateContentVisibility(self, event):
        ...
    def __updateClickProcessing(self, event):
        ...
    def __onExternalBackgroundAlphaChange(self, event):
        ...
    # decorador original: @wg_async
    def __itemClickHandler(self, event):
        ...
    def __showMapSelectionClickHandler(self):
        ...
    def __showWidgetsClickHandler(self):
        ...
    def __infoClickHandler(self, event):
        ...
    # decorador original: @adisp.adisp_async
    def __handleHeaderNavigation(self, callback):
        ...
    def __handleEscape(self):
        ...

def _getTooltipByContentIdMap():
    ...
# decorador original: @adisp.adisp_process
def isHeaderNavigationPossible(callback=None):
    ...
