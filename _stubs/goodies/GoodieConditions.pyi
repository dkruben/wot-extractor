# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/goodies/GoodieConditions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TypeVar as TypeVar
GoodieConditionType: Any

class Condition(object):
    __hash__ = None
    def check(self, other):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...

class MaxVehicleLevel(Condition):
    level: Any
    def __init__(self, level):
        ...
    def __lt__(self, other):
        ...
