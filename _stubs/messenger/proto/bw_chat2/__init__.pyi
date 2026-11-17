# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw_chat2/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger import g_settings as g_settings
from messenger.m_constants import MESSENGER_SCOPE as MESSENGER_SCOPE, PROTO_TYPE as PROTO_TYPE
from messenger.proto.bw_chat2 import chat_handlers as chat_handlers
from messenger.proto.bw_chat2.VOIPChatProvider import VOIPChatProvider as VOIPChatProvider
from messenger.proto.bw_chat2.VOIPChatController import VOIPChatController as VOIPChatController
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.interfaces import IProtoPlugin as IProtoPlugin
from messenger.proto.bw_chat2.provider import BWChatProvider as BWChatProvider
from messenger.proto.bw_chat2.UsersHandler import UsersHandler as UsersHandler

class BWProtoPlugin(IProtoPlugin):
    __slots__: tuple
    __provider: Any
    __adminChat: Any
    __users: Any
    __arenaChat: Any
    __battleCmd: Any
    __unitChat: Any
    __voipProvider: Any
    __voipCtrl: Any
    __isConnected: Any
    def __init__(self):
        ...
    @property
    def arenaChat(self):
        ...
    @property
    def battleCmd(self):
        ...
    @property
    def unitChat(self):
        ...
    @property
    def adminChat(self):
        ...
    @property
    def provider(self):
        ...
    @property
    def voipProvider(self):
        ...
    @property
    def voipController(self):
        ...
    @property
    def users(self):
        ...
    def isConnected(self):
        ...
    def connect(self, scope):
        ...
    def view(self, scope):
        ...
    def disconnect(self):
        ...
    def goToReplay(self):
        ...
    def setFilters(self, msgFilterChain):
        ...
    def init(self):
        ...
    def clear(self):
        ...
    def onActionReceived(self, actionID, reqID, args):
        ...
