# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/utils/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import imghdr as imghdr
import sys as sys
import inspect as inspect
import uuid as uuid
import struct as struct
from builtins import filter as filter, zip as zip, range as range
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems
from past.builtins import cmp as cmp, unicode as unicode
import BigWorld as BigWorld
import AccountCommands as AccountCommands
import Settings as Settings
import constants as constants
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR, LOG_DEBUG as LOG_DEBUG, LOG_WARNING as LOG_WARNING
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.shared.sort_key import SortKey as SortKey
from helpers import getLanguageCode as getLanguageCode
from items import vehicles as vehs_core
from account_helpers import getAccountDatabaseID as getAccountDatabaseID
from account_helpers.AccountSettings import AccountSettings as AccountSettings
from avatar_helpers import getAvatarDatabaseID as getAvatarDatabaseID
SHELLS_COUNT_PROP_NAME = 'shellsCount'
RELOAD_TIME_SECS_PROP_NAME = 'reloadTimeSecs'
RELOAD_TIME_PROP_NAME = 'reloadTime'
RELOAD_MAGAZINE_TIME_PROP_NAME = 'reloadMagazineTime'
SHELL_RELOADING_TIME_PROP_NAME = 'shellReloadingTime'
SHELL_LOADING_TIME_PROP_NAME = 'shellLoadingTime'
DISPERSION_RADIUS_PROP_NAME = 'dispersionRadius'
SHOT_DISPERSION_ANGLE = 'shotDispersionAngle'
DISPERSION_RADIUS = 'dispertionRadius'
AIMING_TIME_PROP_NAME = 'aimingTime'
PIERCING_POWER_PROP_NAME = 'piercingPower'
DAMAGE_PROP_NAME = 'damage'
MAX_MUTABLE_DAMAGE_PROP_NAME = 'maxMutableDamage'
MIN_MUTABLE_DAMAGE_PROP_NAME = 'minMutableDamage'
SHELLS_PROP_NAME = 'shells'
STUN_DURATION_PROP_NAME = 'stunDuration'
AUTO_RELOAD_PROP_NAME = 'autoReloadTime'
GUARANTEED_STUN_DURATION_PROP_NAME = 'guaranteedStunDuration'
CLIP_VEHICLES_PROP_NAME = 'clipVehicles'
UNICHARGED_VEHICLES_PROP_NAME = 'uniChargedVehicles'
VEHICLES_PROP_NAME = 'vehicles'
CLIP_VEHICLES_CD_PROP_NAME = 'clipVehiclesCD'
MAX_STEERING_LOCK_ANGLE = 'maxSteeringLockAngle'
NORMALIZATION_ANGLE = 'normalizationAngle'
RICOCHET_ANGLE = 'ricochetAngle'
PENETRATION_LOSS = 'penetrationLoss'
BURST_FIRE_RATE = 'burstFireRate'
BURST_TIME_INTERVAL = 'burstTimeInterval'
BURST_COUNT = 'burstCount'
BURST_SIZE = 'burstSize'
TEMPERATURE_RELOAD_TIME = 'temperatureReloadTime'
TEMPERATURE_AVG_DAMAGE_PER_MINUTE = 'temperatureAvgDamagePerMinute'
WHEELED_SWITCH_ON_TIME = 'wheeledSwitchOnTime'
WHEELED_SWITCH_OFF_TIME = 'wheeledSwitchOffTime'
WHEELED_SWITCH_TIME = 'wheeledSwitchTime'
WHEELED_SPEED_MODE_SPEED = 'wheeledSpeedModeSpeed'
TURBOSHAFT_SWITCH_ON_TIME = 'turboshaftSwitchOnTime'
TURBOSHAFT_SWITCH_OFF_TIME = 'turboshaftSwitchOffTime'
TURBOSHAFT_SWITCH_TIME = 'turboshaftSwitchTime'
TURBOSHAFT_SPEED_MODE_SPEED = 'turboshaftSpeedModeSpeed'
TURBOSHAFT_ENGINE_POWER = 'turboshaftEnginePower'
TURBOSHAFT_INVISIBILITY_STILL_FACTOR = 'turboshaftInvisibilityStillFactor'
TURBOSHAFT_INVISIBILITY_MOVING_FACTOR = 'turboshaftInvisibilityMovingFactor'
ROCKET_ACCELERATION_ENGINE_POWER = 'rocketAccelerationEnginePower'
ROCKET_ACCELERATION_SPEED_LIMITS = 'rocketAccelerationSpeedLimits'
ROCKET_ACCELERATION_REUSE_AND_DURATION = 'rocketAccelerationReuseAndDuration'
DUAL_GUN_CHARGE_TIME = 'chargeTime'
DUAL_GUN_RATE_TIME = 'rateTime'
DUAL_ACCURACY_AFTER_SHOT_DISPERSION_ANGLE = 'dualAccuracyAfterShotDispersionAngle'
DUAL_ACCURACY_COOLING_DELAY = 'dualAccuracyCoolingDelay'
AVG_DAMAGE_PER_SECOND = 'avgDamagePerSecond'
AUTO_SHOOT_CLIP_FIRE_RATE = 'autoShootClipFireRate'
CONTINUOUS_SHOTS_PER_MINUTE = 'continuousShotsPerMinute'
CONTINUOUS_DAMAGE_PER_SECOND = 'continuousDamagePerSecond'
TWIN_GUN_SWITCH_FIRE_MODE_TIME = 'twinGunSwitchFireModeTime'
TWIN_GUN_TOP_SPEED = 'twinGunTopSpeed'
TWIN_GUN_RELOAD_ONE_GUN_TIME = 'reloadTimeSingleGun'
TWIN_GUN_RELOAD_TWO_GUN_TIME = 'reloadTimeTwinGun'
TWIN_GUN_RELOAD_TIME = 'twinGunReloadTime'
CHASSIS_REPAIR_TIME = 'chassisRepairTime'
CHASSIS_REPAIR_TIME_YOH = 'chassisRepairTimeYoh'
CRITICAL_HIT_CHANCE = 'criticalHitChance'
GUN_CAN_BE_CLIP = 1
GUN_CLIP = 2
GUN_NORMAL = 4
GUN_CAN_BE_AUTO_RELOAD = 5
GUN_AUTO_RELOAD = 6
GUN_CAN_BE_DUAL_GUN = 7
GUN_DUAL_GUN = 8
GUN_CAN_BE_AUTO_SHOOT = 9
GUN_AUTO_SHOOT = 10
GUN_CAN_BE_TWIN_GUN = 11
GUN_TWIN_GUN = 12
GUN_CAN_BE_LOW_CHARGE_SHOT = 13
LOW_CHARGE_SHOT = 14
EXTRA_MODULE_INFO = 'extraModuleInfo'
FIELD_SPECIALIZATIONS = 'specs'
FIELD_HIGHLIGHT_TYPE = 'highlightType'
_FLASH_OBJECT_SYS_ATTRS: tuple
ValidationResult: Any
_STR_CASING_OPTIONS: dict
_REPLACEMENTS: dict
_ROMAN_FORBIDDEN_LANGUAGES: set

