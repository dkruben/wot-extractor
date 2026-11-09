# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/trade_in/trade_in_popup.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewitems as viewitems
from gui.Scaleform.daapi.view.lobby.rally.vo_converters import makeVehicleBasicVO as makeVehicleBasicVO
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import packHeaderColumnData as packHeaderColumnData
from gui.Scaleform.daapi.view.meta.TradeInPopupMeta import TradeInPopupMeta as TradeInPopupMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.Scaleform.locale.DIALOGS import DIALOGS as DIALOGS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.utils.functions import makeTooltip as makeTooltip
from gui.shared.money import Currency as Currency
from helpers import dependency as dependency
from skeletons.gui.game_control import ITradeInController as ITradeInController
from gui.shared.tooltips.formatters import packItemActionTooltipData as packItemActionTooltipData
from skeletons.gui.shared import IItemsCache as IItemsCache
_INACCESSIBLE_FOR_TRADE_STATES: tuple

class TradeInPopup(TradeInPopupMeta):
    itemsCache: Any
    tradeIn: Any
    __tradeInDP: Any
    __tradeInVehCD: Any
    __tradeOffVehCD: Any
    def __init__(self, ctx=None):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __initControls(self):
        ...
    def onWindowClose(self):
        ...
    def onSelectVehicle(self, index):
        ...
    def __onResync(self, reason, diff):
        ...
    def __fillDP(self):
        ...

class _TradeInDataProvider(SortableDAAPIDataProvider):
    __list: Any
    __mapping: Any
    __selectedID: Any
    def __init__(self):
        ...
    @property
    def collection(self):
        ...
    def emptyItem(self):
        ...
    def clear(self):
        ...
    def fini(self):
        ...
    def getSelectedIdx(self):
        ...
    def setSelectedID(self, selId):
        ...
    def buildList(self, changedVehsCDs):
        ...
    def pyGetSelectedIdx(self):
        ...
    def pySortOn(self, fields, order):
        ...
    def __rebuildMapping(self):
        ...
    def __makeVO(self, vehicle):
        ...
    def _getItemPriceActionData(self, vehicle):
        ...
