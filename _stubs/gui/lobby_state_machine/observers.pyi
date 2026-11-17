# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lobby_state_machine/observers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from functools import partial as partial
import typing as typing
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver, State as State
from frameworks_common.state_machine.visitor import isDescendantOf as isDescendantOf
from frameworks.wulf import WindowStatus as WindowStatus
from gui.lobby_state_machine.events import _BackNavigationGeneratedNavigationEvent as _BackNavigationGeneratedNavigationEvent
from gui.lobby_state_machine.recorded_states import _RecordedStates as _RecordedStates
from gui.lobby_state_machine.states import SubScopeSubLayerState as SubScopeSubLayerState, SubScopeTopLayerState as SubScopeTopLayerState, _SubScopeTopLayerEmptyState as _SubScopeTopLayerEmptyState, _TopScopeTopLayerEmptyState as _TopScopeTopLayerEmptyState, LobbyState as LobbyState, UntrackedState as UntrackedState, compareViewKeys as compareViewKeys
from gui.shared.events import NavigationEvent as NavigationEvent
from gui.shared.utils.callable_delayer import CallableDelayer as CallableDelayer, delayUntilParentWindowReady as delayUntilParentWindowReady
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine, VisibleRouteInfo as VisibleRouteInfo
_logger: Any

class _StateClosingObserver(BaseStateObserver):
    __lsmRef: Any
    def __init__(self, lsm):
        ...
    def clear(self):
        ...
    def isObservingState(self, state):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...

class _ViewKillingObserver(BaseStateObserver):
    __lsmRef: Any
    __recordedStates: Any
    __viewKeysToKill: Any
    __subTopsToKill: Any
    __callableDelayer: Any
    def __init__(self, lsm, recordedStates):
        ...
    def isObservingState(self, state):
        ...
    def clear(self):
        ...
    def onExitState(self, state, event):
        ...
    def destroyViewsOfExitedStates(self):
        ...
    def __visibleRouteChanged(self, routeInfo):
        ...
    def __windowsWithViewKeys(self, viewKeys):
        ...
