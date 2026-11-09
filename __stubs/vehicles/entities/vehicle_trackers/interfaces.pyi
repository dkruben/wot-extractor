# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/entities/vehicle_trackers/interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import UNKNOWN_VEHICLE_ID as UNKNOWN_VEHICLE_ID
from events_containers.common.containers import IClientEventsContainer as IClientEventsContainer, IClientEventsContainerListener as IClientEventsContainerListener
from Vehicle import Vehicle as Vehicle

class IVehicleEntityTrackerLogic(object):
    onVehicleEntityCatching = None
    onVehicleEntityReleasing = None
    @property
    def trackedVehicle(self):
        ...
    def startTracking(self):
        ...
    def stopTracking(self):
        ...
    def updateTracking(self, vehicleID=..., vehicle=None):
        ...

class IVehicleEntityTracker(IClientEventsContainer, IVehicleEntityTrackerLogic):
    ...

class IVehicleEntityTrackerListenerLogic(object):
    def onVehicleEntityCatching(self, vehicle):
        ...
    def onVehicleEntityReleasing(self, vehicle):
        ...

class IVehicleEntityTrackerListener(IClientEventsContainerListener, IVehicleEntityTrackerListenerLogic):
    ...
