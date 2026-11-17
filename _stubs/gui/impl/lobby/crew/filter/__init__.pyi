# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/filter/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from gui import GUI_NATIONS as GUI_NATIONS, TANKMEN_ROLES_ORDER_DICT as TANKMEN_ROLES_ORDER_DICT
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.common.filter_toggle_group_model import ToggleGroupType as ToggleGroupType, FilterToggleGroupModel as FilterToggleGroupModel, FilterToggleButtonModel as FilterToggleButtonModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.personal_data_card_model import DataCardFilter as DataCardFilter
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanLocation as TankmanLocation, TankmanKind as TankmanKind
from gui.impl.lobby.crew.filter.state import FilterState as FilterState
from gui.shared.gui_items.Vehicle import VEHICLE_TYPES_ORDER as VEHICLE_TYPES_ORDER
from typing import Iterable as Iterable, Optional as Optional
from frameworks.wulf import PyResAccessor as PyResAccessor
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

def getNationSettings(customTooltipBody=None):
    ...
def getTankmanKindSettings(labelResId=..., options=None, dismissedTooltipTargetId=...):
    ...
def getTankmanLocationSettings(withTankmanKind=True, labelResId=...):
    ...
def getVehicleLocationSettings():
    ...
def getTankmanRoleSettings(hasDiscount=False):
    ...
def getVehicleTypeSettings(labelResId=..., customTooltipBody=...):
    ...
def getVehicleTierSettings(labelResId=...):
    ...
def getVehicleGradeSettings(options=None, withLocation=False, labelResId=..., tooltipDynAccessor=...):
    ...
def getPersonalDataCardTypeSettings():
    ...
def _createTankmanKindToggle(tankmanKind):
    ...
def _getTankmanLocationToggles():
    ...
