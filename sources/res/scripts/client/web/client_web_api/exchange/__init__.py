# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/client_web_api/exchange/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/exchange/__init__.py
from __future__ import absolute_import
from exchange.personal_discounts_constants import EXCHANGE_RATE_TYPES
from helpers import dependency
from skeletons.gui.game_control import IExchangeRatesWithDiscountsProvider
from web.client_web_api.api import C2WHandler, c2w

class PersonalExchangeRatesDiscountsEventHandler(C2WHandler):
    __exchangeRatesProvider = dependency.descriptor(IExchangeRatesWithDiscountsProvider)

    def init(self):
        super(PersonalExchangeRatesDiscountsEventHandler, self).init()
        for exchangeType in EXCHANGE_RATE_TYPES:
            self.__exchangeRatesProvider.get(exchangeType).onUpdated += self.__sendNotify

    def fini(self):
        for exchangeType in EXCHANGE_RATE_TYPES:
            self.__exchangeRatesProvider.get(exchangeType).onUpdated -= self.__sendNotify

        super(PersonalExchangeRatesDiscountsEventHandler, self).fini()

    @c2w(name='personal_exchange_rates_discounts_changed')
    def __sendNotify(self):
        return
