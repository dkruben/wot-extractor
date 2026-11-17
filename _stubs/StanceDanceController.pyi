# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/StanceDanceController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
import BigWorld as BigWorld
import math_utils as math_utils
from constants import STANCE_DANCE_STATE as STANCE_DANCE_STATE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.components.shared_components import StanceDanceParams as StanceDanceParams
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_commands import createMechanicCommandsEvents as createMechanicCommandsEvents, IMechanicCommandsComponent as IMechanicCommandsComponent
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesComponent as IMechanicStatesComponent, IMechanicState as IMechanicState
from typing import Any as Any, Optional as Optional, Dict as Dict
from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents as IMechanicCommandsEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents
_LOG_STANCE_DANCE_DEBUG = False

# base nao representavel no stub: typing.NamedTuple(...)
# decorador original: @ReprInjector.simple(...)
class StanceDanceState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status, params):
        ...
    @property
    def getFightEnergyRatio(self):
        ...
    @property
    def getTurboEnergyRatio(self):
        ...
    @property
    def timeLeftActiveFight(self):
        ...
    @property
    def timeLeftActiveTurbo(self):
        ...
    @property
    def transitionTimeLeft(self):
        ...
    @property
    def isFightState(self):
        ...
    @property
    def isTurboState(self):
        ...
    @property
    def isActiveFightState(self):
        ...
    @property
    def isActiveTurboState(self):
        ...
    @property
    def isSwitchingState(self):
        ...
    @property
    def isEngineDeadState(self):
        ...
    @property
    def isGainingEnergy(self):
        ...
    @property
    def isGainingEnergyBoosted(self):
        ...
    @property
    def progressFight(self):
        ...
    @property
    def progressTurbo(self):
        ...
    @property
    def isEnoughEnergyToActivate(self):
        ...
    def isTransition(self, other):
        ...

# decorador original: @ReprInjector.withParent(...)
class StanceDanceController(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    __params: _Any
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
    def set_abilityState(self, *_):
        ...
    def onDestroy(self):
        ...
    def tryUseActiveAbility(self):
        ...
    def trySwitchStance(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
