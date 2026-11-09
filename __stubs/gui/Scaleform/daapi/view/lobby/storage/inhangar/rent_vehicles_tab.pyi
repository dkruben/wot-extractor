# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inhangar/rent_vehicles_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform import MENU as MENU
from gui.Scaleform.daapi.view.lobby.storage.inhangar import StorageCarouselDataProvider as StorageCarouselDataProvider, StorageCarouselFilter as StorageCarouselFilter
from gui.Scaleform.daapi.view.meta.RentVehiclesTabViewMeta import RentVehiclesTabViewMeta as RentVehiclesTabViewMeta
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters.time_formatters import RentLeftFormatter as RentLeftFormatter
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers.i18n import makeString as _ms
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IRentalsController as IRentalsController
from skeletons.gui.shared import IItemsCache as IItemsCache

class _RentStorageCarouselFilter(StorageCarouselFilter):
    _clientSections: Any
    _criteriesGroups: Any
    def __init__(self, criteries=None):
        ...
    def save(self):
        ...

class _RentVehiclesDataProvider(StorageCarouselDataProvider):
    _baseCriteria: Any
    def __init__(self, carouselFilter, itemsCache):
        ...
    def _addCriteria(self):
        ...
    def applyFilter(self, forceApply=False):
        ...
    def _buildVehicle(self, vehicle):
        ...

class RentVehiclesTabView(RentVehiclesTabViewMeta):
    _itemsCache: Any
    _rentalsCtrl: Any
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getVO(self, item):
        ...
    def _getItemTypeID(self):
        ...
    def removeItem(self, itemId):
        ...
    def showItemInfo(self, itemId):
        ...
    def _buildItems(self):
        ...
    def _createDataProvider(self):
        ...
    def __onCacheResync(self, reason, diff):
        ...
    def __updateVehicles(self, vehicles=None, filterCriteria=None):
        ...
