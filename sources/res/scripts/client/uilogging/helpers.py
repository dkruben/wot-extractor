# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/uilogging/helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/uilogging/helpers.py
from __future__ import absolute_import
import typing, BigWorld
if typing.TYPE_CHECKING:
    from uilogging.base.logger import LOGGERS_TYPING

class _LazyLoggerDescriptor(object):
    __slots__ = ('__class', '__args', '__kwargs', '__instance')

    def __init__(self, class_, *args, **kwargs):
        self.__class = class_
        self.__args = args
        self.__kwargs = kwargs
        self.__instance = None
        return

    def __set__(self, *_, **__):
        raise AttributeError('% is readonly' % self.__class__.__name__)

    def __get__(self, *_, **__):
        if not self.__instance:
            self.__instance = self.__class(*self.__args, **self.__kwargs)
        return self.__instance


def lazyUILogger(class_, *args, **kwargs):
    return _LazyLoggerDescriptor(class_, *args, **kwargs)


def getClientSessionID():
    if BigWorld.player() is None:
        return ''
    else:
        return str(BigWorld.player().connectionMgr.lastSessionID)


def getClientPeripheryID():
    if BigWorld.player() is None:
        return 0
    else:
        return BigWorld.player().connectionMgr.peripheryID
