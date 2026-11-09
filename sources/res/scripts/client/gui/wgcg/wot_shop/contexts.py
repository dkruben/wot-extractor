# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/wot_shop/contexts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/wot_shop/contexts.py
from gui.wgcg.base.contexts import CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType

class WotShopGetStorefrontProductsCtx(CommonWebRequestCtx):
    __slots__ = ('__storefront', )

    def __init__(self, ctx, waitingID=''):
        self.__storefront = ctx.storefront
        super(WotShopGetStorefrontProductsCtx, self).__init__(waitingID)

    def getRequestType(self):
        return WebRequestDataType.WOT_SHOP_GET_STOREFRONT_PRODUCTS

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getStorefront(self):
        return self.__storefront


class WotShopPurchaseStorefrontProductCtx(CommonWebRequestCtx):
    __slots__ = ('__storefront', '__productCode', '__expectedPrice')

    def __init__(self, storefront, productCode, expectedPrice, waitingID=''):
        self.__storefront = storefront
        self.__productCode = productCode
        self.__expectedPrice = expectedPrice
        super(WotShopPurchaseStorefrontProductCtx, self).__init__(waitingID)

    def getRequestType(self):
        return WebRequestDataType.WOT_SHOP_BUY_STOREFRONT_PRODUCT

    def isClanSyncRequired(self):
        return False

    def isCaching(self):
        return False

    def getStorefront(self):
        return self.__storefront

    def getProductCode(self):
        return self.__productCode

    def getExpectedPrice(self):
        return self.__expectedPrice
