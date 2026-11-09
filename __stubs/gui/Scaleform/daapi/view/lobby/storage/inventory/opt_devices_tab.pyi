# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/opt_devices_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import OrderedDict as OrderedDict
from enum import IntEnum as IntEnum
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.shared.event_dispatcher import showSellDialog as showSellDialog
from gui.Scaleform.daapi.view.meta.StorageDevicesTabViewMeta import StorageDevicesTabViewMeta as StorageDevicesTabViewMeta
from gui.Scaleform.daapi.view.lobby.storage.inventory.inventory_view import TABS_SORT_ORDER as TABS_SORT_ORDER, IN_GROUP_SORT_KEYS as IN_GROUP_SORT_KEYS
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyOptionalDevicesUrl as getBuyOptionalDevicesUrl
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.money import Currency as Currency
from gui.shared.gui_items.items_actions import factory as ItemsActionsFactory
from gui.shared.event_dispatcher import showShop as showShop
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
_TYPE_FILTER_ITEMS: list
_BIT_TO_DEVICE_TYPE_MAP: Any

class _OptDeviceTypeFilter(IntEnum):
    ALL = 0
    SIMPLE = 1
    DELUXE = 2
    TROPHY = 4
    MODERNIZED = 8

class OptDevicesTabView(StorageDevicesTabViewMeta):
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getTypeFilters(self, items):
        ...
    def navigateToStore(self):
        ...
    def upgradeItem(self, itemId):
        ...
    def _initFilter(self):
        ...
    def _getClientSectionKey(self):
        ...
    def _getItemTypeID(self):
        ...
    def _getFilteredCriteria(self):
        ...
    def _getRequestCriteria(self, invVehicles):
        ...
    def _getItemSortKey(self, item):
        ...
    def _buildItems(self):
        ...
    def sellItem(self, itemId):
        ...
    def __onClientUpdate(self, diff, _):
        ...
    def __updateBalance(self):
        ...
