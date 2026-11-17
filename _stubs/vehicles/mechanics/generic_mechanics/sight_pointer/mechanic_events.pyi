# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/sight_pointer/mechanic_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import typing as typing
from cgf_events import gun_events as gun_events
from cgf_events.mechanics_events import postSightPointerSectorEvent as postSightPointerSectorEvent
from constants import SIGHT_POINTER_STATE as SIGHT_POINTER_STATE, VISIBILITY as VISIBILITY
from events_containers.common.containers import ClientEventsContainerDebugger as ClientEventsContainerDebugger
from events_handler import eventHandler as eventHandler
from vehicles.components.component_events import VehicleComponentEventsCoreIntegration as VehicleComponentEventsCoreIntegration
from vehicles.mechanics.generic_mechanics.sight_pointer.mechanic_interfaces import ISightPointerStatesEvents as ISightPointerStatesEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic as IMechanicStatesListenerLogic, MechanicStatesEvents as MechanicStatesEvents
from events_containers.common.containers.interfaces import IClientEventsContainer as IClientEventsContainer
from SightPointerComponent import SightPointerState as SightPointerState
_VAR_SECTOR_MINSIZE = 'sectorVision/minsize'
_LERP_DURATION = 0.3
_OPACITY_MIN = 0.06
_OPACITY_MAX = 0.15

class SightPointerStatesEvents(MechanicStatesEvents, ISightPointerStatesEvents):
    def _createCoreIntegration(self):
        ...
    def updateComponentParams(self, maxAngle, minAngle):
        ...
    def _createEventsDebugger(self):
        ...

class SightPointerEventsDebugger(ClientEventsContainerDebugger):
    IGNORED_EVENTS: Any
    _EVENTS_DEBUG_PREFIX = 'SIGHT_POINTER'

class SightPointerStatesCoreIntegration(VehicleComponentEventsCoreIntegration, IMechanicStatesListenerLogic):
    __lastAngle: Any
    __lastDistance: Any
    __maxAngle: Any
    __minAngle: Any
    __isActivated: Any
    def __init__(self, events, component):
        ...
    # decorador original: @eventHandler
    def onStatePrepared(self, state):
        ...
    # decorador original: @eventHandler
    def onStateObservation(self, state):
        ...
    # decorador original: @eventHandler
    def onEventsContainerDestroy(self, events):
        ...
    def updateComponentParams(self, maxAngle, minAngle):
        ...
    def __updateSector(self, state):
        ...
    def __postMinSizeEvent(self, distance):
        ...
    def __calcOpacity(self, angleDeg):
        ...
    def __postSectorLerpEvent(self, targetWidth, targetDistance, targetOpacity):
        ...
