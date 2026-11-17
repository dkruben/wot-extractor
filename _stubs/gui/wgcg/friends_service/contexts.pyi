# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/friends_service/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
_logger: Any

class _FriendServiceCtx(CommonWebRequestCtx):
    def isAuthorizationRequired(self):
        ...
    def isClanSyncRequired(self):
        ...
    def isCaching(self):
        ...

class _SpaIdCtx(_FriendServiceCtx):
    __spaId: Any
    def __init__(self, spaId, waitingID=''):
        ...
    def getSpaId(self):
        ...

class FriendStateCtx(_SpaIdCtx):
    def getRequestType(self):
        ...

class FriendListCtx(_FriendServiceCtx):
    def getRequestType(self):
        ...

class PutBestFriendCtx(_SpaIdCtx):
    def getRequestType(self):
        ...

class DeleteBestFriendCtx(_SpaIdCtx):
    def getRequestType(self):
        ...

class GatherFriendsResourcesCtx(_SpaIdCtx):
    def getRequestType(self):
        ...
