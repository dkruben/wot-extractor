# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/client_update_listener.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/client_update_listener.py
from __future__ import absolute_import
import typing, Event
from PlayerEvents import g_playerEvents
from account_helpers import AccountSyncData
from helpers import dependency
from shared_utils.account_helpers.diff_utils import synchronizeDicts
from skeletons.connection_mgr import IConnectionManager

class ClientUpdateListener(object):
    __slots__ = ('onDataUpdated', '__data', '__key', '__resetOnDisconnect', '__synced',
                 '__default')
    __connectionMgr = dependency.descriptor(IConnectionManager)

    def __init__(self, key, resetOnDisconnect=True, default=None):
        self.__default = default
        self.__data = self.__default
        self.__synced = False
        self.__key = key
        self.__resetOnDisconnect = resetOnDisconnect
        self.onDataUpdated = Event.Event()

    @property
    def data(self):
        return self.__data

    @property
    def synced(self):
        return self.__synced

    def init(self):
        g_playerEvents.onClientUpdated += self.__onClientUpdated
        if self.__resetOnDisconnect:
            self.__connectionMgr.onDisconnected += self.__onDisconnected

    def destroy(self):
        g_playerEvents.onClientUpdated -= self.__onClientUpdated
        if self.__resetOnDisconnect:
            self.__connectionMgr.onDisconnected -= self.__onDisconnected
        self.onDataUpdated.clear()
        self.__data = None
        return

    def reset(self):
        self.__data = self.__default
        self.__synced = False

    def __onClientUpdated(self, diff, *_):
        isFullSync = AccountSyncData.isFullSyncDiff(diff)
        if isFullSync:
            self.reset()
        if self.__key in diff:
            diff = diff[self.__key]
            if isinstance(diff, dict):
                synchronizeDicts(diff, self.__data)
            else:
                self.__data = diff
            self.__synced = True
            self.onDataUpdated(self.__data)

    def __onDisconnected(self):
        self.reset()
