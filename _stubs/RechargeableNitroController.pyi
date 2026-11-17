# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/RechargeableNitroController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
import BigWorld as BigWorld
from constants import RECHARGEABLE_NITRO_STATE as RECHARGEABLE_NITRO_STATE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.components.shared_components import RechargeableNitroParams as RechargeableNitroParams
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent as IMechanicCommandsComponent, createMechanicCommandsEvents as createMechanicCommandsEvents
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from typing import Any as Any, Optional as Optional
from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents as IMechanicCommandsEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents

# base nao representavel no stub: typing.NamedTuple(...)
# decorador original: @ReprInjector.simple(...)
class RechargeableNitroState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status, params):
        ...
    @property
    def progress(self):
        ...
    @property
    def timeLeft(self):
        ...
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class RechargeableNitroController(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    __params: _Any
    __currentState: _Any
    __mechanicPrefabSpawner: _Any
    __commandsEvents: _Any
    __statesEvents: _Any
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
    def set_stateStatus(self, _):
        ...
    def onDestroy(self):
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
