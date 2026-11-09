# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/math_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from decimal import ROUND_HALF_UP as ROUND_HALF_UP, Decimal as Decimal
from math import ceil as ceil, floor as floor
from future.utils import PY3 as PY3
from typing import Union as Union
_CEIL_EPS = 1

def ceilTo(num, decimals=0, epsilon=0.0004):
    ...
def isAlmostEqual(first, second, epsilon=0.0004):
    ...
def almostZero(val, epsilon=0.0004):
    ...
def trim(v, min, max):
    ...
def round_py2_style(number):
    ...
def round_py2_style_int(number):
    ...
def decimal_round(number, precision=0, rounding=...):
    ...
