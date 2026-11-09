# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/wot_shop/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from BWUtil import AsyncReturn as AsyncReturn
from helpers import dependency as dependency
from skeletons.gui.platform.product_fetch_controller import IWotShopFetchController as IWotShopFetchController
from skeletons.gui.platform.product_purchase_controller import IWotShopPurchaseController as IWotShopPurchaseController
from wg_async import wg_async as wg_async, wg_await as wg_await
from gui.platform.products_fetcher.wot_shop.fetch_result import WotShopFetchResult as WotShopFetchResult
_logger: Any

class IShopController(object):
    def fetchProducts(self, storefront, forceFetch=False):
        ...
    def buyProduct(self, storefront, code):
        ...
    def fini(self):
        ...

class IWotShopController(IShopController):
    ...

class WotShopController(IWotShopController):
    __wotShopFetchController: Any
    __wotShopPurchaseController: Any
    # decorador original: @wg_async
    def fetchProducts(self, storefront, forceFetch=False):
        ...
    # decorador original: @wg_async
    def buyProduct(self, storefront, code, expectedPrice):
        ...
    def fini(self):
        ...
