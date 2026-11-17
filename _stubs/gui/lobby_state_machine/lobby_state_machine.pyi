# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lobby_state_machine/lobby_state_machine.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import deque as deque
import typing as typing
from future.utils import itervalues as itervalues
from Event import Event as Event, EventManager as EventManager
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from debug_utils import deprecated as deprecated
from frameworks_common.state_machine import State as State, StateFlags as StateFlags, StateMachine as StateMachine
from frameworks_common.state_machine.exceptions import NodeError as NodeError, StateMachineError as StateMachineError, TransitionError as TransitionError
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from frameworks_common.state_machine.visitor import isDescendantOf as isDescendantOf
from frameworks.wulf import WindowLayer as WindowLayer
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.ScopeTemplates import SimpleScope as SimpleScope
from gui.Scaleform.framework.entities.wulf_adapter import WulfPackageLayoutAdapter as WulfPackageLayoutAdapter
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import NavigationEvent as NavigationEvent, BackNavigationEvent as BackNavigationEvent
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from shared_utils import first as first
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from .events import _NonViewClosingBackNavigationEvent as _NonViewClosingBackNavigationEvent, _StopEvent as _StopEvent, _BackNavigationGeneratedNavigationEvent as _BackNavigationGeneratedNavigationEvent, _BackNavigationEvent as _BackNavigationEvent
from .observers import _StateClosingObserver as _StateClosingObserver, _ViewKillingObserver as _ViewKillingObserver
from .recorded_states import _RecordedStates as _RecordedStates, buildSerializedParamsTopDown as buildSerializedParamsTopDown
from .states import LobbyState as LobbyState, EmptyState as EmptyState, UntrackedState as UntrackedState, _SubScopeState as _SubScopeState, SubScopeSubLayerState as SubScopeSubLayerState, _SubScopeSubLayerEmptyState as _SubScopeSubLayerEmptyState, _SubScopeSubLayerFinalState as _SubScopeSubLayerFinalState, SubScopeTopLayerState as SubScopeTopLayerState, _SubScopeTopLayerEmptyState as _SubScopeTopLayerEmptyState, _TopScopeState as _TopScopeState, TopScopeTopLayerState as TopScopeTopLayerState, _TopScopeTopLayerEmptyState as _TopScopeTopLayerEmptyState, LobbyStateDescription as LobbyStateDescription, compareViewKeys as compareViewKeys, getNavigationDescriptionSafe as getNavigationDescriptionSafe
from .transitions import NavigationTransition as NavigationTransition, GuardTransition as GuardTransition
from gui.Scaleform.framework.entities import View as View
from gui.impl.pub import ViewImpl as ViewImpl
_logger: Any

class VisibleRouteInfo(object):
    state: Any
    params: Any
    visualBackNavigationTarget: Any
    currentDescription: Any
    backDescription: Any
    def __init__(self, state=None, params=None, visualBackNavigationTarget=None, currentDescription=None, backDescription=None):
        ...

class LobbyStateMachine(StateMachine, EventsHandler):
    __eventManager: Any
    onVisibleRouteChanged: Any
    __visibleRouteInfo: Any
    __currentlyProcessedEvent: Any
    __navigationQueue: Any
    __viewAliasesToStates: Any
    __stateIDtoState: Any
    __scopeToLayerToStateMap: Any
    __stateConfigurators: Any
    __transitionConfigurators: Any
    __removableStateSelectors: Any
    __backNavigationDescription: Any
    __recordedStates: Any
    __viewKillingObserver: Any
    __stateClosingObserver: Any
    __subtreePriorities: Any
    def __init__(self):
        ...
    @property
    def backNavigationDescription(self):
        ...
    @property
    def visibleState(self):
        ...
    @property
    def visibleRouteInfo(self):
        ...
    def removeSubtreePrefix(self, stateID):
        ...
    # decorador original: @deprecated
    def getStateByViewKey(self, viewKey):
        ...
    def getStateByCls(self, cls):
        ...
    def getStateByID(self, stateID):
        ...
    def getUntrackedStateFor(self, scope, layer):
        ...
    def getEmptyStateInSubtreeOf(self, state):
        ...
    def getNonEmptyEnteredStates(self, predicate=None, onlyLeaves=True, withNavigationDescription=False):
        ...
    def getRelatedView(self, state):
        ...
    def getStateFromView(self, view):
        ...
    def findOwningSubtree(self, state):
        ...
    def addState(self, state):
        ...
    def addNavigationTransitionFromParent(self, state, transitionType=..., record=False):
        ...
    def addHistoryRemovableStateSelector(self, selector):
        ...
    def addStateConfigurator(self, fn):
        ...
    def addTransitionConfigurator(self, fn):
        ...
    def configure(self, *args, **kwargs):
        ...
    def start(self, doValidate=True):
        ...
    def stop(self):
        ...
    def post(self, event):
        ...
    def _getListeners(self):
        ...
    def _process(self, transitions, event):
        ...
    def __updateVisibleRoute(self):
        ...
    def __findRelevantTransition(self, transitions):
        ...
    def __findPreviousVisibleState(self, state):
        ...
    def __sortNavigationQueue(self):
        ...
    def __getBackNavigationTargetAndParams(self, currentVisibleState, peekOnly=True):
        ...

def _getInitialLeaf(state):
    ...
