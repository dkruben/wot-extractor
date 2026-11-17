# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ShellParamsSwitcherController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from events_handler import eventHandler as eventHandler
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey, VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.components.vehicle_component import VehicleDynamicComponent as VehicleDynamicComponent
from vehicles.components.vehicle_prefabs import createMechanicPrefabSpawner as createMechanicPrefabSpawner
from vehicles.mechanics.gun_mechanics.common import IGunMechanicComponent as IGunMechanicComponent
from vehicles.mechanics.gun_mechanics.shell_params_switcher import ShellParamsSwitcherMechanicState as ShellParamsSwitcherMechanicState, ShellParamsSwitcherComponentParams as ShellParamsSwitcherComponentParams, createShellParamsSwitcherStatesEvents as createShellParamsSwitcherStatesEvents, DEFAULT_SHELL_PARAMS_SWITCHER_PARAMS as DEFAULT_SHELL_PARAMS_SWITCHER_PARAMS, DEFAULT_SHELL_PARAMS_SWITCHER_STATE as DEFAULT_SHELL_PARAMS_SWITCHER_STATE, ShellParamsSwitcherAmmoState as ShellParamsSwitcherAmmoState
from vehicles.mechanics.mechanic_constants import VehicleMechanicCommand as VehicleMechanicCommand
from vehicles.mechanics.mechanic_commands import IMechanicCommandsComponent as IMechanicCommandsComponent, createMechanicCommandsEvents as createMechanicCommandsEvents
from vehicles.mechanics.mechanic_helpers import getVehicleDescrMechanicParams as getVehicleDescrMechanicParams
from vehicles.mechanics.mechanic_states import IMechanicStatesComponent as IMechanicStatesComponent
from vehicles.mechanics.mechanic_states import IMechanicStatesEvents as IMechanicStatesEvents
from vehicles.mechanics.gun_mechanics.shell_params_switcher import IShellParamsSwitcherMechanicState as IShellParamsSwitcherMechanicState, IShellParamsSwitcherComponentParams as IShellParamsSwitcherComponentParams

# decorador original: @ReprInjector.withParent(...)
class ShellParamsSwitcherController(VehicleDynamicComponent, IGunMechanicComponent, IMechanicCommandsComponent, IMechanicStatesComponent):
    __currentShellCD: Any
    __componentParams: Any
    __mechanicState: Any
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
    def set_publicStatus(self, _):
        ...
    def set_status(self, _):
        ...
    def tryActivate(self):
        ...
    # decorador original: @eventHandler
    def onCollectAmmoStates(self, ammoStates):
        ...
    # decorador original: @eventHandler
    def onCurrentShellChanged(self, intCD):
        ...
    def onDestroy(self):
        ...
    def _collectComponentParams(self, typeDescriptor):
        ...
    def _onComponentAppearanceUpdate(self, **kwargs):
        ...
    def _onAppearanceReady(self):
        ...
    def _onComponentAvatarUpdate(self, player):
        ...
    def __updateMechanicState(self):
        ...
