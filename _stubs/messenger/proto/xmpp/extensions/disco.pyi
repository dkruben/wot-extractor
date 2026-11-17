# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/disco.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from messenger.proto.xmpp.extensions import PyQuery as PyQuery, PyExtension as PyExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.shared_handlers import IQHandler as IQHandler
from messenger.proto.xmpp.extensions.wg_items import WgSharedExtension as WgSharedExtension
from messenger.proto.xmpp.gloox_constants import IQ_TYPE as IQ_TYPE
Identity: Any

class IdentityElement(PyExtension):
    def __init__(self):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class FeatureElement(PyExtension):
    def __init__(self):
        ...
    @classmethod
    def getDefaultData(cls):
        ...

class CreatedByElement(PyExtension):
    def __init__(self):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class DiscoInfoExtension(PyExtension):
    def __init__(self):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...
    def _makeChildrenString(self):
        ...

class DiscoInfoQuery(PyQuery):
    def __init__(self, jid):
        ...

class DiscoInfoHandler(IQHandler):
    def __init__(self):
        ...
