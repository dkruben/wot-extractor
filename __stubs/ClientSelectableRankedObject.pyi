# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ClientSelectableRankedObject.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from ClientSelectableObject import ClientSelectableObject as ClientSelectableObject
from helpers import dependency as dependency
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController

class ClientSelectableRankedObject(ClientSelectableObject):
    __rankedController: Any
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def onMouseClick(self):
        ...
    def __onGameModeStatusUpdate(self, *_):
        ...
