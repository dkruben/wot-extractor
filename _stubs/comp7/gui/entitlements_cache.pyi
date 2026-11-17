# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/entitlements_cache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from enum import Enum as Enum
import Event as Event
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import COMP7_ENTITLEMENTS as COMP7_ENTITLEMENTS, COMP7_ENTITLEMENTS_TIMESTAMP as COMP7_ENTITLEMENTS_TIMESTAMP, COMP7_ENTITLEMENTS_BALANCE as COMP7_ENTITLEMENTS_BALANCE
from gui.entitlements.entitlements_requester import EntitlementsRequester as EntitlementsRequester
from helpers import dependency as dependency
from helpers.time_utils import ONE_DAY as ONE_DAY, getServerUTCTime as getServerUTCTime
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
from wg_async import wg_async as wg_async, await_callback as await_callback
_logger: Any

class CacheStatus(Enum):
    IDLE = 'idle'
    PENDING = 'pending'
    DATA_READY = 'data_ready'
    ERROR = 'error'

class EntitlementsCache(object):
    __comp7Controller: Any
    __requester: Any
    __entitlements: Any
    __status: Any
    onCacheUpdated: Any
    def __init__(self):
        ...
    def reset(self):
        ...
    def clear(self):
        ...
    def getEntitlementCount(self, entitlementName):
        ...
    # decorador original: @wg_async
    def update(self, retryTimes=None, force=False):
        ...
    def __shouldBeUpdated(self, force=False):
        ...
    def __getPlayerEntitlements(self):
        ...
    def __isExpired(self):
        ...
    def __setStatus(self, status):
        ...
    def __getExpiryTime(self):
        ...
    def __getCacheEntitlements(self):
        ...
    def __getCacheTTL(self):
        ...
    def __getCacheConfig(self):
        ...
    def __clearCache(self):
        ...
    def __getCacheTimestamp(self):
        ...
