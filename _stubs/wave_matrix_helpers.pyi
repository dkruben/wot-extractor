# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/common/wave_matrix_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import heapq as heapq
import random as random
from future.utils import lrange as lrange
from math import sqrt as sqrt
from death_zones_helpers import zoneIdFrom as zoneIdFrom, idxFrom as idxFrom, getZoneCenterFromIdFor as getZoneCenterFromIdFor
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from math_common import decimal_round as decimal_round

class WaveMatrix(object):
    size: Any
    _grid: Any
    def __init__(self, size):
        ...
    def setValue(self, x, y, value):
        ...
    def getValue(self, x, y):
        ...
    def validate(self, x, y):
        ...
    def fillWave(self, fromX, fromY, weight):
        ...
    def dump(self):
        ...
    def appendWave(self, centerX, centerY, matrix, sign=1):
        ...
    def randomSafeCell(self):
        ...
    def randomNSafeCells(self, arenaTypeID, cellCount):
        ...

def createCenterWaweMatrix(weight):
    ...
