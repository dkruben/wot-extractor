# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inhangar/restore_vehicles_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui import DialogsInterface as DialogsInterface
from gui.Scaleform.daapi.view.dialogs.ExchangeDialogMeta import RestoreExchangeCreditsMeta as RestoreExchangeCreditsMeta
from gui.Scaleform.daapi.view.lobby.storage.inhangar import StorageCarouselDataProvider as StorageCarouselDataProvider, StorageCarouselFilter as StorageCarouselFilter
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getVehicleRestoreInfo as getVehicleRestoreInfo, enoughCreditsForRestore as enoughCreditsForRestore
from gui.Scaleform.daapi.view.meta.RestoreVehiclesTabViewMeta import RestoreVehiclesTabViewMeta as RestoreVehiclesTabViewMeta
from gui.Scaleform.genConsts.CONTEXT_MENU_HANDLER_TYPE import CONTEXT_MENU_HANDLER_TYPE as CONTEXT_MENU_HANDLER_TYPE
from gui.shared import event_dispatcher as shared_events
from gui.shared.formatters import getItemPricesVO as getItemPricesVO
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IRestoreController as IRestoreController
from adisp import adisp_process as adisp_process
from gui.impl import backport as backport
from gui.impl.gen import R as R

class _RestoreStorageCarouselFilter(StorageCarouselFilter):
    _clientSections: Any
    _criteriesGroups: Any
    def __init__(self, criteries=None):
        ...
    def save(self):
        ...

class _RestoreVehiclesDataProvider(StorageCarouselDataProvider):
    _baseCriteria: Any
    def __init__(self, carouselFilter, itemsCache):
        ...
    def _addCriteria(self):
        ...
    def applyFilter(self, forceApply=False):
        ...
    def _buildVehicle(self, vehicle):
        ...

class RestoreVehiclesTabView(RestoreVehiclesTabViewMeta):
    _restoreCtrl: Any
    # decorador original: @adisp_process
    def restoreItem(self, itemId):
        ...
    def showItemInfo(self, itemId):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _createDataProvider(self):
        ...
    def _onCacheResync(self, reason, diff):
        ...
    def __updateVehicles(self, vehicles=None, filterCriteria=None):
        ...
