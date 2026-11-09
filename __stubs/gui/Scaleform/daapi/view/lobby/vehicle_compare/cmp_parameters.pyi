# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/vehicle_compare/cmp_parameters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from copy import copy as copy
import typing as typing
from future.utils import iteritems as iteritems
from gui.Scaleform.daapi.view.lobby.vehicle_compare import cmp_helpers as cmp_helpers
from gui.Scaleform.locale.VEH_COMPARE import VEH_COMPARE as VEH_COMPARE
from gui.game_control.veh_comparison_basket import CONFIGURATION_TYPES as CONFIGURATION_TYPES
from gui.impl import backport as backport
from gui.shared.formatters import text_styles as text_styles
from gui.shared.gui_items import vehicle_adjusters as vehicle_adjusters
from gui.shared.gui_items.Tankman import CrewTypes as CrewTypes
from gui.shared.gui_items.Vehicle import Vehicle as Vehicle
from gui.shared.items_parameters import formatters as formatters
from gui.shared.items_parameters.comparator import rateParameterState as rateParameterState, PARAM_STATE as PARAM_STATE, VehiclesComparator as VehiclesComparator, getParamExtendedData as getParamExtendedData, PARAMS_NORMALIZATION_MAP as PARAMS_NORMALIZATION_MAP
from gui.shared.items_parameters.formatters import FORMAT_SETTINGS as FORMAT_SETTINGS, clipFireRatePreprocessor as clipFireRatePreprocessor, shotDispersionAnglePreprocessor as shotDispersionAnglePreprocessor
from gui.shared.items_parameters.params import VehicleParams as VehicleParams
from gui.shared.items_parameters.params_helper import VehParamsBaseGenerator as VehParamsBaseGenerator, isValidEmptyValue as isValidEmptyValue, updateCrewBonus as updateCrewBonus
from gui.shared.utils import SHOT_DISPERSION_ANGLE as SHOT_DISPERSION_ANGLE, AUTO_SHOOT_CLIP_FIRE_RATE as AUTO_SHOOT_CLIP_FIRE_RATE, TEMPERATURE_RELOAD_TIME as TEMPERATURE_RELOAD_TIME, TEMPERATURE_AVG_DAMAGE_PER_MINUTE as TEMPERATURE_AVG_DAMAGE_PER_MINUTE
from helpers import dependency as dependency
from post_progression_common import VehicleState as VehicleState
from skeletons.gui.game_control import IVehicleComparisonBasket as IVehicleComparisonBasket
from items import tankmen as tankmen
CMP_HIDDEN_PARAMETERS: Any
_HEADER_PARAM_COLOR_SCHEME: tuple
_HEADER_PARAM_NO_COLOR_SCHEME: tuple
_PARAM_COLOR_SCHEME: tuple
_PARAM_NO_COLOR_SCHEME: tuple
_DELTA_PARAM_COLOR_SCHEME: tuple
_NO_COLOR_SCHEMES: tuple
_COLOR_SCHEMES: tuple
_CMP_FORMAT_SETTINGS: Any

class _BestParamsDict(dict):
    __lengths: Any
    def __init__(self, seq=None, **kwargs):
        ...
    def addLen(self, key, value):
        ...
    def toDict(self):
        ...

class _VehParamsValuesGenerator(VehParamsBaseGenerator):
    __headerScheme: Any
    __bodyScheme: Any
    def __init__(self, headerScheme, bodyScheme):
        ...
    def setColorSchemes(self, header, body):
        ...
    def _makeSimpleParamHeaderVO(self, param, isOpen, comparator):
        ...
    def _makeAdvancedParamVO(self, param, parentID, highlight):
        ...

class _CmpVehicleParams(VehicleParams):
    @property
    def clipFireRate(self):
        ...
    @property
    def reloadTime(self):
        ...
    @property
    def avgDamagePerMinute(self):
        ...

class _VehCompareParametersData(object):
    __crewLvl: Any
    __skillsByTankman: Any
    __configurationType: Any
    __isInInventory: Any
    __currentVehParams: Any
    __vehicleStrCD: Any
    __equipment: Any
    __hasCamouflage: Any
    __selectedShellIdx: Any
    __vehicle: Any
    __battleBooster: Any
    __dynSlotType: Any
    __postProgressionState: Any
    __isCrewInvalid: Any
    __isInInvInvalid: Any
    __isConfigurationTypesInvalid: Any
    __isCurrVehParamsInvalid: Any
    __vehicleIntCD: Any
    __cache: Any
    __paramGenerator: Any
    __parameters: Any
    def __init__(self, cache, vehCompareData):
        ...
    def setCrewData(self, crewLvl, skillsByTankman):
        ...
    def setVehicleData(self, vehCompareData):
        ...
    def setConfigurationType(self, newVal):
        ...
    def setIsInInventory(self, newVal):
        ...
    def dispose(self):
        ...
    def getVehicleIntCD(self):
        ...
    def getFormattedParameters(self, vehMaxParams):
        ...
    def getVehicle(self):
        ...
    def getParams(self):
        ...
    def getDeltaParams(self, paramName, paramValue, hasNormalization=False):
        ...
    @classmethod
    def _getConfigurationType(cls, mType):
        ...
    @classmethod
    def __initParameters(cls, vehCD, vehicle):
        ...
    def __showRevertButton(self):
        ...

class IVehCompareView(object):
    def buildList(self, *args):
        ...
    def updateItems(self, *args):
        ...

class VehCompareBasketParamsCache(object):
    comparisonBasket: Any
    __cache: Any
    __view: Any
    def __init__(self, view):
        ...
    def dispose(self):
        ...
    def getParametersDelta(self, index, paramName):
        ...
    def __addParamData(self, index):
        ...
    def __rebuildList(self):
        ...
    def __onVehCountChanged(self, changedData):
        ...
    def __onVehParamsChanged(self, data):
        ...
    def __onNationChange(self, vehicleIDxs):
        ...

def _generateFormatSettings():
    ...
def getUndefinedParam():
    ...
def _hasNormalizeParameters(cache):
    ...
def _reCalcBestParameters(targetCache):
    ...
