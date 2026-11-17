# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/achievements20.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from functools import partial as partial
import AccountCommands as AccountCommands
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from typing import Callable as Callable, Dict as Dict, Optional as Optional

class Achievements20(object):
    __cache: Any
    __ignore: Any
    __syncData: Any
    __commandsProxy: Any
    __account: Any
    def __init__(self, syncData, commandsProxy):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def getCache(self, callback=None):
        ...
    def setAccount(self, account):
        ...
    def synchronize(self, isFullSync, diff):
        ...
    def setAchievementsLayout(self, layout, callback):
        ...
    def __onGetCacheResponse(self, callback, resultID):
        ...
