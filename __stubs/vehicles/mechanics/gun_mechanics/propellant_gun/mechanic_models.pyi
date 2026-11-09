# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/propellant_gun/mechanic_models.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import BigWorld as BigWorld
from constants import PROPELLANT_GUN_STATE as PROPELLANT_GUN_STATE
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from math_utils import lerp as lerp
from vehicles.mechanics.gun_mechanics.propellant_gun.mechanic_interfaces import IPropellantGunComponentParams as IPropellantGunComponentParams, IPropellantGunMechanicState as IPropellantGunMechanicState
from items.components.shared_components import PropellantGunParams as PropellantGunParams

# decorador original: @ReprInjector.simple(...)
class PropellantGunComponentParams(IPropellantGunComponentParams):
    __chargePerSec: Any
    __dischargePerSec: Any
    __stages: Any
    __maxCharge: Any
    __maxOvercharge: Any
    __forbiddenShells: Any
    def __init__(self, chargePerSec, dischargePerSec, maxCharge, maxOvercharge, stages, forbiddenShells):
        ...
    @classmethod
    def fromMechanicParams(cls, params):
        ...
    @property
    def chargePerSec(self):
        ...
    @property
    def dischargePerSec(self):
        ...
    @property
    def maxCharge(self):
        ...
    @property
    def maxOvercharge(self):
        ...
    @property
    def stages(self):
        ...
    @property
    def forbiddenShells(self):
        ...

# decorador original: @ReprInjector.simple(...)
class PropellantGunMechanicState(IPropellantGunMechanicState):
    __state: Any
    __stageID: Any
    __chargeProgress: Any
    __isOvercharge: Any
    __isSwitchCooldownActive: Any
    __updateTime: Any
    __isForbiddenShell: Any
    __params: Any
    __overchargeStageCount: Any
    __lastShotTimestamp: Any
    __lastShotCharge: Any
    def __init__(self, state, stageID, chargeProgress, isOvercharge, isSwitchCooldownActive, updateTime, isForbiddenShell, lastShotTimestamp, lastShotCharge, params):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __hash__(self):
        ...
    @classmethod
    def fromComponentStatus(cls, status, params, isForbiddenShell=None):
        ...
    @property
    def lastShotTimestamp(self):
        ...
    @property
    def lastShotCharge(self):
        ...
    @property
    def state(self):
        ...
    @property
    def currentStage(self):
        ...
    @property
    def currentCharge(self):
        ...
    @property
    def currentThreshold(self):
        ...
    @property
    def isOvercharge(self):
        ...
    @property
    def isAvailable(self):
        ...
    @property
    def isMaxOverCharged(self):
        ...
    @property
    def isMaxCharged(self):
        ...
    @property
    def isLastStage(self):
        ...
    @property
    def isLastChargeStage(self):
        ...
    @property
    def isUsableShell(self):
        ...
    @property
    def timeLeft(self):
        ...
    def getCurrentDamageFactor(self, progress=None):
        ...
    def isTransition(self, other):
        ...
