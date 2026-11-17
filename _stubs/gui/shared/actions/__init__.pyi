# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/actions/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import game_loading_bindings as game_loading_bindings
from adisp import adisp_process as adisp_process
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.prb_control.settings import FUNCTIONAL_FLAG as FUNCTIONAL_FLAG
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.actions.chains import ActionsChain as ActionsChain
from gui.shared.events import LoginEvent as LoginEvent, LoginEventEx as LoginEventEx, GUICommonEvent as GUICommonEvent
from gui.winback.winback_helpers import leaveWinbackMode as leaveWinbackMode
from helpers import dependency as dependency
from predefined_hosts import g_preDefinedHosts as g_preDefinedHosts, getHostURL as getHostURL
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gameplay import IGameplayLogic as IGameplayLogic
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from constants import WINBACK_BATTLE_TOKEN_DRAW_REASON as WINBACK_BATTLE_TOKEN_DRAW_REASON
__all__: tuple
DISCONNECT_FROM_PERIPHERY_DELAY = 0.3
CONNECT_TO_PERIPHERY_DELAY = 2.0

class Action(object):
    _completed: Any
    _running: Any
    def __init__(self):
        ...
    def invoke(self):
        ...
    def isInstantaneous(self):
        ...
    def isRunning(self):
        ...
    def isCompleted(self):
        ...

class LeavePrbModalEntity(Action):
    _running: Any
    _completed: Any
    def __init__(self):
        ...
    def invoke(self):
        ...
    def isInstantaneous(self):
        ...
    # decorador original: @adisp_process
    def __doLeave(self, dispatcher, ctx):
        ...

class LeavePrbEntity(Action):
    _running: Any
    _completed: Any
    def __init__(self):
        ...
    def invoke(self):
        ...
    def isInstantaneous(self):
        ...
    # decorador original: @adisp_process
    def __doLeave(self, dispatcher, ctx):
        ...

class SelectPrb(Action):
    _running: Any
    _prbAction: Any
    _completed: Any
    def __init__(self, prbAction):
        ...
    def invoke(self):
        ...
    def isInstantaneous(self):
        ...
    # decorador original: @adisp_process
    def __doSelect(self, dispatcher):
        ...

class DisconnectFromPeriphery(Action):
    connectionMgr: Any
    loginManager: Any
    gameplay: Any
    appLoader: Any
    __peripheryId: Any
    __endTime: Any
    _running: Any
    _completed: Any
    def __init__(self, loginViewPreselectedPeriphery=None):
        ...
    def isInstantaneous(self):
        ...
    def invoke(self):
        ...
    def isRunning(self):
        ...

class ConnectToPeriphery(Action):
    loginManager: Any
    lobbyContext: Any
    connectionMgr: Any
    __host: Any
    __endTime: Any
    __credentials: Any
    _completed: Any
    _running: Any
    def __init__(self, peripheryID):
        ...
    def isInstantaneous(self):
        ...
    def isRunning(self):
        ...
    def invoke(self):
        ...
    def __doConnect(self):
        ...
    def __addHandlers(self):
        ...
    def __removeHandlers(self):
        ...
    def __onConnected(self):
        ...
    def __onRejected(self, status, responseData):
        ...
    def __onLoginQueueClosed(self, _):
        ...
    def __connectionFailed(self):
        ...

class PrbInvitesInit(Action):
    _completed: Any
    _running: Any
    def isInstantaneous(self):
        ...
    def invoke(self):
        ...
    def __onInvitesListInited(self):
        ...

class WaitFlagActivation(Action):
    _isActive: Any
    _running: Any
    _completed: Any
    def __init__(self):
        ...
    def activate(self):
        ...
    def inactivate(self):
        ...
    def invoke(self):
        ...
    def isRunning(self):
        ...
    def isInstantaneous(self):
        ...

class OnLobbyInitedAction(Action):
    __isLobbyInited: Any
    __onInited: Any
    _running: Any
    _completed: Any
    def __init__(self, onInited=None):
        ...
    def invoke(self):
        ...
    def __onLobbyInited(self, _):
        ...

class LeaveWinbackModeEntity(Action):
    _running: Any
    _completed: Any
    def __init__(self):
        ...
    def invoke(self):
        ...
    def isInstantaneous(self):
        ...
    def __doLeave(self):
        ...
