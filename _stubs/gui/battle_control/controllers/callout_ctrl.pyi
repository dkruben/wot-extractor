# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/callout_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import BattleReplay as BattleReplay
import CommandMapping as CommandMapping
import Event as Event
import Keys as Keys
from chat_commands_consts import _PERSONAL_MESSAGE_MUTE_DURATION as _PERSONAL_MESSAGE_MUTE_DURATION, BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from commendations_common.CommendationHelpers import CommendationsSource as CommendationsSource
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE
from frameworks.wulf import WindowLayer as WindowLayer
from gui import GUI_CTRL_MODE_FLAG as GUI_CTRL_MODE_FLAG
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES as BATTLE_VIEW_ALIASES
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control import event_dispatcher as gui_event_dispatcher
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.event_dispatcher import _makeKeyCtx as _makeKeyCtx
from gui.battle_control.view_components import IViewComponentsController as IViewComponentsController
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, g_eventBus as g_eventBus
from gui.shared.events import GameEvent as GameEvent
from helpers import dependency as dependency
from helpers.CallbackDelayer import CallbackDelayer as CallbackDelayer
from messenger.m_constants import MESSENGER_COMMAND_TYPE as MESSENGER_COMMAND_TYPE
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS
from skeletons.account_helpers.settings_core import IBattleCommunicationsSettings as IBattleCommunicationsSettings
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import ICommendationsController as ICommendationsController
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from uilogging.player_satisfaction_rating.loggers import BattleResponseLogger as BattleResponseLogger
_logger: Any
_CALLOUT_MESSAGES_BLOCK_DURATION = 15
_HINT_TIMEOUT = 10
_DELAY_FOR_OPENING_RADIAL_MENU = 0.2
_COMMENDATION_CALLOUT_ACTION_KEY = Keys.KEY_TAB
_CONSUMERS_LOCKS: tuple
CommandReceivedData: Any
_CALLOUT_COMMANDS_TO_REPLY_COMMANDS: dict

class CalloutController(CallbackDelayer, IViewComponentsController):
    sessionProvider: Any
    battleCommunications: Any
    __commendationsCtrl: Any
    __appLoader: Any
    __guiLoader: Any
    __eventManager: Any
    __isActive: Any
    __isCalloutEnabled: Any
    __isCommendationsCalloutEnabled: Any
    __isCommendationsEnabled: Any
    __isIBCEnabled: Any
    __commandReceivedData: Any
    __lastPersonalMsgTimestamp: Any
    __lastCalloutTimestamp: Any
    __ui: Any
    __radialKeyDown: Any
    __radialMenuIsOpen: Any
    __statsKeyDown: Any
    __statsScreenIsOpen: Any
    __previousForcedGuiControlModeFlags: Any
    _uiPlayerSatisfactionRatingLogger: Any
    onRadialMenuOpenChanged: Any
    def __init__(self, setup):
        ...
    @property
    def isCommendationCalloutActive(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def setViewComponents(self, component):
        ...
    def clearViewComponents(self):
        ...
    def isRadialMenuOpened(self):
        ...
    def __setRadialMenuOpen(self, value):
        ...
    def resetRadialMenuData(self, onStop=False, reshow=False):
        ...
    def _isContainerStateOK(self):
        ...
    def handleTabScreenKeyPress(self, key, isDown):
        ...
    def handleCalloutAndRadialMenuKeyPress(self, key, isDown):
        ...
    def __activateListeners(self):
        ...
    def __deactivateListeners(self):
        ...
    def __onCommandReceived(self, cmd):
        ...
    def __handleCalloutButtonEvent(self, event):
        ...
    def __onBattleCommunicationChanged(self):
        ...
    def __executeHide(self, wasAnswered=False, commandReceived=None):
        ...
    def __delayOpenRadialMenu(self):
        ...
    def __openRadialMenu(self):
        ...
    def __openTabScreen(self):
        ...
    @staticmethod
    def fireCalloutDisplayEvent(isShown):
        ...
    def __onCalloutHidingFinished(self):
        ...
    def __enabledForArenaBonusType(self):
        ...

def createCalloutController(setup):
    ...
