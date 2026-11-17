# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from functools import partial as partial
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process, adisp_async as adisp_async
from client_request_lib.exceptions import ResponseCodes as ResponseCodes
from constants import AUTH_TOKEN_REQUEST_TIMEOUT as AUTH_TOKEN_REQUEST_TIMEOUT
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_DEBUG as LOG_DEBUG
from gui.clans.restrictions import AccountClanLimits as AccountClanLimits, DefaultAccountClanLimits as DefaultAccountClanLimits
from gui.clans.settings import LOGIN_STATE as LOGIN_STATE
from gui.shared.utils import getPlayerDatabaseID as getPlayerDatabaseID, backoff as backoff
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.wgcg.base.contexts import LogInCtx as LogInCtx, LogOutCtx as LogOutCtx, PingCtx as PingCtx
from gui.wgcg.factory import g_webFactory as g_webFactory
from gui.wgcg.requests import WgcgRequestResponse as WgcgRequestResponse
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from helpers import dependency as dependency
from helpers import getClientLanguage as getClientLanguage
from helpers import time_utils as time_utils
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_PING_BACK_OFF_MIN_DELAY = 60
_PING_BACK_OFF_MAX_DELAY = 1200
_PING_BACK_OFF_MODIFIER = 30
_PING_BACK_OFF_EXP_RANDOM_FACTOR = 5
AccessTokenData: Any
_RELOGIN_CODES: tuple

class WebControllerStates(CONST_CONTAINER):
    STATE_NOT_DEFINED = 0
    STATE_AVAILABLE = 1
    STATE_UNAVAILABLE = 2
    STATE_ROAMING = 3
    STATE_DISABLED = 4

# decorador original: @ReprInjector.simple(...)
class _State(object):
    lobbyContext: Any
    connectionMgr: Any
    __stateID: Any
    _webCtrl: Any
    def __init__(self, webCtrl, stateID):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def invalidate(self):
        ...
    def getStateID(self):
        ...
    def getLimits(self, profile):
        ...
    def isAvailable(self):
        ...
    def isLoggedOn(self):
        ...
    def getWebRequester(self):
        ...
    def compare(self, state):
        ...
    def update(self):
        ...
    # decorador original: @adisp_async
    def sendRequest(self, ctx, callback, allowDelay=None):
        ...
    def login(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def loginAsync(self, callback):
        ...
    def logout(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getAccessTokenData(self, force=False, callback=None):
        ...
    def _changeState(self, state):
        ...
    def _getNextState(self):
        ...
    def _makeErrorResponse(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class UndefinedState(_State):
    def __init__(self, webCtrl):
        ...
    def _getNextState(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class RoamingState(_State):
    def __init__(self, webCtrl):
        ...
    def _getNextState(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class DisabledState(_State):
    def __init__(self, webCtrl):
        ...
    def _getNextState(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class _WebState(_State):
    __requestsCtrl: Any
    __webRequester: Any
    __gateUrl: Any
    def __init__(self, webCtrl, stateID):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def getGateUrl(self):
        ...
    def compare(self, state):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def sendRequest(self, ctx, callback, allowDelay=None):
        ...
    # decorador original: @adisp_async
    def _sendRequest(self, ctx, callback, allowDelay=None):
        ...
    def getWebRequester(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class UnavailableState(_WebState):
    __bwCbId: Any
    __ctx: Any
    __isPingRunning: Any
    __backOff: Any
    def __init__(self, webCtrl):
        ...
    def fini(self):
        ...
    def invalidate(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _sendRequest(self, ctx, callback, allowDelay=True):
        ...
    # decorador original: @adisp_process
    def _ping(self):
        ...
    def _schedulePingCB(self):
        ...
    def _cancelPingCB(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class AvailableState(_WebState):
    __loginState: Any
    _tokenRequester: Any
    __waitingRequests: Any
    __clanSync: Any
    __accessTokenData: Any
    __accessTokenCallbacks: Any
    def __init__(self, webCtrl):
        ...
    def init(self):
        ...
    def isAvailable(self):
        ...
    def isLoggedOn(self):
        ...
    def getLimits(self, profile):
        ...
    def clanSync(self, ctx):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def _sendRequest(self, ctx, callback, allowDelay=True):
        ...
    # decorador original: @adisp_process
    def login(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def loginAsync(self, callback):
        ...
    # decorador original: @adisp_process
    def logout(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def getAccessTokenData(self, force=False, callback=None):
        ...
    def _getNextState(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __doLogin(self, callback):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def __doLogOut(self, callback):
        ...
    # decorador original: @adisp_process
    def __processWaitingRequests(self):
        ...
