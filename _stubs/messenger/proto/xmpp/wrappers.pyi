# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/wrappers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import lmap as lmap
from past.builtins import long as long
from collections import namedtuple as namedtuple
from constants import IGR_TYPE as IGR_TYPE, ARENA_GUI_TYPE_LABEL as ARENA_GUI_TYPE_LABEL
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from helpers import time_utils as time_utils
from messenger.proto.entities import ClanInfo as ClanInfo
from messenger.proto.xmpp.gloox_constants import CHAT_STATE as CHAT_STATE
from messenger.proto.xmpp.xmpp_constants import XMPP_BAN_COMPONENT as XMPP_BAN_COMPONENT
from messenger.proto.xmpp.xmpp_constants import ANY_ITEM_LITERAL as ANY_ITEM_LITERAL
XMPPChannelData: Any
ClientInfo: Any
_BanInfoItem: Any
WGExtsInfo: Any
MucInfo: Any

class ChatMessage(object):
    __slots__: tuple
    uuid: Any
    accountDBID: Any
    accountName: Any
    accountAffiliation: Any
    accountRole: Any
    body: Any
    state: Any
    sentAt: Any
    requestID: Any
    isFinalInHistory: Any
    def __init__(self, dbID=0, name='', body='', sentAt=0, affiliation='none', role='none'):
        ...
    def isHistory(self):
        ...

# decorador original: @ReprInjector.simple(...)
class BanInfo(object):
    __slots__: tuple
    _items: Any
    def __init__(self, items):
        ...
    def getFirstActiveItem(self, game=None, components=None):
        ...
    def isBanned(self, game=None, components=None):
        ...

def makeClientInfo(*args):
    ...
def makeClanInfo(*args):
    ...
def makeBanInfo(*args):
    ...
def makeMucInfo(info):
    ...
