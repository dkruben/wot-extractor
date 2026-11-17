# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/xmpp_search_processors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_WARNING as LOG_WARNING
from messenger import g_settings as g_settings
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, CLIENT_ACTION_ID as CLIENT_ACTION_ID, CLIENT_ERROR_ID as CLIENT_ERROR_ID, USER_TAG as USER_TAG
from messenger.proto import proto_getter as proto_getter
from messenger.proto.search_processor import SearchProcessor as SearchProcessor
from messenger.proto.shared_errors import ClientActionError as ClientActionError, ChatCoolDownError as ChatCoolDownError
from messenger.proto.xmpp import xmpp_limits as limits
from messenger.proto.xmpp.entities import XMPPUserEntity as XMPPUserEntity
from messenger.proto.xmpp.errors import createServerActionIQError as createServerActionIQError, createServerIQError as createServerIQError
from messenger.proto.xmpp.gloox_constants import GLOOX_EVENT as GLOOX_EVENT, IQ_TYPE as IQ_TYPE
from messenger.proto.xmpp.xmpp_constants import CHANNEL_LIMIT as CHANNEL_LIMIT
from messenger.proto.xmpp.gloox_wrapper import ClientEventsHandler as ClientEventsHandler
from messenger.proto.xmpp.XmppCooldownManager import XmppCooldownManager as XmppCooldownManager
from messenger.proto.xmpp.extensions.search import ChannelSearchQuery as ChannelSearchQuery, ChannelsListHandler as ChannelsListHandler, NicknamePrefixSearchQuery as NicknamePrefixSearchQuery, NicknamePrefixSearchHandler as NicknamePrefixSearchHandler
from messenger.ext import checkAccountName as checkAccountName
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from soft_exception import SoftException as SoftException

class SearchChannelsProcessor(SearchProcessor, ClientEventsHandler):
    __sentRequestID: Any
    __service: Any
    _lastRequestID: Any
    def __init__(self, service):
        ...
    def __del__(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def find(self, token, **kwargs):
        ...
    def getSearchResultLimit(self):
        ...
    def unregisterHandlers(self):
        ...
    def registerHandlers(self):
        ...
    def getSearchCoolDown(self):
        ...
    def __onIQReceived(self, iqID, iqType, pyGlooxTag):
        ...

class SearchUserRoomsProcessor(SearchChannelsProcessor):
    def __init__(self):
        ...

class SearchUsersProcessor(SearchProcessor, ClientEventsHandler):
    usersStorage: Any
    __sentRequestID: Any
    __limits: Any
    __cooldown: Any
    _lastRequestID: Any
    def __init__(self):
        ...
    def __del__(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def find(self, token, **kwargs):
        ...
    def getSearchCoolDown(self):
        ...
    def getSearchResultLimit(self):
        ...
    def unregisterHandlers(self):
        ...
    def registerHandlers(self):
        ...
    def __onIQReceived(self, iqID, iqType, pyGlooxTag):
        ...
    def __OnSuccesResponse(self, pyGlooxTag):
        ...
    def __checkCooldown(self, actionID):
        ...
