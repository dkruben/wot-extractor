# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AutoreloaderSurgeController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
import BigWorld as BigWorld
from constants import AUTORELOADER_SURGE_RESTRICTION as AUTORELOADER_SURGE_RESTRICTION, AUTORELOADER_SURGE_STATE as AUTORELOADER_SURGE_STATE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from math_utils import clamp01 as clamp01
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent as IMechanicCommandsComponent, createMechanicCommandsEvents as createMechanicCommandsEvents
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents
from typing import Any as Any, Dict as Dict, Optional as Optional
from items.components.shared_components import AutoreloaderSurgeParams as AutoreloaderSurgeParams
from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents as IMechanicCommandsEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents
_LOG_AUTORELOADER_SURGE_DEBUG = True
_logger: _Any

# base nao representavel no stub: typing.NamedTuple(...)
# decorador original: @ReprInjector.simple(...)
class AutoreloaderSurgeState(IMechanicState):
    def __init__(self, state, restrictions, *args):
        ...
    @classmethod
    def fromComponentStatus(cls, status):
        ...
    @property
    def chargeTime(self):
        ...
    @property
    def progress(self):
        ...
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class AutoreloaderSurgeController(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    __params: _Any
    __mechanicPrefabSpawner: _Any
    __commandsEvents: _Any
    __statesEvents: _Any
    __mechanicState: _Any
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
    def getComponentParams(self):
        ...
    def set_abilityState(self, *_):
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
    def __updateMechanicState(self):
        ...
