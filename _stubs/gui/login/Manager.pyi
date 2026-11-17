# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/login/Manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import pickle as pickle
import time as time
import typing as typing
import logging as logging
import BigWorld as BigWorld
import WGC as WGC
import Settings as Settings
import constants as constants
from account_helpers.settings_core.settings_constants import GAME as GAME
from connection_mgr import CONNECTION_METHOD as CONNECTION_METHOD
from .Preferences import Preferences as Preferences
from .Servers import Servers as Servers, DevelopmentServers as DevelopmentServers
from debug_utils import LOG_DEBUG as LOG_DEBUG
from gui import SystemMessages as SystemMessages, makeHtmlString as makeHtmlString, GUI_SETTINGS as GUI_SETTINGS
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.locale.SYSTEM_MESSAGES import SYSTEM_MESSAGES as SYSTEM_MESSAGES
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from helpers.time_utils import ONE_MINUTE as ONE_MINUTE
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts, AUTO_LOGIN_QUERY_ENABLED as AUTO_LOGIN_QUERY_ENABLED, AUTO_LOGIN_QUERY_URL as AUTO_LOGIN_QUERY_URL
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from soft_exception import SoftException as SoftException
from gui.Scaleform.Waiting import Waiting as Waiting
from Event import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from connection_mgr import LOGIN_STATUS as LOGIN_STATUS
_PERIPHERY_DEFAULT_LIFETIME: Any
_LIMIT_LOGIN_COUNT = 5
_logger: Any

class Manager(ILoginManager):
    lobbyContext: Any
    connectionMgr: Any
    settingsCore: Any
    _preferences: Any
    __servers: Any
    __wgcPublication: Any
    __wgcManager: Any
    __triedToInitWGC: Any
    onConnectionInitiated: Any
    onConnectionRejected: Any
    def __init__(self):
        ...
    @property
    def wgcAvailable(self):
        ...
    def getWgcPublication(self):
        ...
    @property
    def isWgcSteam(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def initiateLogin(self, email, password, serverName, isSocialToken2Login, rememberUser):
        ...
    def initiateRelogin(self, login, token2, serverName):
        ...
    def getPreference(self, key):
        ...
    def clearPreferences(self):
        ...
    def clearToken2Preference(self):
        ...
    def writePreferences(self):
        ...
    @property
    def servers(self):
        ...
    def _onLoggedOn(self, responseData):
        ...
    def _onWGCInitiated(self, *_):
        ...
    def _onRejected(self, *_):
        ...
    def _showSecurityMessage(self, responseData):
        ...
    def writePeripheryLifetime(self):
        ...
    @staticmethod
    def getAvailableSocialNetworks():
        ...
    def initiateSocialLogin(self, socialNetworkName, serverName, rememberUser, isRegistration):
        ...
    def _getHost(self, authMethod, hostName):
        ...
    def __dumpUserName(self, name):
        ...
    def addOnWgcErrorListener(self, listener):
        ...
    def removeOnWgcErrorListener(self, listener):
        ...
    def tryWgcLogin(self, serverName=None):
        ...
    def stopWgc(self):
        ...
    def tryPrepareWGCLogin(self):
        ...
    def checkWgcCouldRetry(self, status):
        ...
    def __onServerSettingsChanged(self, diff):
        ...

class _WgcModeManager(object):
    connectionMgr: Any
    __lobbyContext: Any
    onWgcError: Any
    __token2ToStore: Any
    __selectedServer: Any
    onInitiated: Any
    onRejected: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def login(self, selectedServer):
        ...
    def relogin(self, token2, selectedServer):
        ...
    def checkWgcCouldRetry(self, status):
        ...
    def onLoggedOn(self, responseData):
        ...
    def __wgcCheck(self):
        ...
    def __wgcConnect(self):
        ...
    def __onRejected(self, status, _):
        ...
    def __onDisconnected(self):
        ...
    def __onAccountDone(self, *args):
        ...
