# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from chat_shared import CHAT_RESPONSES as CHAT_RESPONSES
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG
from messenger import g_settings as g_settings
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto.bw import errors as errors
from messenger.proto.bw.ChannelsManager import ChannelsManager as ChannelsManager
from messenger.proto.bw.ChatActionsListener import ChatActionsListener as ChatActionsListener
from messenger.proto.bw.ClanListener import ClanListener as ClanListener
from messenger.proto.bw.ServiceChannelManager import ServiceChannelManager as ServiceChannelManager
from messenger.proto.bw.UsersManager import UsersManager as UsersManager
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.interfaces import IProtoPlugin as IProtoPlugin

class BWProtoPlugin(ChatActionsListener, IProtoPlugin):
    __slots__: tuple
    __errorsHandlers: dict
    __defaultErrorHandler = '_BWProtoPlugin__onActionFailure'
    __isConnected: Any
    channels: Any
    users: Any
    clanListener: Any
    serviceChannel: Any
    def __init__(self):
        ...
    def isConnected(self):
        ...
    def clear(self):
        ...
    def connect(self, scope):
        ...
    def disconnect(self):
        ...
    def view(self, scope):
        ...
    def setFilters(self, msgFilterChain):
        ...
    def onChatActionFailure(self, chatAction):
        ...
    def _addChatActionsListeners(self):
        ...
    def _removeChatActionsListeners(self):
        ...
    @classmethod
    def __getClanListener(cls):
        ...
    def __onMemberBanned(self, chatAction):
        ...
    def __onChatBanned(self, chatAction):
        ...
    def __onCommandInCooldown(self, chatAction):
        ...
    def __onActionFailure(self, chatAction):
        ...
    def __passError(self, chatAction):
        ...
