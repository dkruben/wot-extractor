# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ArenaInfo.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from cgf_script.entity_dyn_components import BWEntitiyComponentTracker as BWEntitiyComponentTracker
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
ARENA_INFO_COMPONENTS: dict

class ArenaInfo(BigWorld.Entity, BWEntitiyComponentTracker):
    sessionProvider: Any
    def __init__(self):
        ...
    def set_planeTrajectory(self, _):
        ...
    def showCarpetBombing(self, equipmentID, position, hittingDirection, time):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
