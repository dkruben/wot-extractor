# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/wot_shop/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.platform.products_fetcher.controller import ProductsFetchController as ProductsFetchController
from gui.platform.products_fetcher.wot_shop.descriptors.account_limits_descriptor import AccountLimitsDescriptor as AccountLimitsDescriptor
from gui.platform.products_fetcher.wot_shop.descriptors.categories_descriptor import CategoriesDescriptor as CategoriesDescriptor
from gui.platform.products_fetcher.wot_shop.descriptors.product_descriptor import ProductDescriptor as ProductDescriptor
from gui.platform.products_fetcher.wot_shop.fetch_result import WotShopFetchResult as WotShopFetchResult
from gui.wgcg.wot_shop.contexts import WotShopGetStorefrontProductsCtx as WotShopGetStorefrontProductsCtx
from skeletons.gui.platform.product_fetch_controller import IWotShopFetchController as IWotShopFetchController
_logger: Any

class WotShopFetcherController(ProductsFetchController, IWotShopFetchController):
    platformFetchCtx = WotShopGetStorefrontProductsCtx
    productDescriptor = ProductDescriptor
    accountLimitsDescriptor = AccountLimitsDescriptor
    categoriesDescriptor = CategoriesDescriptor
    dataGetKey = 'data'
    downloadRequired = False
    @property
    def _fetchResultType(self):
        ...
    def _createDescriptors(self, data):
        ...
    def getProducts(self, showWaiting=True, **kwargs):
        ...
