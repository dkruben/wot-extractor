# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ChargeShotComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import CHARGE_SHOT_FLAGS as FLAGS
from constants import VEHICLE_SETTING as VEHICLE_SETTING
from events_handler import eventHandler as eventHandler
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR as CANT_SHOOT_ERROR
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from physics_shared import getShotPredictionWindow as getShotPredictionWindow
from vehicles.components.component_wrappers import ifPlayerVehicle as ifPlayerVehicle
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.entities import ShotParams as ShotParams
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent as IMechanicCommandsComponent, createMechanicCommandsEvents as createMechanicCommandsEvents
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_states import createMechanicStatesEvents as createMechanicStatesEvents, IMechanicState as IMechanicState, IMechanicStatesComponent as IMechanicStatesComponent
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from items.components.gun_installation_components import GunInstallationSlot as GunInstallationSlot
from items.components.shared_components import ChargeShotParams as ChargeShotParams

# decorador original: @ReprInjector.simple(...)
class ChargeShotState(IMechanicState):
    __slots__: tuple
    flags: Any
    level: Any
    endTime: Any
    baseTime: Any
    hasCharging: Any
    hasShotBlock: Any
    canStart: Any
    isGunDestroyed: Any
    def __init__(self, flags, level=0, baseTime=0.0, endTime=0.0):
        ...
    def timeLeft(self):
        ...
    def progress(self, timeLeft):
        ...
    def isTransition(self, other):
        ...

class ChargeShotAmmoState(DefaultComponentAmmoState):
    __mechanicState: Any
    def __init__(self, mechanicState):
        ...
    def canChangeVehicleSetting(self, code):
        ...
    def canShootValidation(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class ChargeShotComponent(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    DEFAULT_MECHANIC_STATE: Any
    __params: Any
    __state: Any
    __mechanicPrefabSpawner: Any
    __statesEvents: Any
    __commandsEvents: Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def statesEvents(self):
        ...
    @property
    def commandsEvents(self):
        ...
    def getComponentParams(self):
        ...
    def getMechanicState(self):
        ...
    def set_privateState(self, _):
        ...
    def set_publicState(self, _):
        ...
    def onDestroy(self):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
    # decorador original: @eventHandler
    def onCollectShotParams(self, shotParamsList):
        ...
    # decorador original: @eventHandler
    def onDiscreteShotDone(self, gunInstallationSlot):
        ...
    # decorador original: @ifPlayerVehicle
    def tryActivate(self, player):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, predictedState=None, **kwargs):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def __getCurrentState(self):
        ...
