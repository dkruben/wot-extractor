# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/feature/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
_logger: Any
UNAVAILABLE_REWARD_ERROR = 'UNAVAILABLE_REWARD_ERROR'
CHANNEL_NAME_PREFIX = 'suv_'
DEFAULT_SEASON_NUMBER = 0

class PurchaseMode(Enum):
    ONE_SERIAL_PRODUCT = 'ONE_SERIAL_PRODUCT'
    SEQUENTIAL_PRODUCT = 'SEQUENTIAL_PRODUCT'
    TWO_PARALLEL_PRODUCTS = 'TWO_PARALLEL_PRODUCTS'

class ResourceType(Enum):
    BLUEPRINTS = 'blueprints'
    CURRENCY = 'currency'
    @classmethod
    def getMember(cls, value):
        ...
