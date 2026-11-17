# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/spa_resolver.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from past.builtins import long as long
from messenger.proto.xmpp.extensions import PyExtension as PyExtension, PyQuery as PyQuery
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.shared_handlers import IQChildHandler as IQChildHandler
from messenger.proto.xmpp.gloox_constants import IQ_TYPE as IQ_TYPE

class SpaResolverError(PyExtension):
    def __init__(self):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def getTag(self):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class SpaResolverItem(PyExtension):
    def __init__(self, dbID=0, nickname=''):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class SpaResolverQuery(PyExtension):
    def __init__(self, items=None):
        ...
    @classmethod
    def getDefaultData(cls):
        ...

class SpaResolverByIDsQuery(PyQuery):
    def __init__(self, dbIDs):
        ...

class SpaResolverHandler(IQChildHandler):
    def __init__(self):
        ...