class _SortKeyByFields(SortKey):
    __slots__: tuple
    fields: Any
    valueGetter: Any
    item: Any
    def __init__(self, fields, valueGetter, item):
        ...
    def _cmp(self, other):
        ...

class SettingRecord(dict):
    def __setattr__(self, name, value):
        ...
    def __getattr__(self, item):
        ...
    def _asdict(self):
        ...
    def __repr__(self):
        ...

class SettingRootRecord(SettingRecord):
    @classmethod
    def load(cls):
        ...
    def save(self):
        ...
    @classmethod
    def _getSettingName(cls):
        ...

def flashObject2Dict(obj):
    ...
def code2str(code):
    ...
def isVehicleObserver(vehTypeCompDescr):
    ...
def class_for_name(module_name, class_name):
    ...
def sortByFields(fields, sequence, valueGetter=...):
    ...
def roundByModulo(value, rate):
    ...
def changeStringCasing(string, isUpper):
    ...
def toLower(string):
    ...
def toUpper(string):
    ...
def copyToClipboard(text):
    ...
def mapTextureToTheMemory(textureData, uniqueID=None, temp=True):
    ...
def removeTextureFromMemory(textureID):
    ...
def getImageSize(imageData):
    ...
def showInvitationInWindowsBar():
    ...
def getPlayerDatabaseID():
    ...
def getPlayerName():
    ...
def avg(devidend, devider):
    ...
def weightedAvg(*args):
    ...
def makeSearchableString(inputString):
    ...
def isPopupsWindowsOpenDisabled():
    ...
def isRomanNumberForbidden():
    ...
def showAFKWarningInWindowsBar():
    ...
