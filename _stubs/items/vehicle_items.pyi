# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/vehicle_items.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import typing as typing
from future.utils import viewvalues as viewvalues
import Math as Math
import nations as nations
from constants import SHELL_TYPES as SHELL_TYPES, ATTACK_REASON as ATTACK_REASON, SHELL_MECHANICS_TYPE as SHELL_MECHANICS_TYPE, INFINITE_SHELL_TAG as INFINITE_SHELL_TAG, RandomizationType as RandomizationType, FORCE_FINITE_SHELL_TAG as FORCE_FINITE_SHELL_TAG, SHELL_TYPES_INDICES as SHELL_TYPES_INDICES
from items import ITEM_TYPES as ITEM_TYPES, ITEM_TYPE_NAMES as ITEM_TYPE_NAMES, makeIntCompactDescrByID as makeIntCompactDescrByID
from items.basic_item import BasicItem as BasicItem
from items.components import chassis_components as chassis_components
from items.components import component_constants as component_constants
from items.components import gun_components as gun_components
from items.components import shared_components as shared_components
from items.components import shell_components as shell_components
from items.components import sound_components as sound_components
from py2to3.patched_future import with_metaclass as with_metaclass
from soft_exception import SoftException as SoftException
from wrapped_reflection_framework import ReflectionMetaclass as ReflectionMetaclass
from typing import TYPE_CHECKING as TYPE_CHECKING, Tuple as Tuple, Sequence as Sequence, Dict as Dict, NamedTuple as NamedTuple, Optional as Optional, Union as Union, Type as Type, List as List
from ModelHitTester import HitTesterManager as HitTesterManager, BoundingBoxManager as BoundingBoxManager
from Vehicular import GeneralWheelsAnimatorConfig as GeneralWheelsAnimatorConfig
from items import vehicles as vehicles
from items.components.shared_components import CustomizationSlotDescription as CustomizationSlotDescription
from items.readers.prefab_effects_readers import GunEffectDesc as GunEffectDesc
_TYPE_ID_TO_CLASS: dict

class VEHICLE_ITEM_STATUS(object):
    UNDEFINED = 0
    EMPTY = 1
    SHARED = 2
    LOCAL = 3

class CHASSIS_ITEM_TYPE(object):
    MONOLITHIC = 0
    SEPARATE = 1
    TRACK_WITHIN_TRACK = 2

class _ShallowCopyWrapper(object):
    __slots__: tuple
    __exclude: Any
    def __init__(self, *exclude):
        ...
    def __call__(self, clazz):
        ...

# decorador original: @add_shallow_copy(...)
class VehicleItem(BasicItem):
    __slots__: tuple
    level: Any
    status: Any
    def __init__(self, typeID, componentID, componentName, compactDescr, level=1, status=...):
        ...
    def __repr__(self):
        ...

# base nao representavel no stub: with_metaclass(...)
# decorador original: @add_shallow_copy(...)
class InstallableItem:
    __slots__: tuple
    weight: Any
    unlocks: Any
    healthParams: Any
    armorHomogenization: Any
    materials: Any
    hitTesterManager: Any
    modelsSets: Any
    models: Any
    camouflage: Any
    sounds: Any
    emblemSlots: Any
    slotsAnchors: Any
    def __init__(self, typeID, componentID, componentName, compactDescr, level=1):
        ...
    @property
    def hitTester(self):
        ...
    @property
    def maxHealth(self):
        ...
    @property
    def repairCost(self):
        ...
    @property
    def maxRegenHealth(self):
        ...
    @property
    def healthRegenPerSec(self):
        ...
    @property
    def healthBurnPerSec(self):
        ...
    @property
    def chanceToHit(self):
        ...
    @property
    def hysteresisHealth(self):
        ...
    @property
    def maxRepairCost(self):
        ...
    @property
    def repairSpeedLimiter(self):
        ...
    @property
    def repairTime(self):
        ...

# base nao representavel no stub: with_metaclass(...)
# decorador original: @add_shallow_copy(...)
class Chassis:
    __slots__: tuple
    hullPosition: Any
    topRightCarryingPoint: Any
    navmeshGirth: Any
    minPlaneNormalY: Any
    specificFriction: Any
    rotationSpeed: Any
    rotationSpeedLimit: Any
    rotationIsAroundCenter: Any
    shotDispersionFactors: Any
    brakeForce: Any
    terrainResistance: Any
    bulkHealthFactor: Any
    drivingWheelsSizes: Any
    carryingTriangles: Any
    traces: Any
    tracks: Any
    wheels: Any
    trackPairs: Any
    bboxManager: Any
    chassisLodDistance: Any
    generalWheelsAnimatorConfig: Any
    groundNodes: Any
    trackNodes: Any
    trackSplineParams: Any
    splineDesc: Any
    leveredSuspension: Any
    hullAimingSound: Any
    suspensionSpringsLength: Any
    effects: Any
    customEffects: Any
    AODecals: Any
    physicalTracks: Any
    customizableVehicleAreas: Any
    wheelHealthParams: Any
    wheelsArmor: Any
    _chassisType: Any
    prefabs: Any
    slotPrefabs: Any
    objectSlots: Any
    def __init__(self, typeID, componentID, componentName, compactDescr, level=1):
        ...
    @property
    def chassisType(self):
        ...
    @property
    def isTrackWithinTrack(self):
        ...
    @property
    def totalBBox(self):
        ...

# decorador original: @add_shallow_copy(...)
class Engine(InstallableItem):
    __slots__: tuple
    power: Any
    fireStartingChance: Any
    minFireStartingDamage: Any
    rpm_min: Any
    rpm_max: Any
    def __init__(self, typeID, componentID, componentName, compactDescr, level=1):
        ...

