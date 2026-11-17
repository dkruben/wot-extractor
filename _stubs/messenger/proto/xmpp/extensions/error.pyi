# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/error.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from shared_utils import findFirst as findFirst
from messenger.proto.xmpp.extensions import PyExtension as PyExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.gloox_constants import ERROR_TYPE as ERROR_TYPE
from messenger.proto.xmpp.xmpp_constants import MUC_CREATION_ERROR as MUC_CREATION_ERROR
STANZA_ERRORS: dict
DEF_STANZA_ERROR_CONDITION = 'undefined-condition'

class StanzaErrorExtension(PyExtension):
    def __init__(self, errorCondition=None, errorType=None):
        ...
    def parseTag(self, pyGlooxTag):
        ...
    @classmethod
    def getDefaultData(cls):
        ...

class WgErrorExtension(PyExtension):
    def __init__(self):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...
