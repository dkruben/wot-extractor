# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/elen/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from gui.shared.utils.requesters import RequestCtx as RequestCtx

class EventBoardsRequestCtx(RequestCtx):
    __slots__: tuple
    _needShowErrorNotification: Any
    def __init__(self):
        ...
    def isAuthorizationRequired(self):
        ...
    def isClanSyncRequired(self):
        ...
    def needShowErrorNotification(self):
        ...

class EventBoardsGetEventDataCtx(EventBoardsRequestCtx):
    _needShowErrorNotification: Any
    def __init__(self, needShowErrorNotification=True):
        ...
    def getRequestType(self):
        ...
    def getSingulizerKey(self):
        ...

class EventBoardsGetPlayerDataCtx(EventBoardsRequestCtx):
    _needShowErrorNotification: Any
    def __init__(self, needShowErrorNotification=True):
        ...
    def getRequestType(self):
        ...

class EventBoardsJoinEventCtx(EventBoardsRequestCtx):
    __slots__: tuple
    __eventID: Any
    _needShowErrorNotification: Any
    def __init__(self, eventID, needShowErrorNotification=True):
        ...
    def getRequestType(self):
        ...
    def getEventID(self):
        ...

class EventBoardsLeaveEventCtx(EventBoardsRequestCtx):
    __slots__: tuple
    __eventID: Any
    _needShowErrorNotification: Any
    def __init__(self, eventID, needShowErrorNotification=True):
        ...
    def getRequestType(self):
        ...
    def getEventID(self):
        ...

class EventBoardsGetMyEventTopCtx(EventBoardsRequestCtx):
    __slots__: tuple
    __eventID: Any
    _needShowErrorNotification: Any
    def __init__(self, eventID, needShowErrorNotification=False):
        ...
    def getRequestType(self):
        ...
    def getEventID(self):
        ...

class EventBoardsGetMyLeaderboardPositionCtx(EventBoardsRequestCtx):
    __slots__: tuple
    __eventID: Any
    __leaderboardID: Any
    _needShowErrorNotification: Any
    def __init__(self, eventID, leaderboardID, needShowErrorNotification=True):
        ...
    def getRequestType(self):
        ...
    def getSingulizerKey(self):
        ...
    def getEventID(self):
        ...
    def getLeaderboardID(self):
        ...

class EventBoardsGetLeaderboardCtx(EventBoardsRequestCtx):
    __slots__: tuple
    __eventID: Any
    __leaderboardID: Any
    __pageNumber: Any
    _needShowErrorNotification: Any
    def __init__(self, eventID, leaderboardID, pageNumber, needShowErrorNotification=True):
        ...
    def getRequestType(self):
        ...
    def getSingulizerKey(self):
        ...
    def getEventID(self):
        ...
    def getLeaderboardID(self):
        ...
    def getPageNumber(self):
        ...

class EventBoardsGetHangarFlagCtx(EventBoardsRequestCtx):
    _needShowErrorNotification: Any
    def __init__(self, needShowErrorNotification=False):
        ...
    def getRequestType(self):
        ...

class EventBoardsGetPlayerProgressionCtx(EventBoardsRequestCtx):
    __slots__: tuple
    __eventID: Any
    __leaderboardID: Any
    _needShowErrorNotification: Any
    def __init__(self, eventID, leaderboardID, needShowErrorNotification=True):
        ...
    def getRequestType(self):
        ...
    def getSingulizerKey(self):
        ...
    def getEventID(self):
        ...
    def getLeaderboardID(self):
        ...
