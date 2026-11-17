# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lobby_state_machine/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import itertools as itertools
import logging as logging
import typing as typing
import weakref as weakref
from enum import IntEnum as IntEnum
from WeakMethod import WeakMethodProxy as WeakMethodProxy
from frameworks_common.state_machine import State as State, StateFlags as StateFlags
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from frameworks_common.state_machine.visitor import isDescendantOf as isDescendantOf, getLCA as getLCA
from frameworks.wulf import WindowStatus as WindowStatus
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.Scaleform.framework.ScopeTemplates import SimpleScope as SimpleScope
from gui.Scaleform.framework.entities.View import View as View
from gui.Scaleform.framework.entities.wulf_adapter import WulfPackageLayoutAdapter as WulfPackageLayoutAdapter
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams as SFViewLoadParams, GuiImplViewLoadParams as GuiImplViewLoadParams
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.lobby_state_machine.events import _NonViewClosingBackNavigationEvent as _NonViewClosingBackNavigationEvent, _BackNavigationEvent as _BackNavigationEvent
from gui.lobby_state_machine.transitions import GuardTransition as GuardTransition, NavigationTransition as NavigationTransition, _StopTransition as _StopTransition
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import NavigationEvent as NavigationEvent, LoadViewEvent as LoadViewEvent, LoadGuiImplViewEvent as LoadGuiImplViewEvent
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl.pub import ViewImpl as ViewImpl
_logger: Any
UNTRACKED_STATE_ID_ENDING = 'untracked'
EMPTY_STATE_ID_ENDING = 'empty'
SFViewLobbyState = ViewLobbyState

class LobbyStateFlags(StateFlags):
    HANGAR: Any
    POST_BATTLE_RESULTS: Any
    MAX = POST_BATTLE_RESULTS

class LobbyStateDescription(object):
    title: Any
    infos: Any
    label: Any
    tooltipHeader: Any
    tooltipBody: Any
    type: Any
    onMoreInfoRequested: Any
    class Info(object):
        label: Any
        tooltipHeader: Any
        tooltipBody: Any
        type: Any
        onMoreInfoRequested: Any
        class Type(IntEnum):
            INFO = 0
            QUESTION = 1
            VIDEO = 2
            DROP_LIST = 3
        def __init__(self, label='', tooltipHeader='', tooltipBody='', type=..., onMoreInfoRequested=...):
            ...
    def __init__(self, title='', infos=...):
        ...

class LobbyState(State):
    STATE_ID = ''
    VIEW_KEY = None
    _PARENT_CLS = None
    def __init__(self, flags=...):
        ...
    @classmethod
    def parentOf(cls, childStateCls):
        ...
    @classmethod
    def goTo(cls, **params):
        ...
    def goBack(self):
        ...
    def getMachine(self):
        ...
    def getNavigationDescription(self):
        ...
    def getBackNavigationDescription(self, params):
        ...
    def serializeParams(self):
        ...
    def getViewKey(self, params=None):
        ...
    def addNavigationTransition(self, targetViewState, transitionType=..., record=False):
        ...
    def addGuardTransition(self, targetViewState, condition, transitionType=..., record=False):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def makeTransition(self, transitionType, record):
        ...
    def compareParams(self, params, otherParams):
        ...
    def _onEntered(self, event):
        ...
    def _onViewExternallyDestroyed(self):
        ...
    def __subscribeToWindowChanges(self):
        ...
    def __unsubscribeFromWindowChanges(self):
        ...
    def __shouldDisposeView(self, _):
        ...
    def __onWindowStatusChanged(self, uniqueWindowId, status):
        ...

class ViewLobbyState(LobbyState):
    def __init__(self, flags=...):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _onEntered(self, event):
        ...

class GuiImplViewLobbyState(LobbyState):
    _viewImplClass: Any
    _scope: Any
    def __init__(self, viewImplClass, scope, flags=...):
        ...
    def _getViewLoadCtx(self, event):
        ...
    def _getViewLoadParams(self, event):
        ...
    def _onEntered(self, event):
        ...
    def _focusView(self, view, event):
        ...

class EmptyState(LobbyState):
    ...

class UntrackedState(LobbyState):
    LOAD_PARAMS_KEY = 'loadParams'
    _paramsEnteredWith: Any
    _paramsExitedWith: Any
    def __init__(self, flags=...):
        ...
    def getViewKey(self, params=None):
        ...
    def serializeParams(self):
        ...
    def getParamsExitedWith(self):
        ...
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...

class _SubScopeState(LobbyState):
    STATE_ID = 'subScope'
    def __init__(self, flags=...):
        ...

# decorador original: @_SubScopeState.parentOf
class SubScopeSubLayerState(LobbyState):
    STATE_ID = 'subLayer'
    def __init__(self, flags=...):
        ...
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...
    def getNavigationDescription(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class _SubScopeSubLayerUntrackedState(UntrackedState):
    STATE_ID = UNTRACKED_STATE_ID_ENDING
    def getNavigationDescription(self):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class _SubScopeSubLayerEmptyState(EmptyState):
    STATE_ID = EMPTY_STATE_ID_ENDING
    def _onEntered(self, event):
        ...

# decorador original: @SubScopeSubLayerState.parentOf
class _SubScopeSubLayerFinalState(LobbyState):
    STATE_ID = 'FINAL'
    def _onEntered(self, event):
        ...
    def _onExited(self):
        ...
    def _onViewExternallyDestroyed(self):
        ...

# decorador original: @_SubScopeState.parentOf
class SubScopeTopLayerState(LobbyState):
    STATE_ID = 'topLayer'
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...

# decorador original: @SubScopeTopLayerState.parentOf
class _SubScopeTopLayerUntrackedState(UntrackedState):
    STATE_ID = UNTRACKED_STATE_ID_ENDING

# decorador original: @SubScopeTopLayerState.parentOf
class _SubScopeTopLayerEmptyState(EmptyState):
    STATE_ID = EMPTY_STATE_ID_ENDING

class _TopScopeState(LobbyState):
    STATE_ID = 'topScope'
    SCOPE = ScopeTemplates.LOBBY_TOP_SUB_SCOPE
    def __init__(self, flags=...):
        ...

# decorador original: @_TopScopeState.parentOf
class TopScopeTopLayerState(LobbyState):
    STATE_ID = 'topLayer'
    def registerStates(self):
        ...
    def registerTransitions(self):
        ...

# decorador original: @TopScopeTopLayerState.parentOf
class _TopScopeTopLayerUntrackedState(UntrackedState):
    STATE_ID = UNTRACKED_STATE_ID_ENDING

# decorador original: @TopScopeTopLayerState.parentOf
class _TopScopeTopLayerEmptyState(EmptyState):
    STATE_ID = EMPTY_STATE_ID_ENDING

def isInHangarState():
    ...
def isHangarState(state):
    ...
def getNavigationDescriptionSafe(state):
    ...
def compareViewKeys(view, stateViewKey):
    ...
