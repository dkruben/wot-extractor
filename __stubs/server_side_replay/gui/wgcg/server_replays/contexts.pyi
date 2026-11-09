# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/wgcg/server_replays/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import str as str
from future.utils import viewitems as viewitems
from typing import Dict as Dict, List as List
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from py2to3.compat import base64compat as base64compat
from server_side_replay.gui.wgcg.data_wrappers import server_replays as server_replays
from server_side_replay.gui.wgcg.requests import SERVER_SIDE_REPLAY_REQUEST_TYPE as SERVER_SIDE_REPLAY_REQUEST_TYPE

class JwtWebRequestCtx(CommonWebRequestCtx):
    jwtToken: Any
    def __init__(self):
        ...

class BestReplaysCtx(JwtWebRequestCtx):
    __accountId: Any
    __vehicleCDs: Any
    __nation: Any
    __vehicleLevel: Any
    __vehicleType: Any
    __fromDate: Any
    __isPrimeTime: Any
    __sortBy: Any
    def __init__(self, account_id=None, vehicleCDs=None, sortBy=None, nation=None, vehicleLevel=None, vehicleType=None, fromDate=None, isPrimeTime=None):
        ...
    def getRequestType(self):
        ...
    def getRequestKwargs(self):
        ...
    def getDataObj(self, incomeData):
        ...

class TopReplaysCtx(JwtWebRequestCtx):
    def getRequestType(self):
        ...
    def getDataObj(self, incomeData):
        ...

class ReplayLinkCtx(JwtWebRequestCtx):
    __replayID: Any
    def __init__(self, replayID=None):
        ...
    def getReplayID(self):
        ...
    def getRequestType(self):
        ...
    def getDataObj(self, incomeData):
        ...

class FindReplayCtx(JwtWebRequestCtx):
    __replayName: Any
    def __init__(self, replayName):
        ...
    def getReplayName(self):
        ...
    def getRequestType(self):
        ...
    def getDataObj(self, incomeData):
        ...

def makeTupleByDict(ntClass, data):
    ...
