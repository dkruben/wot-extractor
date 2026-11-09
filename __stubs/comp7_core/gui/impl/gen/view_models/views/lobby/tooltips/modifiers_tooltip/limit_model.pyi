# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_core/scripts/client/comp7_core/gui/impl/gen/view_models/views/lobby/tooltips/modifiers_tooltip/limit_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class LimitType(Enum):
    MIN = 'min'
    MAX = 'max'

class LimitModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getLimitType(self):
        ...
    def setLimitType(self, value):
        ...
    def getValue(self):
        ...
    def setValue(self, value):
        ...
    def _initialize(self):
        ...
