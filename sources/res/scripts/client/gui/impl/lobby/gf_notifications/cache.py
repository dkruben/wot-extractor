# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/gf_notifications/cache.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/gf_notifications/cache.py
import typing
from wotdecorators import singleton

def getCache():
    return GFNotificationsCache


class IGFNotificationsCache(object):
    __slots__ = ('__data', )

    def setPayload(self, id, payload):
        raise NotImplementedError

    def getPayload(self, id):
        raise NotImplementedError

    def clear(self):
        raise NotImplementedError


@singleton
class GFNotificationsCache(IGFNotificationsCache):

    def __init__(self):
        self.__data = {}

    def setPayload(self, id, payload):
        self.__data[id] = payload

    def getPayload(self, id):
        return self.__data.get(id, {})

    def clear(self):
        self.__data.clear()
