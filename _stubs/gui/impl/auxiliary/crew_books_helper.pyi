# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/auxiliary/crew_books_helper.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from enum import Enum as Enum
from future.utils import iteritems as iteritems, itervalues as itervalues
import BigWorld as BigWorld
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import CREW_BOOKS_VIEWED as CREW_BOOKS_VIEWED
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers.dependency import descriptor as descriptor
from items import tankmen as tankmen
from items.components.crew_books_constants import CREW_BOOK_RARITY as CREW_BOOK_RARITY
from nations import INDICES as INDICES, NONE_INDEX as NONE_INDEX
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
MIN_ROLE_LEVEL = 100
MAX_SKILL_VIEW_COUNT = 4
_g_crewBooksViewedCache = None

class _CrewBooksViewedCache(object):
    _itemsCache: Any
    _lobbyContext: Any
    __viewedItems: Any
    __userLogin: Any
    __booksCountByNation: Any
    __state: Any
    class STATE(Enum):
        DEFAULT = 0
        UPDATE = 1
        RESYNC = 2
    def __init__(self):
        ...
    @property
    def userLogin(self):
        ...
    def addViewedItems(self, nationID):
        ...
    def haveNewCrewBooks(self):
        ...
    def xppToConvert(self):
        ...
    def rewardBookId(self):
        ...
    @property
    def newCrewBooksAmount(self):
        ...
    @property
    def crewBooksAmount(self):
        ...
    @property
    def isCrewBookAvailable(self):
        ...
    def onCrewBooksUpdated(self, diff):
        ...
    def destroy(self):
        ...
    def _setState(self, value=...):
        ...
    def __onDisconnected(self):
        ...
    def __onCacheResync(self, reason, diff):
        ...
    def __syncOwnedItems(self):
        ...
    def __setBooksCount(self, bookType, nationID, count):
        ...
    def __getNationID(self, nationName):
        ...

def crewBooksViewedCache():
    ...
