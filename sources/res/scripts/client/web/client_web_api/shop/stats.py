# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/web/client_web_api/shop/stats.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/web/client_web_api/shop/stats.py
from __future__ import absolute_import
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.game_control import IWalletController
from skeletons.gui.shared import IItemsCache
from web.client_web_api.api import C2WHandler, c2w
from web.common import formatWalletCurrencyStatuses, formatBalance

class BalanceEventHandler(C2WHandler):
    __walletController = dependency.descriptor(IWalletController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def init(self):
        super(BalanceEventHandler, self).init()
        self.__walletController.onWalletStatusChanged += self.__onWalletUpdate
        g_clientUpdateManager.addCallbacks({('stats.{}').format(c): self.__onBalanceUpdate for c in Currency.ALL})
        g_clientUpdateManager.addCallback('stats.freeXP', self.__onBalanceUpdate)
        g_clientUpdateManager.addCallbacks({'cache.dynamicCurrencies': (self.__onBalanceUpdate)})

    def fini(self):
        g_clientUpdateManager.removeObjectCallbacks(self, force=True)
        self.__walletController.onWalletStatusChanged -= self.__onWalletUpdate
        super(BalanceEventHandler, self).fini()

    @c2w(name='balance_update')
    def __onBalanceUpdate(self, *_):
        return formatBalance(self.__itemsCache.items.stats)

    @c2w(name='wallet_update')
    def __onWalletUpdate(self, *_):
        return formatWalletCurrencyStatuses(wallet=self.__walletController, itemsCache=self.__itemsCache)
