# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/entities/vehicle_trackers/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
import BigWorld as BigWorld
from constants import UNKNOWN_VEHICLE_ID as UNKNOWN_VEHICLE_ID
from events_handler import eventHandler as eventHandler
from events_containers.common.containers import ClientEventsContainer as ClientEventsContainer, ContainersListener as ContainersListener
from PlayerEvents import g_playerEvents as g_playerEvents
from vehicles.entities.vehicle_events import IVehicleEventsListenerLogic as IVehicleEventsListenerLogic
from vehicles.entities.vehicle_trackers.interfaces import IVehicleEntityTrackerLogic as IVehicleEntityTrackerLogic
from vehicles.entities.vehicle_trackers.interfaces import IVehicleEntityTrackerListener as IVehicleEntityTrackerListener
from Vehicle import Vehicle as Vehicle

class VehicleEntityTracker(ClientEventsContainer, ContainersListener, IVehicleEntityTrackerLogic, IVehicleEventsListenerLogic):
    __vehicleID: Any
    __isTracking: Any
    __vehicleRef: Any
    onVehicleEntityCatching: Any
    onVehicleEntityReleasing: Any
    def __init__(self, vehicleID):
        ...
    def __repr__(self):
        ...
    @property
    def trackedVehicle(self):
        ...
    def destroy(self):
        ...
    def lateSubscribe(self, listener):
        ...
    def unsubscribe(self, listener):
        ...
    def startTracking(self):
        ...
    def stopTracking(self):
        ...
    def updateTracking(self, vehicleID=..., vehicle=None):
        ...
    # decorador original: @eventHandler
    def onVehicleEntityCreated(self, vehicle):
        ...
    # decorador original: @eventHandler
    def onVehicleDestroyed(self):
        ...
    def __invalidateVehicleEntity(self, vehicle=None):
        ...
    def __catchVehicleEntity(self, vehicle):
        ...
    def __releaseVehicleEntity(self):
        ...
    def __lateVehicleEntityHandler(self, handler):
        ...
