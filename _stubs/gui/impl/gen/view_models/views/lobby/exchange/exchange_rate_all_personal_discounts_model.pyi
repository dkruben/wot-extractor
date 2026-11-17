# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/exchange/exchange_rate_all_personal_discounts_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.exchange.discount_presentation import DiscountPresentation as DiscountPresentation
from gui.impl.gen.view_models.views.lobby.exchange.exchange_rate_model import ExchangeRateModel as ExchangeRateModel

class CurrencyType(Enum):
    CREDITS = 'credits'
    GOLD = 'gold'
    FREEXP = 'freeXP'

class ExchangeRateAllPersonalDiscountsModel(ViewModel):
    __slots__: tuple
    onClose: Any
    def __init__(self, properties=6, commands=1):
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
    def getCurrencyTypeFrom(self):
        ...
    def setCurrencyTypeFrom(self, value):
        ...
    def getCurrencyTypeTo(self):
        ...
    def setCurrencyTypeTo(self, value):
        ...
    def getAllDiscountsLimitsAmount(self):
        ...
    def setAllDiscountsLimitsAmount(self, value):
        ...
    def getDiscounts(self):
        ...
    def setDiscounts(self, value):
        ...
    @staticmethod
    def getDiscountsType():
        ...
    def _initialize(self):
        ...
