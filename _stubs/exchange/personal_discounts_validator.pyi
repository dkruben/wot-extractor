# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/exchange/personal_discounts_validator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from exchange.personal_discounts_constants import ExchangeDiscountType as ExchangeDiscountType, EXCHANGE_RATE_GOLD_NAME as EXCHANGE_RATE_GOLD_NAME, MAX_DISCOUNT_COEFFICIENT as MAX_DISCOUNT_COEFFICIENT, MAX_TIMESTAMP_VALUE as MAX_TIMESTAMP_VALUE, MAX_DISCOUNT_VALUE as MAX_DISCOUNT_VALUE, ExchangeDiscountInfo as ExchangeDiscountInfo, ExchangeRate as ExchangeRate, ExchangeRateShowFormat as ExchangeRateShowFormat

class BaseExchangeValidator(object):
    _maxRateMultiplier = MAX_DISCOUNT_COEFFICIENT
    _maxDiscountValue = MAX_DISCOUNT_VALUE
    _maxLifetime = MAX_TIMESTAMP_VALUE
    _minDiscountRate = 1
    discount: Any
    defaultCourse: Any
    def __init__(self, discount, defaultCourse):
        ...
    def isValid(self):
        ...
    @property
    def isValidDiscountLifetime(self):
        ...
    @property
    def isValidDiscountAmount(self):
        ...
    @property
    def isValidDiscountRates(self):
        ...
    @property
    def _isDynamicCoefficientCorrect(self):
        ...
    @property
    def _isStaticCoefficientCorrect(self):
        ...
    @property
    def _isUnLimited(self):
        ...
    @property
    def _isDiscountAmountCorrect(self):
        ...
    @property
    def dynamicCoefficient(self):
        ...
    @property
    def staticCoefficient(self):
        ...
    @property
    def defaultDynamicCoefficient(self):
        ...
    @property
    def defaultStaticCoefficient(self):
        ...
    @property
    def maxDiscountVal(self):
        ...
    @property
    def isValidShowFormat(self):
        ...

class GoldExchangeValidator(BaseExchangeValidator):
    _minDiscountRate = 1.01

class XpExchangeValidator(BaseExchangeValidator):
    _minDiscountRate = 1.04

def isDiscountValuesCorrect(discount, defaultGoldRateValue, defaultResourceRateValue):
    ...
