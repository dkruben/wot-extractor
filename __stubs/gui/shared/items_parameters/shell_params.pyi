# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/items_parameters/shell_params.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import math as math
import typing as typing
from enum import IntEnum as IntEnum
from collections import OrderedDict as OrderedDict
from future.utils import iteritems as iteritems
from past.utils import old_div as old_div
from constants import SHELL_TYPES as SHELL_TYPES, SHELL_MECHANICS_TYPE as SHELL_MECHANICS_TYPE
from gui.shared.items_parameters import calcShellParams as calcShellParams, getShellDescriptors as getShellDescriptors, NO_DATA as NO_DATA, isShellCalibration as isShellCalibration, isBustleFeedShotGun as isBustleFeedShotGun
from gui.shared.items_parameters.base_params import CompatibleParams as CompatibleParams, ParamsDictProxy as ParamsDictProxy
from gui.shared.items_parameters.functions import isStunParamVisible as isStunParamVisible, getBasicShell as getBasicShell, getBustleFeedDamage as getBustleFeedDamage, getShellCalibrationDamage as getShellCalibrationDamage, getShellCalibrationPiercingPower as getShellCalibrationPiercingPower
from gui.shared.items_parameters.params_constants import AUTOCANNON_SHOT_DISTANCE as AUTOCANNON_SHOT_DISTANCE, PIERCING_DISTANCES as PIERCING_DISTANCES, EPSILON as EPSILON
from gui.shared.utils import AVG_DAMAGE_PER_SECOND as AVG_DAMAGE_PER_SECOND, DAMAGE_PROP_NAME as DAMAGE_PROP_NAME, PIERCING_POWER_PROP_NAME as PIERCING_POWER_PROP_NAME, NORMALIZATION_ANGLE as NORMALIZATION_ANGLE, RICOCHET_ANGLE as RICOCHET_ANGLE, CRITICAL_HIT_CHANCE as CRITICAL_HIT_CHANCE, PENETRATION_LOSS as PENETRATION_LOSS
from gui.shared.utils.functions import getShellImpactParams as getShellImpactParams
from items import vehicles as vehicles
from items.components.component_constants import MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_SHIELDS as MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_SHIELDS
from items.vehicle_mechanics_types import VehicleMechanicKeys as VehicleMechanicKeys
from helpers_common import computePiercingPowerAtDist as computePiercingPowerAtDist
from math_common import round_py2_style as round_py2_style, round_py2_style_int as round_py2_style_int
from typing import Optional as Optional
BASE_SHELL_PARAMETERS: tuple
SHELL_MECHANIC_ADDITIONAL_PARAMETERS: dict
_SHELL_KINDS: tuple

class CriticalHitChanceType(IntEnum):
    STANDARD = 1
    DECREASED = 2
    INCREASED = 3

class ShellParams(CompatibleParams):
    @property
    def caliber(self):
        ...
    @property
    def piercingPower(self):
        ...
    @property
    def damage(self):
        ...
    @property
    def avgDamage(self):
        ...
    @property
    def avgMutableDamage(self):
        ...
    @property
    def avgDamagePerSecond(self):
        ...
    @property
    def avgPiercingPower(self):
        ...
    @property
    def explosionRadius(self):
        ...
    @property
    def piercingPowerTable(self):
        ...
    @property
    def maxShotDistance(self):
        ...
    @property
    def isBasic(self):
        ...
    @property
    def compatibles(self):
        ...
    @property
    def stunMaxDuration(self):
        ...
    @property
    def stunMinDuration(self):
        ...
    @property
    def stunDurationList(self):
        ...
    @property
    def shotSpeed(self):
        ...
    @property
    def normalizationAngle(self):
        ...
    @property
    def ricochetAngle(self):
        ...
    @property
    def penetrationLoss(self):
        ...
    @property
    def screensArmorMultiplier(self):
        ...
    @property
    def criticalHitChance(self):
        ...
    def getParamsDict(self):
        ...
    def _extractRawParams(self):
        ...
    def _getCompatible(self):
        ...
    def __isModernHE(self):
        ...
    def __getShellDescriptor(self):
        ...
    def __getShellType(self):
        ...

def _isDifferentValues(paramName, parameters):
    ...
def getMechanicParameters(mechanic, parameters):
    ...
def _average(listOfNumbers):
    ...
