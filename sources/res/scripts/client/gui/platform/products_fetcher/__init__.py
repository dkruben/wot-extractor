# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/platform/products_fetcher/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/products_fetcher/__init__.py
import typing
from gui.platform.products_fetcher.subscriptions.subscriptions_controller import SubscriptionProductsFetchController
from gui.platform.products_fetcher.user_subscriptions.controller import UserSubscriptionsFetchController
from gui.platform.products_fetcher.wot_shop.controller import WotShopFetcherController
from skeletons.gui.platform.product_fetch_controller import ISubscriptionProductsFetchController, IUserSubscriptionsFetchController, IWotShopFetchController
if typing.TYPE_CHECKING:
    from helpers.dependency import DependencyManager
__all__ = ('getProductFetchControllers', )

def getProductFetchControllers(manager):
    subscriptionsFetchController = SubscriptionProductsFetchController()
    subscriptionsFetchController.init()
    manager.addInstance(ISubscriptionProductsFetchController, subscriptionsFetchController, finalizer='fini')
    userSubscriptionsFetchController = UserSubscriptionsFetchController()
    userSubscriptionsFetchController.init()
    manager.addInstance(IUserSubscriptionsFetchController, userSubscriptionsFetchController, finalizer='fini')
    wotShopController = WotShopFetcherController()
    wotShopController.init()
    manager.addInstance(IWotShopFetchController, wotShopController, finalizer='fini')
