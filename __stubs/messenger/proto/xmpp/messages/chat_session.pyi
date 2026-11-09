# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/messages/chat_session.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import operator as operator
import time as time
import BigWorld as BigWorld
from constants import BAN_REASON as BAN_REASON
from gui import SystemMessages as SystemMessages
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import utils as utils
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.m_constants import CLIENT_ACTION_ID as CLIENT_ACTION_ID, PROTO_TYPE as PROTO_TYPE, USER_TAG as USER_TAG, USER_ACTION_ID as USER_ACTION_ID
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.xmpp import errors as errors, entities as entities
from messenger.proto.xmpp import jid as jid_entity
from messenger.proto.xmpp.XmppCooldownManager import XmppCooldownManager as XmppCooldownManager
from messenger.proto.xmpp.extensions import chat as chat_ext
from messenger.proto.xmpp.gloox_constants import IQ_TYPE as IQ_TYPE, PRESENCE as PRESENCE, MESSAGE_TYPE as MESSAGE_TYPE
from messenger.proto.xmpp.gloox_wrapper import ClientHolder as ClientHolder
from messenger.proto.xmpp.messages.provider import ChatProvider as ChatProvider
from messenger.proto.xmpp.wrappers import ChatMessage as ChatMessage
from messenger.storage import ChannelsStorage as ChannelsStorage, MessengerStorageDescriptor as MessengerStorageDescriptor
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
_logger: Any

class _HISTORY_RQ_STATE(object):
    FREE = 0
    WAIT = 1
    RESULT = 2
    COOLDOWN = 3
    UNAVAILABLE = 4

class ChatSessionHistoryRequester(ClientHolder):
    channelsStorage: Any
    __cooldown: Any
    __limit: Any
    __iqID: Any
    __pool: Any
    __history: Any
    __callbackID: Any
    __state: Any
    __isSuspend: Any
    def __init__(self, limits):
        ...
    def release(self):
        ...
    def suspend(self):
        ...
    def clear(self):
        ...
    def request(self, jid):
        ...
    def cancel(self, jid):
        ...
    def handleIQ(self, iqID, iqType, tag):
        ...
    def addHistory(self, message):
        ...
    def __setChannelHistory(self, jid):
        ...
    def __doNextRequest(self):
        ...
    def __callback(self):
        ...

class ChatSessionsProvider(ChatProvider):
    __gameSession: Any
    __slots__: tuple
    __historyRQ: Any
    def __init__(self, limits):
        ...
    def clear(self):
        ...
    def release(self):
        ...
    def suspend(self):
        ...
    def startSession(self, jid, name):
        ...
    def stopSession(self, jid):
        ...
    def setUserAction(self, actionID, contact):
        ...
    def restore(self, jid, state):
        ...
    def setContactPresence(self, contact):
        ...
    def addMessage(self, jid, message):
        ...
    def requestHistory(self, jid):
        ...
    def handleIQ(self, iqID, iqType, pyGlooxTag):
        ...
    def _searchChannel(self, jid, name=''):
        ...
    def _repeatMessage(self, channel, body, filters):
        ...
    def __getPrivateMessagesForbiddenText(self):
        ...
    def __getNonFriendPrivateMessagesForbiddenText(self):
        ...
    def sendPrivateMessagesRestrictedNotification(self):
        ...
    def sendNonFriendMessagesRestrictedNotification(self):
        ...
    def __addSession(self, session, contactDBID=0, byAction=False):
        ...
    def __removeSession(self, session):
        ...
