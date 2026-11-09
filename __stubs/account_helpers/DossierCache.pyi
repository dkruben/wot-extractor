# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/DossierCache.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import os as os
from future.moves import pickle as pickle
from future.utils import viewvalues as viewvalues
import BigWorld as BigWorld
import AccountCommands as AccountCommands
from account_helpers.SyncController import SyncController as SyncController
from PlayerEvents import g_playerEvents as events
from constants import DOSSIER_TYPE as DOSSIER_TYPE
from external_strings_utils import unicode_from_utf8 as unicode_from_utf8
from py2to3.compat import base64compat as base64compat
from debug_utils import LOG_DEBUG as LOG_DEBUG, LOG_ERROR as LOG_ERROR, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION

class DossierCache(object):
    __account: Any
    __syncController: Any
    __cacheDir: Any
    __cacheFileName: Any
    __cache: Any
    __maxChangeTime: Any
    __version: Any
    __ignore: Any
    __isSynchronizing: Any
    __syncID: Any
    __isFirstSync: Any
    def __init__(self, accountName, accountClassName):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def setAccount(self, account):
        ...
    def synchronize(self):
        ...
    def resynchronize(self, isFullResync=False):
        ...
    def waitForSync(self, callback):
        ...
    def get(self, dossierType, ownerID, callback=None):
        ...
    def getCache(self, callback=None):
        ...
    def __get(self, getterFromCache, default, callback):
        ...
    def __onSyncResponse(self, syncID, resultID, ext=None):
        ...
    def __onSyncComplete(self, syncID, data):
        ...
    def __onGetResponse(self, resultID, getterFromCache, default, callback):
        ...
    def __getNextSyncID(self):
        ...
    def __sendSyncRequest(self, syncID, proxy):
        ...
    def __readCache(self):
        ...
    def __writeCache(self):
        ...
