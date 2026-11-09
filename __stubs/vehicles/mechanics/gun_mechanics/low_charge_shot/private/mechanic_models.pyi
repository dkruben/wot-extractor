# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/private/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import LowChargeShotReloadingState as LowChargeShotReloadingState
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR as CANT_SHOOT_ERROR
from gui.battle_control.components_states.ammo import DefaultComponentAmmoState as DefaultComponentAmmoState, AmmoShootPossibility as AmmoShootPossibility
from gui.battle_control.components_states.ammo.constants import ShellMode as ShellMode
from gui.battle_control.components_states.ammo.shells import DefaultAmmoMode as DefaultAmmoMode
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState
from gui.battle_control.components_states.ammo.interfaces import IAmmoMode as IAmmoMode

# base nao representavel no stub: typing.NamedTuple(...)
# decorador original: @ReprInjector.simple(...)
class LowChargeShotMechanicState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status, params):
        ...
    @property
    def duration(self):
        ...
    def isTransition(self, other):
        ...
    def calculateTimeLeft(self):
        ...

class LowChargeShotAmmoMode(DefaultAmmoMode):
    def getShellMode(self, shellIntCD):
        ...

class LowChargeShotAmmoState(DefaultComponentAmmoState):
    __mechanicState: Any
    __ammoMode: Any
    def __init__(self, mechanicState):
        ...
    def canShootValidation(self):
        ...
    def getShootPossibility(self, currentShells):
        ...
    def getAmmoMode(self):
        ...
