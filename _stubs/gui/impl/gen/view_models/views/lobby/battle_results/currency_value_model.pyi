# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/currency_value_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel

class ValueModifiers(Enum):
    UNDEFINED = 'undefined'
    MUL = 'mul'
    ADD = 'add'
    SUB = 'sub'
    PROCENT = 'procent'
    SHOW_NEGATIVE_IMPACT = 'showNegativeImpact'

class CurrencyValueModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getCurrencyType(self):
        ...
    def setCurrencyType(self, value):
        ...
    def getValue(self):
        ...
    def setValue(self, value):
        ...
    def getIsShown(self):
        ...
    def setIsShown(self, value):
        ...
    def getModifiers(self):
        ...
    def setModifiers(self, value):
        ...
    @staticmethod
    def getModifiersType():
        ...
    def _initialize(self):
        ...
