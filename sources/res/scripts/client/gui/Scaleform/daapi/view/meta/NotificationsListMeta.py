# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/meta/NotificationsListMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/meta/NotificationsListMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class NotificationsListMeta(SmartPopOverView):

    def onClickAction(self, typeID, entityID, action):
        self._printOverrideError('onClickAction')

    def getMessageActualTime(self, msTime):
        self._printOverrideError('getMessageActualTime')

    def onGroupChange(self, groupIdx):
        self._printOverrideError('onGroupChange')

    def onCheckNewsClick(self):
        self._printOverrideError('onCheckNewsClick')

    def registerGFNotification(self, component, alias, gfViewName, isPopUp, linkageData):
        self._printOverrideError('registerGFNotification')

    def as_setInitDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(value)

    def as_setMessagesListS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMessagesList(value)

    def as_appendMessageS(self, messageData):
        if self._isDAAPIInited():
            return self.flashObject.as_appendMessage(messageData)

    def as_updateMessageS(self, messageData):
        if self._isDAAPIInited():
            return self.flashObject.as_updateMessage(messageData)

    def as_updateCountersS(self, counts):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCounters(counts)

    def as_setProgressiveRewardEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgressiveRewardEnabled(isEnabled)

    def as_setIsNewsBlockEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsNewsBlockEnabled(isEnabled)

    def as_setCheckNewsBtnEnabledS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setCheckNewsBtnEnabled(isEnabled)
