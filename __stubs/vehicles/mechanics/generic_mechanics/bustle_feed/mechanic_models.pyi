# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/generic_mechanics/bustle_feed/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from constants import BUSTLE_FEED_STATE as BUSTLE_FEED_STATE, VEHICLE_SETTING as VEHICLE_SETTING, BUSTLE_FEED_SWITCH_ACCESS as BUSTLE_FEED_SWITCH_ACCESS
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState
from gui.battle_control.components_states.ammo.constants import ActiveAmmoMode as ActiveAmmoMode, ShellMode as ShellMode
from gui.battle_control.components_states.ammo.shells import DefaultAmmoMode as DefaultAmmoMode
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from items.components.shared_components import BustleFeedParams as BustleFeedParams
from items.vehicles import VehicleDescriptor as VehicleDescriptor

# decorador original: @ReprInjector.simple(...)
class BustleFeedComponentParams(object):
    __activationTime: Any
    __modifiedShells: Any
    __shotReloadFactor: Any
    def __init__(self, activationTime, modifiedShells, shotReloadFactor):
        ...
    @classmethod
    def fromMechanicParams(cls, params, vehDescr):
        ...
    @property
    def modifiedShells(self):
        ...
    @property
    def activationTime(self):
        ...
    @property
    def shotReloadFactor(self):
        ...

# base nao representavel no stub: namedtuple(...)
class BustleFeedState(IMechanicState):
    def isTransition(self, other):
        ...
    def isSwitchState(self):
        ...
    @property
    def progress(self):
        ...
    @property
    def timeLeft(self):
        ...

class BustleFeedAmmoMode(DefaultAmmoMode):
    __mechanicState: Any
    __modifiedShells: Any
    def __init__(self, mechanicState, modifiedShells):
        ...
    @property
    def isActiveBustleFeed(self):
        ...
    @property
    def isBustleFeedReloadModifierActive(self):
        ...
    def getActiveMode(self):
        ...
    def getModifiedShells(self):
        ...
    def getShellMode(self, shellIntCD):
        ...
    def isBustleShotShell(self, shellIntCD):
        ...

class BustleFeedAmmoState(DefaultComponentAmmoState):
    __mechanicState: Any
    __ammoMode: Any
    __shotReloadFactor: Any
    def __init__(self, mechanicState, modifiedShells, shotReloadFactor):
        ...
    def canChangeVehicleSetting(self, code):
        ...
    def getAmmoMode(self):
        ...
    def getShellReloadTimes(self, currShell, shellChangeTime, shells):
        ...
    def __canChangeCurrentShell(self):
        ...
