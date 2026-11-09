# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/notification/BaseNotificationView.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/notification/BaseNotificationView.py
from __future__ import absolute_import
from debug_utils import LOG_ERROR
_NOT_ID_TUPLE_INDEX = 2

class BaseNotificationView(object):

    def __init__(self, model=None):
        super(BaseNotificationView, self).__init__()
        self._model = None
        self.__flashIDCounter = 0
        self.__flashIdToEntityIdMap = {}
        self.__entityIdToFlashIdMap = {}
        self.setModel(model)
        return

    def setModel(self, value):
        self._model = value

    def cleanUp(self):
        self._model = None
        return

    def _getFlashID(self, notificationInfo):
        if notificationInfo in self.__entityIdToFlashIdMap:
            return self.__entityIdToFlashIdMap[notificationInfo]
        self.__flashIDCounter += 1
        self.__flashIdToEntityIdMap[self.__flashIDCounter] = notificationInfo
        self.__entityIdToFlashIdMap[notificationInfo] = self.__flashIDCounter
        return self.__flashIDCounter

    def _getNotificationID(self, flashId):
        if flashId in self.__flashIdToEntityIdMap:
            return self.__flashIdToEntityIdMap[flashId][_NOT_ID_TUPLE_INDEX]
        else:
            LOG_ERROR('Wrong notification ScaleForm id', flashId)
            return
