# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/battle_pass.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from functools import partial as partial, wraps as wraps
import AccountCommands as AccountCommands
from battle_pass_common import BATTLE_PASS_PDATA_KEY as BATTLE_PASS_PDATA_KEY
from py2to3.backport.inspect import getargspec as getargspec
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
_logger: Any

class BattlePassManager(object):
    __syncData: Any
    __cache: Any
    __commandsProxy: Any
    _ignore: Any
    def __init__(self, syncData, clientCommandsProxy):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def synchronize(self, isFullSync, diff):
        ...
    # decorador original: @_handleNonPlayerIgnoreState
    def getCache(self, callback=None):
        ...
    # decorador original: @_handleNonPlayerIgnoreState
    def activateChapter(self, chapterID, seasonID, callback=None):
        ...
    def __onGetCacheResponse(self, callback, resultID):
        ...

def _handleNonPlayerIgnoreState(func):
    ...
def _makeProxy(callback):
    ...
