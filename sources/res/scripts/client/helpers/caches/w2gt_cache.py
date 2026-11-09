# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/caches/w2gt_cache.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/caches/w2gt_cache.py
from __future__ import absolute_import
from helpers.local_cache import FileLocalCache

class W2gtCache(FileLocalCache):
    _VERSION = 1
    _PROGRESS = 'progress'

    def __init__(self):
        super(W2gtCache, self).__init__('w2gt_cache', ('w2gt_tips', W2gtCache._VERSION), isAsync=False)
        self.__cache = {}
        self.__cachedRequests = set()

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.__cache[key] = data

    def saveProgress(self, arenaUniqueID, playerID, data):
        self.__cache[self._PROGRESS] = {playerID: {arenaUniqueID: data}}

    def getProgress(self, arenaUniqueID, playerID):
        return self.get(self._PROGRESS, {}).get(playerID, {}).get(arenaUniqueID, {})

    def saveRequest(self, key):
        self.__cachedRequests.add(key)

    def isRequestSaved(self, key):
        return key in self.__cachedRequests

    def getData(self):
        return self.__cache

    def clear(self):
        self.__cache = None
        self.__cachedRequests = None
        super(W2gtCache, self).clear()
        return

    def get(self, key, default=None):
        return self.__cache.get(key, default)

    def _getCache(self):
        return self.__cache

    def _setCache(self, data):
        if isinstance(data, dict):
            self.__cache = data
