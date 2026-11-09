# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/shell_params_switcher/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import SHELL_PARAMS_SWITCHER_MASK as SHELL_PARAMS_SWITCHER_MASK, SHELL_PARAMS_SWITCHER_STATE as SHELL_PARAMS_SWITCHER_STATE
from items import vehicles as vehicles
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState
from gui.battle_control.components_states.ammo.constants import ActiveAmmoMode as ActiveAmmoMode, ShellMode as ShellMode
from gui.battle_control.components_states.ammo.shells import DefaultAmmoMode as DefaultAmmoMode
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from vehicles.mechanics.gun_mechanics.shell_params_switcher.mechanic_interfaces import IShellParamsSwitcherMechanicState as IShellParamsSwitcherMechanicState, IShellParamsSwitcherComponentParams as IShellParamsSwitcherComponentParams
from items.components.shared_components import ShellSwitcherParams as ShellSwitcherParams

# decorador original: @ReprInjector.simple(...)
class ShellParamsSwitcherComponentParams(IShellParamsSwitcherComponentParams):
    __shellSubtypes: Any
    def __init__(self, shellSubtypes):
        ...
    @classmethod
    def fromMechanicParams(cls, params, vehIntCD):
        ...
    @property
    def shellSubtypes(self):
        ...

# decorador original: @ReprInjector.simple(...)
class ShellParamsSwitcherMechanicState(IShellParamsSwitcherMechanicState):
    __state: Any
    __mask: Any
    __baseState: Any
    __endTime: Any
    __lastActiveShotTimestamp: Any
    __isActive: Any
    __params: Any
    __shellCD: Any
    def __init__(self, state, endTime, isActive, lastActiveShotTimestamp, params, shellCD):
        ...
    @classmethod
    def fromComponentStatus(cls, status, publicStatus, params, shellCD):
        ...
    @property
    def state(self):
        ...
    @property
    def baseState(self):
        ...
    @property
    def isActive(self):
        ...
    @property
    def lastActiveShotTimestamp(self):
        ...
    @property
    def mechanicSubtype(self):
        ...
    def isTransition(self, other):
        ...
    def isNoAmmo(self):
        ...
    def isCritState(self):
        ...
    def timeLeft(self):
        ...

class ShellParamsSwitcherAmmoMode(DefaultAmmoMode):
    __mechanicState: Any
    __modifiedShells: Any
    def __init__(self, mechanicState, modifiedShells):
        ...
    def getActiveMode(self):
        ...
    def getModifiedShells(self):
        ...
    def getShellMode(self, shellIntCD):
        ...

class ShellParamsSwitcherAmmoState(DefaultComponentAmmoState):
    __ammoMode: Any
    def __init__(self, mechanicState, modifiedShells):
        ...
    def getAmmoMode(self):
        ...
