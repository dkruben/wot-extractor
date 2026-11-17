# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/TeamInfo.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider

class TeamInfo(BigWorld.Entity):
    __sessionProvider: Any
    def onCombatEquipmentUsed(self, vehicleID, equipmentID):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def onDynamicComponentCreated(self, component):
        ...
    def showHittingArea(self, equipmentID, hittingPoint, hittingDirection, hittingTime):
        ...
