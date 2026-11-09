# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/skeletons/gui/platform/product_fetch_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from skeletons.gui.platform.controller import IPlatformRequestController as IPlatformRequestController
from gui.platform.products_fetcher.fetch_result import FetchResult as FetchResult

class IProductFetchController(IPlatformRequestController):
    def reset(self):
        ...
    def getProducts(self, showWaiting=True, **kwargs):
        ...

class ISubscriptionProductsFetchController(IProductFetchController):
    ...

class IUserSubscriptionsFetchController(IPlatformRequestController):
    ...

class IWotShopFetchController(IProductFetchController):
    def getProducts(self, showWaiting=True, **kwargs):
        ...
