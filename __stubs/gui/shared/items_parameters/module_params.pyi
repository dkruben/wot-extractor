# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/items_parameters/module_params.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from past.utils import old_div as old_div
from constants import VEHICLE_MODE as VEHICLE_MODE
from gui.shared.items_parameters import calcGunParams as calcGunParams, getGunDescriptors as getGunDescriptors, isDualAccuracy as isDualAccuracy, isTwinGun as isTwinGun, isUnlimitedClipGun as isUnlimitedClipGun, isOverheatedUnlimitedGun as isOverheatedUnlimitedGun, isTemperatureGun as isTemperatureGun, isLowChargeShotGun as isLowChargeShotGun, getShotsPerMinute as getShotsPerMinute
from gui.shared.items_parameters.base_params import ParamsDictProxy as ParamsDictProxy, WeightedParam as WeightedParam
from gui.shared.items_parameters.params_constants import ONE_HUNDRED_PERCENTS as ONE_HUNDRED_PERCENTS, AUTOCANNON_SHOT_DISTANCE as AUTOCANNON_SHOT_DISTANCE
from gui.shared.items_parameters.functions import isStunParamVisible as isStunParamVisible, getTurboshaftEnginePower as getTurboshaftEnginePower, getRocketAccelerationEnginePower as getRocketAccelerationEnginePower, getMaxSteeringLockAngle as getMaxSteeringLockAngle, getInstalledModuleVehicle as getInstalledModuleVehicle, formatCompatibles as formatCompatibles, getLowChargeReloadTime as getLowChargeReloadTime, getLowChargeShotDispersion as getLowChargeShotDispersion
from gui.shared.items_parameters.params_cache import g_paramsCache as g_paramsCache
from gui.shared.gui_items.vehicle_mechanics.mechanic_detectors import hasChassisMechanicBit as hasChassisMechanicBit, ChassisTypes as ChassisTypes
from gui.shared.utils import DAMAGE_PROP_NAME as DAMAGE_PROP_NAME, PIERCING_POWER_PROP_NAME as PIERCING_POWER_PROP_NAME, AIMING_TIME_PROP_NAME as AIMING_TIME_PROP_NAME, STUN_DURATION_PROP_NAME as STUN_DURATION_PROP_NAME, GUARANTEED_STUN_DURATION_PROP_NAME as GUARANTEED_STUN_DURATION_PROP_NAME, AUTO_RELOAD_PROP_NAME as AUTO_RELOAD_PROP_NAME, GUN_AUTO_RELOAD as GUN_AUTO_RELOAD, GUN_CAN_BE_AUTO_RELOAD as GUN_CAN_BE_AUTO_RELOAD, GUN_AUTO_SHOOT as GUN_AUTO_SHOOT, GUN_CAN_BE_AUTO_SHOOT as GUN_CAN_BE_AUTO_SHOOT, GUN_DUAL_GUN as GUN_DUAL_GUN, GUN_CAN_BE_DUAL_GUN as GUN_CAN_BE_DUAL_GUN, RELOAD_TIME_SECS_PROP_NAME as RELOAD_TIME_SECS_PROP_NAME, DUAL_GUN_CHARGE_TIME as DUAL_GUN_CHARGE_TIME, DUAL_GUN_RATE_TIME as DUAL_GUN_RATE_TIME, DUAL_ACCURACY_AFTER_SHOT_DISPERSION_ANGLE as DUAL_ACCURACY_AFTER_SHOT_DISPERSION_ANGLE, BURST_FIRE_RATE as BURST_FIRE_RATE, MAX_MUTABLE_DAMAGE_PROP_NAME as MAX_MUTABLE_DAMAGE_PROP_NAME, MIN_MUTABLE_DAMAGE_PROP_NAME as MIN_MUTABLE_DAMAGE_PROP_NAME, GUN_CAN_BE_TWIN_GUN as GUN_CAN_BE_TWIN_GUN, GUN_TWIN_GUN as GUN_TWIN_GUN, DISPERSION_RADIUS_PROP_NAME as DISPERSION_RADIUS_PROP_NAME, SHELLS_PROP_NAME as SHELLS_PROP_NAME, SHELLS_COUNT_PROP_NAME as SHELLS_COUNT_PROP_NAME, RELOAD_TIME_PROP_NAME as RELOAD_TIME_PROP_NAME, RELOAD_MAGAZINE_TIME_PROP_NAME as RELOAD_MAGAZINE_TIME_PROP_NAME, SHELL_RELOADING_TIME_PROP_NAME as SHELL_RELOADING_TIME_PROP_NAME, SHELL_LOADING_TIME_PROP_NAME as SHELL_LOADING_TIME_PROP_NAME
from helpers import dependency as dependency
from items.components import component_constants as component_constants
from items.params_utils import getTemperatureRateOfFire as getTemperatureRateOfFire, getHeatedAimingTime as getHeatedAimingTime, getHeatedShotDispersion as getHeatedShotDispersion
from math_common import decimal_round as decimal_round, round_py2_style as round_py2_style, round_py2_style_int as round_py2_style_int
from skeletons.gui.shared import IItemsCache as IItemsCache

