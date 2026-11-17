# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/connection.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
import BigWorld as BigWorld
from constants import TOKEN_TYPE as TOKEN_TYPE
from adisp import adisp_process as adisp_process
from gui.shared.utils import backoff as backoff, getPlayerDatabaseID as getPlayerDatabaseID
from gui.shared.utils.requesters import TokenRequester as TokenRequester, TokenResponse as TokenResponse
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.xmpp.gloox_constants import DISCONNECT_REASON as DISCONNECT_REASON, CONNECTION_IMPL_TYPE as CONNECTION_IMPL_TYPE, GLOOX_EVENT as GLOOX_EVENT
from messenger.proto.xmpp.gloox_wrapper import ClientEventsHandler as ClientEventsHandler
from messenger.proto.xmpp.log_output import CLIENT_LOG_AREA as CLIENT_LOG_AREA, g_logOutput as g_logOutput
from messenger.proto.xmpp.logger import sendEventToServer as sendEventToServer, XMPP_EVENT_LOG as XMPP_EVENT_LOG
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
_BACK_OFF_MIN_DELAY = 10
_BACK_OFF_MAX_DELAY = 5120
_BACK_OFF_MODIFIER = 10
_BACK_OFF_MOD_RANDOM_FACTOR = 2
_BACK_OFF_EXP_RANDOM_FACTOR = 1
_BACK_OFF_MIN_RANDOM = 20
_BACK_OFF_MAX_RANDOM = 30
_MAX_REQ_TOKEN_TRIES = 4
_NUMBER_OF_ITEMS_IN_SAMPLE = 2

class ConnectionsIterator(object):
    next: Any
    __tcp: Any
    __bosh: Any
    def __init__(self, base=None, alt=None, bosh=None):
        ...
    def __iter__(self):
        ...
    def clear(self):
        ...
    def hasNext(self):
        ...
    def __next__(self):
        ...

class ConnectionsInfo(object):
    __iterator: Any
    __backOff: Any
    __address: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def clear(self):
        ...
    def getPlayerFullJID(self):
        ...
    def getNextConnection(self):
        ...
    def getNextDelay(self):
        ...
    def getTries(self):
        ...
    def getLastAddress(self):
        ...

class ChatTokenResponse(TokenResponse):
    def getCredential(self):
        ...

class ConnectionHandler(ClientEventsHandler):
    connectionMgr: Any
    __tokenRequester: Any
    __reconnectCallbackID: Any
    __reqTokenCallbackID: Any
    __connectionsInfo: Any
    __reqTokenBackOff: Any
    def __init__(self):
        ...
    def connect(self):
        ...
    def disconnect(self):
        ...
    def clear(self):
        ...
    def isInGameServer(self):
        ...
    def registerHandlers(self):
        ...
    def unregisterHandlers(self):
        ...
    def __doConnect(self):
        ...
    def __doNextConnect(self):
        ...
    # decorador original: @adisp_process
    def __doLogin(self):
        ...
    def __doNextLogin(self):
        ...
    def __cancelReconnectCallback(self):
        ...
    def __cancelReqTokenCallback(self):
        ...
    def __invokeConnectFailedEvent(self, tries):
        ...
    def __handleConnect(self):
        ...
    def __handleLogin(self):
        ...
    def __handleDisconnect(self, reason, description):
        ...
    def __handleTokenError(self):
        ...

def _makeSample(*args):
    ...
