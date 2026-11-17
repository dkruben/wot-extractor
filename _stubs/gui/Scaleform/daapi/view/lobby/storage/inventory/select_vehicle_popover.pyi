# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/storage/inventory/select_vehicle_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import nations as nations
from gui import GUI_NATIONS_ORDER_INDEX_REVERSED as GUI_NATIONS_ORDER_INDEX_REVERSED
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import packHeaderColumnData as packHeaderColumnData
from gui.Scaleform.daapi.view.lobby.vehicle_selector_base import VehicleSelectorBase as VehicleSelectorBase
from gui.Scaleform.daapi.view.meta.StorageVehicleSelectPopoverMeta import StorageVehicleSelectPopoverMeta as StorageVehicleSelectPopoverMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.STORAGE import STORAGE as STORAGE
from gui.Scaleform.locale.TANK_CAROUSEL_FILTER import TANK_CAROUSEL_FILTER as TANK_CAROUSEL_FILTER
from gui.shared import events as events, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items.Vehicle import VEHICLE_TABLE_TYPES_ORDER_INDICES_REVERSED as VEHICLE_TABLE_TYPES_ORDER_INDICES_REVERSED
from gui.shared.gui_items.Vehicle import getSmallIconPath as getSmallIconPath, getTypeSmallIconPath as getTypeSmallIconPath
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils import sortByFields as sortByFields
from gui.shared.utils.functions import makeTooltip as makeTooltip
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache as IItemsCache
_SEARCH_INPUT_MAX_CHARS = 50

class VehicleSelectPopoverStorage(StorageVehicleSelectPopoverMeta):
    _vehDP: Any
    def __init__(self, ctx=None):
        ...
    def onWindowClose(self):
        ...
    def _initDP(self):
        ...
    def _dispose(self):
        ...
    def _updateSortField(self):
        ...

class VehicleSelectPopover(VehicleSelectPopoverStorage, VehicleSelectorBase):
    _itemsCache: Any
    _searchStr: Any
    def __init__(self, ctx=None):
        ...
    def applyFilters(self, nation, vehicleType, level, isMain):
        ...
    def updateData(self):
        ...
    def setVehicleSelected(self, intCD, autoClose):
        ...
    def changeSearchNameVehicle(self, inputText):
        ...
    def initFilters(self):
        ...
    def _populate(self):
        ...
    def __updateSearchInput(self):
        ...
    def _makeVehicleVOAction(self, vehicle):
        ...
    def __initControls(self):
        ...

class VehiclesDataProvider(SortableDAAPIDataProvider):
    __list: Any
    _sort: Any
    __sortMapping: Any
    def __init__(self):
        ...
    @property
    def sortedCollection(self):
        ...
    @property
    def collection(self):
        ...
    def emptyItem(self):
        ...
    def pySortOn(self, fields, order):
        ...
    def buildList(self, vehicleVOs):
        ...
    def getLastSortMethod(self):
        ...
    def clear(self):
        ...
    def fini(self):
        ...
    def __sortingMethod(self, item, field):
        ...

def _makeVehicleCmpVO(vehicle):
    ...
