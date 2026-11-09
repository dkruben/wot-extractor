# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/exchange/personal_discounts_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from enum import Enum as Enum
EXCHANGE_RATE_GOLD_NAME = 'gold_exchange'
EXCHANGE_RATE_FREE_XP_NAME = 'experience_translation'
EXCHANGE_RATE_TYPES: tuple
MAX_DISCOUNT_VALUE = 2147483647
MAX_TIMESTAMP_VALUE = 9007199254740991
MAX_DISCOUNT_COEFFICIENT = 10
DIGITAL_TEMPLATE = '([1-9]\\d*((_|\\.)\\d+)?)'
EXCHANGE_NAME_TO_GAME_PARAM_NAME: dict
ExchangeRate: Any
ExchangeDiscountInfo: Any

class ExchangeDiscountType(Enum):
    LIMITED = 'limited'
    UNLIMITED = 'unlimited'

class ExchangeRateShowFormat(Enum):
    COEFFICIENT = 'coefficient'
    INTEGER = 'integer'
    TEMPORARY = 'temporary'
    LIMITED = 'limited'

class ExchangeRateCoefficientType(Enum):
    AMOUNT = 'increase'
    MULTIPLY = 'mul'

class ExchangeRateDiscountToken(Enum):
    LIMIT_TYPE = 'limit_type'
    SHOW_FORMAT = 'show_format'
    RATE_TYPE = 'rate_type'
    RATE_VALUE = 'change_on'