class FuelTank(InstallableItem):
    __slots__: tuple
    def __init__(self, typeID, componentID, componentName, compactDescr, level=1):
        ...

# decorador original: @add_shallow_copy(...)
class Radio(InstallableItem):
    __slots__: tuple
    distance: Any
    radarRadius: Any
    radarCooldown: Any
    def __init__(self, typeID, componentID, componentName, compactDescr, level=1):
        ...

# base nao representavel no stub: with_metaclass(...)
# decorador original: @add_shallow_copy(...)
class Turret:
    __slots__: tuple
    gunPosition: Any
    gunJointPitch: Any
    rotationSpeed: Any
    turretRotatorHealth: Any
    surveyingDeviceHealth: Any
    invisibilityFactor: Any
    guns: Any
    secondaryGuns: Any
    circularVisionRadius: Any
    multiGun: Any
    primaryArmor: Any
    physicsShape: Any
    ceilless: Any
    showEmblemsOnGun: Any
    turretRotatorSoundManual: Any
    turretRotatorSoundGear: Any
    AODecals: Any
    turretDetachmentEffects: Any
    customizableVehicleAreas: Any
    prefabs: Any
    slotPrefabs: Any
    objectSlots: Any
    def __init__(self, typeID, componentID, componentName, compactDescr, level=1):
        ...
    @property
    def isGunCarriage(self):
        ...

# base nao representavel no stub: with_metaclass(...)
# decorador original: @add_shallow_copy(...)
class Gun:
    __slots__: tuple
    rotationSpeed: Any
    reloadTime: Any
    aimingTime: Any
    forcedReloadTime: Any
    maxAmmo: Any
    invisibilityFactorAtShot: Any
    turretYawLimits: Any
    shotOffset: Any
    multiGunState: Any
    pitchLimits: Any
    staticTurretYaw: Any
    staticPitch: Any
    shotDispersionAngle: Any
    shotDispersionFactors: Any
    autoreload: Any
    autoreloadHasBoost: Any
    burst: Any
    clip: Any
    shots: Any
    dualGun: Any
    dualAccuracy: Any
    autoShoot: Any
    twinGun: Any
    drivenJoints: Any
    effectsCaliber: Any
    effects: Any
    prefabEffects: Any
    reloadEffect: Any
    impulse: Any
    recoil: Any
    animateEmblemSlots: Any
    customizableVehicleAreas: Any
    edgeByVisualModel: Any
    prefabs: Any
    shootImpulses: Any
    isDamageMutable: Any
    slotPrefabs: Any
    objectSlots: Any
    muzzleBrake: Any
    secondaryGunID: Any
    mechanicsParams: Any
    controllableReload: Any
    def __init__(self, typeID, componentID, componentName, compactDescr, level=1):
        ...
    @property
    def prefabBased(self):
        ...
    @property
    def multiGun(self):
        ...
    @property
    def hasClip(self):
        ...

# base nao representavel no stub: with_metaclass(...)
# decorador original: @add_shallow_copy(...)
class Hull:
    __slots__: tuple
    variantName: Any
    hitTesterManager: Any
    materials: Any
    weight: Any
    maxHealth: Any
    ammoBayHealth: Any
    turretPositions: Any
    turretPitches: Any
    variantMatch: Any
    fakeTurrets: Any
    armorHomogenization: Any
    primaryArmor: Any
    turretHardPoints: Any
    emblemSlots: Any
    slotsAnchors: Any
    modelsSets: Any
    models: Any
    swinging: Any
    customEffects: Any
    AODecals: Any
    camouflage: Any
    hangarShadowTexture: Any
    customizableVehicleAreas: Any
    burnoutAnimation: Any
    prefabs: Any
    slotPrefabs: Any
    objectSlots: Any
    def __init__(self):
        ...
    @property
    def hitTester(self):
        ...
    def copy(self):
        ...

class Shell(BasicItem):
    __slots__: tuple
    caliber: Any
    isTracer: Any
    isForceTracer: Any
    armorDamage: Any
    deviceDamage: Any
    damageRandomization: Any
    damageRandomizationType: Any
    piercingPowerRandomization: Any
    piercingPowerRandomizationType: Any
    stun: Any
    type: Any
    effectsCaliber: Any
    effectsIndex: Any
    prefabEffectsIndex: Any
    dynamicEffectsIndexes: Any
    isGold: Any
    icon: Any
    iconName: Any
    secondaryAttackReason: Any
    isDamageMutable: Any
    obstaclesDamage: Any
    obstaclesPowerReduction: Any
    chanceToHitByProjectileModifier: Any
    def __init__(self, typeID, componentID, componentName, compactDescr):
        ...
    def __repr__(self):
        ...
    @property
    def kind(self):
        ...
    @property
    def kindIdx(self):
        ...
    @property
    def hasStun(self):
        ...
    @property
    def isArmorPercingType(self):
        ...
    @property
    def isPiercingDistanceDependent(self):
        ...
    @property
    def isModernHE(self):
        ...
    def checkType(self, *types):
        ...
    def checkMechanics(self, *mechanics):
        ...
    @property
    def isInfinite(self):
        ...
    @property
    def isForceFinite(self):
        ...
    @property
    def prereqEffectIndexes(self):
        ...

def add_shallow_copy(*exclude):
    ...
def createInstallableItem(itemTypeID, nationID, itemID, name):
    ...
def createChassis(nationID, componentID, name):
    ...
def createTurret(nationID, componentID, name):
    ...
def createGun(nationID, componentID, name):
    ...
def createEngine(nationID, componentID, name):
    ...
def createFuelTank(nationID, componentID, name):
    ...
def createRadio(nationID, componentID, name):
    ...
def createShell(nationID, componentID, name):
    ...
