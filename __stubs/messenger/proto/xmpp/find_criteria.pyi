# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/find_criteria.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, USER_TAG as USER_TAG
from messenger.proto.interfaces import IEntityFindCriteria as IEntityFindCriteria
from messenger.proto.xmpp.gloox_constants import MESSAGE_TYPE as MESSAGE_TYPE
from messenger.proto.xmpp.xmpp_constants import XMPP_ITEM_TYPE as XMPP_ITEM_TYPE

class ItemsFindCriteria(IEntityFindCriteria):
    __slots__: tuple
    __itemTypes: Any
    def __init__(self, itemTypes):
        ...
    def filter(self, entity):
        ...

class GroupFindCriteria(ItemsFindCriteria):
    __slots__: tuple
    __groups: Any
    def __init__(self, group):
        ...
    def filter(self, entity):
        ...

class RqFriendshipCriteria(IEntityFindCriteria):
    def filter(self, entity):
        ...

class MutedOnlyFindCriteria(IEntityFindCriteria):
    def filter(self, entity):
        ...

class XMPPChannelFindCriteria(IEntityFindCriteria):
    __msgType: Any
    def __init__(self, msgType=None):
        ...
    def filter(self, entity):
        ...

class XMPPChannelByJIDFindCriteria(IEntityFindCriteria):
    __jid: Any
    def __init__(self, jid):
        ...
    def filter(self, entity):
        ...

class XMPPChannelByNameFindCriteria(IEntityFindCriteria):
    __name: Any
    def __init__(self, name):
        ...
    def filter(self, entity):
        ...

class XmppClanChannelCriteria(IEntityFindCriteria):
    def filter(self, entity):
        ...
