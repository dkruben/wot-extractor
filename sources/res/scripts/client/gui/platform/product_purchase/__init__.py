# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/platform/product_purchase/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/platform/product_purchase/__init__.py
import typing
from skeletons.gui.platform.product_purchase_controller import IWotShopPurchaseController
from gui.platform.product_purchase.wot_shop_purchase_controller import WotShopPurchaseController
if typing.TYPE_CHECKING:
    from helpers.dependency import DependencyManager
__all__ = ('getProductPurchaseControllers', )

def getProductPurchaseControllers(manager):
    wotShopController = WotShopPurchaseController()
    manager.addInstance(IWotShopPurchaseController, wotShopController)
