# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/client_badges.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import AccountCommands as AccountCommands
_logger: Any

class ClientBadges(object):
    __account: Any
    __syncData: Any
    __cache: Any
    __ignore: Any
    def __init__(self, syncData):
        ...
    def selectBadges(self, badgeList, callback=...):
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
    def get(self, item, callback):
        ...
    def __onGetCacheResponse(self, callback, resultID):
        ...
    def __onGetResponse(self, item, callback, resultID):
        ...

def _skipResponse(resultID, errorCode):
    ...
