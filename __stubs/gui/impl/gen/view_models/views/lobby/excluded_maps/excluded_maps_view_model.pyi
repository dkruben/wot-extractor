# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/excluded_maps/excluded_maps_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.account_dashboard.map_model import MapModel as MapModel
from gui.impl.gen.view_models.views.lobby.excluded_maps.filter_model import FilterModel as FilterModel
from gui.impl.gen.view_models.views.lobby.excluded_maps.map_item_model import MapItemModel as MapItemModel

class MapStateEnum(Enum):
    AVAILABLE = 'Available'
    EXCLUDEDINCOOLDOWN = 'ExcludedInCooldown'
    EXCLUDEDREPLACEABLE = 'ExcludedReplaceable'
    DISABLED = 'Disabled'

class FilterNameEnum(Enum):
    SUMMER = 'summer'
    WINTER = 'winter'
    DESERT = 'desert'

class ExcludedMapsViewModel(ViewModel):
    __slots__: tuple
    onBackAction: Any
    onMapClick: Any
    onMapRemoveFromSlot: Any
    onFilterReset: Any
    onFilterClick: Any
    def __init__(self, properties=6, commands=5):
        ...
    def getMapsSelected(self):
        ...
    def setMapsSelected(self, value):
        ...
    def getMapsTotal(self):
        ...
    def setMapsTotal(self, value):
        ...
    def getIsFilterApplied(self):
        ...
    def setIsFilterApplied(self, value):
        ...
    def getExcludedMaps(self):
        ...
    def setExcludedMaps(self, value):
        ...
    @staticmethod
    def getExcludedMapsType():
        ...
    def getMapFilters(self):
        ...
    def setMapFilters(self, value):
        ...
    @staticmethod
    def getMapFiltersType():
        ...
    def getMaps(self):
        ...
    def setMaps(self, value):
        ...
    @staticmethod
    def getMapsType():
        ...
    def _initialize(self):
        ...
