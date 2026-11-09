# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_trackers/tracker_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from events_handler import eventHandler as eventHandler
from events_containers.common.containers import ClientEventsContainer as ClientEventsContainer, ContainersListener as ContainersListener
from events_containers.components.life_cycle import isLifeCycleComponent as isLifeCycleComponent, IComponentLifeCycleListenerLogic as IComponentLifeCycleListenerLogic
from vehicles.entities.vehicle_events import IVehicleEventsListenerLogic as IVehicleEventsListenerLogic
from vehicles.mechanics.mechanic_constants import TRACKABLE_VEHICLE_MECHANICS as TRACKABLE_VEHICLE_MECHANICS
from vehicles.mechanics.mechanic_helpers import isValidMechanicComponent as isValidMechanicComponent, getVehicleMechanicsComponents as getVehicleMechanicsComponents
from vehicles.mechanics.mechanic_trackers.tracker_interfaces import IVehicleMechanicsTrackerLogic as IVehicleMechanicsTrackerLogic
from events_containers.components.life_cycle import ILifeCycleComponent as ILifeCycleComponent
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from Vehicle import Vehicle as Vehicle
from vehicles.mechanics.mechanic_trackers.tracker_interfaces import IVehicleMechanicsTrackerListener as IVehicleMechanicsTrackerListener

class _TrackableComponentCriteria(object):
    __trackedMechanics: Any
    def __init__(self, trackedMechanics):
        ...
    def __call__(self, component):
        ...

class VehicleMechanicsTracker(ClientEventsContainer, ContainersListener, IVehicleMechanicsTrackerLogic, IVehicleEventsListenerLogic, IComponentLifeCycleListenerLogic):
    __trackedMechanics: Any
    __trackedComponents: Any
    __trackable: Any
    onMechanicComponentCatching: Any
    onMechanicComponentsUpdate: Any
    onMechanicComponentReleasing: Any
    def __init__(self, trackedMechanics):
        ...
    def __repr__(self):
        ...
    @property
    def trackedComponents(self):
        ...
    def getTrackedComponent(self, mechanic):
        ...
    def destroy(self):
        ...
    def lateSubscribe(self, listener):
        ...
    def unsubscribe(self, listener):
        ...
    # decorador original: @eventHandler
    def onDynamicComponentCreated(self, component):
        ...
    # decorador original: @eventHandler
    def onComponentDestroyed(self, component):
        ...
    # decorador original: @eventHandler
    def onVehicleEntityCatching(self, vehicle):
        ...
    # decorador original: @eventHandler
    def onVehicleEntityReleasing(self, vehicle):
        ...
    def __catchMechanicComponents(self, vehicle):
        ...
    def __releaseMechanicComponents(self):
        ...
    def __catchMechanicComponent(self, mechanicComponent):
        ...
    def __releaseMechanicComponent(self, mechanicComponent):
        ...
    def __lateMechanicComponentHandler(self, handler):
        ...
    def __lateMechanicComponentsUpdate(self, handler):
        ...
