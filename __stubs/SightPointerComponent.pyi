# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/SightPointerComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import SIGHT_POINTER_STATE as SIGHT_POINTER_STATE, SIGHT_POINTER_COMMON_CONSTANTS as SIGHT_POINTER_COMMON_CONSTANTS
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from items.vehicles import VehicleDescriptor as VehicleDescriptor
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent as IMechanicCommandsComponent, IMechanicCommandsEvents as IMechanicCommandsEvents, createMechanicCommandsEvents as createMechanicCommandsEvents
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.generic_mechanics.sight_pointer import createSightPointerStatesEvents as createSightPointerStatesEvents
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent, IMechanicStatesEvents as IMechanicStatesEvents

# base nao representavel no stub: typing.NamedTuple(...)
class SightPointerState(IMechanicState):
    def canUseAbility(self):
        ...
    @property
    def timeLeft(self):
        ...
    @property
    def progress(self):
        ...
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class SightPointerComponent(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    __commandsEvents: Any
    __statesEvents: Any
    __mechanicPrefabSpawner: Any
    __mechanicParams: Any
    __baseTime: Any
    __maxAngle: Any
    __minAngle: Any
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
    def getMechanicState(self):
        ...
    def set_abilityInfo(self, _):
        ...
    def set_status(self, _):
        ...
    def onDestroy(self):
        ...
    def getComponentParams(self):
        ...
    def tryActivate(self):
        ...
    def tryDeactivate(self):
        ...
    def alternateOnState(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def __applyComponentParams(self):
        ...
