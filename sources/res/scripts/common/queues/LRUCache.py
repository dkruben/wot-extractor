# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/queues/LRUCache.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/queues/LRUCache.py
from __future__ import absolute_import
import collections

class LRUCache(object):

    def __init__(self, limit):
        self.__cache = collections.OrderedDict()
        self.__limit = limit

    def get(self, key):
        try:
            value = self.__cache.pop(key)
            self.__cache[key] = value
            return value
        except KeyError:
            return

        return

    def peek(self, key):
        return self.__cache.get(key, None)

    def set(self, key, value):
        try:
            self.__cache.pop(key)
        except KeyError:
            if len(self.__cache) >= self.__limit:
                self.__cache.popitem(last=False)

        self.__cache[key] = value

    def pop(self, key):
        return self.__cache.pop(key, None)

    def clear(self):
        self.__cache.clear()
