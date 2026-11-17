# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/mechanic_trackers/tracker_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from events_containers.common.containers import IClientEventsContainer as IClientEventsContainer, IClientEventsContainerListener as IClientEventsContainerListener
from vehicles.entities.vehicle_trackers import IVehicleEntityTrackerListenerLogic as IVehicleEntityTrackerListenerLogic
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey

class IVehicleMechanicsTrackerLogic(IVehicleEntityTrackerListenerLogic):
    onMechanicComponentCatching = None
    onMechanicComponentReleasing = None
    onMechanicComponentsUpdate = None
    @property
    def trackedComponents(self):
        ...
    def getTrackedComponent(self, mechanic):
        ...

class IVehicleMechanicsTracker(IClientEventsContainer, IVehicleMechanicsTrackerLogic):
    ...

class IVehicleMechanicsTrackerListenerLogic(object):
    def onMechanicComponentCatching(self, component):
        ...
    def onMechanicComponentReleasing(self, component):
        ...
    def onMechanicComponentsUpdate(self, components):
        ...

class IVehicleMechanicsTrackerListener(IClientEventsContainerListener, IVehicleMechanicsTrackerListenerLogic):
    ...
