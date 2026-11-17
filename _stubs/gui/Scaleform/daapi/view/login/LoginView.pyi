# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/login/LoginView.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
from collections import defaultdict as defaultdict
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from adisp import adisp_process as adisp_process
from connection_mgr import LOGIN_STATUS as LOGIN_STATUS
from frameworks.wulf import WindowFlags as WindowFlags, WindowStatus as WindowStatus
from gui import DialogsInterface as DialogsInterface, GUI_SETTINGS as GUI_SETTINGS
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.LoginPageMeta import LoginPageMeta as LoginPageMeta
from gui.Scaleform.daapi.view.servers_data_provider import ServersDataProvider as ServersDataProvider
from gui.Scaleform.framework.entities.View import View as View
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams
from gui.impl import backport as backport
from gui.impl.dialogs import dialogs as dialogs
from gui.impl.dialogs.builders import ResSimpleDialogBuilder as ResSimpleDialogBuilder
from gui.impl.dialogs.dialogs import showSimple as showSimple
from gui.impl.gen import R as R
from gui.Scaleform.daapi.view.login.login_modes import createLoginMode as createLoginMode
from gui.Scaleform.daapi.view.login.login_modes.base_mode import INVALID_FIELDS as INVALID_FIELDS
from gui.shared import events as events, g_eventBus as g_eventBus
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import OpenLinkEvent as OpenLinkEvent, LoginEventEx as LoginEventEx, ArgsEvent as ArgsEvent, LoginEvent as LoginEvent, LoadViewEvent as LoadViewEvent
from helpers import getFullClientVersion as getFullClientVersion, dependency as dependency, uniprof as uniprof
from helpers.i18n import makeString as _ms
from helpers.statistics import HANGAR_LOADING_STATE as HANGAR_LOADING_STATE
from helpers.time_utils import makeLocalServerTime as makeLocalServerTime
from predefined_hosts import AUTO_LOGIN_QUERY_URL as AUTO_LOGIN_QUERY_URL, AUTO_LOGIN_QUERY_ENABLED as AUTO_LOGIN_QUERY_ENABLED, g_preDefinedHosts as g_preDefinedHosts
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from skeletons.helpers.statistics import IStatisticsCollector as IStatisticsCollector
from wg_async import wg_async as wg_async, wg_await as wg_await
_STATUS_TO_INVALID_FIELDS_MAPPING: Any

class CustomLoginStatuses(CONST_CONTAINER):
    ANOTHER_PERIPHERY = 'another_periphery'
    CHECKOUT_ERROR = 'checkout_error'
    CENTER_RESTART = 'centerRestart'
    VERSION_MISMATCH = 'versionMismatch'
    ACCESS_FORBIDDEN_TO_PERIPHERY = 'accessForbiddenToPeriphery'

class LoginView(LoginPageMeta):
    loginManager: Any
    connectionMgr: Any
    sessionProvider: Any
    statsCollector: Any
    __gui: Any
    __isListInitialized: Any
    __loginRetryDialogShown: Any
    __loginQueueDialogShown: Any
    __capsLockState: Any
    __lang: Any
    __capsLockCallbackID: Any
    __customLoginStatus: Any
    _autoSearchVisited: Any
    _servers: Any
    _loginMode: Any
    _serversDP: Any
    def __init__(self, ctx=None):
        ...
    def onRegister(self, host):
        ...
    def onSetRememberPassword(self, remember):
        ...
    # decorador original: @wg_async
    def onLogin(self, userName, password, serverName, isSocialToken2Login):
        ...
    def _onLoggedOn(self, *args):
        ...
    def resetToken(self):
        ...
    def showLegal(self):
        ...
    def onRecovery(self):
        ...
    def onTextLinkClick(self, linkId):
        ...
    def isToken(self):
        ...
    def onEscape(self):
        ...
    def changeAccount(self):
        ...
    def startListenCsisUpdate(self, startListenCsis):
        ...
    def onLoginNameUpdated(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def _populate(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def _dispose(self):
        ...
    def update(self):
        ...
    def _clearLoginView(self, *args):
        ...
    def _onKickedWhileLogin(self, peripheryID):
        ...
    def _onHandleQueue(self, queueNumber):
        ...
    def _onLoginQueueClosed(self, event):
        ...
    def _onLoginQueueSwitched(self, event):
        ...
    def _onLoginRejected(self, loginStatus, responseData):
        ...
    def _dropLoginQueue(self, loginStatus):
        ...
    def __clearFields(self, invalidField):
        ...
    # decorador original: @adisp_process
    def __loginRejectedUpdateNeeded(self):
        ...
    def __loginRejectedBan(self, responseData):
        ...
    def __loginRejectedRateLimited(self):
        ...
    def __loginRejectedWithCustomState(self):
        ...
    def __showLoginRetryDialog(self, data):
        ...
    def __closeLoginRetryDialog(self, event=None):
        ...
    def __closeLoginQueueDialog(self):
        ...
    def __checkUserInputState(self):
        ...
    def __updateServersList(self, *args):
        ...
    def __closeOpenedDialogs(self):
        ...
    # decorador original: @wg_async
    def __showExitDialog(self):
        ...
    def __getServerText(self, key, serverName):
        ...
    def __clearPeripheryRouting(self):
        ...

def DialogPredicate(window):
    ...
