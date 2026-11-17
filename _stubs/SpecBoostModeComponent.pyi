# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/SpecBoostModeComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import PHASED_MECHANIC_STATE as PHASED_MECHANIC_STATE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanic as VehicleMechanic, VehicleMechanicKey as VehicleMechanicKey, SpecBoostModeMechanicVariant as SpecBoostModeMechanicVariant
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.generic_mechanics.spec_boost_mode import ISpecBoostModeMechanicParams as ISpecBoostModeMechanicParams, ISpecBoostModeMechanicState as ISpecBoostModeMechanicState, SpecBoostModeMechanicState as SpecBoostModeMechanicState, SpecBoostModeMechanicParams as SpecBoostModeMechanicParams, DEFAULT_SPEC_BOOST_MODE_STATE as DEFAULT_SPEC_BOOST_MODE_STATE, DEFAULT_SPEC_BOOST_MODE_PARAMS as DEFAULT_SPEC_BOOST_MODE_PARAMS
from vehicles.mechanics.mechanic_commands import createMechanicCommandsEvents as createMechanicCommandsEvents, IMechanicCommandsComponent as IMechanicCommandsComponent
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents as IMechanicCommandsEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents

# decorador original: @ReprInjector.withParent(...)
class SpecBoostModeComponent(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    __componentParams: Any
    __mechanicState: Any
    __commandsEvents: Any
    __statesEvents: Any
    __mechanicPrefabSpawner: Any
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
    def set_status(self, _):
        ...
    def onDestroy(self):
        ...
    def tryActivate(self):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def __updateMechanicState(self):
        ...
