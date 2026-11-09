# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/utils/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/utils/handlers.py
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType

class UtilsRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.SPA_GET_ACCOUNT_ATTRIBUTE): (self.__getAccountAttributeByPrefix), 
           (WebRequestDataType.PLATFORM_FETCH_PRODUCT_LIST): (self.__fetchProductList), 
           (WebRequestDataType.PLATFORM_GET_USER_SUBSCRIPTIONS): (self.__getUserSubscriptions)}
        return handlers

    def __getAccountAttributeByPrefix(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('spa', 'get_account_attribute_by_prefix'), ctx.getRequestedAttr())

    def __fetchProductList(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('agate', 'agate_v4_fetch_product_list_state'), ctx.getParams())

    def __getUserSubscriptions(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('agate', 'agate_v6_get_user_subscriptions3'), ctx.getParams())
