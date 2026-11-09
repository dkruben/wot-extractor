# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/bw/find_criteria.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import chat_shared as chat_shared
from messenger.m_constants import PROTO_TYPE as PROTO_TYPE, LAZY_CHANNEL as LAZY_CHANNEL
from messenger.proto.bw.entities import PREBATTLE_TYPE_CHAT_FLAG as PREBATTLE_TYPE_CHAT_FLAG
from messenger.proto.interfaces import IEntityFindCriteria as IEntityFindCriteria

class BWAllChannelFindCriteria(IEntityFindCriteria):
    def filter(self, entity):
        ...

class BWPrbChannelFindCriteria(IEntityFindCriteria):
    __prbFlag: Any
    def __init__(self, prbType):
        ...
    def filter(self, entity):
        ...

class BWLazyChannelFindCriteria(IEntityFindCriteria):
    __channelsNames: Any
    def __init__(self, criteria):
        ...
    def filter(self, entity):
        ...

class BWActiveChannelFindCriteria(IEntityFindCriteria):
    def filter(self, entity):
        ...

class BWClanChannelFindCriteria(IEntityFindCriteria):
    def filter(self, entity):
        ...

class BWLobbyChannelFindCriteria(IEntityFindCriteria):
    def filter(self, entity):
        ...

class BWBattleChannelFindCriteria(IEntityFindCriteria):
    def filter(self, entity):
        ...

class BWBattleTeamChannelFindCriteria(IEntityFindCriteria):
    def filter(self, entity):
        ...
