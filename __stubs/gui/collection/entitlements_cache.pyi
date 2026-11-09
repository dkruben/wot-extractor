# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/collection/entitlements_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import namedtuple as namedtuple
from functools import partial as partial
import typing as typing
import BigWorld as BigWorld
from adisp import adisp_process as adisp_process
from gui.wgcg.agate.contexts import AgateGetInventoryEntitlementsCtx as AgateGetInventoryEntitlementsCtx
from helpers import dependency as dependency
from skeletons.gui.web import IWebController as IWebController
from typing import Callable as Callable, Dict as Dict
_logger: Any
Entitlement: Any
COLLECTIONS_TAG = 'collections'
COLLECTIONS_TAG_PREFIX = 'collections_{}'
_MAX_RETRY_ATTEMPTS = 5
_INITIAL_ATTEMPTS_COUNT = 0
_RETRY_DELAY = 1

class EntitlementsCache(object):
    __slots__: tuple
    __web: Any
    __balanceCache: Any
    __pendingEntitlementAttempts: Any
    __isSyncing: Any
    __isInited: Any
    __retryCallback: Any
    def __init__(self):
        ...
    def getBalance(self):
        ...
    def getCollectionBalance(self, collectionId):
        ...
    def updateAll(self, onResponseCallback):
        ...
    def update(self, entitlementCode, onResponseCallback):
        ...
    def clear(self):
        ...
    # decorador original: @adisp_process
    def __request(self, entitlementsTags, onResponseCallback):
        ...
    def __processPendingEntitlements(self, onResponseCallback):
        ...
    def __clearPendingEntitlements(self):
        ...
    def __createEntitlementFromResponse(self, response):
        ...
    def __getPendingEntitlementTags(self):
        ...
    def __clearAbsentEntitlements(self):
        ...
