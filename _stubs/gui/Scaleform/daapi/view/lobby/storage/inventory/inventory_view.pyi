# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/inventory_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
from gui import GUI_NATIONS_ORDER_INDICES as GUI_NATIONS_ORDER_INDICES
from gui.Scaleform.daapi.view.lobby.storage import storage_helpers as storage_helpers
from gui.Scaleform.daapi.view.lobby.storage.category_view import InventoryCategoryView as InventoryCategoryView
from gui.Scaleform.daapi.view.meta.StorageCategoryStorageViewMeta import StorageCategoryStorageViewMeta as StorageCategoryStorageViewMeta
from gui.Scaleform.genConsts.STORAGE_CONSTANTS import STORAGE_CONSTANTS as STORAGE_CONSTANTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.crew_book import orderKey as crewBookOrderKey
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.storage_novelty import IStorageNovelty as IStorageNovelty
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from constants import SwitchState as SwitchState
from gui.shared.event_dispatcher import showSellDialog as showSellDialog
VERSION = 1
_TABS_DATA: tuple
_TABS_ITEM_TYPES: dict
TABS_SORT_ORDER: dict
_OPT_DEVICE_TYPE_ORDER: tuple
IN_GROUP_SORT_KEYS: dict

class InventoryCategoryStorageView(StorageCategoryStorageViewMeta):
    __storageNovelty: Any
    __currentTabId: Any
    __views: Any
    def __init__(self):
        ...
    def onOpenTab(self, index):
        ...
    def setActiveState(self, isActive):
        ...
    def setActiveTab(self, tabId):
        ...
    def getTabsData(self):
        ...
    def _populate(self):
        ...
    def _destroy(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def _updateTabCounters(self):
        ...

class RegularInventoryCategoryTabView(InventoryCategoryView):
    __lobbyContext: Any
    _currentTabId: Any
    def __init__(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _sellItems(self, itemId):
        ...
    def setTabId(self, tabId):
        ...
    def _getItemList(self):
        ...
    def _getItemTypeID(self):
        ...
    def _getRequestCriteria(self, invVehicles):
        ...
    def _getVO(self, item):
        ...
    def _getItemSortKey(self, item):
        ...
    def __onCacheResync(self, *args):
        ...

def _getTabDataIndexById(tabID):
    ...
def _defaultInGroupSortKey(item):
    ...
def _getDeviceCategoriesOrder(optDevice):
    ...
def _optionalDevicesSortKey(item):
    ...
def _shellsSortKey(item):
    ...
def _gunsSortKey(item):
    ...
def _crewBookSortKey(item):
    ...
