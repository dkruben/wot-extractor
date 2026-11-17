# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/app_loader/spaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from adisp import adisp_process as adisp_process
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, ACCOUNT_KICK_REASONS as ACCOUNT_KICK_REASONS
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.app_loader.settings import APP_NAME_SPACE as APP_NAME_SPACE
from gui.game_loading import loading as gameLoading
from gui.game_loading.state_machine.const import GameLoadingStates as GameLoadingStates
from gui.impl.gen import R as R
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import LobbySimpleEvent as LobbySimpleEvent, LoginEvent as LoginEvent, ViewEventType as ViewEventType, CloseWindowEvent as CloseWindowEvent
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from helpers import dependency as dependency, isPlayerAvatar as isPlayerAvatar
from skeletons.connection_mgr import DisconnectReason as DisconnectReason, IConnectionManager as IConnectionManager
from skeletons.gameplay import IGameplayLogic as IGameplayLogic
from skeletons.gui.app_loader import IGlobalSpace as IGlobalSpace, GuiGlobalSpaceID as _SPACE_ID, ApplicationStateID as ApplicationStateID
from skeletons.gui.game_control import IReloginController as IReloginController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.login_manager import ILoginManager as ILoginManager
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
_REASON = DisconnectReason

class ShowDialogAction(object):
    __slots__: tuple
    def getAppNS(self):
        ...
    def doAction(self):
        ...

class DisconnectDialogAction(ShowDialogAction):
    __slots__: tuple
    __reason: Any
    __kickReasonType: Any
    __expiryTime: Any
    def __init__(self, reason, kickReasonType=..., expiryTime=None):
        ...
    def doAction(self):
        ...

class ReplayVersionDiffersDialogAction(ShowDialogAction):
    __slots__: tuple
    # decorador original: @adisp_process
    def doAction(self):
        ...

class ReplayFinishDialogAction(ShowDialogAction):
    def getAppNS(self):
        ...
    # decorador original: @adisp_process
    def doAction(self):
        ...

class CloseGameLoadingMixin(object):
    __callbackID: Any
    def __init__(self, *args, **kwargs):
        ...
    def init(self, *args, **kwargs):
        ...
    def fini(self, *args, **kwargs):
        ...
    def _closeGameLoading(self):
        ...
    def _unsubscribe(self):
        ...
    def __cancelCallback(self):
        ...
    def __waitingHiddenHandler(self, _):
        ...
    def __delayedWaitingHiddenHandler(self):
        ...

# decorador original: @ReprInjector.simple(...)
class LoginSpace(IGlobalSpace):
    __slots__: tuple
    hangarSpace: Any
    connectionMgr: Any
    loginManager: Any
    reloginCtrl: Any
    _action: Any
    _isPlayerLoadingActive: Any
    def __init__(self, action=None):
        ...
    def getSpaceID(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    @property
    def __isReconnectActive(self):
        ...
    def setup(self, action=None):
        ...
    def update(self):
        ...
    def showGUI(self, appFactory, appNS, appState):
        ...
    def updateGUI(self, appFactory, appNS):
        ...
    def hideGUI(self, appFactory, newState):
        ...
    def _doActionIfNeed(self, appNS):
        ...
    def _onDisconnected(self, *_):
        ...
    def _onLoginFailed(self, *_):
        ...
    def _onTryToLogin(self, *_):
        ...
    def _onEULAClosed(self, event):
        ...
    def _loginViewReadyHandler(self, *_):
        ...
    def _loadViewHandler(self, event):
        ...
    @classmethod
    def _clearEntitiesAndSpaces(cls):
        ...

# decorador original: @ReprInjector.simple(...)
class WaitingSpace(IGlobalSpace):
    __slots__: tuple
    def getSpaceID(self):
        ...

# decorador original: @ReprInjector.simple(...)
class LobbySpace(CloseGameLoadingMixin, IGlobalSpace):
    __slots__: tuple
    gameplay: Any
    def init(self, *args, **kwargs):
        ...
    def fini(self, *args, **kwargs):
        ...
    def getSpaceID(self):
        ...
    def showGUI(self, appFactory, appNS, appState):
        ...
    def hideGUI(self, appFactory, newState):
        ...
    @staticmethod
    def _disconnectStartHandler(*_):
        ...

class _ArenaSpace(IGlobalSpace):
    __slots__: tuple
    _arenaGuiType: Any
    def __init__(self, arenaGuiType=...):
        ...

# decorador original: @ReprInjector.simple(...)
class BattleLoadingSpace(CloseGameLoadingMixin, _ArenaSpace):
    __slots__: tuple
    def __init__(self, arenaGuiType=...):
        ...
    def getSpaceID(self):
        ...
    def hideGUI(self, appFactory, newState):
        ...
    def showGUI(self, appFactory, appNS, appState):
        ...
    def updateGUI(self, appFactory, appNS):
        ...
    def _closeGameLoading(self):
        ...

# decorador original: @ReprInjector.simple(...)
class ReplayLoadingSpace(BattleLoadingSpace):
    __slots__: tuple
    def showGUI(self, appFactory, appNS, appState):
        ...
    def hideGUI(self, appFactory, newState):
        ...

# decorador original: @ReprInjector.simple(...)
class BattleSpace(_ArenaSpace):
    __slots__: tuple
    def getSpaceID(self):
        ...
    def showGUI(self, appFactory, appNS, appState):
        ...

# decorador original: @ReprInjector.simple(...)
class ReplayBattleSpace(BattleSpace):
    __slots__: tuple
    def hideGUI(self, appFactory, newState):
        ...

def _disableTimeWarpInReplay():
    ...
def _acceptVersionDiffering():
    ...
def _stopBattleReplay():
    ...
def _onReplayBattleLoadingFinished():
    ...
