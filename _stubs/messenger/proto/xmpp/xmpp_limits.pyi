# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/xmpp/xmpp_limits.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from messenger.proto.interfaces import IUserSearchLimits as IUserSearchLimits, IProtoLimits as IProtoLimits
from messenger.proto.xmpp.xmpp_constants import USER_SEARCH_LIMITS as USER_SEARCH_LIMITS, MESSAGE_LIMIT as MESSAGE_LIMIT

class FindUserSearchLimits(IUserSearchLimits):
    def getMaxResultSize(self):
        ...
    def getRequestCooldown(self):
        ...

class MessageLimits(IProtoLimits):
    def getMessageMaxLength(self):
        ...
    def getBroadcastCoolDown(self):
        ...
    def getHistoryMaxLength(self):
        ...
