# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/ingame_menu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
from BWUtil import AsyncReturn as AsyncReturn
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from gui.Scaleform.daapi.view.battle.shared.premature_leave import showResDialogWindow as showResDialogWindow, showLeaverReplayWindow as showLeaverReplayWindow, closeDialogWindow as closePrematureLeaveWindow
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.Scaleform.genConsts.INGAMEMENU_CONSTANTS import INGAMEMENU_CONSTANTS as INGAMEMENU_CONSTANTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import LoadViewEvent as LoadViewEvent
from story_mode.gui.story_mode_gui_constants import VIEW_ALIAS as VIEW_ALIAS
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.consts import LogWindows as LogWindows, LogButtons as LogButtons
from story_mode.uilogging.story_mode.loggers import WindowLogger as WindowLogger
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.Scaleform.daapi.view.battle.shared.ingame_menu import IngameMenu as IngameMenu
from gui.Scaleform.genConsts.INTERFACE_STATES import INTERFACE_STATES as INTERFACE_STATES
from helpers import dependency as dependency
from gui.Scaleform.locale.MENU import MENU as MENU

class StoryModeIngameMenu(IngameMenu):
    _storyModeCtrl: Any
    _uiLogger: Any
    def __init__(self, ctx=None):
        ...
    # decorador original: @wg_async
    def quitBattleClick(self):
        ...
    def onCounterNeedUpdate(self):
        ...
    def settingsClick(self):
        ...
    def helpClick(self):
        ...
    def cancelClick(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _setServerSettings(self):
        ...
    def _setServerStats(self):
        ...
    def _setMenuButtonsLabels(self):
        ...
    def _setMenuButtons(self):
        ...
    # decorador original: @wg_async
    def _openConfirmExitDialog(self):
        ...
    @property
    def __isForceOnboarding(self):
        ...
    @property
    def __isOnboardingGuiType(self):
        ...
