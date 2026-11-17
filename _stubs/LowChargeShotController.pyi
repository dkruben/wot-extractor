# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/LowChargeShotController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import LowChargeShotReloadingState as LowChargeShotReloadingState
from events_handler import eventHandler as eventHandler
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from math_utils import almostEqual as almostEqual
from physics_shared import getShotPredictionWindow as getShotPredictionWindow
from vehicles.components.component_wrappers import ifObservedVehicle as ifObservedVehicle
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.entities import ShotParams as ShotParams
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import createMechanicStatesEvents as createMechanicStatesEvents, IMechanicStatesComponent as IMechanicStatesComponent
from vehicles.mechanics.gun_mechanics.low_charge_shot.private import LowChargeShotAmmoState as LowChargeShotAmmoState, LowChargeShotMechanicState as LowChargeShotMechanicState, LowChargeShotUILogging as LowChargeShotUILogging, DEFAULT_MECHANIC_STATE as DEFAULT_MECHANIC_STATE
from items.components.shared_components import LowChargeShotParams as LowChargeShotParams

# decorador original: @ReprInjector.withParent(...)
class LowChargeShotController(VehicleDynamicComponent, IGunMechanicComponent, IMechanicStatesComponent):
    __params: Any
    __prevBaseTime: Any
    __mechanicState: Any
    __mechanicPrefabSpawner: Any
    __statesEvents: Any
    __uiLogging: Any
    def __init__(self):
        ...
    @property
    def vehicleMechanicKey(self):
        ...
    @property
    def statesEvents(self):
        ...
    def getComponentParams(self):
        ...
    def getMechanicState(self):
        ...
    def set_stateStatus(self, _=None):
        ...
    def onDestroy(self):
        ...
    # decorador original: @eventHandler
    def onObserverVehicleDataUpdated(self):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
    # decorador original: @eventHandler
    def onCollectShotParams(self, shotParamsList):
        ...
    def _onAppearanceReady(self):
        ...
    def _onAvatarReady(self, player):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def __updateMechanicState(self):
        ...
    # decorador original: @ifObservedVehicle
    def __updateVehicleGunReloadTime(self, player, _):
        ...
