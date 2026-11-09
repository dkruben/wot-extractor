# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/ClientBattleRoyale.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import AccountCommands as AccountCommands
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV

class ClientBattleRoyale(object):
    __DATA_KEY = 'battleRoyale'
    __account: Any
    __syncData: Any
    __cache: Any
    __ignore: Any
    def __init__(self, syncData):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def setAccount(self, account):
        ...
    def synchronize(self, isFullSync, diff):
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
