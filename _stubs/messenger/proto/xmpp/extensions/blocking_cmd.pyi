# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/blocking_cmd.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from messenger.proto.xmpp.extensions import PyExtension as PyExtension, PyQuery as PyQuery
from messenger.proto.xmpp.extensions.contact_item import ContactItemExtension as ContactItemExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.shared_handlers import IQChildHandler as IQChildHandler
from messenger.proto.xmpp.gloox_constants import IQ_TYPE as IQ_TYPE

class BlockListQuery(PyQuery):
    def __init__(self):
        ...

class BlockListHandler(IQChildHandler):
    def __init__(self):
        ...

class BlockItemQuery(PyQuery):
    def __init__(self, jid):
        ...

class BlockItemHandler(IQChildHandler):
    def __init__(self):
        ...

class UnblockItemQuery(PyQuery):
    def __init__(self, jid):
        ...

class UnblockItemHandler(IQChildHandler):
    def __init__(self):
        ...

def _createBlockListExt():
    ...
def _createBlockItemExt(jid=None):
    ...
def _createUnblockItemExt(jid=None):
    ...
