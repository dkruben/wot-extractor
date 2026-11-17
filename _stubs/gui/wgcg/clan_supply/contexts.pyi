# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/clan_supply/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from gui.clans.data_wrapper import clan_supply as clan_supply
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from shared_utils import makeTupleByDict as makeTupleByDict
from typing import Dict as Dict
_logger: Any

class ProgressionSettingsCtx(CommonWebRequestCtx):
    def getRequestType(self):
        ...
    def getDataObj(self, incomeData):
        ...
    def isAuthorizationRequired(self):
        ...

class ProgressionProgressCtx(CommonWebRequestCtx):
    def getRequestType(self):
        ...
    def getDataObj(self, incomeData):
        ...
    def isAuthorizationRequired(self):
        ...

class QuestsInfoCtx(CommonWebRequestCtx):
    def getRequestType(self):
        ...
    def getDataObj(self, incomeData):
        ...
    def isAuthorizationRequired(self):
        ...

class PostQuestsInfoCtx(QuestsInfoCtx):
    def getRequestType(self):
        ...

class ClaimRewardsCtx(CommonWebRequestCtx):
    def getRequestType(self):
        ...
    def isAuthorizationRequired(self):
        ...

class PurchaseProgressionStageCtx(CommonWebRequestCtx):
    __stageID: Any
    __price: Any
    def __init__(self, stageID, price):
        ...
    def getRequestArgs(self):
        ...
    def getRequestType(self):
        ...
    def isAuthorizationRequired(self):
        ...
