# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/search.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from messenger.proto.xmpp.extensions import PyQuery as PyQuery, PyExtension as PyExtension
from messenger.proto.xmpp.extensions.disco import CreatedByElement as CreatedByElement
from messenger.proto.xmpp.extensions.shared_handlers import IQChildHandler as IQChildHandler
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG, XML_NAME_SPACE as _NS
from messenger.proto.xmpp.entities import XMPPMucChannelEntity as XMPPMucChannelEntity
from messenger.proto.xmpp.extensions.spa_resolver import SpaResolverItem as SpaResolverItem
from messenger.proto.xmpp.extensions.wg_items import WgSharedExtension as WgSharedExtension
from messenger.proto.xmpp.gloox_constants import IQ_TYPE as IQ_TYPE
XmppUserSearchInfo: Any

class _SimpleCriterionExtension(PyExtension):
    def __init__(self, name, value):
        ...

class ChannelSearchQuery(PyQuery):
    _token: Any
    _results_count: Any
    _ext: Any
    def __init__(self, token, to='', count=50):
        ...
    def __initExtension(self):
        ...

class ChannelsListHandler(IQChildHandler):
    def __init__(self):
        ...

class ChannelItemExtension(PyExtension):
    def __init__(self):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class UsersSearchQuery(PyQuery):
    _nickname: Any
    _ext: Any
    def __init__(self, token, to=''):
        ...
    def __initExtension(self):
        ...

class UserSearchHandler(IQChildHandler):
    def __init__(self):
        ...

class NicknamePrefixSearchQuery(PyQuery):
    _prefix: Any
    _limit: Any
    _ext: Any
    def __init__(self, token, limit=50, to=''):
        ...
    def __initExtension(self):
        ...

class NicknamePrefixSearchHandler(IQChildHandler):
    def __init__(self):
        ...

class UserSearchItemExtension(SpaResolverItem):
    def __init__(self):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...
