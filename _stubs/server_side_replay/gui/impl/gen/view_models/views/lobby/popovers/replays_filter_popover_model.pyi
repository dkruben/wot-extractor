# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/popovers/replays_filter_popover_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum, IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.filter_toggle_group_model import FilterToggleGroupModel as FilterToggleGroupModel
from server_side_replay.gui.impl.gen.view_models.views.lobby.popovers.filter_popover_vehicle_model import FilterPopoverVehicleModel as FilterPopoverVehicleModel

class VehicleSortColumn(Enum):
    NAME = 'name'
    TIER = 'tier'
    TYPE = 'type'

class Checkboxes(IntEnum):
    PRIMETIME = 0

class ReplaysFilterPopoverModel(ViewModel):
    __slots__: tuple
    onCheckboxSelect: Any
    onLastDaysOptionSelect: Any
    onUpdateFilter: Any
    onSelectVehicle: Any
    onResetFilter: Any
    onApplyFilter: Any
    onSortVehiclesByColumn: Any
    def __init__(self, properties=8, commands=7):
        ...
    def getFilterGroups(self):
        ...
    def setFilterGroups(self, value):
        ...
    @staticmethod
    def getFilterGroupsType():
        ...
    def getVehicles(self):
        ...
    def setVehicles(self, value):
        ...
    @staticmethod
    def getVehiclesType():
        ...
    def getVehicleSortColumn(self):
        ...
    def setVehicleSortColumn(self, value):
        ...
    def getIsVehicleSortAscending(self):
        ...
    def setIsVehicleSortAscending(self, value):
        ...
    def getCanResetFilter(self):
        ...
    def setCanResetFilter(self, value):
        ...
    def getCanApplyFilter(self):
        ...
    def setCanApplyFilter(self, value):
        ...
    def getIsPrimeTime(self):
        ...
    def setIsPrimeTime(self, value):
        ...
    def getSelectedLastDays(self):
        ...
    def setSelectedLastDays(self, value):
        ...
    def _initialize(self):
        ...
