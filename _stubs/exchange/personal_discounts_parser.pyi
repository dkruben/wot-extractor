# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/exchange/personal_discounts_parser.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import re as re
from backports.functools_lru_cache import lru_cache as lru_cache
import typing as typing
from exchange.personal_discounts_constants import EXCHANGE_RATE_GOLD_NAME as EXCHANGE_RATE_GOLD_NAME, ExchangeRateCoefficientType as ExchangeRateCoefficientType, ExchangeDiscountInfo as ExchangeDiscountInfo, ExchangeDiscountType as ExchangeDiscountType, ExchangeRateShowFormat as ExchangeRateShowFormat, ExchangeRateDiscountToken as ExchangeRateDiscountToken, EXCHANGE_RATE_FREE_XP_NAME as EXCHANGE_RATE_FREE_XP_NAME, DIGITAL_TEMPLATE as DIGITAL_TEMPLATE
from exchange.personal_discounts_helper import isExchangeRateDiscountAvailable as isExchangeRateDiscountAvailable
from exchange.personal_discounts_validator import isDiscountValuesCorrect as isDiscountValuesCorrect
from math_common import decimal_round as decimal_round
from typing import Tuple as Tuple, Dict as Dict, Union as Union, List as List, Optional as Optional, Any as Any
_logger: _Any

def convertTokensToExchangeDiscounts(tokens, defCourse, currentTime):
    ...
def _getDiscountFromTokensInfo(tokenName, tokenInfo, defaultGoldRateValue, defaultResourceRateValue, currentTime):
    ...
# decorador original: @lru_cache(...)
def __getTokenPattern(isLimited=False):
    ...
def _parseToken(tokenName):
    ...
def _calculateDiscountRate(parsedToken, defaultGoldRateValue, defaultResourceRateValue):
    ...
def _updateDiscountLimit(tokenInfo):
    ...
def _createDiscountInfoFromDict(tokenInfo):
    ...
