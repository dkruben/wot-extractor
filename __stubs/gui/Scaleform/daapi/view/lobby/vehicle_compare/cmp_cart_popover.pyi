# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_cart_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform import getNationsFilterAssetPath as getNationsFilterAssetPath
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import packHeaderColumnData as packHeaderColumnData
from gui.Scaleform.daapi.view.meta.VehicleCompareCartPopoverMeta import VehicleCompareCartPopoverMeta as VehicleCompareCartPopoverMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.prb_control.dispatcher import g_prbLoader as g_prbLoader
from gui.shared.event_dispatcher import showVehicleCompare as showVehicleCompare
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import getTypeSmallIconPath as getTypeSmallIconPath
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from nations import AVAILABLE_NAMES as AVAILABLE_NAMES
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache

class VehicleCompareCartPopover(VehicleCompareCartPopoverMeta):
    comparisonBasket: Any
    lobbyContext: Any
    _cartDP: Any
    def remove(self, vehId):
        ...
    def removeAll(self):
        ...
    def onWindowClose(self):
        ...
    def gotoCompareView(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __onVehCmpBasketStateChanged(self):
        ...
    def __initControls(self):
        ...
    def __onBasketChange(self, _):
        ...
    def __updateButtonsState(self):
        ...
    def __onServerSettingChanged(self, diff):
        ...

class _VehicleCompareCartDataProvider(SortableDAAPIDataProvider):
    itemsCache: Any
    comparisonBasket: Any
    _list: Any
    _listMapping: Any
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
    def setFlashObject(self, movieClip, autoPopulate=True, setScript=True):
        ...
    def getVO(self, index):
        ...
    def buildList(self, changedVehsCDs):
        ...
    def rebuildList(self, cache):
        ...
    def pyGetSelectedIdx(self):
        ...
    def refreshRandomItems(self, indexes, items):
        ...
    def refreshSingleItem(self, index, item):
        ...
    def _makeVO(self, vehicleCD, index):
        ...
    def __basketChanged(self, *args):
        ...
