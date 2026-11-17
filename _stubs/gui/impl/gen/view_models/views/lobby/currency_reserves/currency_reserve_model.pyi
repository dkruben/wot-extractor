# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/currency_reserves/currency_reserve_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class CurrencyEnum(Enum):
    CREDITS = 'Credits'
    GOLD = 'Gold'

class CurrencyReserveModel(ViewModel):
    __slots__: tuple
    onInfoButtonClick: Any
    onActionButtonClick: Any
    def __init__(self, properties=5, commands=2):
        ...
    def getCurrency(self):
        ...
    def setCurrency(self, value):
        ...
    def getMaxCapacity(self):
        ...
    def setMaxCapacity(self, value):
        ...
    def getAmount(self):
        ...
    def setAmount(self, value):
        ...
    def getIsActive(self):
        ...
    def setIsActive(self, value):
        ...
    def getIsEnabled(self):
        ...
    def setIsEnabled(self, value):
        ...
    def _initialize(self):
        ...
