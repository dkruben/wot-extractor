# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/gen/view_models/views/lobby/filter_toggle_group_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen import R as R
from server_side_replay.gui.impl.gen.view_models.views.lobby.filter_toggle_button_model import FilterToggleButtonModel as FilterToggleButtonModel

class ToggleGroupType(Enum):
    DEFAULT = 'default'
    NATION = 'nation'
    LOCATION = 'location'
    TANKMANROLE = 'tankmanRole'
    TANKMANKIND = 'tankmanKind'
    VEHICLEGRADE = 'vehicleGrade'
    VEHICLETIER = 'vehicleTier'
    VEHICLETYPE = 'vehicleType'
    PERSONALDATATYPE = 'personalDataType'
    VEHICLECD = 'vehicle'

class FilterToggleGroupModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=5, commands=0):
        ...
    def getLabel(self):
        ...
    def setLabel(self, value):
        ...
    def getId(self):
        ...
    def setId(self, value):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getHasDiscount(self):
        ...
    def setHasDiscount(self, value):
        ...
    def getFilters(self):
        ...
    def setFilters(self, value):
        ...
    @staticmethod
    def getFiltersType():
        ...
    def _initialize(self):
        ...
