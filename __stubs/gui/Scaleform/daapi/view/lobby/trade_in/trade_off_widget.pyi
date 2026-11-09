# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/trade_in/trade_off_widget.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.meta.TradeOffWidgetMeta import TradeOffWidgetMeta as TradeOffWidgetMeta
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity as EventSystemEntity
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.shop import showTradeOffOverlay as showTradeOffOverlay
from gui.shared import events as events
from gui.shared.gui_items import Vehicle as Vehicle
from gui.shared.gui_items.Vehicle import getSmallIconPath as getSmallIconPath
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from helpers import dependency as dependency
from items import UNDEFINED_ITEM_CD as UNDEFINED_ITEM_CD
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import ITradeInController as ITradeInController
from skeletons.gui.shared import IItemsCache as IItemsCache
_DEFAULT_TRADE_IN_VEHICLE_LEVEL = 10

class TradeOffWidget(TradeOffWidgetMeta, EventSystemEntity):
    __tradeIn: Any
    __itemsCache: Any
    __appLoader: Any
    __toolTipMgr: Any
    __tradeInVehicle: Any
    def __init__(self):
        ...
    def setTradeInVehicle(self, tradeInVehicle):
        ...
    def onClick(self):
        ...
    def onResetClick(self):
        ...
    def getTooltip(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onTradeOffSelectedChanged(self, _=None):
        ...
    def __setData(self, vehicle=None):
        ...
    def __createVO(self, vehicle=None):
        ...
    def __onCacheSyncCompleted(self, updateReason, _=None):
        ...
