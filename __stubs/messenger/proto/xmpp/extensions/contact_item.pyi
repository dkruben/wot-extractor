# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/contact_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from messenger.proto.xmpp.extensions import PyExtension as PyExtension
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.extensions.wg_items import WgSharedExtension as WgSharedExtension
from messenger.proto.xmpp.jid import ContactJID as ContactJID

class ContactItemExtension(PyExtension):
    def __init__(self, jid=None):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def parseTag(self, pyGlooxTag):
        ...
