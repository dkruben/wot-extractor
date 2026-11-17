# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/commendations_messages_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
import BattleReplay as BattleReplay
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from commendations_common import CommendationHelpers as CommendationHelpers
from constants import CommendationsState as CommendationsState
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from messenger.m_constants import MESSENGER_COMMAND_TYPE as MESSENGER_COMMAND_TYPE
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.shared_messages import ClientActionMessage as ClientActionMessage, ACTION_MESSAGE_TYPE as ACTION_MESSAGE_TYPE
from skeletons.account_helpers.settings_core import IBattleCommunicationsSettings as IBattleCommunicationsSettings
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from messenger_common_chat2 import MESSENGER_ACTION_IDS as _ACTIONS
from skeletons.gui.game_control import ICommendationsController as ICommendationsController
from commendations_common.CommendationHelpers import CommendationsSource as CommendationsSource
from messenger.proto.bw_chat2.battle_chat_cmd import _ReceivedCmdDecorator as _ReceivedCmdDecorator
from gui.battle_control.controllers.repositories import BattleSessionSetup as BattleSessionSetup
_logger: Any
_RECIPIENT_DURATION_MS = 5000
_SENDER_DURATION_MS = 2000
MESSAGE_STATE_RESOURCE_MAP: dict
MESSAGE_STATE_MARKER_MAP: dict

class _CommendationsActionMessage(ClientActionMessage):
    _iconName: Any
    def __init__(self, message, iconName):
        ...
    def getIconName(self):
        ...

class CommendationsMessagesController(IBattleController):
    __sessionProvider: Any
    __battleComSettings: Any
    __commendationsCtrl: Any
    _arena: Any
    __isActive: Any
    def __init__(self, setup):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def getControllerID(self):
        ...
    def sendCommendations(self, targetID, source):
        ...
    def _activateListeners(self):
        ...
    def _deactivateListeners(self):
        ...
    def _canHandleCommand(self, cmd):
        ...
    def _canShowFeedback(self, cmd):
        ...
    def _onCommandReceived(self, cmd):
        ...
    def _addToChat(self, targetID, resourceName):
        ...
    def _onConfigChanged(self):
        ...
