# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_reserves/disabled_category.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class CategoryType(Enum):
    PERSONAL = 'personal'
    CLAN = 'clan'
    EVENT = 'event'

class DisabledCategory(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getCategoryType(self):
        ...
    def setCategoryType(self, value):
        ...
    def getIsDisabled(self):
        ...
    def setIsDisabled(self, value):
        ...
    def _initialize(self):
        ...
