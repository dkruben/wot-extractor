# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/filters/filter_by_type.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import copy as copy
import typing as typing
from builtins import filter as filter
from future.utils import viewvalues as viewvalues
from frameworks.wulf import PyResAccessor as PyResAccessor
from helpers import dependency as dependency
from constants import SwitchState as SwitchState
from account_helpers import AccountSettings as AccountSettings
from gui import GUI_NATIONS_ORDER_INDICES as GUI_NATIONS_ORDER_INDICES
from gui.Scaleform.daapi.view.lobby.storage import storage_helpers as storage_helpers
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import IN_GROUP_SORT_KEYS as IN_GROUP_SORT_KEYS
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import TABS_SORT_ORDER as TABS_SORT_ORDER
from gui.Scaleform.daapi.view.meta.ItemsWithTypeFilterTabViewMeta import ItemsWithTypeFilterTabViewMeta as ItemsWithTypeFilterTabViewMeta
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showBattleBoosterSellDialog as showBattleBoosterSellDialog
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from items import UNDEFINED_ITEM_CD as UNDEFINED_ITEM_CD
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from gui.shared.event_dispatcher import showSellDialog as showSellDialog
from typing import Dict as Dict, Union as Union, Callable as Callable

class FiltrableInventoryCategoryByTypeTabView(ItemsWithTypeFilterTabViewMeta):
    filterItems = None
    _filterMask: Any
    _totalCount: Any
    _currentCount: Any
    def __init__(self):
        ...
    def setActiveState(self, isActive):
        ...
    def sellItem(self, itemId):
        ...
    def onFiltersChange(self, filters):
        ...
    def resetFilter(self):
        ...
    def _parseLoadedFilters(self, filterDict):
        ...
    def _prepareDataForFilterSaving(self):
        ...
    def _getClientSectionKey(self):
        ...
    def _getFilteredCriteria(self):
        ...
    def _initFilter(self):
        ...
    def _getTypeFilters(self, items):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _buildItems(self):
        ...
    def _getVO(self, item):
        ...
    def _getVoList(self):
        ...
    def containItemType(self, itemType):
        ...
    def _getItemSortKey(self, item):
        ...
    def _getInitFilterItems(self):
        ...
    def _shouldShowCounter(self):
        ...
    def __loadFilters(self):
        ...
    def __saveFilters(self):
        ...
    def __updateUI(self):
        ...
    def __updateFilterCounter(self):
        ...
    def __updateScreen(self):
        ...
    def __onCacheResync(self, *args):
        ...

class FiltrableRegularCategoryByTypeTabView(FiltrableInventoryCategoryByTypeTabView):
    _lobbyContext: Any
    def _getItemList(self):
        ...

def processFilterEntry(item, field, calculator):
    ...
