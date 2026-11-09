# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/wgcg/agate/contexts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from enum import Enum as Enum
from gui.wgcg.base.contexts import CommonWebRequestCtx as CommonWebRequestCtx
from gui.wgcg.settings import WebRequestDataType as WebRequestDataType
from typing import Dict as Dict, List as List

class InventoryEntitlementsCtx(CommonWebRequestCtx):
    __slots__: tuple
    __entitlementCodes: Any
    def __init__(self, entitlementCodes=..., waitingID=''):
        ...
    def getRequestType(self):
        ...
    def isAuthorizationRequired(self):
        ...
    def isClanSyncRequired(self):
        ...
    def isCaching(self):
        ...
    def getEntitlementCodes(self):
        ...

class AgateGetInventoryEntitlementsCtx(CommonWebRequestCtx):
    __slots__: tuple
    __entitlementsFilter: Any
    class _FilterKeys(Enum):
        CODE = 'code'
        TAG = 'tag'
    class _FilterOperators(Enum):
        IN = 'in'
        NOT_IN = 'not_in'
        EQ = 'eq'
        NEQ = 'neq'
    def __init__(self, entitlementsFilter, waitingID=''):
        ...
    def getRequestType(self):
        ...
    def isAuthorizationRequired(self):
        ...
    def isClanSyncRequired(self):
        ...
    def isCaching(self):
        ...
    def getEntitlementsFilter(self):
        ...
    @classmethod
    def createFilterByTags(cls, tags):
        ...
    @classmethod
    def createFilterByCodes(cls, codes):
        ...
    @classmethod
    def __makeRequestArgsForValues(cls, valuesList):
        ...
