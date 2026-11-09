# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/ChatManager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/ChatManager.py
from __future__ import absolute_import
from chat_shared import CHAT_ACTIONS, CHAT_CHANNEL_BATTLE, CHAT_CHANNEL_BATTLE_TEAM
import Event
from Singleton import Singleton

class ChatManager(Singleton):

    @staticmethod
    def instance():
        return ChatManager()

    def _singleton_init(self):
        self.battleTeamChannelID = 0
        self.battleCommonChannelID = 0
        self.playerProxy = None
        self.__chatActionCallbacks = {}
        return

    def subscribeChatAction(self, callback, action, channelId=None):
        cbs = self.__getChatActionCallbacks(action, channelId)
        cbs += callback

    def unsubscribeChatAction(self, callback, action, channelId=None):
        cbs = self.__getChatActionCallbacks(action, channelId)
        cbs -= callback

    def unsubcribeAllChatActions(self):
        for handlers in self.__chatActionCallbacks.values():
            handlers.clear()

    def __getChatActionCallbacks(self, action, channelId):
        channelId = channelId if channelId is not None else 0
        key = (action, channelId)
        if key not in self.__chatActionCallbacks:
            handlers = self.__chatActionCallbacks[key] = Event.Event()
        else:
            handlers = self.__chatActionCallbacks[key]
        return handlers

    def switchPlayerProxy(self, proxy):
        self.__cleanupMyCallbacks()
        self.__setProxyChatActionsCallbacks({})
        self.playerProxy = proxy
        self.__setProxyChatActionsCallbacks(self.__chatActionCallbacks)
        self.__setupMyCallbacks()

    def __setProxyChatActionsCallbacks(self, callbacks):
        if self.playerProxy is not None:
            self.playerProxy.setChatActionsCallbacks(callbacks)
        return

    def __cleanupMyCallbacks(self):
        if self.playerProxy is not None:
            self.battleTeamChannelID = 0
            self.battleCommonChannelID = 0
            self.playerProxy.unsubscribeChatAction(self.__onChannelsListReceived, CHAT_ACTIONS.requestChannels)
        return

    def __setupMyCallbacks(self):
        if self.playerProxy is not None:
            self.playerProxy.subscribeChatAction(self.__onChannelsListReceived, CHAT_ACTIONS.requestChannels)
        return

    def __onChannelsListReceived(self, chatActionData):
        for chInfo in chatActionData['data']:
            flags = chInfo.get('flags', 0)
            if flags & CHAT_CHANNEL_BATTLE == CHAT_CHANNEL_BATTLE:
                if flags & CHAT_CHANNEL_BATTLE_TEAM == CHAT_CHANNEL_BATTLE_TEAM:
                    self.battleTeamChannelID = chInfo.get('id', 0)
                else:
                    self.battleCommonChannelID = chInfo.get('id', 0)


chatManager = ChatManager.instance()
