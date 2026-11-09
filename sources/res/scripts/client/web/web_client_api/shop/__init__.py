# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/web_client_api/shop/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/web_client_api/shop/__init__.py
from __future__ import absolute_import
from web.web_client_api import w2capi
from web.web_client_api.shop.actions import ActionsWebApiMixin
from web.web_client_api.shop.boosters import BoostersInfoWebApiMixin
from web.web_client_api.shop.common import SettingsWebApiMixin
from web.web_client_api.shop.renewable_subscription import RenewableSubWebApiMixin
from web.web_client_api.shop.stats import BalanceWebApiMixin
from web.web_client_api.shop.stock import ItemsWebApiMixin
from web.web_client_api.shop.telecom_rentals import TelecomRentalsWebApiMixin
from web.web_client_api.shop.trade import TradeWebApiMixin
from web.web_client_api.shop.unified_trade_in import UnifiedTradeInWebApiMixin

@w2capi(name='shop', key='action')
class ShopWebApi(ActionsWebApiMixin, BalanceWebApiMixin, ItemsWebApiMixin, TradeWebApiMixin, UnifiedTradeInWebApiMixin, BoostersInfoWebApiMixin, RenewableSubWebApiMixin, TelecomRentalsWebApiMixin, SettingsWebApiMixin):
    pass
