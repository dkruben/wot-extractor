# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw/limits.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from constants import CHAT_MESSAGE_MAX_LENGTH as CHAT_MESSAGE_MAX_LENGTH, CHAT_MESSAGE_MAX_LENGTH_IN_BATTLE as CHAT_MESSAGE_MAX_LENGTH_IN_BATTLE
from messenger.m_constants import MESSAGES_HISTORY_MAX_LEN as MESSAGES_HISTORY_MAX_LEN
from messenger.proto.interfaces import IProtoLimits as IProtoLimits
from soft_exception import SoftException as SoftException

class BattleLimits(IProtoLimits):
    def getMessageMaxLength(self):
        ...
    def getHistoryMaxLength(self):
        ...
    def getBroadcastCoolDown(self):
        ...

class LobbyLimits(IProtoLimits):
    def getMessageMaxLength(self):
        ...
    def getHistoryMaxLength(self):
        ...
    def getBroadcastCoolDown(self):
        ...

class CHANNEL_LIMIT(object):
    NAME_MIN_LENGTH = 3
    NAME_MAX_LENGTH = 32
    PWD_MIN_LENGTH = 3
    PWD_MAX_LENGTH = 12
