# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/battle_modifiers_common/battle_modifiers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from builtins import object as object
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from ResMgr import DataSection as DataSection
from constants import AOI as AOI, PIERCING_POWER_INTERPOLATION_DIST_FIRST as PIERCING_POWER_INTERPOLATION_DIST_FIRST, PIERCING_POWER_INTERPOLATION_DIST_LAST as PIERCING_POWER_INTERPOLATION_DIST_LAST, DAMAGE_INTERPOLATION_DIST_FIRST as DAMAGE_INTERPOLATION_DIST_FIRST, DAMAGE_INTERPOLATION_DIST_LAST as DAMAGE_INTERPOLATION_DIST_LAST
from typing import TYPE_CHECKING as TYPE_CHECKING, Optional as Optional, Any as Any, Tuple as Tuple, Union as Union, Dict as Dict, List as List
from items.vehicles import VehicleType as VehicleType
from battle_modifiers_ext.battle_modifiers import BattleModifier as BattleModifier
EXT_DATA_MODIFIERS_KEY = 'battleModifiers'
CONSTANTS_ORIGINAL: _Any
BATTLE_MODIFIERS_TYPE: _Any

class BattleParams(object):
    VEHICLE_HEALTH = 'vehicleHealth'
    GRAVITY_FACTOR = 'gravityFactor'
    DISP_FACTOR_CHASSIS_MOVEMENT = 'dispFactorChassisMovement'
    DISP_FACTOR_CHASSIS_ROTATION = 'dispFactorChassisRotation'
    TURRET_ROTATION_SPEED = 'turretRotationSpeed'
    GUN_ROTATION_SPEED = 'gunRotationSpeed'
    RELOAD_TIME = 'reloadTime'
    TWIN_GUN_RELOAD_TIME = 'twinGunReloadTime'
    CLIP_INTERVAL = 'clipInterval'
    BURST_INTERVAL = 'burstInterval'
    AUTORELOAD_TIME = 'autoreloadTime'
    AIMING_TIME = 'aimingTime'
    SHOT_DISPERSION_RADIUS = 'shotDispersionRadius'
    DISP_FACTOR_TURRET_ROTATION = 'dispFactorTurretRotation'
    DISP_FACTOR_AFTER_SHOT = 'dispFactorAfterShot'
    DISP_FACTOR_WHILE_GUN_DAMAGED = 'dispFactorWhileGunDamaged'
    SHELL_GRAVITY = 'shellGravity'
    SHELL_SPEED = 'shellSpeed'
    PIERCING_POWER_FIRST = 'piercingPowerFirst'
    PIERCING_POWER_LAST = 'piercingPowerLast'
    DAMAGE_RANDOMIZATION = 'damageRandomization'
    PIERCING_POWER_RANDOMIZATION = 'piercingPowerRandomization'
    NORMALIZATION_ANGLE = 'normalizationAngle'
    RICOCHET_ANGLE = 'ricochetAngle'
    ENGINE_POWER = 'enginePower'
    ENGINE_FIRE_FACTOR = 'engineFireFactor'
    FW_MAX_SPEED = 'fwMaxSpeed'
    BK_MAX_SPEED = 'bkMaxSpeed'
    ROTATION_SPEED_ON_STILL = 'rotationSpeedOnStill'
    ROTATION_SPEED_ON_MOVE = 'rotationSpeedOnMove'
    ARMOR_DAMAGE_FIRST = 'armorDamageFirst'
    ARMOR_DAMAGE_LAST = 'armorDamageLast'
    DEVICE_DAMAGE_FIRST = 'deviceDamageFirst'
    DEVICE_DAMAGE_LAST = 'deviceDamageLast'
    INVISIBILITY_ON_STILL = 'invisibilityOnStill'
    INVISIBILITY_ON_MOVE = 'invisibilityOnMove'
    VISION_RADIUS = 'visionRadius'
    RADIO_DISTANCE = 'radioDistance'
    BATTLE_LENGTH = 'battleLength'
    VEHICLE_RAMMING_DAMAGE = 'vehicleRammingDamage'
    VEHICLE_PRESSURE_DAMAGE = 'vehiclePressureDamage'
    TURRET_RAMMING_DAMAGE = 'turretRammingDamage'
    TURRET_PRESSURE_DAMAGE = 'turretPressureDamage'
    ENV_HULL_DAMAGE = 'envHullDamage'
    ENV_CHASSIS_DAMAGE = 'envChassisDamage'
    ENV_TANKMAN_DAMAGE_CHANCE = 'envTankmanDamageChance'
    ENV_MODULE_DAMAGE_CHANCE = 'envModuleDamageChance'
    REPAIR_SPEED = 'repairSpeed'
    VISION_MIN_RADIUS = 'visionMinRadius'
    VISION_MAX_RADIUS = 'visionMaxRadius'
    VISION_TIME = 'visionTime'
    EQUIPMENT_COOLDOWN = 'equipmentCooldown'
    FWD_FRICTION = 'fwdFriction'
    SIDE_FRICTION = 'sideFriction'
    DIRT_RELEASE_RATE = 'dirtReleaseRate'
    MAX_DIRT = 'maxDirt'
    SHOT_EFFECTS = 'shotEffects'
    GUN_EFFECTS = 'gunEffects'
    SHOT_PREFAB_EFFECTS = 'shotPrefabEffects'
    GUN_PREFAB_EFFECTS = 'gunPrefabEffects'
    DESTRUCTION_EFFECT = 'destructionEffect'
    FULL_DESTRUCTION_EFFECT = 'fullDestructionEffect'
    CHASSIS_DECALS = 'chassisDecals'
    ENGINE_SOUNDS = 'engineSounds'
    EXHAUST_EFFECTS = 'exhaustEffects'
    ARMOR_SPALLS_ARMOR_DAMAGE_FIRST = 'armorSpallsArmorDamageFirst'
    ARMOR_SPALLS_ARMOR_DAMAGE_LAST = 'armorSpallsArmorDamageLast'
    ARMOR_SPALLS_DEVICE_DAMAGE_FIRST = 'armorSpallsDeviceDamageFirst'
    ARMOR_SPALLS_DEVICE_DAMAGE_LAST = 'armorSpallsDeviceDamageLast'
    ARMOR_SPALLS_IMPACT_RADIUS = 'armorSpallsImpactRadius'
    ARMOR_SPALLS_CONE_ANGLE = 'armorSpallsConeAngle'
    ARMOR_SPALLS_DAMAGE_ABSORPTION = 'armorSpallsDamageAbsorption'
    CHANGE_SHELL_TYPE = 'changeShellType'
    CALIBER_TO_EXPLOSION_RADIUS = 'caliberToExplosionRadius'
    MODE_CREDITS_FACTOR = 'modeCreditsFactor'
    INVISIBILITY_FACTOR_AT_SHOT = 'invisibilityFactorAtShot'
    VEHICLE_AOI_RADIUS = 'vehicleAoIRadius'
    SOUND_NOTIFICATIONS = 'soundNotifications'
    DIVING_DESTRUCTION_DELAY = 'divingDestructionDelay'
    STUN_FACTOR_ENGINE_POWER = 'stunFactorEnginePower'
    STUN_FACTOR_VEHICLE_ROTATION_SPEED = 'stunFactorVehicleRotationSpeed'
    STUN_FACTOR_TURRET_TRAVERSE = 'stunFactorTurretTraverse'
    STUN_FACTOR_MAX_SPEED = 'stunFactorMaxSpeed'
    PIERCING_POWER_INTERPOLATION_DIST_FIRST = 'piercingPowerInterpolationDistFirst'
    PIERCING_POWER_INTERPOLATION_DIST_LAST = 'piercingPowerInterpolationDistLast'
    DAMAGE_INTERPOLATION_DIST_FIRST = 'damageInterpolationDistFirst'
    DAMAGE_INTERPOLATION_DIST_LAST = 'damageInterpolationDistLast'
    BONUS_CAPS_OVERRIDES = 'bonusCapsOverrides'
    CRYSTAL_REWARDS = 'crystalRewards'
    GOLD_RESERVE_GAINS = 'goldReserveGains'
    DAMAGE_RANDOMIZATION_TYPE = 'damageRandomizationType'
    PIERCING_POWER_RANDOMIZATION_TYPE = 'piercingPowerRandomizationType'
    SHELL_STUN = 'shellStun'
    FORCED_RELOAD_TIME = 'forcedReloadTime'
    AUTO_SHOOT_DISPERSION_PER_SHOT = 'autoShootDispersionPerShot'
    AUTO_SHOOT_MAX_SHOT_DISPERSION_FACTOR = 'autoShootMaxShotDispersionFactor'
    GUN_MAIN_PREFAB = 'gunMainPrefab'
    POSTMORTEM_OVERRIDES = 'postMortemOverrides'
    ROOT_PREFABS_MECHANIC_EFFECTS = 'rootPrefabsMechanicEffects'
    AMMO_BAY_HEALTH = 'ammoBayHealth'
    ENGINE_HEALTH = 'engineHealth'
    FUEL_TANK_HEALTH = 'fuelTankHealth'
    TURRET_ROTATOR_HEALTH = 'turretRotatorHealth'
    SURVEYING_DEVICE_HEALTH = 'surveyingDeviceHealth'
    CHASSIS_HEALTH = 'chassisHealth'
    GUN_HEALTH = 'gunHealth'
    FAKE_MODIFIER = 'fakeModifier'
    VSE_MODIFIER = 'vseModifier'
    DYNAMIC: set
    ALL: _Any

