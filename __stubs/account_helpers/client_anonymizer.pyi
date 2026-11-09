# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/client_anonymizer.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import AccountCommands as AccountCommands
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
_logger: Any
_ANONYMIZER_KEY = 'anonymizer'

class ClientAnonymizer(object):
    __syncData: Any
    __account: Any
    __cache: Any
    __ignore: Any
    def __init__(self, syncData):
        ...
    def clear(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def setAccount(self, account):
        ...
    def setAnonymized(self, anonymized=True, callback=...):
        ...
    def synchronize(self, isFullSync, diff):
        ...
    def getCache(self, callback=None):
        ...
    def __onGetCacheResponse(self, callback, resultID):
        ...

def _printResponse(resultID, errorCode):
    ...
