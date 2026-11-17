# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/event_boards/event_boards_vehicles_overlay.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_vos import makeFiltersVO as makeFiltersVO, makeVehicleVO as makeVehicleVO
from gui.Scaleform.daapi.view.lobby.event_boards.event_helpers import LEVELS_RANGE as LEVELS_RANGE
from gui.Scaleform.daapi.view.meta.EventBoardsVehiclesOverlayMeta import EventBoardsVehiclesOverlayMeta as EventBoardsVehiclesOverlayMeta
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS as EVENT_BOARDS
from gui.event_boards.event_boards_items import EVENT_TYPE as EVENT_TYPE
from gui.shared.formatters.vehicle_filters import packVehicleTypesFilter as packVehicleTypesFilter, packVehicleLevelsFilter as packVehicleLevelsFilter, packNationsFilter as packNationsFilter
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import int2roman as int2roman, dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache as IItemsCache

class EventBoardsVehiclesOverlay(EventBoardsVehiclesOverlayMeta):
    itemsCache: Any
    __lid = None
    __opener = None
    __filters: dict
    def setOpener(self, view):
        ...
    def changeFilter(self, lid):
        ...
    def applyFilters(self, nation, vehicleType, level, isMain, compatibleOnly):
        ...
    def _setData(self):
        ...
