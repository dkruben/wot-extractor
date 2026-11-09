# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/user_subscriptions/fetch_result.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.platform.products_fetcher.fetch_result import FetchResult as FetchResult, ResponseStatus as ResponseStatus

class UserSubscriptionFetchResult(FetchResult):
    _CACHE_TTL = 600
    status: Any
    products: Any
    def stop(self):
        ...
