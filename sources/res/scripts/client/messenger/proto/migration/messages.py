# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/messenger/proto/migration/messages.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/messenger/proto/migration/messages.py
from __future__ import absolute_import
from messenger.proto.bw import bw_chat_string_utils
from messenger.proto.events import g_messengerEvents
from messenger.proto.migration.proxy import MigrationProxy
from messenger.proto.xmpp import xmpp_string_utils
from messenger.proto.xmpp.jid import JID

class MessagesManagerProxy(MigrationProxy):
    __slots__ = ()

    def getSearchUserRoomsProcessor(self):
        raise NotImplementedError

    def getUserRoomValidator(self):
        raise NotImplementedError

    def createUserRoom(self, name, password=''):
        raise NotImplementedError

    def joinToUserRoom(self, roomID, name, password=''):
        raise NotImplementedError


class BWMessagesManagerProxy(MessagesManagerProxy):
    __slots__ = ()

    def getSearchUserRoomsProcessor(self):
        from messenger.proto.bw import search_processors
        return search_processors.SearchChannelsProcessor()

    def getUserRoomValidator(self):
        return bw_chat_string_utils

    def createUserRoom(self, name, password=''):
        self._proto.channels.createChannel(name, password)
        return True

    def joinToUserRoom(self, roomID, name, password=''):
        self._proto.channels.joinToChannel(roomID, password)
        return True


class XMPPMessagesManagerProxy(MessagesManagerProxy):
    __slots__ = ()

    def getSearchUserRoomsProcessor(self):
        from messenger.proto.xmpp import xmpp_search_processors
        return xmpp_search_processors.SearchUserRoomsProcessor()

    def getUserRoomValidator(self):
        return xmpp_string_utils

    def createUserRoom(self, name, password=''):
        result, error = self._proto.messages.createUserRoom(name, password)
        if not result:
            g_messengerEvents.onErrorReceived(error)
        return result

    def joinToUserRoom(self, roomID, name, password=''):
        result, error = self._proto.messages.joinToMUC(JID(roomID), password=password, name=name)
        if not result:
            g_messengerEvents.onErrorReceived(error)
        return result
