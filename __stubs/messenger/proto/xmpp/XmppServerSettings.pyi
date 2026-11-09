# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/XmppServerSettings.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import random as random
from future.utils import lfilter as lfilter, viewitems as viewitems
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.shared.utils import getPlayerDatabaseID as getPlayerDatabaseID
from messenger.proto.interfaces import IProtoSettings as IProtoSettings
from messenger.proto.xmpp.gloox_constants import CONNECTION_IMPL_TYPE as CONNECTION_IMPL_TYPE
from messenger.proto.xmpp.jid import ContactJID as ContactJID
from soft_exception import SoftException as SoftException
_NUMBER_OF_ITEMS_IN_SAMPLE = 2

class ConnectionsIterator(object):
    next: Any
    __tcp: Any
    __bosh: Any
    def __init__(self, base=None, alt=None, bosh=None):
        ...
    def __iter__(self):
        ...
    def __len__(self):
        ...
    def clear(self):
        ...
    def hasNext(self):
        ...
    def __next__(self):
        ...

class XmppServerSettings(IProtoSettings):
    __slots__: tuple
    mucServices: Any
    enabled: Any
    connections: Any
    altConnections: Any
    boshConnections: Any
    domain: Any
    port: Any
    resource: Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    @property
    def userRoomsService(self):
        ...
    def update(self, data):
        ...
    def clear(self):
        ...
    def isEnabled(self):
        ...
    def getFullJID(self, databaseID=None):
        ...
    def getConnectionsIterator(self):
        ...
    def isMucServiceAllowed(self, service='', hostname=''):
        ...
    def getChannelByType(self, channelType):
        ...

def _makeSample(*args):
    ...
def _validateConnection(record):
    ...
