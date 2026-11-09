# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/client_ranked.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import AccountCommands as AccountCommands
import season_common as season_common
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from helpers import time_utils as time_utils

class ClientRanked(object):
    __account: Any
    __syncData: Any
    __cache: Any
    __ignore: Any
    def __init__(self, syncData):
        ...
    def isEnabled(self):
        ...
    def getSeason(self):
        ...
    def getConfigs(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def setAccount(self, account):
        ...
    def synchronize(self, _, diff):
        ...
    def getCache(self, callback=None):
        ...
    def get(self, itemName, callback):
        ...
    def __onGetCacheResponse(self, callback, resultID):
        ...
    def __onGetResponse(self, itemName, callback, resultID):
        ...

def _skipResponse(resultID, errorCode):
    ...
