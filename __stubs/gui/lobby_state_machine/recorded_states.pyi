# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lobby_state_machine/recorded_states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from frameworks_common.state_machine.visitor import isDescendantOf as isDescendantOf, getAncestors as getAncestors
from frameworks.wulf import WindowStatus as WindowStatus
from gui.lobby_state_machine.states import LobbyState as LobbyState, compareViewKeys as compareViewKeys
from helpers import dependency as dependency
from helpers.events_handler import EventsHandler as EventsHandler
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from gui.lobby_state_machine.lobby_state_machine import LobbyStateMachine as LobbyStateMachine
from gui.lobby_state_machine.transitions import NavigationTransition as NavigationTransition
_logger: Any

class _RecordedStates(EventsHandler):
    removableStateSelectors: Any
    __onRecordedStatesExternallyChanged: Any
    __stateWithParamStack: Any
    def __init__(self, onRecordedStatesExternallyChanged):
        ...
    def __repr__(self):
        ...
    def getStateWithParamStack(self):
        ...
    def clear(self):
        ...
    def push(self, state, params=None):
        ...
    def peek(self):
        ...
    def pop(self):
        ...
    def hasEntries(self):
        ...
    def contains(self, predicate):
        ...
    def pushRecordedTransitionSource(self, transition, isTransitioningByBackNavigation):
        ...
    def clearCycles(self, lsm, state, params):
        ...
    def _getEvents(self):
        ...
    def __onWindowStatusChanged(self, uniqueWindowId, status):
        ...

def buildSerializedParamsTopDown(sourceState):
    ...
def getViewKeyAlias(view):
    ...
