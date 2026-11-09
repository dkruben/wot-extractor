# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/extensions/wg_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from past.builtins import long as long
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from shared_utils import findFirst as findFirst
from messenger.proto.xmpp.extensions import PyExtension as PyExtension, SimpleExtension as SimpleExtension, PyHandler as PyHandler
from messenger.proto.xmpp.extensions.ext_constants import XML_NAME_SPACE as _NS
from messenger.proto.xmpp.extensions.ext_constants import XML_TAG_NAME as _TAG
from messenger.proto.xmpp.wrappers import makeClanInfo as makeClanInfo, makeClientInfo as makeClientInfo, makeBanInfo as makeBanInfo, WGExtsInfo as WGExtsInfo

class WgSharedExtension(PyExtension):
    def __init__(self, includeNS=True):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def getTag(self):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class WgClientExtension(PyExtension):
    def __init__(self):
        ...
    def setIgrID(self, igrID):
        ...
    def setIgrRoomID(self, igrRoomID):
        ...
    def setGameServerHost(self, host):
        ...
    def setArenaGuiLabel(self, label):
        ...
    @classmethod
    def getDefaultData(cls):
        ...
    def getTag(self):
        ...
    def parseTag(self, pyGlooxTag):
        ...

class WgClientHandler(PyHandler):
    def __init__(self):
        ...
    def getFilterString(self):
        ...

def makeWGInfoFromPresence(info):
    ...
