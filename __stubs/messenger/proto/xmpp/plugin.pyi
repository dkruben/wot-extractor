# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/plugin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger import g_settings as g_settings
from messenger.proto.xmpp.messages import MessagesManager as MessagesManager
from messenger.proto.xmpp.contacts import ContactsManager as ContactsManager
from messenger.proto.interfaces import IProtoPlugin as IProtoPlugin
from messenger.proto.xmpp.logger import LogHandler as LogHandler
from messenger.proto.xmpp.connection import ConnectionHandler as ConnectionHandler
from messenger.proto.xmpp.gloox_wrapper import ClientDecorator as ClientDecorator
from messenger.proto.xmpp.spa_requesters import NicknameResolver as NicknameResolver
from messenger.proto.xmpp.xmpp_clan_listener import XmppClanListener as XmppClanListener

class XmppPlugin(IProtoPlugin):
    __slots__: tuple
    __client: Any
    __contacts: Any
    __connection: Any
    __messages: Any
    __logger: Any
    __nicknameResolver: Any
    __clanListener: Any
    __isClientInited: Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    @property
    def client(self):
        ...
    @property
    def logger(self):
        ...
    @property
    def contacts(self):
        ...
    @property
    def messages(self):
        ...
    @property
    def nicknames(self):
        ...
    @property
    def clanListener(self):
        ...
    def isConnected(self):
        ...
    def init(self):
        ...
    def clear(self):
        ...
    def connect(self, scope):
        ...
    def view(self, scope):
        ...
    def disconnect(self):
        ...
    def setFilters(self, msgFilterChain):
        ...
    def __initClientEnv(self):
        ...
    def __finiClientEnv(self):
        ...
    def __clearClanListener(self):
        ...
    @classmethod
    def __getClanListener(cls):
        ...
