# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/avatar_components/vehicle_removal_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from helpers import uniprof as uniprof

class VehicleRemovalController(object):
    sessionProvider: Any
    def onBecomePlayer(self):
        ...
    def handleKey(self, isDown, key, mods):
        ...
    def onBecomeNonPlayer(self):
        ...
    # decorador original: @uniprof.regionDecorator(...)
    def removeVehicle(self, vehID):
        ...
