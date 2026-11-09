# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/ui/shop.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/ui/shop.py
from __future__ import absolute_import
from past.builtins import basestring
from gui.shared import event_dispatcher, g_eventBus, events
from gui.shared.event_dispatcher import hideWebBrowserOverlay
from web.web_client_api import w2c, W2CSchema, Field

class _OpenShopSchema(W2CSchema):
    path = Field(required=False, type=basestring)


class ShopWebApiMixin(object):

    @w2c(_OpenShopSchema, 'shop')
    def openShop(self, cmd):
        hideWebBrowserOverlay()
        event_dispatcher.showShop(path=cmd.path)

    @w2c(W2CSchema, 'premium_shop_external_browser')
    def openShopExternalBrowser(self, *_):
        g_eventBus.handleEvent(events.OpenLinkEvent(events.OpenLinkEvent.PREM_SHOP))
