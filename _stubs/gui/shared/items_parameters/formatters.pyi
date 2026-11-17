# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/items_parameters/formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from builtins import zip as zip
from collections import namedtuple as namedtuple
from future.utils import iteritems as iteritems, lzip as lzip
from itertools import chain as chain
from past.builtins import unicode as unicode
from typing import TYPE_CHECKING as TYPE_CHECKING
from constants import BonusTypes as BonusTypes, DAMAGE_INTERPOLATION_DIST_LAST as DAMAGE_INTERPOLATION_DIST_LAST
from debug_utils import LOG_ERROR as LOG_ERROR
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES as HANGAR_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as TOOLTIPS_CONSTANTS
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import KPI as KPI, kpiFormatValue as kpiFormatValue, kpiFormatNoSignValue as kpiFormatNoSignValue
from gui.shared.items_parameters import RELATIVE_PARAMS as RELATIVE_PARAMS
from gui.shared.items_parameters.comparator import PARAM_STATE as PARAM_STATE
from gui.shared.items_parameters.params_helper import hasGroupPenalties as hasGroupPenalties, getCommonParam as getCommonParam, isValidEmptyValue as isValidEmptyValue, PARAMS_GROUPS as PARAMS_GROUPS
from gui.shared.items_parameters.shell_params import CriticalHitChanceType as CriticalHitChanceType
from gui.shared.utils import AUTO_RELOAD_PROP_NAME as AUTO_RELOAD_PROP_NAME, MAX_STEERING_LOCK_ANGLE as MAX_STEERING_LOCK_ANGLE, WHEELED_SWITCH_ON_TIME as WHEELED_SWITCH_ON_TIME, WHEELED_SWITCH_OFF_TIME as WHEELED_SWITCH_OFF_TIME, WHEELED_SWITCH_TIME as WHEELED_SWITCH_TIME, WHEELED_SPEED_MODE_SPEED as WHEELED_SPEED_MODE_SPEED, DUAL_GUN_CHARGE_TIME as DUAL_GUN_CHARGE_TIME, DUAL_GUN_RATE_TIME as DUAL_GUN_RATE_TIME, TURBOSHAFT_SPEED_MODE_SPEED as TURBOSHAFT_SPEED_MODE_SPEED, TURBOSHAFT_ENGINE_POWER as TURBOSHAFT_ENGINE_POWER, TURBOSHAFT_INVISIBILITY_STILL_FACTOR as TURBOSHAFT_INVISIBILITY_STILL_FACTOR, TURBOSHAFT_INVISIBILITY_MOVING_FACTOR as TURBOSHAFT_INVISIBILITY_MOVING_FACTOR, TURBOSHAFT_SWITCH_TIME as TURBOSHAFT_SWITCH_TIME, CHASSIS_REPAIR_TIME as CHASSIS_REPAIR_TIME, CHASSIS_REPAIR_TIME_YOH as CHASSIS_REPAIR_TIME_YOH, ROCKET_ACCELERATION_ENGINE_POWER as ROCKET_ACCELERATION_ENGINE_POWER, ROCKET_ACCELERATION_SPEED_LIMITS as ROCKET_ACCELERATION_SPEED_LIMITS, ROCKET_ACCELERATION_REUSE_AND_DURATION as ROCKET_ACCELERATION_REUSE_AND_DURATION, DUAL_ACCURACY_COOLING_DELAY as DUAL_ACCURACY_COOLING_DELAY, SHOT_DISPERSION_ANGLE as SHOT_DISPERSION_ANGLE, DISPERSION_RADIUS as DISPERSION_RADIUS, BURST_FIRE_RATE as BURST_FIRE_RATE, BURST_TIME_INTERVAL as BURST_TIME_INTERVAL, BURST_SIZE as BURST_SIZE, BURST_COUNT as BURST_COUNT, AVG_DAMAGE_PER_SECOND as AVG_DAMAGE_PER_SECOND, AUTO_SHOOT_CLIP_FIRE_RATE as AUTO_SHOOT_CLIP_FIRE_RATE, CONTINUOUS_SHOTS_PER_MINUTE as CONTINUOUS_SHOTS_PER_MINUTE, CONTINUOUS_DAMAGE_PER_SECOND as CONTINUOUS_DAMAGE_PER_SECOND, TWIN_GUN_SWITCH_FIRE_MODE_TIME as TWIN_GUN_SWITCH_FIRE_MODE_TIME, TWIN_GUN_TOP_SPEED as TWIN_GUN_TOP_SPEED, TWIN_GUN_RELOAD_ONE_GUN_TIME as TWIN_GUN_RELOAD_ONE_GUN_TIME, TWIN_GUN_RELOAD_TWO_GUN_TIME as TWIN_GUN_RELOAD_TWO_GUN_TIME, TWIN_GUN_RELOAD_TIME as TWIN_GUN_RELOAD_TIME, SHELL_RELOADING_TIME_PROP_NAME as SHELL_RELOADING_TIME_PROP_NAME, SHELL_LOADING_TIME_PROP_NAME as SHELL_LOADING_TIME_PROP_NAME, RELOAD_TIME_PROP_NAME as RELOAD_TIME_PROP_NAME, TEMPERATURE_RELOAD_TIME as TEMPERATURE_RELOAD_TIME, TEMPERATURE_AVG_DAMAGE_PER_MINUTE as TEMPERATURE_AVG_DAMAGE_PER_MINUTE, NORMALIZATION_ANGLE as NORMALIZATION_ANGLE, RICOCHET_ANGLE as RICOCHET_ANGLE, PENETRATION_LOSS as PENETRATION_LOSS, CRITICAL_HIT_CHANCE as CRITICAL_HIT_CHANCE
from helpers.i18n import makeString as makeString, isValidKey as isValidKey
from items import vehicles as vehicles, artefacts as artefacts, getTypeOfCompactDescr as getTypeOfCompactDescr, ITEM_TYPES as ITEM_TYPES
from math_common import decimal_round as decimal_round, round_py2_style as round_py2_style
from web_stubs import i18n as i18n
from typing import Optional as Optional, Tuple as Tuple, Dict as Dict
from gui.shared.items_parameters.comparator import _ParameterInfo as _ParameterInfo
ChangeCondition: Any
MEASURE_UNITS: dict
MEASURE_UNITS_NO_BRACKETS: dict
KPI_FORMATTERS: dict
COLORLESS_SCHEME: tuple
NO_BONUS_SIMPLIFIED_SCHEME: tuple
NO_BONUS_BASE_SCHEME: tuple
SIMPLIFIED_SCHEME: tuple
BASE_SCHEME: tuple
EXTRACTED_BONUS_SCHEME: tuple
SITUATIONAL_SCHEME: tuple
VEHICLE_PARAMS: Any
ITEMS_PARAMS_LIST: dict
FORMAT_NAME_C_S_VALUE_S_UNITS = '{paramName} {paramValue} {paramUnits}'
_COUNT_OF_AUTO_RELOAD_SLOTS_TIMES_TO_SHOW_IN_INFO = 5
_EQUAL_TO_ZERO_LITERAL = '~0'
MULTIPLE_MEASURE_UNITS_PARAMS: dict
CRITICAL_HIT_CHANCE_TYPE_DYN_PATH: dict
MULTIPLE_TITLES_PARAMS: dict
_NBSP: Any
_DASH: Any
_SLASH: Any
_COLON: Any
_niceFormat: dict
_niceRangeFormat: dict
_listFormat: dict
_niceListFormat: dict
_niceListFormatWithoutNone: dict
_integralFormat: dict
_percentFormat: dict
_plusPercentFormat: dict
FORMAT_SETTINGS: dict
DELTA_PARAMS_SETTING: Any
SMART_ROUND_PARAMS: set
_STATES_INDEX_IN_COLOR_MAP: dict

