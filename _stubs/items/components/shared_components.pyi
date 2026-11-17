# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/shared_components.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from functools import partial as partial
import typing as typing
from past.builtins import xrange as xrange
from future.moves import pickle as pickle
from future.utils import lmap as lmap, lzip as lzip, viewitems as viewitems
from math import radians as radians
from collections import namedtuple as namedtuple
from constants import IS_CLIENT as IS_CLIENT, IS_WEB as IS_WEB, IS_EDITOR as IS_EDITOR, IS_BOT as IS_BOT, HEATING_ZONES_GUN_STATE as HEATING_ZONES_GUN_STATE, DEBUFFS_TYPES as DEBUFFS_TYPES, SIGHT_POINTER_COMMON_CONSTANTS as SIGHT_POINTER_COMMON_CONSTANTS
from debug_utils import LOG_WARNING as LOG_WARNING
from items import ITEM_TYPES as ITEM_TYPES, _xml as _xml
from items.components import component_constants as component_constants, c11n_constants as c11n_constants, path_builder as path_builder
from items.components.component_constants import KMH_TO_MS as KMH_TO_MS
from items.components.c11n_constants import AttachmentSize as AttachmentSize
from items.vehicle_mechanics_types import readMechanicVariant as readMechanicVariant, VehicleMechanic as VehicleMechanic
from items.attributes_helpers import ALLOWED_STATIC_ATTRS as ALLOWED_STATIC_ATTRS, isclose as isclose
from py2to3.patched_future import with_metaclass as with_metaclass
from soft_exception import SoftException as SoftException
from wrapped_reflection_framework import ReflectionMetaclass as ReflectionMetaclass, reflectedNamedTuple as reflectedNamedTuple
from typing import Any as Any, Dict as Dict, List as List, Optional as Optional, Sequence as Sequence, Set as Set
from constants import VEHICLE_TTC_ASPECTS as VEHICLE_TTC_ASPECTS
from items.vehicles import VehicleDescriptor as VehicleDescriptor
__all__: tuple
MaterialInfo: _Any
DEFAULT_MATERIAL_INFO: _Any
EmblemSlot: _Any
MiscSlot: _Any
LodSettings: _Any
NodesAndGroups: _Any
Camouflage: _Any
DEFAULT_CAMOUFLAGE: _Any
EMPTY_CAMOUFLAGE: _Any
SwingingSettings: _Any
DEFAULT_DEVICE_HEALTH: _Any
ImpulseData: _Any
SpeedTriggerData: _Any
TickedImpulseData: _Any
TemperatureGunThermalState: _Any
PropellantGunStage: _Any
SightPointerAbilityStage: _Any
MECHANIC_NAME_TO_IDX: dict
ObjectSlot: _Any

class i18n(object):
    @classmethod
    def makeString(cls, key):
        ...

# base nao representavel no stub: with_metaclass(...)
class CustomizationSlotDescription:
    __slots__: tuple
    type: _Any
    slotId: _Any
    anchorPosition: _Any
    anchorDirection: _Any
    applyTo: _Any
    def __init__(self, slotType='', slotId=0, anchorPosition=None, anchorDirection=None, applyTo=None, tags=None):
        ...

# base nao representavel no stub: with_metaclass(...)
class ProjectionDecalSlotDescription:
    __slots__: tuple
    type: _Any
    slotId: _Any
    position: _Any
    rotation: _Any
    scale: _Any
    scaleFactors: _Any
    doubleSided: _Any
    hiddenForUser: _Any
    canBeMirroredVertically: _Any
    showOn: _Any
    tags: _Any
    clipAngle: _Any
    compatibleModels: _Any
    itemId: _Any
    options: _Any
    anchorShift: _Any
    modificationOrder: _Any
    def __init__(self, slotType='', slotId=0, position=None, rotation=None, scale=None, scaleFactors=..., doubleSided=False, hiddenForUser=False, canBeMirroredVertically=False, showOn=None, tags=None, clipAngle=..., compatibleModels=..., itemId=None, options=..., anchorShift=..., modificationOrder=0):
        ...

# base nao representavel no stub: with_metaclass(...)
class AttachmentSlotDescription:
    __slots__: tuple
    type: _Any
    slotId: _Any
    position: _Any
    rotation: _Any
    scale: _Any
    attachNode: _Any
    hiddenForUser: _Any
    enableVisTunnel: _Any
    applyType: _Any
    size: _Any
    hangerId: _Any
    hangerRotation: _Any
    compatibleModels: _Any
    def __init__(self, slotType='', slotId=0, position=None, rotation=None, scale=None, attachNode=None, hiddenForUser=False, enableVisTunnel=False, applyType='', size='', hangerId=0, hangerRotation=None, compatibleModels=...):
        ...
    @property
    def scaleFactorId(self):
        ...