class ConstantsSet(object):
    __slots__: tuple
    VEHICLE_CIRCULAR_AOI_RADIUS: _Any
    VEHICLE_CIRCULAR_AOI_RADIUS_HYSTERESIS_MARGIN: _Any
    PIERCING_POWER_INTERPOLATION_DIST_FIRST: _Any
    PIERCING_POWER_INTERPOLATION_DIST_LAST: _Any
    DAMAGE_INTERPOLATION_DIST_FIRST: _Any
    DAMAGE_INTERPOLATION_DIST_LAST: _Any
    def __init__(self):
        ...

class ModifierScope(object):
    BASE = 1
    CELL = 2
    CLIENT = 4
    POST_BATTLE = 8
    HANGAR = 16
    BATTLE: _Any
    FULL: _Any
    ID_TO_NAME: dict
    NAME_TO_ID: dict
    ALL: _Any
    NAMES: _Any

class BattleModifiers(object):
    __nonzero__: _Any
    def __init__(self, source=None):
        ...
    def __call__(self, paramId, value, ctx=None):
        ...
    def __iter__(self):
        ...
    def __getitem__(self, paramId):
        ...
    def __len__(self):
        ...
    def __contains__(self, paramId):
        ...
    def __bool__(self):
        ...
    def __hash__(self):
        ...
    def __eq__(self, other):
        ...
    def __repr__(self):
        ...
    @staticmethod
    def retrieveDescr(descr, scope=...):
        ...
    @staticmethod
    def getConstantsOriginal():
        ...
    @staticmethod
    def clearVehicleModifications():
        ...
    @staticmethod
    def clearConstantsModifications():
        ...
    def get(self, paramId):
        ...
    def descr(self, scope=...):
        ...
    def domain(self):
        ...
    def haveDomain(self, domain):
        ...
    def scope(self):
        ...
    def haveScope(self, scope):
        ...
    def id(self):
        ...
    def getVehicleModification(self, vehType):
        ...
    def getConstantsModification(self):
        ...
    def getVsePlansByAspect(self, aspect):
        ...

class ModifiersContext(object):
    __slots__: tuple
    __nonzero__: _Any
    __modifiers: _Any
    __modificationCtx: _Any
    def __init__(self, modifiers, **modificationCtx):
        ...
    def __getattr__(self, item):
        ...
    def __deepcopy__(self, memo):
        ...
    def __copy__(self):
        ...
    def __call__(self, paramId, value):
        ...
    def __iter__(self):
        ...
    def __getitem__(self, paramId):
        ...
    def __len__(self):
        ...
    def __contains__(self, paramId):
        ...
    def __bool__(self):
        ...
    def __hash__(self):
        ...
    def __eq__(self, other):
        ...
    def __repr__(self):
        ...
    @property
    def modifiers(self):
        ...
    @property
    def modificationCtx(self):
        ...

def getDevGlobalModifiers():
    ...
