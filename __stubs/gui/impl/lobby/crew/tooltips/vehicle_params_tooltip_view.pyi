# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/crew/tooltips/vehicle_params_tooltip_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import collections as collections
from functools import partial as partial
from typing import TYPE_CHECKING as TYPE_CHECKING
import constants as constants
from CurrentVehicle import g_currentVehicle as g_currentVehicle, g_currentPreviewVehicle as g_currentPreviewVehicle
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.crew.tooltips.vehicle_params_category import VehicleParamsCategory as VehicleParamsCategory
from gui.impl.gen.view_models.views.lobby.crew.tooltips.vehicle_params_item import VehicleParamsItem as VehicleParamsItem, ValueStyleEnum as ValueStyleEnum
from gui.impl.gen.view_models.views.lobby.crew.tooltips.vehicle_params_note import VehicleParamsNote as VehicleParamsNote, NoteThemeEnum as NoteThemeEnum
from gui.impl.gen.view_models.views.lobby.crew.tooltips.vehicle_params_tooltip_view_model import VehicleParamsTooltipViewModel as VehicleParamsTooltipViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.gui_items import KPI as KPI
from gui.shared.items_parameters import isTemperatureGun as isTemperatureGun
from gui.shared.items_parameters import formatters as param_formatter
from gui.shared.items_parameters.bonus_helper import isSituationalBonus as isSituationalBonus, isAppropriateVehicle as isAppropriateVehicle
from gui.shared.items_parameters.comparator import combineParameterInfos as combineParameterInfos
from gui.shared.items_parameters.formatters import isRelativeParameter as isRelativeParameter
from gui.shared.items_parameters.param_name_helper import getVehicleParameterText as getVehicleParameterText
from gui.shared.items_parameters.params_constants import PIERCING_DISTANCES as PIERCING_DISTANCES
from gui.shared.utils import CHASSIS_REPAIR_TIME as CHASSIS_REPAIR_TIME, SHOT_DISPERSION_ANGLE as SHOT_DISPERSION_ANGLE, DUAL_ACCURACY_COOLING_DELAY as DUAL_ACCURACY_COOLING_DELAY, ROCKET_ACCELERATION_ENGINE_POWER as ROCKET_ACCELERATION_ENGINE_POWER, RELOAD_TIME_SECS_PROP_NAME as RELOAD_TIME_SECS_PROP_NAME, RELOAD_TIME_PROP_NAME as RELOAD_TIME_PROP_NAME, TURBOSHAFT_ENGINE_POWER as TURBOSHAFT_ENGINE_POWER, TURBOSHAFT_INVISIBILITY_MOVING_FACTOR as TURBOSHAFT_INVISIBILITY_MOVING_FACTOR, TURBOSHAFT_INVISIBILITY_STILL_FACTOR as TURBOSHAFT_INVISIBILITY_STILL_FACTOR, DUAL_GUN_CHARGE_TIME as DUAL_GUN_CHARGE_TIME, AUTO_RELOAD_PROP_NAME as AUTO_RELOAD_PROP_NAME, AIMING_TIME_PROP_NAME as AIMING_TIME_PROP_NAME, AUTO_SHOOT_CLIP_FIRE_RATE as AUTO_SHOOT_CLIP_FIRE_RATE, isRomanNumberForbidden as isRomanNumberForbidden
from helpers import i18n as i18n
from items import perks as perks, vehicles as vehicles, tankmen as tankmen, parseIntCompactDescr as parseIntCompactDescr
from post_progression_common import ACTION_TYPES as ACTION_TYPES
from typing import Optional as Optional
from gui.shared.gui_items import Vehicle as Vehicle
from gui.shared.tooltips.contexts import HangarParamContext as HangarParamContext
_BONUS_TYPES_ORDER: dict
_CREW_TYPES: tuple
_MULTI_KPI_PARAMS: Any
AUTORELOAD_TIME = 'autoReloadTime'
_PARAMS_WITH_AGGREGATED_PENALTIES: set
_CREW_ICON = 'all'
BonusCreationParams: Any
_TYPE_ITEMS_COMPARATORS: dict

class BaseVehicleParamsTooltipView(ViewImpl):
    __slots__: tuple
    _paramName: Any
    _context: Any
    _supportAdvanced: Any
    _extendedData: Any
    _hasPerksBonuses: Any
    def __init__(self, paramName, context, supportAdvanced):
        ...
    @property
    def vehicle(self):
        ...
    @property
    def viewModel(self):
        ...
    @staticmethod
    def _formatValueText(style, text):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _fillModel(self, model):
        ...

class BaseVehicleAdvancedParamsTooltipView(BaseVehicleParamsTooltipView):
    def _fillModel(self, model):
        ...
    def _hasExtendedInfo(self):
        ...
    def _getAutoReloadTimeDescription(self):
        ...
    def _getAutoReloadTimeExtendedDescription(self):
        ...
    def _getShotDispersionAngleDescription(self, vehicle):
        ...
    def __getTitleStr(self, titleParamName):
        ...

class VehicleAdvancedParamsTooltipView(BaseVehicleAdvancedParamsTooltipView):
    def _fillModel(self, model):
        ...
    def _fillBonuses(self, model):
        ...
    def _fillFootNotes(self, model, hasSituational):
        ...
    def _fillActiveVehicleParamItem(self, itemModel, bonusCreationParams):
        ...
    def _getTooltipGroupingForBonus(self, bonusType, bonusName):
        ...
    def _hasExtendedInfo(self):
        ...
    def _getAutoReloadTimeDescription(self):
        ...
    def _getAutoReloadTimeExtendedDescription(self):
        ...
    @staticmethod
    def __getBonusIcon(bnsID, bnsType, vehPostProgressionBonusLevels, isVehSkillTree=False):
        ...

class VehicleAvgParamsTooltipView(BaseVehicleAdvancedParamsTooltipView):
    _AVG_TO_RANGE_PARAMETER_NAME: dict
    def _fillModel(self, model):
        ...

def _optDeviceCmp(x, y):
    ...
def _bonusCmp(x, y):
    ...
def _getBonusID(bnsType, bnsId):
    ...
def _getBonusName(bnsType, bnsId, enabled=True, archetype=None, isVehSkillTree=False):
    ...
def _isUpgradedInstanceOfInstalled(installedDevices, deviceDescr):
    ...
def _isDowngradedInstanceOfInstalled(installedDevices, deviceDescr):
    ...
