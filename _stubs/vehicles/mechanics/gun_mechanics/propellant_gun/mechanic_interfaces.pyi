# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/propellant_gun/mechanic_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from vehicles.mechanics.mechanic_states import IMechanicState as IMechanicState
from items.components.shared_components import PropellantGunParams as PropellantGunParams

class IPropellantGunComponentParams(object):
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

class IPropellantGunMechanicState(IMechanicState):
    @classmethod
    def fromComponentStatus(cls, status, params):
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
    def timeLeft(self):
        ...
    @property
    def isLastStage(self):
        ...
    @property
    def isUsableShell(self):
        ...
    @property
    def lastShotTimestamp(self):
        ...
    @property
    def lastShotCharge(self):
        ...
    def getCurrentDamageFactor(self, progress=None):
        ...
