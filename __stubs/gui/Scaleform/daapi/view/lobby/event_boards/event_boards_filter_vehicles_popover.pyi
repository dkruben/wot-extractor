# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_filter_vehicles_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_vos import makeVehiclePopoverVO as makeVehiclePopoverVO, vehicleValueGetter as vehicleValueGetter
from gui.Scaleform.daapi.view.lobby.vehicle_compare.formatters import packHeaderColumnData as packHeaderColumnData
from gui.Scaleform.daapi.view.lobby.vehicle_selector_base import VehicleSelectorBase as VehicleSelectorBase
from gui.Scaleform.daapi.view.meta.EventBoardsResultFilterVehiclesPopoverViewMeta import EventBoardsResultFilterVehiclesPopoverViewMeta as EventBoardsResultFilterVehiclesPopoverViewMeta
from gui.Scaleform.framework.entities.DAAPIDataProvider import SortableDAAPIDataProvider as SortableDAAPIDataProvider
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS as EVENT_BOARDS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils import sortByFields as sortByFields
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache as IItemsCache

class EventBoardsFilterVehiclesPopover(EventBoardsResultFilterVehiclesPopoverViewMeta, VehicleSelectorBase):
    itemsCache: Any
    caller: Any
    eventID: Any
    _vehDP: Any
    __eventData: Any
    __onChangeFilter: Any
    __selectedVehicleCD: Any
    def __init__(self, ctx=None):
        ...
    def initFilters(self):
        ...
    def applyFilters(self, nation, vehicleType, level, isMain, hangarOnly):
        ...
    def updateData(self):
        ...
    def onWindowClose(self):
        ...
    def setData(self, eventData, onApply, leaderboardID=None):
        ...
    def setVehicleSelected(self, dbID):
        ...
    def resetFilters(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _makeVehicleVOAction(self, vehicle):
        ...
    def __initControls(self):
        ...
    def __updateSortField(self):
        ...

class VehiclesDataProvider(SortableDAAPIDataProvider):
    __list: Any
    _sort: Any
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
    def buildList(self, vehicleVOs, selected=None):
        ...
    def getLastSortMethod(self):
        ...
    def clear(self):
        ...
    def fini(self):
        ...
    def __sort(self):
        ...
    def __selectVehicle(self, vehCD):
        ...
