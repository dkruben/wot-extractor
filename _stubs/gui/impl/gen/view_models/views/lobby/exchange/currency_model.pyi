# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/exchange/currency_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class CurrencyType(Enum):
    CREDITS = 'credits'
    GOLD = 'gold'
    CRYSTAL = 'crystal'
    FREEXP = 'freeXP'

class CurrencyModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getCurrencyType(self):
        ...
    def setCurrencyType(self, value):
        ...
    def getValue(self):
        ...
    def setValue(self, value):
        ...
    def getTooltipId(self):
        ...
    def setTooltipId(self, value):
        ...
    def _initialize(self):
        ...
