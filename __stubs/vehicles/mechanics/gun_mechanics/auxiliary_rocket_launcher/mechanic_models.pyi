# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/auxiliary_rocket_launcher/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
from constants import SECONDARY_GUN_STATE as SECONDARY_GUN_STATE
from gui.battle_control.components_states.ammo import ActiveAmmoMode as ActiveAmmoMode, DefaultAmmoMode as DefaultAmmoMode, DefaultComponentAmmoState as DefaultComponentAmmoState, ShellMode as ShellMode
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState
from gui.battle_control.components_states.ammo.interfaces import IAmmoMode as IAmmoMode

# base nao representavel no stub: namedtuple(...)
class AuxiliaryRocketLauncherState(IMechanicState):
    @property
    def progress(self):
        ...
    @property
    def timeLeft(self):
        ...
    def isTransition(self, other):
        ...
    def isValidForAimingMode(self):
        ...

class AuxiliaryRocketLauncherAmmoMode(DefaultAmmoMode):
    __isInAimingMode: Any
    def __init__(self, isInAimingMode):
        ...
    def getActiveMode(self):
        ...
    def getShellMode(self, shellIntCD):
        ...

class AuxiliaryRocketLauncherAmmoState(DefaultComponentAmmoState):
    __ammoMode: Any
    def __init__(self, isInAimingMode):
        ...
    def getAmmoMode(self):
        ...
