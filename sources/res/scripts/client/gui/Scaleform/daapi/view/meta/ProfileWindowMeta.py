# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/ProfileWindowMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/ProfileWindowMeta.py
from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ProfileWindowMeta(AbstractWindowView):

    def userAddFriend(self):
        self._printOverrideError('userAddFriend')

    def userAddToClan(self):
        self._printOverrideError('userAddToClan')

    def userSetIgnored(self):
        self._printOverrideError('userSetIgnored')

    def userCreatePrivateChannel(self):
        self._printOverrideError('userCreatePrivateChannel')

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)

    def as_addFriendAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_addFriendAvailable(value)

    def as_addToClanAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_addToClanAvailable(value)

    def as_addToClanVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_addToClanVisible(value)

    def as_setIgnoredAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIgnoredAvailable(value)

    def as_setCreateChannelAvailableS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCreateChannelAvailable(value)
