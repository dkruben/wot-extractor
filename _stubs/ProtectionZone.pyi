# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ProtectionZone.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Math as Math
from debug_utils import LOG_DEBUG as LOG_DEBUG

class ProtectionZone(BigWorld.Entity):
    __lowerLeft: Any
    __upperRight: Any
    def __init__(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def set_isActive(self, oldValue):
        ...
    @property
    def bound(self):
        ...
