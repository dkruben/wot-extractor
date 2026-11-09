# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/wgcg/promo_screens/handlers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/wgcg/promo_screens/handlers.py
from typing import TYPE_CHECKING
from gui.wgcg.base.handlers import RequestHandlers
from gui.wgcg.settings import WebRequestDataType
if TYPE_CHECKING:
    from gui.wgcg.promo_screens.contexts import PromoGetTeaserRequestCtx, PromoSendTeaserShownRequestCtx, PromoGetUnreadCountRequestCtx, PromoSendActionLogCtx
    from typing import Callable

class PromoScreensRequestHandlers(RequestHandlers):

    def get(self):
        handlers = {(WebRequestDataType.PROMO_GET_TEASER): (self.__getTeaser), 
           (WebRequestDataType.PROMO_TEASER_SHOWN): (self.__sendShownTeaser), 
           (WebRequestDataType.PROMO_GET_UNREAD): (self.__getUnreadCount), 
           (WebRequestDataType.PROMO_SEND_LOG): (self.__sendActionLog)}
        return handlers

    def __getTeaser(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('promo_screens', 'get_teaser'), **ctx.getAdditionalData())

    def __sendShownTeaser(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('promo_screens', 'send_teaser'), ctx.getPromoID(), **ctx.getAdditionalData())

    def __getUnreadCount(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('promo_screens', 'get_unread_count'), **ctx.getAdditionalData())

    def __sendActionLog(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, ('promo_screens', 'client_promo_log'), ctx.getActionData())
