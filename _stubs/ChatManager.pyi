# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ChatManager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from chat_shared import CHAT_ACTIONS as CHAT_ACTIONS, CHAT_CHANNEL_BATTLE as CHAT_CHANNEL_BATTLE, CHAT_CHANNEL_BATTLE_TEAM as CHAT_CHANNEL_BATTLE_TEAM
import Event as Event
from Singleton import Singleton as Singleton
chatManager: Any

class ChatManager(Singleton):
    battleTeamChannelID: Any
    battleCommonChannelID: Any
    playerProxy: Any
    __chatActionCallbacks: Any
    @staticmethod
    def instance():
        ...
    def _singleton_init(self):
        ...
    def subscribeChatAction(self, callback, action, channelId=None):
        ...
    def unsubscribeChatAction(self, callback, action, channelId=None):
        ...
    def unsubcribeAllChatActions(self):
        ...
    def __getChatActionCallbacks(self, action, channelId):
        ...
    def switchPlayerProxy(self, proxy):
        ...
    def __setProxyChatActionsCallbacks(self, callbacks):
        ...
    def __cleanupMyCallbacks(self):
        ...
    def __setupMyCallbacks(self):
        ...
    def __onChannelsListReceived(self, chatActionData):
        ...
