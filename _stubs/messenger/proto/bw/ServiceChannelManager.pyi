# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw/ServiceChannelManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import deque as deque
import BigWorld as BigWorld
from chat_shared import CHAT_ACTIONS as CHAT_ACTIONS
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_WARNING as LOG_WARNING
from gui.impl.lobby.gf_notifications.cache import getCache as getCache
from gui.shared.system_factory import collectMessengerClientFormatter as collectMessengerClientFormatter, collectMessengerServerFormatter as collectMessengerServerFormatter
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from messenger.m_constants import MESSENGER_SCOPE as MESSENGER_SCOPE, SCH_MSGS_MAX_LENGTH as SCH_MSGS_MAX_LENGTH
from messenger.m_constants import SCH_CLIENT_MSG_TYPE as SCH_CLIENT_MSG_TYPE
from messenger.formatters.collections_by_type import initRegistrationFormatters as initRegistrationFormatters
from messenger.proto.bw.ChatActionsListener import ChatActionsListener as ChatActionsListener
from messenger.proto.bw.wrappers import ServiceChannelMessage as ServiceChannelMessage
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from adisp import adisp_process as adisp_process

class ServiceChannelManager(ChatActionsListener):
    __idGenerator: Any
    __messages: Any
    __unreadMessagesCount: Any
    def __init__(self):
        ...
    def addListeners(self):
        ...
    def clear(self):
        ...
    def switch(self, scope):
        ...
    def requestLastServiceMessages(self):
        ...
    def onReceiveSysMessage(self, chatAction):
        ...
    def onReceivePersonalSysMessage(self, chatAction):
        ...
    def pushClientSysMessage(self, message, msgType, isAlert=False, priority=None, messageData=None, savedData=None):
        ...
    def pushClientMessage(self, message, msgType, isAlert=False, auxData=None):
        ...
    def getReadMessages(self):
        ...
    def getMessage(self, clientID):
        ...
    def getUnreadCount(self):
        ...
    def resetUnreadCount(self):
        ...
    def handleUnreadMessages(self):
        ...
    def _handleUnreadMessage(self, isServerMsg, clientID, formatted, settings):
        ...
    # decorador original: @adisp_process
    def __addServerMessage(self, message):
        ...
    def __addClientMessage(self, message, msgType, isAlert=False, auxData=None):
        ...
