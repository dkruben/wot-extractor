# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inhangar/all_vehicles_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from PlayerEvents import g_playerEvents as g_playerEvents
from gui.filters.carousel_filter import CriteriesGroup as CriteriesGroup
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.storage.inhangar import StorageCarouselDataProvider as StorageCarouselDataProvider, StorageCarouselFilter as StorageCarouselFilter
from gui.Scaleform.daapi.view.lobby.storage.storage_carousel_environment import StorageCarouselEnvironment as StorageCarouselEnvironment
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyVehiclesUrl as getBuyVehiclesUrl
from gui.Scaleform.daapi.view.meta.AllVehiclesTabViewMeta import AllVehiclesTabViewMeta as AllVehiclesTabViewMeta
from gui.Scaleform.locale.STORAGE import STORAGE as STORAGE
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS as TOOLTIPS
from gui.prb_control.ctrl_events import g_prbCtrlEvents as g_prbCtrlEvents
from gui.shared import event_dispatcher as shared_events
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.utils.requesters.ItemsRequester import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.game_control import IIGRController as IIGRController
from gui.shared.event_dispatcher import showShop as showShop

class _AllVehiclesTabCriteriesGroup(CriteriesGroup):
    _criteria: Any
    def update(self, filters):
        ...
    @staticmethod
    def isApplicableFor(vehicle):
        ...

class AllVehiclesTabView(AllVehiclesTabViewMeta, StorageCarouselEnvironment):
    _igrCtrl: Any
    def sellItem(self, itemId):
        ...
    def navigateToStore(self):
        ...
    def applyFilter(self, forceApply=False):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _createDataProvider(self):
        ...
    def __onViewLoaded(self, view, *args, **kwargs):
        ...
    def _onCacheResync(self, reason, diff):
        ...
    def __updateVehicles(self, vehicles=None, filterCriteria=None, forceFilter=False):
        ...
    def __updateIgrType(self, roomType, xpFactor):
        ...
    def __updateFilterWarning(self):
        ...
    def __onVehicleBecomeElite(self, *vehicles):
        ...
    def __onVehicleClientStateChanged(self, vehicles):
        ...
