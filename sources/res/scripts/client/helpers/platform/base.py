# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/platform/base.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/platform/base.py
from __future__ import absolute_import
from Event import EventManager, Event
from skeletons.helpers.platform import IPublishPlatform

class BasePublishPlatform(IPublishPlatform):
    __slots__ = ('__eventMgr', 'onPayment', 'onOverlay')

    def __init__(self):
        super(BasePublishPlatform, self).__init__()
        self.__eventMgr = EventManager()
        self.onPayment = Event(self.__eventMgr)
        self.onOverlay = Event(self.__eventMgr)

    def init(self):
        pass

    def fini(self):
        self.__eventMgr.clear()

    def isInited(self):
        return False

    def isConnected(self):
        return False
