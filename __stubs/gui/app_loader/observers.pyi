# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/app_loader/observers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from functools import partial as partial
import typing as typing
import BattleReplay as BattleReplay
import BigWorld as BigWorld
from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS as ARENA_BONUS_TYPE_CAPS
from constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE, ACCOUNT_KICK_REASONS as ACCOUNT_KICK_REASONS, ARENA_PERIOD as ARENA_PERIOD
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver
from frameworks_common.state_machine import StateEvent as StateEvent
from frameworks_common.state_machine import StateObserversContainer as StateObserversContainer
from frameworks_common.state_machine.observers import StateIdsObserver as StateIdsObserver
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework.managers.containers import POP_UP_CRITERIA as POP_UP_CRITERIA
from gui.app_loader import spaces as spaces
from helpers import dependency as dependency
from skeletons.connection_mgr import DisconnectReason as DisconnectReason
from skeletons.gameplay import GameplayStateID as GameplayStateID, IGameplayLogic as IGameplayLogic, PlayerEventID as PlayerEventID
from skeletons.gui.app_loader import GuiGlobalSpaceID as GuiGlobalSpaceID
from frameworks_common.state_machine import State as State
_BATTLE_OBSERVER_OVERRIDE_HANDLERS: Any

class PredicativeSingleStateObserver(StateIdsObserver):
    __slots__: tuple
    _predicates: Any
    def __init__(self, stateID):
        ...
    def addPredicate(self, predicate):
        ...
    def removePredicate(self, predicate):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...
    def _allPredicatesMatch(self):
        ...

class AppLoaderObserver(PredicativeSingleStateObserver):
    __slots__: tuple
    _proxy: Any
    def __init__(self, stateID, proxy):
        ...
    def clear(self):
        ...

class BattleStateResetObserver(AppLoaderObserver):
    def getStateIDs(self):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...
    def resetBattleState(self):
        ...

class WaitingObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class CreateLobbyObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class LoginObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class LobbyObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class SwitchToBattleObserver(BattleStateResetObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...
    def _destroyLobby(self):
        ...
    def _createBattle(self, arenaGuiType):
        ...

class BattleLoadingObserver(BattleStateResetObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class BattlePageObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...
    def onExitState(self, state, event):
        ...

class SwitchToLobbyObserver(AppLoaderObserver):
    __slots__: tuple
    _triggerID: Any
    _doCreate: Any
    def __init__(self, stateID, triggerID, proxy):
        ...
    def getStateIDs(self):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...
    def _createLobby(self):
        ...

class ReplayEnteringOnlineObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class ReplayExitingOnlineObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class ReplayVersionDiffersObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class ReplayCreateBattleObserver(SwitchToBattleObserver):
    __slots__: tuple
    __isInvoked: Any
    def __init__(self, stateID, proxy):
        ...
    def resetBattleState(self):
        ...
    def onEnterState(self, state, event):
        ...

class ReplayBattleLoadingObserver(BattleLoadingObserver):
    __slots__: tuple
    __toggleID: Any
    __isToggled: Any
    def __init__(self, stateID, toggleID, proxy):
        ...
    def getStateIDs(self):
        ...
    def resetBattleState(self):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...
    def onEnterState(self, state, event):
        ...

class ReplayBattlePageObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class ReplayFinishObserver(PredicativeSingleStateObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class ReplayRewindObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class PrebattleLoadingObserver(AppLoaderObserver):
    __slots__: tuple
    def onEnterState(self, state, event):
        ...

class NormalAppTracker(StateObserversContainer):
    __slots__: tuple
    def __init__(self, proxy):
        ...

class ReplayAppTracker(StateObserversContainer):
    __slots__: tuple
    def __init__(self, proxy):
        ...

class GameplayStatesObserver(BaseStateObserver):
    gameplay: Any
    __slots__: tuple
    __proxy: Any
    __tracker: Any
    def __init__(self, appLoader):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def getStateIDs(self):
        ...
    def isObservingState(self, state):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...
    def __clearTracker(self):
        ...

def registerBattleObserverOverrideHandler(handler):
    ...
def extendBattleObserverList(battle, proxy):
    ...
def makePredicatedObservers(predicate, *observers):
    ...
