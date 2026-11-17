# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/wgcg/requests.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from gui.shared.utils.requesters.abstract import Response as Response, ClientRequestsByIDProcessor as ClientRequestsByIDProcessor
from gui.shared.utils.requesters.RequestsController import RequestsController as RequestsController
from client_request_lib.exceptions import ResponseCodes as ResponseCodes

class SERVER_SIDE_REPLAY_REQUEST_TYPE(CONST_CONTAINER):
    GET_BEST_REPLAYS = 1
    GET_TOP_REPLAYS = 2
    GET_REPLAY_LINK = 3
    POST_FIND_REPLAY = 4

class ServerSideReplayRequestResponse(Response):
    def isSuccess(self):
        ...
    def getCode(self):
        ...
    def clone(self, data=None):
        ...
    def mergeData(self, data):
        ...

class ServerSideReplayRequester(ClientRequestsByIDProcessor):
    def __init__(self, sender):
        ...
    def _getSenderMethod(self, sender, methodName):
        ...
    def _doCall(self, method, *args, **kwargs):
        ...

class ServerSideReplayRequestsController(RequestsController):
    __handlers: Any
    def __init__(self, requester):
        ...
    def fini(self):
        ...
    def _getHandlerByRequestType(self, requestTypeID):
        ...
    def __getBestReplays(self, ctx, callback):
        ...
    def __getTopReplays(self, ctx, callback):
        ...
    def __getReplayLink(self, ctx, callback):
        ...
    def __postFindReplay(self, ctx, callback):
        ...
