# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/goodies/storage_novelty.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import SwitchState as SwitchState
import Event as Event
from account_helpers.AccountSettings import AccountSettings as AccountSettings, DEMOUNT_KIT_SEEN as DEMOUNT_KIT_SEEN, RECERTIFICATION_FORM_SEEN as RECERTIFICATION_FORM_SEEN
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.storage_novelty import IStorageNovelty as IStorageNovelty
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class StorageNovelty(IStorageNovelty):
    __goodiesCache: Any
    __itemsCache: Any
    __lobbyContext: Any
    onUpdated: Any
    __showNovelty: Any
    def __init__(self):
        ...
    @property
    def __noveltyData(self):
        ...
    @property
    def showNovelty(self):
        ...
    @property
    def noveltyCount(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def setAsSeen(self, item):
        ...
    @staticmethod
    def getItemsStatus(args):
        ...
    @staticmethod
    def isItemsEnabled(args):
        ...
    def __isRecertificationFormsEnabled(self):
        ...
    def __resolveNovelty(self):
        ...
    def __onGoodiesUpdated(self, *_):
        ...
    def __onCacheResync(self, *_):
        ...
