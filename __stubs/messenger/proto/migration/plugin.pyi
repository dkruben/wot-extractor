# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/migration/plugin.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from messenger import g_settings as g_settings
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE
from messenger.proto.events import g_messengerEvents as g_messengerEvents
from messenger.proto.interfaces import IProtoPlugin as IProtoPlugin
from messenger.proto.migration import contacts as contacts, messages as messages

class MigrationPlugin(IProtoPlugin):
    __slots__: tuple
    __bwProto: Any
    __bw2Proto: Any
    __xmppProto: Any
    __contacts: Any
    __messages: Any
    def __init__(self, plugins):
        ...
    def isConnected(self):
        ...
    @property
    def contacts(self):
        ...
    @property
    def messages(self):
        ...
    def clear(self):
        ...
    def connect(self, scope):
        ...
    def disconnect(self):
        ...
    def __onPluginConnected(self, protoType):
        ...
    def __onPluginDisconnected(self, protoType):
        ...
