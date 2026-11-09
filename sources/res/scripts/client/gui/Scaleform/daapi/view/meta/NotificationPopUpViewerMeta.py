# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/NotificationPopUpViewerMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationPopUpViewerMeta.py
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class NotificationPopUpViewerMeta(BaseDAAPIComponent):

    def setListClear(self):
        self._printOverrideError('setListClear')

    def onMessageHidden(self, byTimeout, wasNotified, typeID, entityID):
        self._printOverrideError('onMessageHidden')

    def onClickAction(self, typeID, entityID, action):
        self._printOverrideError('onClickAction')

    def getMessageActualTime(self, msTime):
        self._printOverrideError('getMessageActualTime')

    def registerGFNotification(self, component, alias, gfViewName, isPopUp, linkageData):
        self._printOverrideError('registerGFNotification')

    def as_hasPopUpIndexS(self, typeID, entityID):
        if self._isDAAPIInited():
            return self.flashObject.as_hasPopUpIndex(typeID, entityID)

    def as_appendMessageS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(data)

    def as_updateMessageS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(data)

    def as_removeMessageS(self, typeID, entityID):
        if self._isDAAPIInited():
            return self.flashObject.as_removeMessage(typeID, entityID)

    def as_removeAllMessagesS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_removeAllMessages()

    def as_initInfoS(self, maxMessagessCount, padding):
        if self._isDAAPIInited():
            return self.flashObject.as_initInfo(maxMessagessCount, padding)

    def as_setViewPaddingS(self, enabled, paddingX, paddingY):
        if self._isDAAPIInited():
            return self.flashObject.as_setViewPadding(enabled, paddingX, paddingY)