class RadioParams(WeightedParam):
    @property
    def radioDistance(self):
        ...

class EngineParams(WeightedParam):
    @property
    def enginePower(self):
        ...
    @property
    def turboshaftEnginePower(self):
        ...
    @property
    def rocketAccelerationEnginePower(self):
        ...
    @property
    def fireStartingChance(self):
        ...
    @property
    def forwardMaxSpeed(self):
        ...

class ChassisParams(WeightedParam):
    itemsCache: Any
    @property
    def rotationSpeed(self):
        ...
    @property
    def maxSteeringLockAngle(self):
        ...
    @property
    def chassisRepairTime(self):
        ...
    @property
    def isWheeled(self):
        ...
    @property
    def hasAutoSiege(self):
        ...
    @property
    def isWheeledOnSpotRotation(self):
        ...

class TurretParams(WeightedParam):
    @property
    def armor(self):
        ...
    @property
    def rotationSpeed(self):
        ...
    @property
    def circularVisionRadius(self):
        ...
    @property
    def gunCompatibles(self):
        ...
    def _getCompatible(self):
        ...

class GunParams(WeightedParam):
    _GUNS_WITH_HIDDEN_RELOAD_TIME: tuple
    @property
    def caliber(self):
        ...
    @property
    def shellsCount(self):
        ...
    @property
    def shellReloadingTime(self):
        ...
    @property
    def reloadMagazineTime(self):
        ...
    @property
    def reloadTime(self):
        ...
    @property
    def reloadTimeSecs(self):
        ...
    @property
    def reloadTimeSingleGun(self):
        ...
    @property
    def reloadTimeTwinGun(self):
        ...
    @property
    def shellLoadingTime(self):
        ...
    @property
    def chargeTime(self):
        ...
    @property
    def rateTime(self):
        ...
    @property
    def avgPiercingPower(self):
        ...
    @property
    def avgDamageList(self):
        ...
    @property
    def maxAvgMutableDamageList(self):
        ...
    @property
    def minAvgMutableDamageList(self):
        ...
    @property
    def dispertionRadius(self):
        ...
    @property
    def aimingTime(self):
        ...
    @property
    def compatibles(self):
        ...
    @property
    def clipVehiclesCompatibles(self):
        ...
    @property
    def shellsCompatibles(self):
        ...
    @property
    def maxShotDistance(self):
        ...
    @property
    def clipVehiclesCD(self):
        ...
    @property
    def continuousShotsPerMinute(self):
        ...
    @property
    def continuousDamagePerSecond(self):
        ...
    @property
    def avgDamagePerMinute(self):
        ...
    @property
    def stunMaxDurationList(self):
        ...
    @property
    def burstTimeInterval(self):
        ...
    @property
    def burstCount(self):
        ...
    @property
    def burstSize(self):
        ...
    @property
    def stunMinDurationList(self):
        ...
    @property
    def autoReloadTime(self):
        ...
    @property
    def dualAccuracyAfterShotDispersionAngle(self):
        ...
    @property
    def dualAccuracyCoolingDelay(self):
        ...
    def getParamsDict(self):
        ...
    def getReloadingType(self, vehicleCD=None):
        ...
    def _extractRawParams(self):
        ...
    def _getCompatible(self):
        ...
    def __getVehicleGun(self):
        ...
    def __isSiegeModeDescr(self):
        ...
