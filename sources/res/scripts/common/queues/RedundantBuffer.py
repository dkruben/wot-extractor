# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/queues/RedundantBuffer.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/queues/RedundantBuffer.py
from __future__ import absolute_import
import collections
from itertools import chain

class RedundantBuffer(object):

    def __init__(self, redundancy, callback=None, limit=None):
        self.__cache = collections.deque()
        self.__redundancy = redundancy
        self.__callback = callback
        self.__limit = limit

    def __repr__(self):
        return str(self.__cache)

    def snapshot(self):
        return list(chain.from_iterable(self.__cache))

    def flush(self):
        if not self.__cache:
            result = []
        else:
            result = self.snapshot()
            self.__cache.appendleft([])
            if len(self.__cache) > self.__redundancy:
                self.__cache.pop()
        if self.__callback is not None:
            self.__callback(result)
        return result

    def fini(self):
        for _ in range(0, self.__redundancy):
            self.flush()

    def add(self, value):
        if not self.__cache:
            self.__cache.appendleft([value])
            return
        else:
            if self.__limit is not None and len(self.__cache[0]) >= self.__limit:
                self.flush()
            self.__cache[0].append(value)
            return

    def clear(self):
        self.__cache.clear()
