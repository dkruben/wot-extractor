# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/helpers/drr_scale.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
from math_common import decimal_round as decimal_round
DRR_MIN_SCALE_VALUE = 0.6
DRR_MAX_SCALE_VALUE = 1.0
DRR_MAX_STEP_VALUE = 0.05
DRR_EPSILON_VALUE: Any
PERCENT_MODIFIER = 100.0

def normalizeScale(value):
    ...
def getPercent(value):
    ...
def changeScaleByStep(offset):
    ...
def stepUp():
    ...
def stepDown():
    ...
