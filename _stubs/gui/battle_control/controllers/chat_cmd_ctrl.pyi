# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/chat_cmd_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import math as math
import weakref as weakref
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import CommandMapping as CommandMapping
import DestructibleEntity as DestructibleEntity
import Math as Math
import Vehicle as Vehicle
from AvatarInputHandler import aih_global_binding as aih_global_binding
from AvatarInputHandler.cameras import getWorldRayAndPoint as getWorldRayAndPoint
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from arena_component_system.sector_base_arena_component import ID_TO_BASENAME as ID_TO_BASENAME
from chat_commands_consts import MarkerType as MarkerType, DefaultMarkerSubType as DefaultMarkerSubType, ReplyState as ReplyState, BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES, INVALID_MARKER_SUBTYPE as INVALID_MARKER_SUBTYPE, _COMMAND_NAME_TRANSFORM_MARKER_TYPE as _COMMAND_NAME_TRANSFORM_MARKER_TYPE, ONE_SHOT_COMMANDS_TO_REPLIES as ONE_SHOT_COMMANDS_TO_REPLIES, COMMAND_RESPONDING_MAPPING as COMMAND_RESPONDING_MAPPING
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events, g_eventBus as g_eventBus
from helpers import dependency as dependency
from helpers import isPlayerAvatar as isPlayerAvatar
from messenger import MessengerEntry as MessengerEntry
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.bw_chat2.battle_chat_cmd import EPIC_GLOBAL_CMD_NAMES as EPIC_GLOBAL_CMD_NAMES, LOCATION_CMD_NAMES as LOCATION_CMD_NAMES, TARGET_CMD_NAMES as TARGET_CMD_NAMES
from skeletons.account_helpers.settings_core import IBattleCommunicationsSettings as IBattleCommunicationsSettings
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.game_control import ICommendationsController as ICommendationsController
from uilogging.player_satisfaction_rating.loggers import KeyboardShortcutLogger as KeyboardShortcutLogger
_logger: Any
CONTEXTCOMMAND = 'CONTEXTCOMMAND'
CONTEXTCOMMAND2 = 'CONTEXTCOMMAND2'
KB_MAPPING: dict
TARGET_TYPE_TRANSLATION_MAPPING: dict
DIRECT_ACTION_BATTLE_CHAT_COMMANDS: list
PROHIBITED_IF_DEAD: list
PROHIBITED_IF_SPECTATOR: list

class ChatCommandsController(IBattleController):
    __slots__: tuple
    sessionProvider: Any
    battleCommunications: Any
    commendationsCtrl: Any
    _aimOffset: Any
    __arenaDP: Any
    __feedback: Any
    __ammo: Any
    __markersManager: Any
    __isEnabled: Any
    _uiPlayerSatisfactionRatingLogger: Any
    def __init__(self, setup, feedback, ammo):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def getAimedAtTargetData(self):
        ...
    def getReplyStateForTargetIDAndMarkerType(self, targetID, targetMarkerType):
        ...
    def isTargetAllyCommittedToMe(self, targetID):
        ...
    def handleContexChatCommand(self, key):
        ...
    def sendAdvancedPositionPing(self, action, isInRadialMenu=False):
        ...
    def sendReplyChatCommand(self, targetID, action):
        ...
    def sendCancelReplyChatCommand(self, targetID, action):
        ...
    def sendClearChatCommandsFromTarget(self, targetID, targetMarkerType):
        ...
    def handleChatCommand(self, action, targetID=None, isInRadialMenu=False):
        ...
    def sendAttentionToPosition3D(self, position, name):
        ...
    def sendAttentionToObjective(self, hqIdx, isAtk, action=None):
        ...
    def sendCommandToBase(self, baseIdx, cmdName, baseName=''):
        ...
    def sendCommand(self, cmdName):
        ...
    def sendEpicGlobalCommand(self, cmdName, baseName=''):
        ...
    def sendTargetedCommand(self, cmdName, targetID, isInRadialMenu=False):
        ...
    def sendReloadingCommand(self):
        ...
    def __isProhibitedToSendIfDeadOrObserver(self, name):
        ...
    def __isSPG(self):
        ...
    def __isSPGAndInStrategicOrArtyMode(self):
        ...
    def __getReloadTime(self):
        ...
    def __sendChatCommand(self, command):
        ...
    def __onBattleCommunicationChanged(self):
        ...
    def __getAimedAtVehicleOrObject(self):
        ...
    def __isTargetCorrect(self, player, target):
        ...
    def __onMarkersManagerMarkersCreated(self, event):
        ...

def getAimedAtPositionWithinBorders(aimOffsetX, aimOffsetY):
    ...
