# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client_common/shared_utils/account_helpers/BattleResultsCache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
import zlib as zlib
from functools import partial as partial
from future.moves import pickle as pickle
from future.utils import viewitems as viewitems
import BigWorld as BigWorld
import AccountCommands as AccountCommands
import constants as constants
from battle_results_shared import VehicleInteractionDetails as VehicleInteractionDetails
from battle_results import unpackClientBattleResults as unpackClientBattleResults
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from external_strings_utils import unicode_from_utf8 as unicode_from_utf8
from py2to3.compat import base64compat as base64compat
BATTLE_RESULTS_VERSION = 1
CACHE_DIR: Any

class BattleResultsCache(object):
    __account: Any
    __ignore: Any
    __waiting: Any
    def __init__(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def setAccount(self, account):
        ...
    def get(self, arenaUniqueID, callback):
        ...
    def getOther(self, arenaUniqueID, resultsSubUrl, callback):
        ...
    def __checkErrorsAndGetFromCache(self, arenaUniqueID, uniqueFolderName):
        ...
    def __onGetResponse(self, callback, resultsSubUrl, requestID, resultID, errorStr, ext=None):
        ...
    def __onStreamComplete(self, callback, resultsSubUrl, isSuccess, data):
        ...

def save(accountName, battleResults):
    ...
def load(uniqueFolderName, arenaUniqueID):
    ...
def getFolderName(uniqueFolderName, arenaUniqueID):
    ...
def clean():
    ...
def convertToFullForm(compactForm):
    ...
