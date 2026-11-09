# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/exchange/exchange_rate_discount_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_model import ExchangeRateModel as ExchangeRateModel

class DiscountType(Enum):
    LIMITED = 'limited'
    UNLIMITED = 'unlimited'

class ShowFormat(Enum):
    COEFFICIENT = 'coefficient'
    INTEGER = 'integer'
    TEMPORARY = 'temporary'
    LIMITED = 'limited'

class ExchangeRateDiscountModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=7, commands=0):
        ...
    @property
    def exchangeRate(self):
        ...
    @staticmethod
    def getExchangeRateType():
        ...
    def getIsDiscountAvailable(self):
        ...
    def setIsDiscountAvailable(self, value):
        ...
    def getDiscountType(self):
        ...
    def setDiscountType(self, value):
        ...
    def getShowFormat(self):
        ...
    def setShowFormat(self, value):
        ...
    def getAmountOfDiscount(self):
        ...
    def setAmountOfDiscount(self, value):
        ...
    def getDiscountLifetime(self):
        ...
    def setDiscountLifetime(self, value):
        ...
    def getDiscountPercent(self):
        ...
    def setDiscountPercent(self, value):
        ...
    def _initialize(self):
        ...
