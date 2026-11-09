# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/cgf_components/bunkers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Union as Union
import CGF as CGF
from BunkerLogicComponent import BunkerLogicComponent as BunkerLogicComponent

class BunkersSystem(CGF.System):
    BunkerLogicActivated: Any
    BunkerLogicDeactivated: Any
    BunkerLogicIterate: Any
    Reactions: Any
    def update(self):
        ...
    def activeBunkersDirect(self):
        ...
    def findActiveBunkerDirect(self, entityID):
        ...
    def findActiveBunkerLink(self, entityID):
        ...
