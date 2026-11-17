# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PowerModeController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from constants import POWER_MODE_STATE as POWER_MODE_STATE
from gui.battle_control.battle_constants import VEHICLE_UPDATE_INTERVAL as VEHICLE_UPDATE_INTERVAL
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from math_utils import clamp01 as clamp01
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents

# base nao representavel no stub: namedtuple(...)
class PowerModeState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status, timeInfo=None):
        ...
    @property
    def activeProgress(self):
        ...
    @property
    def progress(self):
        ...
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class PowerModeController(VehicleDynamicComponent, IMechanicComponent, IMechanicStatesComponent):
    DEFAULT_MODE_STATE: Any
    __mechanicState: Any
    __mechanicPrefabSpawner: Any
    __statesEvents: Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def statesEvents(self):
        ...
    def getMechanicState(self):
        ...
    def set_stateStatus(self, _):
        ...
    def set_timeInfo(self, _):
        ...
    def onDestroy(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def __updateMechanicState(self):
        ...
