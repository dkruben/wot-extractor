# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/gui/Scaleform/meta/ContactsListPopoverMeta.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/meta/ContactsListPopoverMeta.py
from gui.Scaleform.daapi.view.lobby.popover.SmartPopOverView import SmartPopOverView

class ContactsListPopoverMeta(SmartPopOverView):

    def addToFriends(self, uid, name):
        self._printOverrideError('addToFriends')

    def addToIgnored(self, uid, name):
        self._printOverrideError('addToIgnored')

    def isEnabledInRoaming(self, uid):
        self._printOverrideError('isEnabledInRoaming')

    def changeGroup(self, dbId, contactName, groupData):
        self._printOverrideError('changeGroup')

    def copyIntoGroup(self, contactDbId, groupData):
        self._printOverrideError('copyIntoGroup')

    def as_setInitInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitInfo(data)

    def as_editGroupS(self, targetGroupName):
        if self._isDAAPIInited():
            return self.flashObject.as_editGroup(targetGroupName)

    def as_removeGroupS(self, targetGroupName):
        if self._isDAAPIInited():
            return self.flashObject.as_removeGroup(targetGroupName)

    def as_createContactNoteS(self, userName, databaseID):
        if self._isDAAPIInited():
            return self.flashObject.as_createContactNote(userName, databaseID)

    def as_editContactNoteS(self, userName, databaseID):
        if self._isDAAPIInited():
            return self.flashObject.as_editContactNote(userName, databaseID)
