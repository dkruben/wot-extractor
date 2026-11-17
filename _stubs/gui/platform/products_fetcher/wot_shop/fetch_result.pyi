# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/wot_shop/fetch_result.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from gui.platform.products_fetcher.fetch_result import FetchResult as FetchResult, ResponseStatus as ResponseStatus
ResponseData: Any

class WotShopFetchResult(FetchResult):
    __accountLimits: Any
    __categories: Any
    def __init__(self, status=...):
        ...
    def getAccountLimits(self):
        ...
    def setAccountLimits(self, accountLimits):
        ...
    def getCategories(self):
        ...
    def setCategories(self, categories):
        ...
    def getData(self):
        ...
    def stop(self):
        ...
