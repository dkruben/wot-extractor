# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/referral_program_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from Event import Event as Event
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import REFERRAL_COUNTER as REFERRAL_COUNTER
from account_helpers.settings_core.ServerSettingsManager import UI_STORAGE_KEYS as UI_STORAGE_KEYS
from constants import Configs as Configs
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.referral_program.browser.web_handlers import createReferralWebHandlers as createReferralWebHandlers
from gui.Scaleform.daapi.view.lobby.referral_program.referral_program_helpers import getReferralProgramURL as getReferralProgramURL, isCurrentUserRecruit as isCurrentUserRecruit
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl.lobby.common.sound_constants import SUBVIEW_SOUND_SPACE as SUBVIEW_SOUND_SPACE
from gui.limited_ui.lui_rules_storage import LUI_RULES as LUI_RULES
from gui.shared import g_eventBus as g_eventBus, events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showHangar as showHangar
from gui.wgnc.custom_actions_keeper import CustomActionsKeeper as CustomActionsKeeper
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IReferralProgramController as IReferralProgramController, ILimitedUIController as ILimitedUIController
from skeletons.gui.game_window_controller import GameWindowController as GameWindowController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

class ReferralProgramController(GameWindowController, IReferralProgramController):
    __settingsCore: Any
    __appLoader: Any
    __limitedUIController: Any
    __lobbyContext: Any
    __isReferralEnabled: Any
    __isEnabled: Any
    __isReferralHardDisabled: Any
    __serverSettings: Any
    __referralConfig: Any
    onReferralStateChanged: Any
    onReferralProgramUpdated: Any
    def __init__(self):
        ...
    @property
    def isEnabled(self):
        ...
    def setReferralHardDisabled(self, isDisabled=True):
        ...
    def onAccountBecomePlayer(self):
        ...
    @property
    def isNewReferralSeason(self):
        ...
    def showWindow(self, url=None, invokedFrom=None):
        ...
    def hideWindow(self):
        ...
    def isFirstIndication(self):
        ...
    def getBubbleCount(self):
        ...
    def updateBubble(self):
        ...
    def _openWindow(self, url, _=None):
        ...
    def _getUrl(self):
        ...
    def __updateReferralState(self, hardStateChange=False):
        ...
    def __checkReferralState(self):
        ...
    def _addListeners(self):
        ...
    def _removeListeners(self):
        ...
    def __getBrowserView(self):
        ...
    def __onReferralProgramButtonClicked(self, _):
        ...
    def __onServerSettingsChanged(self, serverSettings):
        ...
    def __onReferralConfigChanged(self, diff):
        ...
    def __setViewedSeason(self):
        ...
    def __resetBubbleCount(self):
        ...
    def __updateBubbleEvent(self):
        ...
    def __setButtonCirclesShown(self):
        ...
    def __processButtonPress(self, **_):
        ...
    def __updateBubbleVisibility(self, *_):
        ...
    def onDisconnected(self):
        ...
