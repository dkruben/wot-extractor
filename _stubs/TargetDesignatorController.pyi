# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TargetDesignatorController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import TARGET_DESIGNATOR_STATE as STATE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent as IMechanicCommandsComponent, createMechanicCommandsEvents as createMechanicCommandsEvents
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents
from typing import Optional as Optional
from items.components.shared_components import TargetDesignatorParams as TargetDesignatorParams
from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents as IMechanicCommandsEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents

# decorador original: @ReprInjector.simple(...)
class TargetDesignatorState(IMechanicState):
    __slots__: tuple
    state: Any
    params: Any
    baseTime: Any
    startTime: Any
    endTime: Any
    def __init__(self, state, params, startTime=0.0, endTime=0.0):
        ...
    def timeLeft(self):
        ...
    def baseTimeLeft(self):
        ...
    def progress(self, timeLeft):
        ...
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class TargetDesignatorController(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    __mechanicPrefabSpawner: Any
    __commandsEvents: Any
    __statesEvents: Any
    __params: Any
    __state: Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def commandsEvents(self):
        ...
    @property
    def statesEvents(self):
        ...
    def getComponentParams(self):
        ...
    def getMechanicState(self):
        ...
    def set_abilityState(self, _):
        ...
    def onDestroy(self):
        ...
    def tryActivate(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def __updateState(self):
        ...
