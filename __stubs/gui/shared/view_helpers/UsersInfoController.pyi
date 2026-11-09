# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/view_helpers/UsersInfoController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
from AccountCommands import isCodeValid as isCodeValid
from debug_utils import LOG_WARNING as LOG_WARNING
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.shared.utils.requesters import RequestCtx as RequestCtx
from gui.shared.utils.requesters.RequestsController import RequestsController as RequestsController
from messenger.storage import MessengerStorageDescriptor as MessengerStorageDescriptor, UsersStorage as UsersStorage
from messenger.proto import proto_getter as proto_getter, PROTO_TYPE as PROTO_TYPE
_GR_MAX_CHUNK_SIZE = 20
_NAMES_MAX_CHUNK_SIZE = 50

class USER_INFO_RQ_TYPE(CONST_CONTAINER):
    GET_GLOBAL_RATINGS = 1
    GET_NICKNAMES = 2

# decorador original: @ReprInjector.withParent(...)
class _GetGlobalRatingCtx(RequestCtx):
    __dbIDs: Any
    def __init__(self, dbIDs, waitingID=''):
        ...
    def getDbIDs(self):
        ...
    def getRequestType(self):
        ...
    def getCooldown(self):
        ...

# decorador original: @ReprInjector.withParent(...)
class _GetNicknamesCtx(RequestCtx):
    __dbIDs: Any
    def __init__(self, dbIDs, waitingID=''):
        ...
    def getDbIDs(self):
        ...
    def getRequestType(self):
        ...
    def getCooldown(self):
        ...

class UsersInfoController(RequestsController):
    usersStorage: Any
    __handlers: Any
    def __init__(self):
        ...
    def fini(self):
        ...
    # decorador original: @proto_getter(...)
    def proto(self):
        ...
    def requestNicknames(self, accountDbIDs, callback):
        ...
    def requestGlobalRatings(self, accountDbIDs, callback):
        ...
    def _getGlobalRatings(self, ctx, callback=None):
        ...
    def _getNicknames(self, ctx, callback=None):
        ...
    def _getHandlerByRequestType(self, requestTypeID):
        ...
    def _getRequestTimeOut(self):
        ...
