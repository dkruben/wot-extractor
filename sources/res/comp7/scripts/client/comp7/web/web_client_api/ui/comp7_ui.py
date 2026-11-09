# wot-extractor: codigo DESCOMPILADO de sources/res/comp7/scripts/client/comp7/web/web_client_api/ui/comp7_ui.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7/scripts/client/comp7/web/web_client_api/ui/comp7_ui.py
from __future__ import absolute_import
from account_helpers import AccountSettings
from account_helpers.AccountSettings import NEW_SHOP_TABS, IS_COMP7_BONS_BANNER_VISITED
from comp7.gui.shared import event_dispatcher as comp7_events
from web.web_client_api import w2c, W2CSchema

class OpenComp7Mixin(object):

    @w2c(W2CSchema, name='open_comp7_page')
    def openComp7Page(self, _):
        comp7_events.showComp7ShopPage()

    @w2c(W2CSchema, name='set_is_comp7_bons_banner_visited')
    def setIsComp7BonsBannerVisited(self, _):
        newShopTabsCounter = AccountSettings.getCounters(NEW_SHOP_TABS)
        newShopTabsCounter.update({IS_COMP7_BONS_BANNER_VISITED: True})
        AccountSettings.setCounters(NEW_SHOP_TABS, newShopTabsCounter)
