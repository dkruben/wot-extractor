# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/festivity_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial
import AccountCommands as AccountCommands
from helpers import dependency as dependency
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from skeletons.festivity_factory import IFestivityFactory as IFestivityFactory
_logger: Any

class FestivityManager(object):
    _festivityFactory: Any
    __syncData: Any
    __cache: Any
    __ignore: Any
    __festivityKey: Any
    __commandProxy: Any
    def __init__(self, syncData, clientCommandsProxy):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
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
