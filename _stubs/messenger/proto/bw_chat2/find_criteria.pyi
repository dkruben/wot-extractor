# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw_chat2/find_criteria.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PREBATTLE_TYPE as PREBATTLE_TYPE
from messenger.ext import channel_num_gen as channel_num_gen
from messenger.m_constants import BATTLE_CHANNEL as BATTLE_CHANNEL, PROTO_TYPE as PROTO_TYPE
from messenger.proto.interfaces import IEntityFindCriteria as IEntityFindCriteria

class BWBattleChannelFindCriteria(IEntityFindCriteria):
    __ids: Any
    def __init__(self):
        ...
    def filter(self, entity):
        ...

class BWPrebattleChannelFindCriteria(IEntityFindCriteria):
    def filter(self, entity):
        ...

class BWChatTypeFindCriteria(IEntityFindCriteria):
    __chatType: Any
    def __init__(self, chatType):
        ...
    def filter(self, entity):
        ...
