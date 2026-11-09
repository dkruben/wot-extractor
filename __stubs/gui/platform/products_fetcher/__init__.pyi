# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.platform.products_fetcher.subscriptions.subscriptions_controller import SubscriptionProductsFetchController as SubscriptionProductsFetchController
from gui.platform.products_fetcher.user_subscriptions.controller import UserSubscriptionsFetchController as UserSubscriptionsFetchController
from gui.platform.products_fetcher.wot_shop.controller import WotShopFetcherController as WotShopFetcherController
from skeletons.gui.platform.product_fetch_controller import ISubscriptionProductsFetchController as ISubscriptionProductsFetchController, IUserSubscriptionsFetchController as IUserSubscriptionsFetchController, IWotShopFetchController as IWotShopFetchController
from helpers.dependency import DependencyManager as DependencyManager
__all__: tuple

def getProductFetchControllers(manager):
    ...
