# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/overheat_gun/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import typing as typing
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from constants import OVERHEAT_GUN_STATE as OVERHEAT_GUN_STATE
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR as CANT_SHOOT_ERROR
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from helpers import dependency as dependency
from messenger_common_chat2 import messageArgs as messageArgs
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from vehicles.mechanics.gun_mechanics.temperature.overheat_gun.mechanic_interfaces import IOverheatGunComponentParams as IOverheatGunComponentParams, IOverheatGunMechanicState as IOverheatGunMechanicState
from items.components.shared_components import OverheatGunParams as OverheatGunParams
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun import ITemperatureGunMechanicState as ITemperatureGunMechanicState

# decorador original: @ReprInjector.simple(...)
class OverheatGunComponentParams(IOverheatGunComponentParams):
    __overheatWarnPercent: Any
    __overheatOffPercent: Any
    __overheatOffThreshold: Any
    def __init__(self, overheatWarnPercent, overheatOffPercent, overheatOffThreshold):
        ...
    @classmethod
    def fromMechanicParams(cls, params):
        ...
    @property
    def overheatWarnPercent(self):
        ...
    @property
    def overheatOffPercent(self):
        ...
    @property
    def overheatOffThreshold(self):
        ...

# decorador original: @ReprInjector.simple(...)
class OverheatGunMechanicState(IOverheatGunMechanicState):
    __overheatState: Any
    __params: Any
    def __init__(self, overheatState, params):
        ...
    @classmethod
    def fromComponentStatus(cls, overheatState, params):
        ...
    @property
    def isOverheated(self):
        ...
    @property
    def overheatState(self):
        ...
    def isTransition(self, other):
        ...
    def overheatTimeLeft(self, temperatureGunState):
        ...

class OverheatGunAmmoState(DefaultComponentAmmoState):
    __sessionProvider: Any
    __mechanicState: Any
    def __init__(self, mechanicState):
        ...
    def canShootValidation(self):
        ...
    def getSpecialReloadMessage(self):
        ...
