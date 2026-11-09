# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/popovers/replays_filter_popover_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import Event as Event
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from server_side_replay.gui.impl.gen.view_models.views.lobby.filter_toggle_group_model import FilterToggleGroupModel as FilterToggleGroupModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.popovers.filter_popover_vehicle_model import FilterPopoverVehicleModel as FilterPopoverVehicleModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.popovers.replays_filter_popover_model import ReplaysFilterPopoverModel as ReplaysFilterPopoverModel, VehicleSortColumn as VehicleSortColumn, Checkboxes as Checkboxes
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.common.vehicle_model_helpers import fillVehicleModel as fillVehicleModel
from server_side_replay.gui.impl.lobby.sort_helpers import SortHeap as SortHeap
from server_side_replay.gui.impl.lobby.filter import VEHICLE_FILTER as VEHICLE_FILTER
from server_side_replay.gui.impl.lobby.utils import buildPopoverTankKeySortCriteria as buildPopoverTankKeySortCriteria
from server_side_replay.gui.impl.lobby.filter.state import FilterState as FilterState
from server_side_replay.gui.impl.lobby.utils import buildPopoverTankFilterCriteria as buildPopoverTankFilterCriteria
from gui.impl.pub import PopOverViewImpl as PopOverViewImpl
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
from server_side_replay.gui.impl.lobby.filter import FilterGroupSettings as GroupSettings
from typing import Iterable as Iterable, Optional as Optional, Callable as Callable
FilterGroups: Any

class ReplaysFilterPopoverView(PopOverViewImpl):
    __slots__: tuple
    itemsCache: Any
    __groupSettings: Any
    __onStateUpdated: Any
    __state: Any
    __hasVehicleFilter: Any
    __vehiclesSortColum: Any
    __isVehicleSortAscending: Any
    __canResetCallback: Any
    onTooltipCreated: Any
    def __init__(self, groupSettings, onStateUpdated, state=None, hasVehicleFilter=False, canResetCallback=None):
        ...
    @property
    def viewModel(self):
        ...
    def updateGroupSettings(self, groupSettings):
        ...
    def createToolTip(self, event):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    # decorador original: @args2params(...)
    def __onUpdateFilter(self, groupID, toggleID):
        ...
    # decorador original: @args2params(...)
    def __onSelectVehicleLastDays(self, count):
        ...
    # decorador original: @args2params(...)
    def __onCheckboxSelect(self, checkboxId):
        ...
    # decorador original: @args2params(...)
    def __onSortVehiclesByColumn(self, column):
        ...
    # decorador original: @args2params(...)
    def __onSelectVehicle(self, vehicleCD):
        ...
    def __onResetFilter(self):
        ...
    def __onApplyFilter(self):
        ...
    def __fillModel(self, updateVehicles=True):
        ...
    def __fillVehicleList(self, model):
        ...
