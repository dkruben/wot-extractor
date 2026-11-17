# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/components_states/ammo/states.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR as CANT_SHOOT_ERROR
from gui.battle_control.components_states.ammo.constants import AmmoShootPossibility as AmmoShootPossibility
from gui.battle_control.components_states.ammo.interfaces import IComponentAmmoState as IComponentAmmoState
from gui.battle_control.components_states.ammo.interfaces import IAmmoMode as IAmmoMode

class DefaultComponentAmmoState(IComponentAmmoState):
    def isReloadingBlocked(self):
        ...
    def canChangeVehicleSetting(self, code):
        ...
    def canShootValidation(self):
        ...
    def getShotsAmount(self):
        ...
    def getShootPossibility(self, currentShells):
        ...
    def getSpecialReloadMessage(self):
        ...
    def getAmmoMode(self):
        ...
    def getShellReloadTimes(self, currShell, shellChangeTime, shells):
        ...
