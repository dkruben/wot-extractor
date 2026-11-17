# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from helpers.ro_property import ROPropertyMeta as ROPropertyMeta
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, PROTO_TYPE_NAMES as PROTO_TYPE_NAMES
from messenger.proto.bw import BWProtoPlugin as BWProtoPlugin
from messenger.proto.bw_chat2 import BWProtoPlugin as BWProtoPlugin_chat2
from messenger.proto.bw.BWServerSettings import BWServerSettings as BWServerSettings
from messenger.proto.bw_chat2.BWServerSettings import BWServerSettings as BWServerSettings_chat2
from messenger.proto.interfaces import IProtoPlugin as IProtoPlugin
from messenger.proto.migration import MigrationPlugin as MigrationPlugin
from messenger.proto.migration.MigrationServerSettings import MigrationServerSettings as MigrationServerSettings
from messenger.proto.xmpp import XmppPlugin as XmppPlugin, XmppServerSettings as XmppServerSettings
from messenger.proto.xmpp.xmpp_constants import XMPP_MUC_CHANNEL_TYPE as XMPP_MUC_CHANNEL_TYPE
from py2to3.patched_future import with_metaclass as with_metaclass
__all__: tuple
_SUPPORTED_PROTO_PLUGINS: dict
_SUPPORTED_PROTO_SETTINGS: dict

# base nao representavel no stub: with_metaclass(...)
class ProtoPluginsDecorator:
    __readonly__: dict
    def __repr__(self):
        ...
    def connect(self, scope):
        ...
    def disconnect(self):
        ...
    def view(self, scope):
        ...
    def goToReplay(self):
        ...
    def setFilters(self, msgFilterChain):
        ...
    def init(self):
        ...
    def clear(self):
        ...
    def _invoke(self, method, *args):
        ...

# base nao representavel no stub: with_metaclass(...)
class ServerSettings:
    __readonly__: dict
    def __repr__(self):
        ...
    def update(self, data):
        ...
    def clear(self):
        ...
    def useToShowContacts(self, protoType):
        ...
    def isUserRoomsEnabled(self, protoType):
        ...
    def getSystemChannels(self, protoType):
        ...
    def isXmppClansEnabled(self):
        ...
    def _isXmppEnabled(self):
        ...
    def _isXmppMucChannelEnabled(self, channelType):
        ...
    def _isXmppUserRoomsEnabled(self):
        ...
    def _getSystemChannels(self):
        ...

class _proto_type_getter(object):
    _type: Any
    def __init__(self, protoType):
        ...
    def get(self):
        ...
    def __call__(self, _):
        ...

class proto_getter(_proto_type_getter):
    def get(self):
        ...

class settings_getter(_proto_type_getter):
    def get(self):
        ...
