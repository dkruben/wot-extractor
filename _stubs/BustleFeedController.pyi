# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/BustleFeedController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
import BigWorld as BigWorld
from constants import ARENA_PERIOD as ARENA_PERIOD, BUSTLE_FEED_STATE as BUSTLE_FEED_STATE, BUSTLE_FEED_SWITCH_ACCESS as BUSTLE_FEED_SWITCH_ACCESS
from events_handler import eventHandler as eventHandler
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from vehicles.components.component_wrappers import ifAppearanceReady as ifAppearanceReady, ifPlayerVehicle as ifPlayerVehicle, ifObservedVehicle as ifObservedVehicle
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.entities import ShotParams as ShotParams
from vehicles.mechanics.generic_mechanics.bustle_feed import createBustleFeedStatesEvents as createBustleFeedStatesEvents, DEFAULT_BUSTLE_FEED_PARAMS as DEFAULT_BUSTLE_FEED_PARAMS, BustleFeedComponentParams as BustleFeedComponentParams, BustleFeedState as BustleFeedState, BustleFeedAmmoState as BustleFeedAmmoState
from vehicles.mechanics.common import IMechanicComponent as IMechanicComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent as IMechanicCommandsComponent, createMechanicCommandsEvents as createMechanicCommandsEvents
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_inputs import createMechanicSingleInput as createMechanicSingleInput
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent
import CGF as CGF
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents
from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents as IMechanicCommandsEvents

class PlayerVehicleInputPredicate(object):
    _entityRef: Any
    def __init__(self, entity):
        ...
    def __call__(self):
        ...
    @staticmethod
    def _hasBattleStarted():
        ...

# decorador original: @ReprInjector.withParent(...)
class BustleFeedController(VehicleDynamicComponent, IMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    _INPUT_ACTION_NAME = 'ABILITY_1_INPUT_ACTION'
    _INPUT_PROFILE_NAME = 'ABILITY_1_INPUT_PROFILE'
    __singleInput: Any
    __componentParams: Any
    __variableStorageGO: Any
    __commandsEvents: Any
    __statesEvents: Any
    __prefabSpawner: Any
    __shootingBlockTimestamp: Any
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
    def getVariableStorageGO(self):
        ...
    def setVariableStorageGO(self, go):
        ...
    def set_status(self, *_):
        ...
    def set_reloadStatus(self, *_):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
    # decorador original: @eventHandler
    def onCollectShotParams(self, shotParamsList):
        ...
    # decorador original: @eventHandler
    def onObserverVehicleDataUpdated(self):
        ...
    def onDestroy(self):
        ...
    # decorador original: @ifAppearanceReady
    def startBustleReload(self, shell, side):
        ...
    # decorador original: @ifPlayerVehicle
    def tryActivate(self, _):
        ...
    def _onAvatarReady(self, player):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    # decorador original: @ifObservedVehicle
    def __updateVehicleGunReloadTime(self, player, _):
        ...
