# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/account_helpers/festivity_manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/account_helpers/festivity_manager.py
from __future__ import absolute_import
import logging
from functools import partial
import AccountCommands
from helpers import dependency
from shared_utils.account_helpers.diff_utils import synchronizeDicts
from skeletons.festivity_factory import IFestivityFactory
_logger = logging.getLogger()

class FestivityManager(object):
    _festivityFactory = dependency.descriptor(IFestivityFactory)

    def __init__(self, syncData, clientCommandsProxy):
        self.__syncData = syncData
        self.__cache = {}
        self.__ignore = True
        self.__festivityKey = self._festivityFactory.getRequester().dataKey
        self.__commandProxy = clientCommandsProxy

    def onAccountBecomePlayer(self):
        self._festivityFactory.getProcessor().setCommandProxy(self.__commandProxy)
        self.__ignore = False

    def onAccountBecomeNonPlayer(self):
        self._festivityFactory.getProcessor().setCommandProxy(None)
        self.__ignore = True
        return

    def synchronize(self, isFullSync, diff):
        if isFullSync:
            self.__cache.clear()
        itemDiff = diff.get(self.__festivityKey, None)
        _logger.debug('Syncing cache for key %s: %s', self.__festivityKey, itemDiff)
        if itemDiff is not None:
            synchronizeDicts(itemDiff, self.__cache.setdefault(self.__festivityKey, {}))
        return

    def getCache(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
        return

    def get(self, itemName, callback):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetResponse, itemName, callback))
        return

    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache)
        return

    def __onGetResponse(self, itemName, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache[self.__festivityKey].get(itemName, None))
        return
