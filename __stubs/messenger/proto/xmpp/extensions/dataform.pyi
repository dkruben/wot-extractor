# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/dataform.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import namedtuple as namedtuple
from messenger.proto.xmpp.extensions import PyExtension as PyExtension, SimpleExtension as SimpleExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.xmpp_constants import FORM_TYPE as FORM_TYPE
from shared_utils import findFirst as findFirst
Field: Any

class FieldElement(PyExtension):
    def __init__(self, field=None):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class DataForm(PyExtension):
    _isEmpty: Any
    def __init__(self, fields=None):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def getTag(self):
        ...
    def parseTag(self, pyGlooxTag):
        ...
