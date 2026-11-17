# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/entitlements/tankmen_entitlements_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import logging as logging
from collections import namedtuple as namedtuple
import typing as typing
from enum import Enum as Enum
from adisp import adisp_process as adisp_process
from functools import partial as partial
from gui.wgcg.agate.contexts import AgateGetInventoryEntitlementsCtx as AgateGetInventoryEntitlementsCtx
from helpers import dependency as dependency
from skeletons.gui.web import IWebController as IWebController
from typing import Callable as Callable, Dict as Dict, List as List
_logger: Any
Entitlement: Any
_DELAY = 1

class _FilterKeys(Enum):
    CODE = 'code'
    TAG = 'tag'

class _FilterOperators(Enum):
    IN = 'in'
    NOT_IN = 'not_in'
    EQ = 'eq'
    NEQ = 'neq'

class TankmenEntitlementsCache(object):
    __slots__: tuple
    __web: Any
    __balanceCache: Any
    __isSyncing: Any
    def __init__(self):
        ...
    def getBalance(self):
        ...
    def update(self, entitlementsFilter, onResponseCallback):
        ...
    def updateWithDelay(self, filter, onResponseCallback):
        ...
    def clear(self):
        ...
    # decorador original: @adisp_process
    def __request(self, entitlementsFilter, onResponseCallback):
        ...
    def __createEntitlementFromResponse(self, response):
        ...
    def __createFilterByTags(self, tags):
        ...
    def __createFilter(self, filters):
        ...
