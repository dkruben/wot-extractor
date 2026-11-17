# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/items_parameters/comparator.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import collections as collections
import logging as logging
import sys as sys
import typing as typing
from future.utils import iteritems as iteritems
from constants import BonusTypes as BonusTypes
from gui.shared.gui_items import KPI as KPI
from gui.shared.items_parameters import params_cache as params_cache
from math_common import decimal_round as decimal_round, round_py2_style as round_py2_style
from shared_utils import first as first
from gui.shared.utils import WHEELED_SWITCH_ON_TIME as WHEELED_SWITCH_ON_TIME, WHEELED_SWITCH_OFF_TIME as WHEELED_SWITCH_OFF_TIME, DUAL_GUN_CHARGE_TIME as DUAL_GUN_CHARGE_TIME, SHOT_DISPERSION_ANGLE as SHOT_DISPERSION_ANGLE, TURBOSHAFT_INVISIBILITY_STILL_FACTOR as TURBOSHAFT_INVISIBILITY_STILL_FACTOR, TURBOSHAFT_INVISIBILITY_MOVING_FACTOR as TURBOSHAFT_INVISIBILITY_MOVING_FACTOR, DISPERSION_RADIUS as DISPERSION_RADIUS, CHASSIS_REPAIR_TIME as CHASSIS_REPAIR_TIME, TURBOSHAFT_SWITCH_TIME as TURBOSHAFT_SWITCH_TIME, DUAL_GUN_RATE_TIME as DUAL_GUN_RATE_TIME, DUAL_ACCURACY_COOLING_DELAY as DUAL_ACCURACY_COOLING_DELAY, BURST_FIRE_RATE as BURST_FIRE_RATE, BURST_TIME_INTERVAL as BURST_TIME_INTERVAL, AUTO_SHOOT_CLIP_FIRE_RATE as AUTO_SHOOT_CLIP_FIRE_RATE, TWIN_GUN_RELOAD_ONE_GUN_TIME as TWIN_GUN_RELOAD_ONE_GUN_TIME, TWIN_GUN_RELOAD_TWO_GUN_TIME as TWIN_GUN_RELOAD_TWO_GUN_TIME, SHELL_LOADING_TIME_PROP_NAME as SHELL_LOADING_TIME_PROP_NAME, PENETRATION_LOSS as PENETRATION_LOSS
from gui.shared.items_parameters.params import _PenaltyInfo as _PenaltyInfo
_logger: Any
BACKWARD_QUALITY_PARAMS: Any
NEGATIVE_PARAMS: list
ROUND_PARAMS: list
PARAMS_WITH_IGNORED_EMPTY_VALUES: set
CREW_LEVEL_INCREASE_AFFECTING_PARAMS: Any
PARAMS_NORMALIZATION_MAP: dict
_CUSTOM_QUALITY_PARAMS: dict
DEFAULT_AVG_VALUE: tuple
CONDITIONAL_BONUSES: dict
NOT_HARD_DEPENDENCY: set

class PARAM_STATE(object):
    WORSE = 'worse'
    NORMAL = 'normal'
    BETTER = 'better'
    SITUATIONAL = 'situational'
    NOT_APPLICABLE = 'N/A'

class ItemsComparator(object):
    _currentParams: Any
    _otherParams: Any
    def __init__(self, currentParams, otherParams):
        ...
    def getAllDifferentParams(self):
        ...
    def getExtendedData(self, paramName, hasNormalization=False):
        ...
    def getPenalties(self, _):
        ...
    def _getPenaltiesAndBonuses(self, _):
        ...

class VehiclesComparator(ItemsComparator):
    __suitableArtefacts: Any
    __bonuses: Any
    __penalties: Any
    __paramsThatCountAsSituational: Any
    __situationalKPI: Any
    __highlightedBonuses: Any
    __situationalCrewLevelIncrease: Any
    def __init__(self, currentVehicleParams, otherVehicleParams, suitableArtefacts=None, bonuses=None, penalties=None, paramsThatCountAsSituational=None, situationalKPI=None, highlightedBonuses=None):
        ...
    def hasBonusOfType(self, bnsType):
        ...
    def getExtendedData(self, paramName, hasNormalization=False):
        ...
    def getPenalties(self, paramName):
        ...
    def _getPenaltiesAndBonuses(self, paramName):
        ...
    def __getPossibleParamBonuses(self, paramName):
        ...
    def __getCurrentParamBonuses(self, paramName, possibleBonuses):
        ...
    def __getConditionalBonuses(self, paramName, possibleBonuses):
        ...
    def __getUnmatchedDependency(self, paramName, activeBonuses, bonus):
        ...

# base nao representavel no stub: collections.namedtuple(...)
class _ParameterInfo:
    def getParamDiff(self):
        ...

def normalizeShotDispersionValue(value):
    ...
def normalizeClipFireRateValue(value):
    ...
def getParamExtendedData(paramName, value, otherValue, penalties=None, customQualityParams=None, isSituational=False, hasNormalization=False, highlightedBonuses=None):
    ...
def _getComparableValue(currentValue, comparableList, idx):
    ...
def _getParamStateInfo(paramName, val1, val2, customReverted=False, isSituational=False):
    ...
def rateParameterState(paramName, val1, val2, customQualityParams=None, isSituational=False):
    ...
def addParameterValuesOfTheSameType(val1, val2):
    ...
def combineParameterInfos(paramInfos):
    ...
