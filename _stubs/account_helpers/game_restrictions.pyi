# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/game_restrictions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import AccountCommands as AccountCommands
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
_logger: Any
_CACHE_DIFF_KEY = 'cache'
_GAME_RESTRICTIONS_KEY = 'gameRestrictions'

class GameRestrictions(object):
    __syncData: Any
    __cache: Any
    __ignore: Any
    def __init__(self, syncData):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def getCache(self, callback=None):
        ...
    def synchronize(self, isFullSync, diff):
        ...
    def __onGetCacheResponse(self, callback, resultID):
        ...
