# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/resources.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from past.builtins import cmp as cmp
from constants import IGR_TYPE as IGR_TYPE, WG_GAMES as WG_GAMES
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.shared.sort_key import SortKey as SortKey
from messenger.m_constants import USER_TAG as USER_TAG
from messenger.proto.xmpp.gloox_constants import PRESENCES_ORDER as PRESENCES_ORDER, PRESENCE as PRESENCE
from messenger.proto.xmpp.wrappers import WGExtsInfo as WGExtsInfo
from messenger import g_settings as g_settings

# decorador original: @ReprInjector.simple(...)
class Resource(object):
    __slots__: tuple
    priority: Any
    message: Any
    presence: Any
    __wgExts: Any
    __mucInfo: Any
    __order: Any
    def __init__(self, priority=0, message=0, presence=..., wgExts=None, mucInfo=None):
        ...
    def getTags(self):
        ...
    def getWgDatabaseID(self):
        ...
    def getWgNickname(self):
        ...
    def getClientInfo(self):
        ...
    def getClanInfo(self):
        ...
    def getBanInfo(self):
        ...
    def getMucInfo(self):
        ...
    def getOrder(self):
        ...
    def replace(self, other):
        ...

class PrioritySortKey(SortKey):
    __slots__: tuple
    resItem: Any
    def __init__(self, resItem):
        ...
    def _cmp(self, other):
        ...

class ResourceDictionary(object):
    __slots__: tuple
    __resources: Any
    __highest: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def setResource(self, jid, resource):
        ...
    def removeResource(self, jid):
        ...
    def getTags(self):
        ...
    def isEmpty(self):
        ...
    def getHighestPriority(self):
        ...
    def getHighestPriorityID(self):
        ...
    def __initHighestData(self):
        ...
