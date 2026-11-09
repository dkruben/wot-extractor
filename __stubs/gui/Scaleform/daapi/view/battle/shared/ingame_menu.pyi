# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/ingame_menu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
import BattleReplay as BattleReplay
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.genConsts.INGAMEMENU_CONSTANTS import INGAMEMENU_CONSTANTS as INGAMEMENU_CONSTANTS
from gui.battle_control.battle_session import BattleExitResult as BattleExitResult
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui import DialogsInterface as DialogsInterface, GUI_SETTINGS as GUI_SETTINGS
from gui import makeHtmlString as makeHtmlString
from account_helpers.counter_settings import getCountNewSettings as getCountNewSettings
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID as DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta as I18nConfirmDialogMeta
from gui.Scaleform.daapi.view.meta.IngameMenuMeta import IngameMenuMeta as IngameMenuMeta
from gui.Scaleform.genConsts.GLOBAL_VARS_MGR_CONSTS import GLOBAL_VARS_MGR_CONSTS as GLOBAL_VARS_MGR_CONSTS
from gui.Scaleform.genConsts.INTERFACE_STATES import INTERFACE_STATES as INTERFACE_STATES
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.Scaleform.managers.battle_input import BattleGUIKeyHandler as BattleGUIKeyHandler
from gui.battle_control import event_dispatcher as battle_event_dispatcher
from gui.shared import event_dispatcher as shared_event_dispatcher
from gui.shared import events as events
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import i18n as i18n, dependency as dependency
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import IServerStatsController as IServerStatsController
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.daapi.view.battle.shared.premature_leave import showLeaverAliveWindow as showLeaverAliveWindow, showExitWindow as showExitWindow, showLeaverReplayWindow as showLeaverReplayWindow

class IngameMenu(IngameMenuMeta, BattleGUIKeyHandler):
    serverStats: Any
    sessionProvider: Any
    connectionMgr: Any
    def onWindowClose(self):
        ...
    def handleEscKey(self, isDown):
        ...
    def quitBattleClick(self):
        ...
    def settingsClick(self):
        ...
    def helpClick(self):
        ...
    def cancelClick(self):
        ...
    def onCounterNeedUpdate(self):
        ...
    def _populate(self):
        ...
    def __updateNewSettingsCount(self):
        ...
    def _dispose(self):
        ...
    # decorador original: @wg_async
    def _doLeaveArena(self):
        ...
    def _doExit(self):
        ...
    def _setServerSettings(self):
        ...
    def _setServerStats(self):
        ...
    def _setMenuButtonsLabels(self):
        ...
    def _setMenuButtons(self):
        ...
    # decorador original: @adisp_process
    def __doLeaveTutorial(self):
        ...
    def _getExitResult(self):
        ...
    @staticmethod
    def _showLeaverAliveWindow(isPlayerIGR):
        ...
    @staticmethod
    def __isPlayerIGR(playerInfo):
        ...
    def __onViewLoaded(self, view, *args, **kwargs):
        ...
