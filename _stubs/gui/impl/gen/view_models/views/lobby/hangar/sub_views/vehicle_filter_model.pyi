# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/hangar/sub_views/vehicle_filter_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel

class RoleSection(Enum):
    LIGHTTANK = 'light_tank'
    MEDIUMTANK = 'medium_tank'
    HEAVYTANK = 'heavy_tank'
    ATSPG = 'at_spg'

class FilterSection(Enum):
    NATIONS = 'nations'
    VEHICLETYPES = 'vehicle_types'
    LEVELS = 'levels'
    SPECIALS = 'specials'
    TEXTSEARCH = 'text_search'
    ROLES = 'roles'
    BATTLEPASS = 'battle_pass'

class VehicleFilterModel(ViewModel):
    __slots__: tuple
    onSaveFilter: Any
    onCarouselTypeChange: Any
    onResetFilter: Any
    def __init__(self, properties=4, commands=3):
        ...
    def getFilters(self):
        ...
    def setFilters(self, value):
        ...
    def getDefaultFilters(self):
        ...
    def setDefaultFilters(self, value):
        ...
    def getNationsOrder(self):
        ...
    def setNationsOrder(self, value):
        ...
    @staticmethod
    def getNationsOrderType():
        ...
    def getCarouselRowCount(self):
        ...
    def setCarouselRowCount(self, value):
        ...
    def _initialize(self):
        ...
