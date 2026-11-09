# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/InBattleUpgrades.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import BigWorld as BigWorld
import CGF as CGF
from aih_constants import CTRL_MODE_NAME as CTRL_MODE_NAME
from wotdecorators import noexcept as noexcept

class UpgradeInProgressComponent(object):
    ...

class InBattleUpgrades(BigWorld.DynamicScriptComponent):
    def onEnterWorld(self, *args):
        ...
    def onLeaveWorld(self, *args):
        ...
    def upgradeVehicle(self, indCD):
        ...
    def onVehicleUpgraded(self, newVehCompactDescr, newVehOutfitCompactDescr):
        ...
    # decorador original: @noexcept
    def __onVehicleUpgraded(self, vehicle, newVehCompactDescr, newVehOutfitCompactDescr):
        ...
    def testClientMethod(self):
        ...
    def set_upgradeReadinessTime(self, prev):
        ...

def onBattleRoyalePrerequisites(vehicle, oldTypeDescriptor, forceReloading):
    ...
