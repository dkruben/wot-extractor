# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_states/mechanic_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from events_containers.common.containers import ClientEventsContainer as ClientEventsContainer
from events_containers.components.common import ClientComponentEventsDebugger as ClientComponentEventsDebugger
from vehicles.mechanics.mechanic_states.mechanic_interfaces import IMechanicStatesEventsLogic as IMechanicStatesEventsLogic
from vehicles.mechanics.mechanic_states.mechanic_interfaces import IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent, IMechanicStatesListener as IMechanicStatesListener

class MechanicStatesEvents(ClientEventsContainer, IMechanicStatesEventsLogic):
    __componentRef: Any
    __mechanicState: Any
    onStatePrepared: Any
    onStateObservation: Any
    onStateTransition: Any
    onStateTick: Any
    def __init__(self, component, tickInterval):
        ...
    def destroy(self):
        ...
    def lateSubscribe(self, listener):
        ...
    def processStatePrepared(self):
        ...
    def updateMechanicState(self, state):
        ...
    def _isStateTransition(self, prevState, newState):
        ...
    def _getComponent(self):
        ...
    def _createEventsDebugger(self):
        ...
    def __lateStatePrepared(self, handler):
        ...
    def __lateStateObservation(self, handler):
        ...
    def __tickState(self):
        ...

class MechanicStatesEventsDebugger(ClientComponentEventsDebugger):
    IGNORED_EVENTS: Any
    _EVENTS_DEBUG_PREFIX = 'MECHANIC_STATE'
