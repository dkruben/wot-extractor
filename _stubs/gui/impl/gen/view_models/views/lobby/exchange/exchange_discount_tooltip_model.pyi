# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/exchange/exchange_discount_tooltip_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_model import ExchangeRateModel as ExchangeRateModel

class CurrencyType(Enum):
    CREDITS = 'credits'
    GOLD = 'gold'
    FREEXP = 'freeXP'

class ExchangeDiscountTooltipModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=6, commands=0):
        ...
    @property
    def defaultExchangeRate(self):
        ...
    @staticmethod
    def getDefaultExchangeRateType():
        ...
    @property
    def commonExchangeRate(self):
        ...
    @staticmethod
    def getCommonExchangeRateType():
        ...
    @property
    def personalExchangeRate(self):
        ...
    @staticmethod
    def getPersonalExchangeRateType():
        ...
    def getIsTemporary(self):
        ...
    def setIsTemporary(self, value):
        ...
    def getCurrencyTypeFrom(self):
        ...
    def setCurrencyTypeFrom(self, value):
        ...
    def getCurrencyTypeTo(self):
        ...
    def setCurrencyTypeTo(self, value):
        ...
    def _initialize(self):
        ...
