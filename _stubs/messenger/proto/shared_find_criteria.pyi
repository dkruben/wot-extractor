# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/proto/shared_find_criteria.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_WARNING as LOG_WARNING
from messenger.m_constants import USER_TAG as USER_TAG
from messenger.proto.interfaces import IEntityFindCriteria as IEntityFindCriteria

class ProtoFindCriteria(IEntityFindCriteria):
    __slots__: tuple
    __protoType: Any
    def __init__(self, protoType):
        ...
    def filter(self, entity):
        ...

class OnlineFindCriteria(IEntityFindCriteria):
    __onlineMode: Any
    def __init__(self, onlineMode=None):
        ...
    def getOnlineMode(self):
        ...
    def setOnlineMode(self, onlineMode):
        ...
    def filter(self, entity):
        ...
    def _checkOnlineMode(self, user):
        ...

class UserTagsFindCriteria(OnlineFindCriteria):
    _tags: Any
    def __init__(self, tags, onlineMode=None):
        ...
    def addTags(self, tags):
        ...
    def removeTags(self, tags):
        ...
    def filter(self, entity):
        ...

class FriendsFindCriteria(UserTagsFindCriteria):
    def __init__(self, onlineMode=None):
        ...

class MutualFriendsFindCriteria(FriendsFindCriteria):
    def filter(self, entity):
        ...

class PendingFriendsCandidatesFindCriteria(UserTagsFindCriteria):
    def __init__(self, onlineMode=None):
        ...

class IgnoredFindCriteria(UserTagsFindCriteria):
    def __init__(self, includeTmpIgnore=False):
        ...
    def setOnlineMode(self, onlineMode):
        ...

class MutedFindCriteria(UserTagsFindCriteria):
    def __init__(self, onlineMode=None):
        ...
