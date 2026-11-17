# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/connection_mgr.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import hashlib as hashlib
import json as json
import ResMgr as ResMgr
import BigWorld as BigWorld
import constants as constants
import pwd_token as pwd_token
from Event import Event as Event, SafeEvent as SafeEvent, EventManager as EventManager
from PlayerEvents import g_playerEvents as g_playerEvents
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_NOTE as LOG_NOTE, LOG_WARNING as LOG_WARNING
from shared_utils import nextTick as nextTick
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts, AUTO_LOGIN_QUERY_URL as AUTO_LOGIN_QUERY_URL
from helpers import getClientLanguage as getClientLanguage, uniprof as uniprof
from account_shared import isValidClientVersion as isValidClientVersion
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
_MIN_RECONNECTION_TIMEOUT = 5
_RECONNECTION_TIMEOUT_INCREMENT = 5
_MAX_RECONNECTION_TIMEOUT = 20
INVALID_TOKEN2_EXPIRED: tuple

class CONNECTION_METHOD(object):
    BASIC = 'basic'
    TOKEN = 'token'
    TOKEN2 = 'token2'

class LOGIN_STATUS(object):
    NOT_SET = 'NOT_SET'
    LOGGED_ON = 'LOGGED_ON'
    LOGGED_ON_OFFLINE = 'LOGGED_ON_OFFLINE'
    CONNECTION_FAILED = 'CONNECTION_FAILED'
    DNS_LOOKUP_FAILED = 'DNS_LOOKUP_FAILED'
    UNKNOWN_ERROR = 'UNKNOWN_ERROR'
    CANCELLED = 'CANCELLED'
    ALREADY_ONLINE_LOCALLY = 'ALREADY_ONLINE_LOCALLY'
    LOGIN_REJECTED_BAN = 'LOGIN_REJECTED_BAN'
    LOGIN_REJECTED_NO_SUCH_USER = 'LOGIN_REJECTED_NO_SUCH_USER'
    LOGIN_REJECTED_INVALID_PASSWORD = 'LOGIN_REJECTED_INVALID_PASSWORD'
    SESSION_END = 'SESSION_END'
    LOGIN_REJECTED_ALREADY_LOGGED_IN = 'LOGIN_REJECTED_ALREADY_LOGGED_IN'
    LOGIN_REJECTED_BAD_DIGEST = 'LOGIN_REJECTED_BAD_DIGEST'
    LOGIN_REJECTED_DB_GENERAL_FAILURE = 'LOGIN_REJECTED_DB_GENERAL_FAILURE'
    LOGIN_REJECTED_DB_NOT_READY = 'LOGIN_REJECTED_DB_NOT_READY'
    LOGIN_REJECTED_ILLEGAL_CHARACTERS = 'LOGIN_REJECTED_ILLEGAL_CHARACTERS'
    LOGIN_CUSTOM_DEFINED_ERROR = 'LOGIN_CUSTOM_DEFINED_ERROR'
    LOGIN_BAD_PROTOCOL_VERSION = 'LOGIN_BAD_PROTOCOL_VERSION'
    LOGIN_REJECTED_SERVER_NOT_READY = 'LOGIN_REJECTED_SERVER_NOT_READY'
    LOGIN_REJECTED_RATE_LIMITED = 'LOGIN_REJECTED_RATE_LIMITED'

class ConnectionData(object):
    username: Any
    password: Any
    inactivityTimeout: Any
    publicKeyPath: Any
    clientContext: Any
    peripheryRoutingGroup: Any
    def __init__(self):
        ...

class ConnectionManager(IConnectionManager):
    __connectionData: Any
    __connectionUrl: Any
    __connectionMethod: Any
    __connectionStatus: Any
    __lastLoginName: Any
    __hostItem: Any
    __availableHosts: Any
    __lastSessionID: Any
    __retryConnectionPeriod: Any
    __retryConnectionCallbackID: Any
    __connectionInProgress: Any
    __eManager: Any
    onLoggedOn: Any
    onConnected: Any
    onRejected: Any
    onDisconnected: Any
    onKickedFromServer: Any
    onKickWhileLoginReceived: Any
    onQueued: Any
    onPeripheryRoutingGroupUpdated: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    def initiateConnection(self, params, password, serverName):
        ...
    def stopRetryConnection(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def __connect(self):
        ...
    def __tryConnect(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def __serverResponseHandler(self, stage, status, responseDataJSON):
        ...
    def __setConnectionData(self, params, password):
        ...
    def __swtichToToken2(self, token2):
        ...
    def __setHostData(self, predefinedHost):
        ...
    def __setHostDataAndConnect(self, predefinedHost):
        ...
    def __reconnect(self):
        ...
    def __getRetryConnectionPeriod(self):
        ...
    def __processKick(self, peripheryID):
        ...
    def __processQueue(self, queueNumber):
        ...
    @property
    def serverUserName(self):
        ...
    @property
    def serverUserNameShort(self):
        ...
    @property
    def peripheryID(self):
        ...
    @property
    def areaID(self):
        ...
    @property
    def url(self):
        ...
    @property
    def loginName(self):
        ...
    @property
    def lastLoginName(self):
        ...
    @property
    def lastSessionID(self):
        ...
    @property
    def databaseID(self):
        ...
    @property
    def connectionMethod(self):
        ...
    @property
    def peripheryRoutingGroup(self):
        ...
    @property
    def availableHosts(self):
        ...
    def isAvailablePeriphery(self, peripheryID=None):
        ...
    def disconnect(self):
        ...
    def setKickedFromServer(self, reason, kickReasonType, expiryTime):
        ...
    def isDisconnected(self):
        ...
    def isStandalone(self):
        ...
    def isConnected(self):
        ...
    def checkClientServerVersions(self, clientVersion, serverVersion):
        ...
    def setLastLogin(self, email):
        ...
    def setPeripheryRoutingGroup(self, routingGroup, availableHosts):
        ...
