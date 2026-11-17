# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/Comp7Lighting.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import AnimationSequence as AnimationSequence
import BigWorld as BigWorld
from enum import Enum as Enum
import math_utils as math_utils
_logger: Any

class Comp7LightingTriggers(Enum):
    DEFAULT = 'default_lighting'
    FLYBY = 'purchase_lighting'

class Comp7Lighting(BigWorld.Entity):
    __animator: Any
    def __init__(self):
        ...
    def prerequisites(self):
        ...
    def onEnterWorld(self, prereqs):
        ...
    def onLeaveWorld(self):
        ...
    def setTrigger(self, triggerName):
        ...
