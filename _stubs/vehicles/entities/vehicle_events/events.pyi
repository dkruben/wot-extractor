# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/entities/vehicle_events/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from events_containers.common.containers import ClientEventsContainer as ClientEventsContainer, ClientEventsContainerDebugger as ClientEventsContainerDebugger
from vehicles.entities.vehicle_events.interfaces import IVehicleEventsLogic as IVehicleEventsLogic
from gui.battle_control.components_states.ammo import IComponentAmmoState as IComponentAmmoState
from Vehicle import Vehicle as Vehicle

class VehicleEvents(ClientEventsContainer, IVehicleEventsLogic):
    __vehicle: Any
    onAppearanceReady: Any
    onAppearanceComponentsReady: Any
    onAppearanceReset: Any
    onSiegeStateUpdated: Any
    onVehicleDestroyed: Any
    onCollectAmmoStates: Any
    onCollectShotParams: Any
    onCurrentShellChanged: Any
    onDynamicComponentCreated: Any
    onDynamicComponentDestroyed: Any
    onDiscreteShotDone: Any
    onShowDamageFromShot: Any
    onVehicleHealthChanged: Any
    onObserverVehicleDataUpdated: Any
    def __init__(self, vehicle):
        ...
    def destroy(self):
        ...
    def collectAmmoStates(self):
        ...
    def _createEventsDebugger(self):
        ...

class VehicleEventsDebugger(ClientEventsContainerDebugger):
    IGNORED_EVENTS: Any
    __vehicleID: Any
    def __init__(self, events, vehicleID):
        ...
    def _getDebugPrefix(self):
        ...
