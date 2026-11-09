# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/PillboxSiegeComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import Input as Input
import logging as logging
from constants import VEHICLE_SIEGE_STATE as VEHICLE_SIEGE_STATE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.component_wrappers import ifPlayerVehicle as ifPlayerVehicle, ifObservedVehicle as ifObservedVehicle
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_commands import createMechanicCommandsEvents as createMechanicCommandsEvents, IMechanicCommandsEvents as IMechanicCommandsEvents, IMechanicCommandsComponent as IMechanicCommandsComponent
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent, createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesEvents as IMechanicStatesEvents, IMechanicState as IMechanicState
from Input import TriggerEvent as TriggerEvent
_logger: Any

class PlayerVehicleInputPredicate(object):
    _entityRef: Any
    def __init__(self, entity):
        ...
    def __call__(self):
        ...

# base nao representavel no stub: namedtuple(...)
class PillboxSiegeModeState(IMechanicState):
    @property
    def progress(self):
        ...
    @property
    def timeLeft(self):
        ...
    @property
    def isStateSwitching(self):
        ...
    def isTransition(self, other):
        ...
    def toSiegeState(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class PillboxSiegeComponent(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    TAP_TIME = 0.25
    HOLD_TIME = 1.0
    DURATION: Any
    TAP_ACTION_NAME = 'pbs_tap'
    HOLD_ACTION_NAME = 'pbs_hold'
    PBS_PROFILE_NAME = 'PBS_INPUT_PROFILE'
    __holdTime: Any
    __mechanicPrefabSpawner: Any
    __commandsEvents: Any
    __statesEvents: Any
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
    def set_status(self, _):
        ...
    def set_publicStatus(self, _):
        ...
    def onDestroy(self):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onAvatarReady(self, player):
        ...
    # decorador original: @ifPlayerVehicle
    def __attachInput(self, *_, **__):
        ...
    # decorador original: @ifPlayerVehicle
    def __detachInput(self, *_, **__):
        ...
    def __onTapCanceled(self):
        ...
    def __onTapCompleted(self):
        ...
    def __onHoldStarted(self):
        ...
    def __onHoldCompleted(self):
        ...
    def __onHoldCanceled(self):
        ...
    # decorador original: @ifObservedVehicle
    def __notifyStateChange(self, player, _, mechanicState):
        ...
