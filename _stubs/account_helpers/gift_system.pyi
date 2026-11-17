# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/gift_system.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from functools import partial as partial
import AccountCommands as AccountCommands
from gui.gift_system.wrappers import GiftsHistoryData as GiftsHistoryData
from shared_utils import makeTupleByDict as makeTupleByDict
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
_logger: Any
_CACHE_DIFF_KEY = 'cache'
_GIFT_SYSTEM_KEY = 'giftsData'

class _RequestHistoryProxy(object):
    __reqEventIds: Any
    __callback: Any
    def __init__(self, reqEventIds, callback):
        ...
    def __call__(self, requestID, resultID, errorStr, ext=None):
        ...

class GiftSystem(object):
    __cache: Any
    __ignore: Any
    __syncData: Any
    __commandsProxy: Any
    def __init__(self, syncData, commandsProxy):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def getCache(self, callback=None):
        ...
    def requestGiftsHistory(self, reqEventIds, callback):
        ...
    def synchronize(self, isFullSync, diff):
        ...
    def __onGetCacheResponse(self, callback, resultID):
        ...

def _packEventHistoryData(eventExt):
    ...
