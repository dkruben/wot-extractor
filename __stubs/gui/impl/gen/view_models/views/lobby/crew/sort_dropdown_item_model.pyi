# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/sort_dropdown_item_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel

class SortingTypeEnum(IntEnum):
    DEFAULT = 0
    COMMON = 1
    LEGENDARY = 2

class SortDropdownItemModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getIsSelected(self):
        ...
    def setIsSelected(self, value):
        ...
    def getIsEnabled(self):
        ...
    def setIsEnabled(self, value):
        ...
    def getMType(self):
        ...
    def setMType(self, value):
        ...
    def _initialize(self):
        ...
