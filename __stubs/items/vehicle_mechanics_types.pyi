# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/vehicle_mechanics_types.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import viewitems as viewitems
from enum import Enum as Enum
from items import _xml as _xml
from items.components.shared_components import MechanicsParams as MechanicsParams
VEHICLE_MECHANIC_VALUES: Any
ALL_VEHICLE_MECHANIC_KEYS: Any
MECHANIC_KEY_BY_NAME: dict
_MECHANIC_VARIANT_TYPES_BY_MECHANIC: dict
_MECHANIC_VARIANT_VALUES_BY_MECHANIC: dict

class VehicleMechanic(Enum):
    ACCURACY_STACKS = 'accuracyStacks'
    AUTO_LOADER_GUN = 'autoLoaderGun'
    AUTO_LOADER_GUN_BOOST = 'autoLoaderGunBoost'
    AUTORELOADER_SURGE = 'autoreloaderSurge'
    AUTO_SHOOT_GUN = 'autoShootGun'
    AUXILIARY_ROCKET_LAUNCHER = 'auxiliaryRocketLauncher'
    BATTLE_FURY = 'battleFury'
    BUSTLE_FEED = 'bustleFeed'
    CHARGEABLE_BURST = 'chargeableBurst'
    CHARGE_SHOT = 'chargeShot'
    CONCENTRATION_MODE = 'concentrationMode'
    CREST_MOVING = 'crestMoving'
    DAMAGE_MUTABLE = 'damageMutable'
    DUAL_ACCURACY = 'dualAccuracy'
    DUAL_GUN = 'dualGun'
    EXTRA_SHOT_CLIP = 'extraShotClip'
    HEATING_ZONES_GUN = 'heatingZonesGun'
    HYDRAULIC_CHASSIS = 'hydraulicChassis'
    HYDRAULIC_WHEELED_CHASSIS = 'hydraulicWheeledChassis'
    IMPROVED_RAMMING = 'improvedRamming'
    LOW_CHARGE_SHOT = 'lowChargeShot'
    MAGAZINE_GUN = 'magazineGun'
    OVERHEAT_GUN = 'overheatGun'
    OVERHEAT_STACKS = 'overheatStacks'
    PILLBOX_SIEGE_MODE = 'pillboxSiegeMode'
    POWER_MODE = 'powerMode'
    PROPELLANT_GUN = 'propellantAfterburnerGun'
    RECHARGEABLE_NITRO = 'rechargeableNitro'
    ROCKET_ACCELERATION = 'rocketAcceleration'
    SHELL_PARAMS_SWITCHER = 'shellParamsSwitcher'
    SHELL_CALIBRATION = 'shellCalibration'
    SIEGE_MODE = 'siegeMode'
    SIGHT_POINTER = 'sightPointer'
    SPEC_BOOST_MODE = 'specBoostMode'
    STAGED_JET_BOOSTERS = 'stagedJetBoosters'
    STANCE_DANCE = 'stanceDance'
    STATIONARY_RELOAD = 'stationaryReload'
    STUN = 'stun'
    SUPPORT_WEAPON = 'supportWeapon'
    TARGET_DESIGNATOR = 'targetDesignator'
    TEMPERATURE_GUN = 'temperatureGun'
    TRACK_WITHIN_TRACK = 'trackWithinTrack'
    TURBOSHAFT_ENGINE = 'turboshaftEngine'
    TWIN_GUN = 'twinGun'
    WHEELED_DASH = 'wheeledDash'
    @classmethod
    def find(cls, value):
        ...

class VehicleMechanicVariant(object):
    @classmethod
    def fromString(cls, value):
        ...

class SpecBoostModeMechanicVariant(VehicleMechanicVariant, Enum):
    COMBAT_THROTTLE = 'combatThrottle'

# base nao representavel no stub: typing.NamedTuple(...)
class VehicleMechanicKey:
    __slots__: tuple
    def __new__(cls, mechanic, mechanicVariant=None):
        ...
    @property
    def uniqueName(self):
        ...

class VehicleMechanicKeys(object):
    ACCURACY_STACKS: Any
    AUTO_LOADER_GUN: Any
    AUTO_LOADER_GUN_BOOST: Any
    AUTORELOADER_SURGE: Any
    AUTO_SHOOT_GUN: Any
    AUXILIARY_ROCKET_LAUNCHER: Any
    BATTLE_FURY: Any
    BUSTLE_FEED: Any
    CHARGEABLE_BURST: Any
    CHARGE_SHOT: Any
    CONCENTRATION_MODE: Any
    CREST_MOVING: Any
    DAMAGE_MUTABLE: Any
    DUAL_ACCURACY: Any
    DUAL_GUN: Any
    EXTRA_SHOT_CLIP: Any
    HEATING_ZONES_GUN: Any
    HYDRAULIC_CHASSIS: Any
    HYDRAULIC_WHEELED_CHASSIS: Any
    IMPROVED_RAMMING: Any
    LOW_CHARGE_SHOT: Any
    MAGAZINE_GUN: Any
    OVERHEAT_GUN: Any
    OVERHEAT_STACKS: Any
    PILLBOX_SIEGE_MODE: Any
    POWER_MODE: Any
    PROPELLANT_GUN: Any
    RECHARGEABLE_NITRO: Any
    ROCKET_ACCELERATION: Any
    SHELL_PARAMS_SWITCHER: Any
    SHELL_CALIBRATION: Any
    SIGHT_POINTER: Any
    SIEGE_MODE: Any
    STAGED_JET_BOOSTERS: Any
    STANCE_DANCE: Any
    STATIONARY_RELOAD: Any
    STUN: Any
    SUPPORT_WEAPON: Any
    TARGET_DESIGNATOR: Any
    TEMPERATURE_GUN: Any
    TRACK_WITHIN_TRACK: Any
    TURBOSHAFT_ENGINE: Any
    TWIN_GUN: Any
    WHEELED_DASH: Any
    COMBAT_THROTTLE: Any

def getVehicleMechanicKey(mechanic, mechanicParams):
    ...
def readMechanicVariant(xmlCtx, section, mechanic):
    ...
