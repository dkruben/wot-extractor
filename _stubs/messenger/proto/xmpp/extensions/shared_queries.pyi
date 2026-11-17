# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/shared_queries.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from messenger.proto.xmpp.extensions import PyQuery as PyQuery
from messenger.proto.xmpp.extensions.wg_items import WgClientExtension as WgClientExtension

class MessageQuery(PyQuery):
    __slots__: tuple
    _body: Any
    def __init__(self, msgType, to, msgBody='', ext=None):
        ...
    def getBody(self):
        ...

class PresenceQuery(PyQuery):
    def __init__(self, queryType, to=''):
        ...
    def getStatus(self):
        ...
    def isMucNsUsed(self):
        ...
    def setIgrID(self, igrID):
        ...
    def setIgrRoomID(self, igrRoomID):
        ...
    def setGameServerHost(self, host):
        ...
    def setArenaGuiLabel(self, label):
        ...