class I18nString(object):
    __slots__: tuple
    __value: _Any
    __converted: _Any
    def __init__(self, key):
        ...
    @property
    def value(self):
        ...

class _I18nConvertedFlags(object):
    UNDEFINED = 0
    USER_STRING = 1
    SHORT_STRING = 2
    DESCRIPTION = 4
    SHORT_DESCRIPTION_SPECIAL = 8
    LONG_DESCRIPTION_SPECIAL = 16
    SHORT_FILTER_ALERT_SPECIAL = 18
    LONG_FILTER_ALERT_SPECIAL = 20

class I18nComponent(object):
    __slots__: tuple
    __userString: _Any
    __description: _Any
    __converted: _Any
    __shortString: _Any
    __shortDescriptionSpecial: _Any
    __longDescriptionSpecial: _Any
    __longFilterAlertSpecial: _Any
    __shortFilterAlertSpecial: _Any
    def __init__(self, userStringKey, descriptionKey, shortStringKey='', shortDescriptionSpecialKey='', longDescriptionSpecialKey='', shortFilterAlertKey='', longFilterAlertKey=''):
        ...
    @property
    def userString(self):
        ...
    @property
    def shortString(self):
        ...
    @property
    def description(self):
        ...
    @property
    def shortDescriptionSpecial(self):
        ...
    @property
    def longDescriptionSpecial(self):
        ...
    @property
    def longFilterAlertSpecial(self):
        ...
    @property
    def shortFilterAlertSpecial(self):
        ...

class I18nExposedComponent(I18nComponent):
    __slots__: tuple
    __userKey: _Any
    __descriptionKey: _Any
    __longDescriptionSpecialKey: _Any
    __name: _Any
    __shortDescriptionSpecialKey: _Any
    def __init__(self, userStringKey, descriptionKey, longDescriptionSpecialKey='', name='', shortDescriptionSpecialKey=''):
        ...
    @property
    def userKey(self):
        ...
    @property
    def descriptionKey(self):
        ...
    @property
    def longDescriptionSpecialKey(self):
        ...
    @property
    def name(self):
        ...
    @property
    def shortDescriptionSpecialKey(self):
        ...

class DeviceHealth(object):
    __slots__: tuple
    repairTime: _Any
    maxHealth: _Any
    repairCost: _Any
    maxRegenHealth: _Any
    healthRegenPerSec: _Any
    hysteresisHealth: _Any
    healthBurnPerSec: _Any
    chanceToHit: _Any
    invulnerable: _Any
    repairSpeedLimiter: _Any
    def __init__(self, maxHealth, repairCost=..., maxRegenHealth=...):
        ...
    def __repr__(self):
        ...
    @property
    def maxRepairCost(self):
        ...

# base nao representavel no stub: with_metaclass(...)
class ModelStatesPaths:
    __slots__: tuple
    __undamaged: _Any
    __destroyed: _Any
    __exploded: _Any
    def __init__(self, undamaged, destroyed, exploded):
        ...
    def __repr__(self):
        ...
    @property
    def undamaged(self):
        ...
    @property
    def destroyed(self):
        ...
    @property
    def exploded(self):
        ...
    def setUndamaged(self, value):
        ...
    def setDestroyed(self, value):
        ...
    def setExploded(self, value):
        ...
    def getPathByStateName(self, stateName):
        ...

class RocketAccelerationParams(object):
    __slots__: tuple
    deployTime: _Any
    reloadTime: _Any
    reuseCount: _Any
    duration: _Any
    impulse: _Any
    modifiers: _Any
    kpi: _Any
    def __init__(self, deployTime, reloadTime, reuseCount, duration, impulse, modifiers, kpi):
        ...
    def __repr__(self):
        ...

