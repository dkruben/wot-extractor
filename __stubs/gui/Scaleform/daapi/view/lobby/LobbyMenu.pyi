# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/LobbyMenu.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import constants as constants
from account_helpers.AccountSettings import AccountSettings as AccountSettings, LOBBY_MENU_MANUAL_TRIGGER_SHOWN as LOBBY_MENU_MANUAL_TRIGGER_SHOWN
from account_helpers.counter_settings import getCountNewSettings as getCountNewSettings
from adisp import adisp_process as adisp_process
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showHangar as showHangar
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui import DialogsInterface as DialogsInterface, GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.view.dialogs import DIALOG_BUTTON_ID as DIALOG_BUTTON_ID
from gui.Scaleform.daapi.view.meta.LobbyMenuMeta import LobbyMenuMeta as LobbyMenuMeta
from gui.Scaleform.genConsts.MENU_CONSTANTS import MENU_CONSTANTS as MENU_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl.dialogs import dialogs as dialogs
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.shared import event_dispatcher as event_dispatcher, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from gui.shared.formatters import text_styles as text_styles, icons as icons
from gui.shared.tutorial_helper import getTutorialGlobalStorage as getTutorialGlobalStorage
from gui.sounds.ambients import LobbySubViewEnv as LobbySubViewEnv
from helpers import dependency as dependency, getFullClientVersion as getFullClientVersion
from skeletons.gameplay import IGameplayLogic as IGameplayLogic
from skeletons.gui.game_control import IManualController as IManualController
from skeletons.gui.game_control import IPromoController as IPromoController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from tutorial.control.context import GLOBAL_FLAG as GLOBAL_FLAG

class LobbyMenu(LobbyMenuMeta):
    __sound_env__ = LobbySubViewEnv
    promo: Any
    lobbyContext: Any
    gameplay: Any
    manualController: Any
    gui: Any
    __manualBtnIsVisible: Any
    __postBtnIsVisible: Any
    def __init__(self, *args, **kwargs):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    # decorador original: @adisp_process
    def postClick(self):
        ...
    def settingsClick(self):
        ...
    def onWindowClose(self):
        ...
    def cancelClick(self):
        ...
    def onEscapePress(self):
        ...
    # decorador original: @adisp_process
    def refuseTraining(self):
        ...
    # decorador original: @adisp_process
    def logoffClick(self):
        ...
    # decorador original: @wg_async
    def quitClick(self):
        ...
    def onCounterNeedUpdate(self):
        ...
    def manualClick(self):
        ...
    def showLegal(self):
        ...
    def toReportContent(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __updateManualBtn(self):
        ...
    def __updateVersionState(self):
        ...
    def __updateUIState(self):
        ...
    def __setPostButtonsIcons(self):
        ...
    def __isInQueue(self):
        ...
    def __updateNewSettingsCount(self):
        ...
    def __addListeners(self):
        ...
    def __removeListeners(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...
    def __updatePostButton(self):
        ...
    @staticmethod
    def __showLobbyMenu():
        ...
