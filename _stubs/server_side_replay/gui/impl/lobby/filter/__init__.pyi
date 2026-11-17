# wot-extractor: STUB (.pyi) gerado a partir de sources/res/server_side_replay/scripts/client/server_side_replay/gui/impl/lobby/filter/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from builtins import str as str
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from gui import GUI_NATIONS as GUI_NATIONS
from gui.impl.gen import R as R
from server_side_replay.gui.impl.gen.view_models.views.lobby.filter_toggle_group_model import ToggleGroupType as ToggleGroupType, FilterToggleGroupModel as FilterToggleGroupModel, FilterToggleButtonModel as FilterToggleButtonModel
from server_side_replay.gui.impl.lobby.filter.state import FilterState as FilterState
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER
from typing import Iterable as Iterable, Optional as Optional
VEHICLE_FILTER = 'vehicle'
VEHICLE_LOCATION_IN_HANGAR = 'in_hangar'
GRADE_PREMIUM = 'premium'
GRADE_ELITE = 'elite'
GRADE_PRIMARY = 'primary'
VEHICLE_GRADES: tuple
SEARCH_MAX_LENGTH = 50

class ToggleButtonSettings(object):
    id: Any
    icon: Any
    tooltipHeader: Any
    tooltipBody: Any
    tooltipContentId: Any
    tooltipTargetId: Any
    counter: Any
    def __init__(self, toggleID, icon=..., tooltipHeader=..., tooltipBody=..., tooltipContentId=..., tooltipTargetId=..., counter=0):
        ...
    def pack(self, model, state=None):
        ...

class FilterGroupSettings(object):
    id: Any
    labelResId: Any
    toggleType: Any
    toggles: Any
    hasDiscount: Any
    def __init__(self, toggleID, labelResId, toggleType, toggles, hasDiscount=False):
        ...
    def pack(self, model, state=None):
        ...

def getNationSettings():
    ...
def getVehicleTypeSettings(labelResId=..., customTooltipBody=...):
    ...
def getVehicleTierSettings(labelResId=...):
    ...
