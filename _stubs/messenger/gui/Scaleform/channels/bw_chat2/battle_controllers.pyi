# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/gui/Scaleform/channels/bw_chat2/battle_controllers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import BigWorld as BigWorld
from arena_component_system.sector_base_arena_component import ID_TO_BASENAME as ID_TO_BASENAME
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.locale.EPIC_BATTLE import EPIC_BATTLE as EPIC_BATTLE
from gui.battle_control.arena_info.arena_vos import EPIC_BATTLE_KEYS as EPIC_BATTLE_KEYS
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import MessengerEvent as MessengerEvent
from helpers import dependency as dependency
from helpers import i18n as i18n
from messenger.ext import isBattleChatEnabled as isBattleChatEnabled
from messenger.ext.player_helpers import isCurrentPlayer as isCurrentPlayer
from messenger.formatters import chat_message as chat_message
from messenger.formatters.users_messages import getBroadcastIsInCoolDownMessage as getBroadcastIsInCoolDownMessage
from messenger.gui.Scaleform.channels.layout import BattleLayout as BattleLayout
from messenger.m_constants import CLIENT_ERROR_ID as CLIENT_ERROR_ID
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, MESSENGER_COMMAND_TYPE as MESSENGER_COMMAND_TYPE
from messenger.proto import proto_getter as proto_getter
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.shared_errors import ClientError as ClientError
from messenger_common_chat2 import MESSENGER_LIMITS as MESSENGER_LIMITS
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from soft_exception import SoftException as SoftException
_EPIC_MINIMAP_ZOOM_MODE_SCALE = 500
_NONCAPTURED_BASES_FOR_LANE_DICT: dict

class _check_arena_in_waiting(object):
    sessionProvider: Any
    def __call__(self, func):
        ...

class _ChannelController(BattleLayout):
    sessionProvider: Any
    def __init__(self, channel, messageBuilder, isSecondaryChannelCtrl=False):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def getSettings(self):
        ...
    def filterMessage(self, cmd):
        ...
    def clear(self):
        ...
    def activate(self):
        ...
    def canSendMessage(self):
        ...
    def _formatMessage(self, message, doFormatting=True):
        ...
    def _formatCommand(self, command):
        ...

class TeamChannelController(_ChannelController):
    def __init__(self, channel):
        ...
    # decorador original: @_check_arena_in_waiting(...)
    def sendCommand(self, command):
        ...
    def filterMessage(self, cmd):
        ...
    # decorador original: @_check_arena_in_waiting(...)
    def _broadcast(self, message):
        ...
    def isEnabled(self):
        ...
    def _formatCommand(self, command):
        ...

class EpicTeamChannelController(TeamChannelController):
    def __getNameSuffix(self, avatarSessionID):
        ...
    def _formatMessage(self, message, doFormatting=True):
        ...
    def _formatCommand(self, command):
        ...

class CommonChannelController(_ChannelController):
    def __init__(self, channel):
        ...
    def isEnabled(self):
        ...
    # decorador original: @_check_arena_in_waiting(...)
    def _broadcast(self, message):
        ...

class SquadChannelController(_ChannelController):
    def __init__(self, channel):
        ...
    def isEnabled(self):
        ...
    def setView(self, view):
        ...
    def canSendMessage(self):
        ...
    def _broadcast(self, message):
        ...
