# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/avatar_helpers/AvatarSyncData.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_helpers/AvatarSyncData.py
from __future__ import absolute_import
import AccountCommands

class AvatarSyncData(object):

    def __init__(self):
        self.__isSynchronized = False
        self.__subscribers = []
        self.__avatar = None
        return

    def setAvatar(self, avatar):
        self.__avatar = avatar

    def onAvatarBecomePlayer(self):
        self.__isSynchronized = self.__avatar.isSynchronized()
        if not self.__isSynchronized:
            self.__avatar._doCmdStr(AccountCommands.CMD_GET_AVATAR_SYNC, '', self.__onSyncResponse)

    def onAvatarBecomeNonPlayer(self):
        pass

    def waitForSync(self, callback):
        if self.__isSynchronized:
            callback(AccountCommands.RES_CACHE)
        if callback is not None:
            self.__subscribers.append(callback)
        return

    def __onSyncResponse(self, syncID, resultID, ext=None):
        ext = ext or {}
        self.__isSynchronized = True
        subscribers = self.__subscribers
        self.__subscribers = []
        for callback in subscribers:
            callback(resultID)
