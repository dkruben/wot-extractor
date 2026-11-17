# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_preview/info/bottom_panel_trade_in.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentPreviewVehicle as g_currentPreviewVehicle
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.VehiclePreviewBottomPanelTradeInMeta import VehiclePreviewBottomPanelTradeInMeta as VehiclePreviewBottomPanelTradeInMeta
from gui.Scaleform.genConsts.VEHPREVIEW_CONSTANTS import VEHPREVIEW_CONSTANTS as VEHPREVIEW_CONSTANTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared import event_dispatcher as event_dispatcher, events as events
from gui.shared.formatters import getItemPricesVO as getItemPricesVO, text_styles as text_styles
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from skeletons.gui.game_control import ITradeInController as ITradeInController
from skeletons.gui.shared import IItemsCache as IItemsCache
_RScopeTradeIn = R.strings.vehicle_preview.buyingPanel.tradeIn

class VehiclePreviewBottomPanelTradeIn(VehiclePreviewBottomPanelTradeInMeta):
    __tradeIn: Any
    __itemsCache: Any
    __tradeInVehicleToBuy: Any
    __tradeInVehicleToSell: Any
    __backAlias: Any
    __backCallback: Any
    def __init__(self):
        ...
    def onBuyClick(self):
        ...
    def setBackAlias(self, backAlias):
        ...
    def setBackCallback(self, backCallback):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _onRegisterFlashComponent(self, viewPy, alias):
        ...
    def __updateData(self, _=None):
        ...
    def __getVO(self):
        ...
    def __updateTradeVehicles(self):
        ...
    def __getSelectedPrice(self):
        ...
    def __getStatus(self):
        ...
    def __onCacheSyncCompleted(self, updateReason, _=None):
        ...
