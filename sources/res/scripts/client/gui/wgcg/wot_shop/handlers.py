# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/wot_shop/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/wot_shop/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class WotShopRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.WOT_SHOP_GET_STOREFRONT_PRODUCTS): (self.__getStorefrontProducts), 
           (WebRequestDataType.WOT_SHOP_BUY_STOREFRONT_PRODUCT): (self.__buyStorefrontProduct)}
        return handlers

    def __getStorefrontProducts(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('wot_shop', 'get_storefront_products'), ctx)

    def __buyStorefrontProduct(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('wot_shop', 'buy_storefront_product'), ctx)
