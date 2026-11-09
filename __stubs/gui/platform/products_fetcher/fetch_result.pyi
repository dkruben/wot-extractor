# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/fetch_result.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
import BigWorld as BigWorld
from constants import SECONDS_IN_DAY as SECONDS_IN_DAY

class ResponseStatus(Enum):
    UNDEFINED = 0
    PROCESSED = 1
    FAILED = 2
    FAILED_BY_TIMEOUT = 3

class FetchResult(object):
    _CACHE_TTL = SECONDS_IN_DAY
    status: Any
    products: Any
    __timerTTL: Any
    def __init__(self, status=...):
        ...
    @property
    def isUndefined(self):
        ...
    @property
    def isProcessed(self):
        ...
    @property
    def isFailed(self):
        ...
    @property
    def isFailedByTimeout(self):
        ...
    @property
    def isProductsReady(self):
        ...
    def getProducts(self):
        ...
    def setProducts(self, products):
        ...
    def reset(self):
        ...
    def stop(self):
        ...
    def setProcessed(self):
        ...
    def setFailed(self):
        ...
    def setFailedByTimeout(self):
        ...
    def getProductByID(self, productID):
        ...
    def _isStatus(self, status):
        ...
    def __onTTLTimer(self):
        ...
    def _clearTimeoutBwCbId(self):
        ...
