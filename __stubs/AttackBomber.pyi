# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/AttackBomber.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
import BigWorld as BigWorld
import Math as Math
from AreaOfEffect import AreaOfEffect as AreaOfEffect
from constants import SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from items import vehicles as vehicles

class AttackBomber(AreaOfEffect):
    SKIP_FLAGS = 18
    STRIKE_LINES: tuple
    LINE_WIDTH = 5.0
    _attackCallbackId: Any
    def __init__(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def _carpetBombing(self):
        ...
