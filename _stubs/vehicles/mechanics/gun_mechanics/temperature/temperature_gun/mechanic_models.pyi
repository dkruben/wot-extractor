# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/temperature/temperature_gun/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import TEMPERATURE_GUN_STATE as TEMPERATURE_GUN_STATE
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from vehicles.mechanics.gun_mechanics.temperature.common import TemperatureComponentParams as TemperatureComponentParams, TemperatureMechanicState as TemperatureMechanicState
from vehicles.mechanics.gun_mechanics.temperature.temperature_gun.mechanic_interfaces import ITemperatureGunComponentParamsLogic as ITemperatureGunComponentParamsLogic, ITemperatureGunMechanicStateLogic as ITemperatureGunMechanicStateLogic
from items.components.shared_components import TemperatureGunParams as TemperatureGunParams

# decorador original: @ReprInjector.withParent(...)
class TemperatureGunComponentParams(TemperatureComponentParams, ITemperatureGunComponentParamsLogic):
    __coolingDelay: Any
    def __init__(self, maxTemperature, coolingPerSec, coolingDelay):
        ...
    @classmethod
    def fromMechanicParams(cls, params):
        ...
    @property
    def coolingDelay(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class TemperatureGunMechanicState(TemperatureMechanicState, ITemperatureGunMechanicStateLogic):
    @classmethod
    def fromComponentStatus(cls, status, params):
        ...
    def getCoolingTime(self, targetTemperature):
        ...

class TemperatureGunAmmoState(DefaultComponentAmmoState):
    __mechanicState: Any
    def __init__(self, mechanicState):
        ...
    @property
    def mechanicState(self):
        ...