def needUseYohChassisRepairTime(vehicleDescr):
    ...
def formatCriticalHitChance(value, _=None):
    ...
def getMeasureParamName(vehicleDescr, paramName):
    ...
def getMeasureUnitsForParameter(vehicleDescr, paramName):
    ...
def getTitleParamName(vDescr, paramName):
    ...
def measureUnitsForParameter(paramName):
    ...
def isRelativeParameter(paramName):
    ...
def isRelativeParameterVisible(parameter):
    ...
def isDiffEnoughToDisplay(value):
    ...
def getParameterSmallIconPath(parameter):
    ...
def getParameterBigIconPath(parameter):
    ...
def formatModuleParamName(paramName, vDescr=None):
    ...
def formatNameColonValue(nameStr, valueStr):
    ...
def formatParamNameColonValueUnits(paramName, paramValue):
    ...
def formatVehicleParamName(paramName, showMeasureUnit=True):
    ...
def getRelativeDiffParams(comparator):
    ...
def _autoReloadPreprocessor(reloadTimes, rowStates):
    ...
def clipFireRatePreprocessor(values, states):
    ...
def shotDispersionAnglePreprocessor(values, states):
    ...
def _getRoundReload(value):
    ...
def _deltaWrapper(fn):
    ...
def _getDeltaSettings():
    ...
def colorize(paramStr, state, colorScheme):
    ...
def colorizedFormatParameter(parameter, colorScheme):
    ...
def colorizedFullFormatParameter(parameter, colorScheme):
    ...
def simplifiedDeltaParameter(parameter, isSituational=False, isApproximately=False):
    ...
def _applyFormat(value, state, settings, doSmartRound, colorScheme):
    ...
def formatParameter(parameterName, paramValue, parameterState=None, colorScheme=None, formatSettings=None, allowSmartRound=True, showZeroDiff=False):
    ...
def formatParameterDelta(pInfo, deltaScheme=None, formatSettings=None):
    ...
def getFormattedParamsList(descriptor, parameters, excludeRelative=False):
    ...
def getBonusIconRes(bonusId, bonusType, archetype=None):
    ...
def getBonusIcon(bonusId, bonusType, archetype=None):
    ...
def getPenaltyIconRes(penaltyId):
    ...
def getPenaltyIcon(penaltyId):
    ...
def packSituationalIcon(text, icon):
    ...
def getGroupPenaltyIcon(parameter, comparator):
    ...
def getAllParametersTitles(hiddenParams=...):
    ...
def _cutDigits(value):
    ...