class MechanicsParams(object):
    __slots__: tuple
    MECHANICS_NAME = None
    COMPONENT_TYPE_ID = None
    __origin: _Any
    mechanicVariant: _Any
    modifiers: _Any
    def __init__(self, modifiers=None, mechanicVariant=None):
        ...
    @classmethod
    def getSubClasses(cls, uniqueParamNames=None):
        ...
    @classmethod
    def readMechanicsParams(cls, xmlCtx, section, readModifiers):
        ...
    def createMechanicsParamsOrigin(self):
        ...
    def getMechanicsMiscAttributes(self):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def isActiveMechanics(self, vehicleDescriptor):
        ...
    def applyMiscAttrToMechanics(self, miscAttrs):
        ...
    def applyDynModifiersToMechanics(self, dynModifiers):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...
    def _saveOrigin(self):
        ...
    def __repr__(self):
        ...

class GunMechanicsParams(MechanicsParams):
    __slots__: tuple
    COMPONENT_TYPE_ID = ITEM_TYPES.vehicleGun
    gunInstallationSlot: _Any
    def __init__(self, modifiers=None):
        ...
    def setGunInstallationSlot(self, gunInstallationSlot):
        ...

class RechargeableNitroParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.RECHARGEABLE_NITRO.value
    deployTime: _Any
    reloadTime: _Any
    duration: _Any
    threshold: _Any
    cooldown: _Any
    addMaxSpeedForwardBonus: _Any
    addRotationSpeedBonus: _Any
    impulse: _Any
    def __init__(self, deployTime, reloadTime, duration, cooldown, addMaxSpeedForwardBonus, addRotationSpeedBonus, impulse, modifiers, threshold=0):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...
    def __applyMulModifier(self, modifierType, modifierName, bonusValue):
        ...
    def __repr__(self):
        ...

class ConcentrationModeParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.CONCENTRATION_MODE.value
    deployTime: _Any
    reloadTime: _Any
    duration: _Any
    def __init__(self, deployTime, reloadTime, duration, modifiers):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class ImprovedRammingParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.IMPROVED_RAMMING.value
    damageBonusStageSize: _Any
    damageBonusBasicFactor: _Any
    damageBonusChangeFactor: _Any
    trackDamageBonusStageSize: _Any
    trackDamageBonusBasicFactor: _Any
    trackDamageBonusChangeFactor: _Any
    reductionDamageBonusStageSize: _Any
    reductionDamageBonusBasicFactor: _Any
    reductionDamageBonusChangeFactor: _Any
    damageValueToShowAnimation: _Any
    effectSpeedThreshold: _Any
    def __init__(self, damageBonusStageSize, damageBonusBasicFactor, damageBonusChangeFactor, trackDamageBonusStageSize, trackDamageBonusBasicFactor, trackDamageBonusChangeFactor, reductionDamageBonusStageSize, reductionDamageBonusBasicFactor, reductionDamageBonusChangeFactor, damageValueToShowAnimation, effectSpeedThreshold):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class PowerModeParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.POWER_MODE.value
    DEFAULT_VEHICLE_PARAMS: dict
    modeThreshold: _Any
    modeDuration: _Any
    accelerationFactor: _Any
    attenuationFactor: _Any
    speedThreshold: _Any
    gracePeriod: _Any
    vehicleParams: _Any
    def __init__(self, modeThreshold, modeDuration, accelerationFactor, attenuationFactor, speedThreshold, gracePeriod, vehicleParams):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class BattleFuryParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.BATTLE_FURY.value
    maxLevel: _Any
    duration: _Any
    reloadSpdBonus: _Any
    gainPerHit: _Any
    gainPerKill: _Any
    def __init__(self, maxLevel, duration, reloadSpdBonus, gainPerHit, gainPerKill):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class PillboxSiegeModeParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.PILLBOX_SIEGE_MODE.value
    switchDriveToPillboxTime: _Any
    switchSiegeToPillboxTime: _Any
    switchPillboxToSiegeTime: _Any
    switchPillboxToDriveTime: _Any
    modifiers: _Any
    def __init__(self, switchDriveToPillboxTime, switchSiegeToPillboxTime, switchPillboxToSiegeTime, switchPillboxToDriveTime, modifiers):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class StationaryReloadParams(GunMechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.STATIONARY_RELOAD.value
    preparingSpeedFactor: _Any
    finishingSpeedFactor: _Any
    preparingDelay: _Any
    finishingDelay: _Any
    fixAngles: _Any
    def __init__(self, preparingSpeedFactor, finishingSpeedFactor, preparingDelay, finishingDelay, fixAngles):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class ExtraShotClipParams(GunMechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.EXTRA_SHOT_CLIP.value
    extraReloadTime: _Any
    def __init__(self, extraReloadTime):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def isActiveMechanics(self, vehicleDescriptor):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class AccuracyStacksParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.ACCURACY_STACKS.value
    levelMax: _Any
    levelInitial: _Any
    levelAfterShot: _Any
    aimLevelBonus: _Any
    aimBonusCap: _Any
    gainMaxSpd: _Any
    gainTime: _Any
    stabilizeBonus: _Any
    def __init__(self, levelMax, levelInitial, levelAfterShot, aimLevelBonus, aimBonusCap, gainMaxSpd, gainTime, stabilizeBonus):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

# base nao representavel no stub: with_metaclass(...)
class SecondaryGunParams:
    __slots__: tuple
    MECHANICS_NAME = 'secondaryGun'
    initiationTime: _Any
    dependentOnMainGun: _Any
    def __init__(self, initiationTime, dependentOnMainGun):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def getMechanicsMiscAttributes(self):
        ...
    def isActiveMechanics(self, vehicleDescriptor):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...
    @staticmethod
    def _generateMechanicMiscAttributes(gunDescr=None):
        ...

class SupportWeaponParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.SUPPORT_WEAPON.value
    def __init__(self):
        ...
    def isActiveMechanics(self, vehicleDescriptor):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...

class ChargeableBurstParams(GunMechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.CHARGEABLE_BURST.value
    penetrationCount: _Any
    burstDispersionFactor: _Any
    def __init__(self, penetrationCount, burstDispersionFactor, modifiers):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def isActiveMechanics(self, vehicleDescriptor):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class LowChargeShotParams(GunMechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.LOW_CHARGE_SHOT.value
    almostFinishedTime: _Any
    reloadTimeCoefficient: _Any
    def __init__(self, almostFinishedTime, reloadTimeCoefficient, modifiers):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class ChargeShotParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.CHARGE_SHOT.value
    timePerLevel: _Any
    damageFactorsPerLevel: _Any
    maxLevel: _Any
    shotBlockTime: _Any
    def __init__(self, timePerLevel, damageFactorsPerLevel, shotBlockTime):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class OverheatStacksParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.OVERHEAT_STACKS.value
    levelMax: _Any
    gainTime: _Any
    gainMaxSpd: _Any
    delayTimerDuration: _Any
    heatingTime: _Any
    coolingTime: _Any
    dmgBonus: _Any
    aimBonus: _Any
    levelInc: _Any
    levelDec: _Any
    dmgLevelBonus: _Any
    aimLevelBonus: _Any
    def __init__(self, heatingTime, coolingTime, dmgBonus, aimBonus, gainMaxSpd, delayTimerDuration):
        ...
    def configure(self):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, _):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...
    def applyMiscAttrToMechanics(self, miscAttrs):
        ...
    @staticmethod
    def __clampAimLevelBonus(aimLevelBonus):
        ...

class TargetDesignatorParams(MechanicsParams):
    __slots__: _Any
    MECHANICS_NAME = VehicleMechanic.TARGET_DESIGNATOR.value
    damageIncomeFactor: _Any
    cooldownTime: _Any
    deployTime: _Any
    spottedMarkedTime: _Any
    unspottedMarkedTime: _Any
    def __init__(self, damageIncomeFactor, cooldownTime, deployTime, spottedMarkedTime, unspottedMarkedTime):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, _):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class AutoreloaderSurgeParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.AUTORELOADER_SURGE.value
    _MIN_CHARGES = 2
    _MAX_CHARGES = 4
    maxCharges: _Any
    startCharges: _Any
    chargeTimeSRegular: _Any
    chargeTimeSFullClip: _Any
    reloadTime: _Any
    def __init__(self, maxCharges, startCharges, chargeTimeSRegular, chargeTimeSFullClip, reloadTime):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class StanceDanceParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.STANCE_DANCE.value
    timeSwitchStance: _Any
    maxEnergy: _Any
    gainFightEnergyPoints: _Any
    gainTurboEnergyPoints: _Any
    gainEnergyTime: _Any
    gainTurboEnergyBonusPoints: _Any
    gainTurboEnergySpdLimitKmh: _Any
    passiveFightEnergyBonusPerHit: _Any
    passiveTurboFwdSpdBonusKmh: _Any
    passiveTurboBkwdSpdBonusKmh: _Any
    passiveTurboEnginePowerBonus: _Any
    passiveTurboAccuracyDebuff: _Any
    passiveTurboAimSpeedDebuff: _Any
    passiveTurboStabilizeDebuff: _Any
    passiveTurboAfterShotDispersionDebuff: _Any
    activeFightCost: _Any
    activeFightDuration: _Any
    activeFightAccuracyBonus: _Any
    activeFightAimSpeedBonus: _Any
    activeFightStabilizeBonus: _Any
    activeFightAfterShotDispersionBonus: _Any
    activeFightReloadSpdBonus: _Any
    activeTurboCost: _Any
    activeTurboDuration: _Any
    activeTurboFwdSpdBonusKmh: _Any
    activeTurboBkwdSpdBonusKmh: _Any
    activeTurboEnginePowerBonus: _Any
    activeTurboRotationSpeedDebuff: _Any
    activeTurboRammingDmgBonus: _Any
    impulse: _Any
    modifiers: _Any
    def __init__(self, timeSwitchStance, maxEnergy, gainFightEnergyPoints, gainTurboEnergyPoints, gainEnergyTime, gainTurboEnergyBonusPoints, gainTurboEnergySpdLimitKmh, passiveFightEnergyBonusPerHit, passiveTurboFwdSpdBonusKmh, passiveTurboBkwdSpdBonusKmh, passiveTurboEnginePowerBonus, passiveTurboAccuracyDebuff, passiveTurboAimSpeedDebuff, passiveTurboStabilizeDebuff, passiveTurboAfterShotDispersionDebuff, activeFightCost, activeFightDuration, activeFightAccuracyBonus, activeFightAimSpeedBonus, activeFightStabilizeBonus, activeFightAfterShotDispersionBonus, activeFightReloadSpdBonus, activeTurboCost, activeTurboDuration, activeTurboFwdSpdBonusKmh, activeTurboBkwdSpdBonusKmh, activeTurboEnginePowerBonus, activeTurboRotationSpeedDebuff, activeTurboRammingDmgBonus, impulse):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class DebuffsParams(MechanicsParams):
    __slots__: _Any
    MECHANICS_NAME = 'reactiveDebuffs'
    debuffs: _Any
    def __init__(self, debuffs):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...

class TemperatureGunThermalStates(object):
    __slots__: tuple
    _MAX_THERMAL_STATES = 10
    states: _Any
    thermalStateHysteresis: _Any
    def __init__(self, states, thermalStateHysteresis):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...
    def __hash__(self):
        ...
    @classmethod
    def readThermalStates(cls, ctx, section, readModifiers, mechanicName):
        ...

class TemperatureGunParams(GunMechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.TEMPERATURE_GUN.value
    thermalStates: _Any
    heatingPerShot: _Any
    coolingDelay: _Any
    coolingPerSec: _Any
    def __init__(self, thermalStates, heatingPerShot, coolingDelay, coolingPerSec):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    @property
    def maxTemperature(self):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class OverheatGunParams(GunMechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.OVERHEAT_GUN.value
    coolingPerSecFactor: _Any
    tempOverheatOnThreshold: _Any
    tempOverheatOffThreshold: _Any
    tempOverheatWarnThreshold: _Any
    def __init__(self, coolingPerSecFactor, tempOverheatOnThreshold, tempOverheatOffThreshold, tempOverheatWarnThreshold):
        ...
    def isActiveMechanics(self, vehicleDescriptor):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class HeatingZonesGunParams(GunMechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.HEATING_ZONES_GUN.value
    ZONE_STATE = HEATING_ZONES_GUN_STATE
    zones: _Any
    def __init__(self, zones):
        ...
    def isActiveMechanics(self, vehicleDescriptor):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...

class StagedJetBoostersParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.STAGED_JET_BOOSTERS.value
    deployTime: _Any
    reloadTime: _Any
    reuseCount: _Any
    duration: _Any
    impulse: _Any
    impulseSpeedLimits: _Any
    modifiers: _Any
    customRotationPoints: _Any
    def __init__(self, deployTime, reloadTime, reuseCount, duration, impulse, impulseSpeedLimits, modifiers, customRotationPoints):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    @classmethod
    def _readCustomRotationPoints(cls, ctx, section):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class PropellantGunDamageFactors(object):
    __slots__: tuple
    __hash__ = None
    minFactor: _Any
    maxFactor: _Any
    def __init__(self, minFactor, maxFactor):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...

class PropellantGunParams(GunMechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.PROPELLANT_GUN.value
    _MAX_STAGES = 10
    chargeStages: _Any
    chargingPerSec: _Any
    chargeSpendingAfterShot: _Any
    forbiddenShells: _Any
    shouldPauseOnReload: _Any
    chargeDelay: _Any
    dischargingPerSec: _Any
    overchargeSwitchCooldown: _Any
    def __init__(self, chargeStages, chargingPerSec, chargeSpendingAfterShot, forbiddenShells, shouldPauseOnReload, chargeDelay, dischargingPerSec, overchargeSwitchCooldown):
        ...
    @property
    def maxCharge(self):
        ...
    @property
    def maxOvercharge(self):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def applyDynModifiersToMechanics(self, dynModifiers):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    @classmethod
    def _readChargeStages(cls, ctx, section, readModifiers):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...
    def __applyDamageFactor(self, factorType, value, isOvercharge):
        ...

class WheeledDashParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.WHEELED_DASH.value
    deployTime: _Any
    reloadTime: _Any
    duration: _Any
    speedTrigger: _Any
    speedReloadTimeFactor: _Any
    tickedImpulse: _Any
    def __init__(self, deployTime, reloadTime, duration, modifiers, speedTrigger, speedReloadTimeFactor, tickedImpulse):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    @classmethod
    def readReloadTimeBoostData(cls, ctx, section, subsection='reloadTimeBoost'):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class AuxiliaryRocketLauncherParams(GunMechanicsParams):
    MECHANICS_NAME = VehicleMechanic.AUXILIARY_ROCKET_LAUNCHER.value
    def __init__(self):
        ...
    def isActiveMechanics(self, vehicleDescriptor):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...

class ShellSwitcherParams(GunMechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.SHELL_PARAMS_SWITCHER.value
    modifiedShells: _Any
    def __init__(self, modifiedShells):
        ...
    def isActiveMechanics(self, vehicleDescriptor):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...

class ShellCalibrationBonus(object):
    __slots__: tuple
    __hash__ = None
    dmgBonus: _Any
    modifiers: _Any
    def __init__(self, damageCoefficient, modifiers):
        ...
    def __eq__(self, other):
        ...
    def __ne__(self, other):
        ...

class ShellCalibrationParams(GunMechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.SHELL_CALIBRATION.value
    penBonuses: _Any
    nonPenBonuses: _Any
    forbiddenShells: _Any
    def __init__(self, penBonuses, nonPenBonuses, forbiddenShells):
        ...
    def isActiveMechanics(self, vehicleDescriptor):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def applyDynModifiersToMechanics(self, dynModifiers):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class CrestMovingParams(MechanicsParams):
    MECHANICS_NAME = VehicleMechanic.CREST_MOVING.value

class BustleFeedParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.BUSTLE_FEED.value
    activationTime: _Any
    deactivationTime: _Any
    animationTime: _Any
    bustleShotReloadFactor: _Any
    bustleShotDamageBonusShell0: _Any
    bustleShotDamageBonusShell1: _Any
    bustleShotsIndices: _Any
    def __init__(self, activationTime, deactivationTime, modifiers, bustleShotReloadFactor, bustleShotDamageBonusShell0, bustleShotDamageBonusShell1):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    def getBustleShotDamageBonusShell(self, idx):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...

class SightPointerParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.SIGHT_POINTER.value
    _MAX_STAGES = 10
    _MIN_DURATION = 1
    initialDeployTime: _Any
    reloadTime: _Any
    activeStages: _Any
    selfReveal: _Any
    selfRevealVisionTime: _Any
    sightPointerStages: _Any
    def __init__(self, initialDeployTime, reloadTime, activeStages, selfReveal, selfRevealVisionTime, sightPointerStages):
        ...
    @property
    def duration(self):
        ...
    @classmethod
    def getDefaultMechanicsMiscAttributes(cls):
        ...
    def _applyMechanicsAttrs(self, attr, value):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...
    @classmethod
    def _readStages(cls, ctx, section, readModifiers):
        ...

class SpecBoostModeParams(MechanicsParams):
    __slots__: tuple
    MECHANICS_NAME = VehicleMechanic.SPEC_BOOST_MODE.value
    deployTime: _Any
    reloadTime: _Any
    duration: _Any
    def __init__(self, deployTime, cooldown, duration, modifiers, mechanicVariant):
        ...
    def __repr__(self):
        ...
    @classmethod
    def _readMechanicsParams(cls, ctx, section, readModifiers):
        ...

def readImpulseData(ctx, section, subsection='impulse'):
    ...
def readTickedImpulseData(ctx, section, subsection='tickedImpulse'):
    ...
def readShellCDsByName(ctx, section, subsection='shells'):
    ...
def addMechanicsParamsAttrs(attrsSet):
    ...
