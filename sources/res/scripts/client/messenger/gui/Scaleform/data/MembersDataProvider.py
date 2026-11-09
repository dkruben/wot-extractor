# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/gui/Scaleform/data/MembersDataProvider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/gui/Scaleform/data/MembersDataProvider.py
from __future__ import absolute_import
from gui.Scaleform.framework.entities.DAAPIDataProvider import DAAPIDataProvider
from messenger import g_settings
from messenger.m_constants import USER_GUI_TYPE
from messenger.storage import MessengerStorageDescriptor, UsersStorage

class MembersDataProvider(DAAPIDataProvider):
    usersStorage = MessengerStorageDescriptor(UsersStorage)

    def __init__(self):
        super(MembersDataProvider, self).__init__()
        self.__list = []

    @property
    def collection(self):
        return self.__list

    def buildList(self, members):
        self.__list = []
        members = sorted(members, key=(lambda member: member.getName().lower()))
        getUser = self.usersStorage.getUser
        getColors = g_settings.getColorScheme('rosters').getColors
        for member in members:
            dbID = member.getDatabaseID()
            isOnline = member.isOnline()
            user = getUser(dbID)
            if user:
                tags = list(user.getTags())
                colors = getColors(user.getGuiType())
            else:
                tags = []
                colors = getColors(USER_GUI_TYPE.OTHER)
            self.__list.append({'dbID': dbID, 
               'userName': (member.getFullName()), 
               'isOnline': isOnline, 
               'color': (colors[0 if isOnline else 1]), 
               'tags': tags, 
               'isPlayerSpeaking': False})

    def emptyItem(self):
        return {'dbID': 0, 
           'userName': '', 
           'isOnline': False, 
           'color': 0, 
           'tags': [], 'isPlayerSpeaking': False}
