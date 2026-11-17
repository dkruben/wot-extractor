# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/migration/messages.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from messenger.proto.bw import bw_chat_string_utils as bw_chat_string_utils
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.migration.proxy import MigrationProxy as MigrationProxy
from messenger.proto.xmpp import xmpp_string_utils as xmpp_string_utils
from messenger.proto.xmpp.jid import JID as JID

class MessagesManagerProxy(MigrationProxy):
    __slots__: tuple
    def getSearchUserRoomsProcessor(self):
        ...
    def getUserRoomValidator(self):
        ...
    def createUserRoom(self, name, password=''):
        ...
    def joinToUserRoom(self, roomID, name, password=''):
        ...

class BWMessagesManagerProxy(MessagesManagerProxy):
    __slots__: tuple
    def getSearchUserRoomsProcessor(self):
        ...
    def getUserRoomValidator(self):
        ...
    def createUserRoom(self, name, password=''):
        ...
    def joinToUserRoom(self, roomID, name, password=''):
        ...

class XMPPMessagesManagerProxy(MessagesManagerProxy):
    __slots__: tuple
    def getSearchUserRoomsProcessor(self):
        ...
    def getUserRoomValidator(self):
        ...
    def createUserRoom(self, name, password=''):
        ...
    def joinToUserRoom(self, roomID, name, password=''):
        ...
