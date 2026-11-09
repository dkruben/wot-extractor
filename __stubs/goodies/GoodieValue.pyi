# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/goodies/GoodieValue.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from soft_exception import SoftException as SoftException
from math import floor as floor
from typing import TypeVar as TypeVar
from math_common import round_py2_style_int as round_py2_style_int
GoodieValueType: Any

class GoodieValue(object):
    __slots__: list
    __hash__ = None
    isAbsolute: Any
    value: Any
    def __init__(self, value, isAbsolute=True):
        ...
    def __lt__(self, other):
        ...
    def __gt__(self, other):
        ...
    def __eq__(self, other):
        ...
    @staticmethod
    def percent(value):
        ...
    @staticmethod
    def absolute(value):
        ...
    def increase(self, x):
        ...
    def reduce(self, x):
        ...
    def delta(self, x):
        ...
