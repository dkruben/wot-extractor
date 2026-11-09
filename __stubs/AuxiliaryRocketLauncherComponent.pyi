# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AuxiliaryRocketLauncherComponent.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import SECONDARY_GUN_STATE as SECONDARY_GUN_STATE
from events_handler import eventHandler as eventHandler
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.component_wrappers import ifPlayerVehicle as ifPlayerVehicle
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.gun_mechanics.auxiliary_rocket_launcher import createAuxiliaryRocketLauncherStatesEvents as createAuxiliaryRocketLauncherStatesEvents, AuxiliaryRocketLauncherState as AuxiliaryRocketLauncherState, AuxiliaryRocketLauncherAmmoState as AuxiliaryRocketLauncherAmmoState
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent
from vehicles.mechanics.mechanic_commands import createMechanicCommandsEvents as createMechanicCommandsEvents, IMechanicCommandsComponent as IMechanicCommandsComponent
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_inputs import createAuxiliaryRocketLauncherInput as createAuxiliaryRocketLauncherInput
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent
from vehicles.mechanics.mechanic_commands import IMechanicCommandsEvents as IMechanicCommandsEvents
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents

# decorador original: @ReprInjector.withParent(...)
class AuxiliaryRocketLauncherComponent(VehicleDynamicComponent, IGunMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    _SWITCH_MODE_INPUT_PROFILE_NAME = 'ABILITY_0_INPUT_PROFILE'
    _SWITCH_MODE_INPUT_ACTION_NAME = 'ABILITY_0_INPUT_ACTION'
    _ACTIVATE_INPUT_PROFILE_NAME = 'ARL_ACTIVATE_INPUT_PROFILE'
    _ACTIVATE_INPUT_ACTION_NAME = 'ARL_ACTIVATE_INPUT_ACTION'
    __isInAimingMode: Any
    __mechanicInput: Any
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
    @property
    def isInAimingMode(self):
        ...
    def getMechanicState(self):
        ...
    def getGunInstallationIndex(self):
        ...
    def set_status(self, _):
        ...
    def set_visualStatus(self, _):
        ...
    def onDestroy(self):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
    def _onAvatarReady(self, player):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    # decorador original: @ifPlayerVehicle
    def __switchAimingMode(self, player):
        ...
    def __tryActivate(self):
        ...
