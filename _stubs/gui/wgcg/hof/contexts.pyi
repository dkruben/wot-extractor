# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/hof/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.clans import items as items
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from shared_utils import makeTupleByDict as makeTupleByDict

class _BaseHofRequestCtx(CommonWebRequestCtx):
    def isAuthorizationRequired(self):
        ...
    def isClanSyncRequired(self):
        ...
    def getDataObj(self, incomeData):
        ...
    def isCaching(self):
        ...

class HofUserInfoCtx(_BaseHofRequestCtx):
    def getRequestType(self):
        ...

class HofUserExcludeCtx(_BaseHofRequestCtx):
    def getRequestType(self):
        ...

class HofUserRestoreCtx(_BaseHofRequestCtx):
    def getRequestType(self):
        ...
