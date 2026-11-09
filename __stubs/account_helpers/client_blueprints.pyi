# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/client_blueprints.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from functools import partial as partial
from future.utils import viewitems as viewitems
import AccountCommands as AccountCommands
from gui.shared.utils.requesters.blueprints_requester import getFragmentNationID as getFragmentNationID
from helpers import dependency as dependency
from items import vehicles as vehicles
from shared_utils.account_helpers.diff_utils import synchronizeDicts as synchronizeDicts
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
_BLUEPRINT_KEY = 'blueprints'

class ClientBlueprints(object):
    __itemsCache: Any
    __account: Any
    __ignore: Any
    __syncData: Any
    __cache: Any
    def __init__(self, syncData=None):
        ...
    def clear(self):
        ...
    def setAccount(self, account):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def synchronize(self, isFullSync, diff):
        ...
    def getCache(self, callback=None):
        ...
    def get(self, callback):
        ...
    def convertBlueprintFragment(self, fragmentTypeCD, position, requestedCount, usedNationalFragments, callback):
        ...
    def markFragmentsAsSeen(self, fragmentCDs, callback):
        ...
    def __onGetCacheResponse(self, callback, resultID):
        ...
    def __onGetResponse(self, callback, resultID):
        ...
