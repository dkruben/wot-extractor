# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/w2gt/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType

class W2gtCtx(CommonWebRequestCtx):
    __eTag: Any
    __params: Any
    def __init__(self, clientVersion, eTag, geometryName, gameplayType, vehRole, vehLevel, team, waitingID=''):
        ...
    @staticmethod
    def normalizeVehicleRole(vehRole):
        ...
    def getRequestType(self):
        ...
    def isAuthorizationRequired(self):
        ...
    def isClanSyncRequired(self):
        ...
    def isCaching(self):
        ...
    def getParams(self):
        ...
    def getHeaders(self):
        ...
