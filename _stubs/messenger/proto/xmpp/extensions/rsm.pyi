# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/rsm.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from shared_utils import findFirst as findFirst
from messenger.proto.xmpp.extensions import PyExtension as PyExtension, SimpleExtension as SimpleExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS

class ResultSet(PyExtension):
    __slots__: tuple
    _converter: Any
    def __init__(self, converter=...):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def clear(self):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class RqResultSet(ResultSet):
    __slots__: tuple
    def __init__(self, max=0, after=None, before=None):
        ...
    def getTag(self):
        ...
