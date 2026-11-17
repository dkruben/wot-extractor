# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/dialogs/sub_views/currency_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class CurrencySize(Enum):
    SMALL = 'small'
    BIG = 'big'
    LARGE = 'large'

class CurrencyType(Enum):
    CREDITS = 'credits'
    GOLD = 'gold'
    CRYSTAL = 'crystal'
    XP = 'xp'
    FREEXP = 'freeXP'
    EQUIPCOIN = 'equipCoin'
    ELITEXP = 'eliteXP'

class CurrencyViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=7, commands=0):
        ...
    def getValue(self):
        ...
    def setValue(self, value):
        ...
    def getIsEnough(self):
        ...
    def setIsEnough(self, value):
        ...
    def getIsDiscount(self):
        ...
    def setIsDiscount(self, value):
        ...
    def getDiscountValue(self):
        ...
    def setDiscountValue(self, value):
        ...
    def getShowPlus(self):
        ...
    def setShowPlus(self, value):
        ...
    def getSize(self):
        ...
    def setSize(self, value):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def _initialize(self):
        ...
