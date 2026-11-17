# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/artefacts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import os as os
from re import findall as findall
from enum import Enum as Enum, unique as unique
from future.utils import listvalues as listvalues, viewitems as viewitems, viewvalues as viewvalues
from typing import NamedTuple as NamedTuple, Set as Set, Dict as Dict, Optional as Optional, Any as Any, Tuple as Tuple, List as List
from Math import Vector3 as Vector3
from ResMgr import DataSection as DataSection
import items as items
import nations as nations
from ArenaType import readVisualScriptSection as readVisualScriptSection
from constants import IS_CLIENT as IS_CLIENT, IS_CELLAPP as IS_CELLAPP, IS_WEB as IS_WEB, VEHICLE_TTC_ASPECTS as VEHICLE_TTC_ASPECTS, ATTACK_REASON as ATTACK_REASON, ATTACK_REASON_INDICES as ATTACK_REASON_INDICES, SERVER_TICK_LENGTH as SERVER_TICK_LENGTH, SkillProcessorArgs as SkillProcessorArgs, GroupSkillProcessorArgs as GroupSkillProcessorArgs, TTC_TOOLTIP_SECTIONS as TTC_TOOLTIP_SECTIONS
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from extension_utils import importClass as importClass
from items import ITEM_OPERATION as ITEM_OPERATION, PREDEFINED_HEAL_GROUPS as PREDEFINED_HEAL_GROUPS
from items import _xml as _xml, vehicles as vehicles
from items.artefacts_helpers import VehicleFilter as VehicleFilter, _ArtefactFilter as _ArtefactFilter, readKpi as readKpi
from items.basic_item import BasicItem as BasicItem
from items.components import shared_components as shared_components, component_constants as component_constants
from items.components.supply_slot_categories import SupplySlotFilter as SupplySlotFilter, LevelsFactor as LevelsFactor, AttrsOperation as AttrsOperation, SlotCategories as SlotCategories
from items.vehicles import VehicleDescriptor as VehicleDescriptor, _readPriceForOperation as _readPriceForOperation
from items.tankmen import MAX_SKILL_LEVEL as MAX_SKILL_LEVEL
from soft_exception import SoftException as SoftException
from vehicle_filters import getVehicleFilters as getVehicleFilters
UpgradeInfo: _Any
DowngradeInfo: _Any
_APPLICATION_POSITION_KEY = 'applicationPosition'
_readTags = vehicles._readTags

class i18n(object):
    @classmethod
    def makeString(cls, key):
        ...

# decorador original: @unique
class ExportParamsTag(Enum):
    VSE = 'vse'
    TOOLTIP = 'tooltip'

# decorador original: @unique
class OrderTypes(str, Enum):
    RANDOM = 'random'
    SEQUENTIALLY = 'sequentially'
    @classmethod
    def values(cls):
        ...

class CommonXmlSectionReader(object):
    __xmlTagKeyMap: _Any
    __readersMap: _Any
    def __init__(self, xmlTagKeyMap, dictInstance):
        ...
    def read(self, xmlCtx, section, subsection_name):
        ...
    @staticmethod
    def __createReaders(dictInstance):
        ...

class VehicleFactorsXmlReader(CommonXmlSectionReader):
    __readerImpl = None
    def __init__(self):
        ...
    @staticmethod
    def readFactors(xmlCtx, section, subsection_name):
        ...

class Artefact(BasicItem):
    __slots__: tuple
    icon: _Any
    iconName: _Any
    removable: _Any
    price: _Any
    showInShop: _Any
    _vehWeightFraction: _Any
    _weight: _Any
    _exportParams: _Any
    __vehicleFilter: _Any
    __artefactFilter: _Any
    isImproved: _Any
    kpi: _Any
    _groupName: _Any
    __tooltipSection: _Any
    __archetype: _Any
    name: _Any
    id: _Any
    compactDescr: _Any
    tags: _Any
    i18n: _Any
    def __init__(self, typeID, itemID, itemName, compactDescr):
        ...
    def init(self, xmlCtx, section):
        ...
    @property
    def isAvatarEquipment(self):
        ...
    @property
    def tooltipParams(self):
        ...
    def updatePrice(self, newPrice, showInShop):
        ...
    def extraName(self):
        ...
    def removeItem(self, *args, **kwargs):
        ...
    @property
    def groupName(self):
        ...
    @property
    def tooltipSection(self):
        ...
    @property
    def archetype(self):
        ...
    def _readWeight(self, xmlCtx, section):
        ...
    def weightOnVehicle(self, vehicleDescr):
        ...
    def checkCompatibilityWithVehicle(self, vehicleDescr):
        ...
    def checkCompatibilityWithOther(self, other):
        ...
    def checkCompatibilityWithActiveOther(self, other):
        ...
    def compatibleNations(self):
        ...
    def checkCompatibilityWithComponents(self, vehicleDescr):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        ...
    def getVehicleFilter(self):
        ...
    def _readBasicConfig(self, xmlCtx, section):
        ...
    def _getExportParamsDict(self, exportTag):
        ...
    @staticmethod
    def _readExportParams(section):
        ...

class OptionalDevice(Artefact):
    __slots__: tuple
    categories: _Any
    _overridableFactors: _Any
    _tier: _Any
    _tierlessName: _Any
    _isModernized: _Any
    _isUpgradable: _Any
    _isUpgraded: _Any
    def __init__(self):
        ...
    def _readBasicConfig(self, xmlCtx, section):
        ...
    def extraName(self):
        ...
    @property
    def tier(self):
        ...
    @property
    def tierlessName(self):
        ...
    @property
    def groupName(self):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        ...
    def updateVehicleDescrAttrs(self, vehicleDescr):
        ...
    @property
    def canUseDemountKit(self):
        ...
    @property
    def isDeluxe(self):
        ...
    @property
    def isTrophy(self):
        ...
    @property
    def isModernized(self):
        ...
    @property
    def isUpgradable(self):
        ...
    @property
    def isUpgraded(self):
        ...
    @property
    def isRegular(self):
        ...
    def defineActiveLevel(self, vehicleDescr):
        ...
    def defineActiveValueForSpecFactor(self, vehicleDescr, factorName, level=None):
        ...
    def _defineFactorFor(self, vehicleDescr, factorName):
        ...
    def _readSpecFactorsFromConfig(self, xmlCtx, section):
        ...
    def _readCategories(self, xmlCtx, section):
        ...
    def _readTier(self, xmlCtx, section):
        ...

class StaticOptionalDevice(OptionalDevice):
    __slots__: tuple
    _factors: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _readFactorsFromConfig(self, xmlCtx, section):
        ...
    @staticmethod
    def defineAttrsDict(vehicleDescr, modulePath):
        ...
    def updateVehicleDescrAttrs(self, vehicleDescr):
        ...
    def getFactorValue(self, vehicleDescr, attrPath, default=0.0):
        ...
    def factorsContainCrewLevelIncrease(self):
        ...

class StillVehicleOptionalDevice(StaticOptionalDevice):
    __slots__: tuple
    activateWhenStillSec: _Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        ...
    def _checkAspect(self, aspect):
        ...
    def transformFactors(self, level, vehicleDescr):
        ...
    def updateFactorsDictWithTransformed(self, factorsDict, transformedFactors):
        ...

class Stereoscope(StillVehicleOptionalDevice):
    __slots__: tuple
    CIRCULAR_VISION_RADIUS = 'circularVisionRadius'
    circularVisionRadiusFactor: _Any
    def extraName(self):
        ...
    def _checkAspect(self, aspect):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def transformFactors(self, level, vehicleDescr):
        ...
    def updateFactorsDictWithTransformed(self, factorsDict, transformedFactors):
        ...

class CamouflageNet(StillVehicleOptionalDevice):
    invisibilityBonusName = 'invisibilityBonus'
    invisibilityAttr = 'invisibility'
    def extraName(self):
        ...
    @property
    def competesBy(self):
        ...
    def transformFactors(self, level, vehicleDescr):
        ...
    def updateFactorsDictWithTransformed(self, factorsDict, transformedFactors):
        ...
    def _checkAspect(self, aspect):
        ...

class LowNoiseTracks(StaticOptionalDevice):
    invisibilityBonusName = 'invisibilityBonus'
    def updateVehicleDescrAttrs(self, vehicleDescr):
        ...

class ImprovedConfiguration(StaticOptionalDevice):
    __slots__: tuple
    engineReduceFineFactor: _Any
    ammoBayReduceFineFactor: _Any
    def extraName(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Equipment(Artefact):
    __slots__: tuple
    equipmentType: _Any
    stunResistanceEffect: _Any
    stunResistanceDuration: _Any
    repeatedStunDurationFactor: _Any
    reuseCount: _Any
    cooldownSeconds: _Any
    soundNotification: _Any
    clientSelector: _Any
    playerMessagesKey: _Any
    messagePostfix: _Any
    usagePrefab: _Any
    usagePrefabEnemy: _Any
    ownerPrefab: _Any
    def __init__(self):
        ...
    def _readBasicConfig(self, xmlCtx, section):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        ...
    def extraName(self):
        ...
    def checkCompatibilityWithEquipment(self, other):
        ...
    def checkCompatibilityWithActiveEquipment(self, other):
        ...
    def offload(self, inventoryCallback):
        ...
    def doesDependOnOptionalDevice(self):
        ...

class EpicEmptySlot(Equipment):
    ...

class ExtraHealthReserve(StaticOptionalDevice):
    def updateVehicleDescrAttrs(self, vehicleDescr):
        ...

class Grousers(StaticOptionalDevice):
    __slots__: tuple
    rotationFactor: _Any
    rollingFrictionFactor: _Any
    def updateVehicleDescrAttrs(self, vehicleDescr):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class RotationMechanisms(StaticOptionalDevice):
    __slots__: tuple
    trackMoveSpeedFactor: _Any
    wheelMoveSpeedFactor: _Any
    trackRotateSpeedFactor: _Any
    wheelRotateSpeedFactor: _Any
    wheelCenterRotationFwdSpeed: _Any
    def updateVehicleDescrAttrs(self, vehicleDescr):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Extinguisher(Equipment):
    __slots__: tuple
    fireStartingChanceFactor: _Any
    autoactivate: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        ...

class Fuel(Equipment):
    __slots__: tuple
    enginePowerFactor: _Any
    turretRotationSpeedFactor: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        ...

class Stimulator(Equipment):
    __slots__: tuple
    crewLevelIncrease: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Repairkit(Equipment):
    __slots__: tuple
    bonusValue: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class CountableConsumableConfigReader(object):
    _CONSUMABLE_SLOTS: tuple
    consumeAmmo: _Any
    def initCountableConsumableSlots(self):
        ...
    def readCountableConsumableConfig(self, xmlCtx, section):
        ...

class RemovedRpmLimiter(Equipment):
    __slots__: tuple
    enginePowerFactor: _Any
    engineHpLossPerSecond: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        ...

class Afterburning(Equipment):
    __slots__: tuple
    deploySeconds: _Any
    consumeSeconds: _Any
    rechargeSeconds: _Any
    enginePowerFactor: _Any
    maxSpeedFactor: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, aspect, *args, **kwargs):
        ...

class RageEquipmentConfigReader(object):
    _RAGE_EQUIPMENT_SLOTS: tuple
    reusable: _Any
    cooldownTime: _Any
    deployTime: _Any
    def initRageEquipmentSlots(self):
        ...
    def readRageEquipmentConfig(self, xmlCtx, section):
        ...

class SharedCooldownConsumableConfigReader(object):
    _SHARED_COOLDOWN_CONSUMABLE_SLOTS: tuple
    cooldownTime: _Any
    cooldownFactors: _Any
    prepareTime: _Any
    consumeAmmo: _Any
    disableAllyDamage: _Any
    setUnavailableAfterAmmoLeft: _Any
    sharedCooldownTime: _Any
    def initSharedCooldownConsumableSlots(self):
        ...
    def readSharedCooldownConsumableConfig(self, xmlCtx, section):
        ...
    def _readCooldownFactors(self, xmlCtx, section, name):
        ...

class CooldownConsumableConfigReader(object):
    _CONSUMABLE_SLOTS: tuple
    deployTime: _Any
    cooldownTime: _Any
    def initConsumableWithDeployTimeSlots(self):
        ...
    def readConsumableWithTimeConfig(self, xmlCtx, section):
        ...

class TooltipConfigReader(object):
    _SHARED_TOOLTIPS_CONSUMABLE_SLOTS: tuple
    shortDescription: _Any
    longDescription: _Any
    shortFilterAlert: _Any
    longFilterAlert: _Any
    tooltipIdentifiers: _Any
    def initTooltipInformation(self):
        ...
    def readTooltipInformation(self, xmlCtx, section):
        ...

class BaseMarkerConfigReader(object):
    _MARKER_SLOTS_: tuple
    areaVisual: _Any
    areaColor: _Any
    areaMarker: _Any
    areaUsedPrefab: _Any
    def initMarkerInformation(self):
        ...
    def readMarkerConfig(self, xmlCtx, section):
        ...

class AreaMarkerConfigReader(BaseMarkerConfigReader):
    _MARKER_SLOTS_: _Any
    areaRadius: _Any
    areaLength: _Any
    areaWidth: _Any
    def initMarkerInformation(self):
        ...
    def readMarkerConfig(self, xmlCtx, section):
        ...

class EffectsConfigReader(object):
    _EFFECTS_SLOTS_: tuple
    effects: _Any
    def initEffectsInformation(self):
        ...
    def readEffectConfig(self, xmlCtx, section):
        ...
    def _readEffect(self, xmlCtx, section):
        ...
    def _readSequencesConfig(self, section):
        ...

class ArtilleryConfigReader(AreaMarkerConfigReader):
    _ARTILLERY_SLOTS: _Any
    delay: _Any
    duration: _Any
    shotsNumber: _Any
    shellCompactDescr: _Any
    piercingPower: _Any
    shotSoundPreDelay: _Any
    wwsoundShot: _Any
    wwsoundEquipmentUsed: _Any
    noOwner: _Any
    def initArtillerySlots(self):
        ...
    def readArtilleryConfig(self, xmlCtx, section):
        ...

class PlaneConfigReader(object):
    _PLANE_SLOTS: tuple
    delay: _Any
    speed: _Any
    modelName: _Any
    soundEvent: _Any
    heights: _Any
    areaVisual: _Any
    areaColor: _Any
    areaMarker: _Any
    def initPlaneSlots(self):
        ...
    def readPlaneConfig(self, xmlCtx, section):
        ...

class BomberConfigReader(PlaneConfigReader):
    _BOMBER_SLOTS: _Any
    areaLength: _Any
    areaWidth: _Any
    antepositions: _Any
    lateropositions: _Any
    bombingMask: _Any
    waveFraction: _Any
    bombsNumber: _Any
    shellCompactDescr: _Any
    tracerKind: _Any
    piercingPower: _Any
    gravity: _Any
    shootingDistance: _Any
    noOwner: _Any
    wwsoundEquipmentUsed: _Any
    def initBomberSlots(self):
        ...
    def readBomberConfig(self, xmlCtx, section):
        ...

class SmokeConfigReader(object):
    _SMOKE_SLOTS: tuple
    minDelay: _Any
    deltaDelayRange: _Any
    smokeModelName: _Any
    startRadius: _Any
    expandedRadius: _Any
    startHeight: _Any
    expandedHeight: _Any
    heightUpFraction: _Any
    expansionDuration: _Any
    dispersionRadius: _Any
    totalDuration: _Any
    smokeOpacity: _Any
    attrFactorMods: _Any
    expireDelay: _Any
    postEffectTeams: _Any
    dotParams: _Any
    areaLength: _Any
    areaWidth: _Any
    projectilesNumber: _Any
    shellCompactDescr: _Any
    areaVisual: _Any
    areaColor: _Any
    areaMarker: _Any
    noOwner: _Any
    smokeEffectNameAlly: _Any
    smokeEffectNameEnemy: _Any
    shotSoundPreDelay: _Any
    wwsoundShot: _Any
    orthogonalDir: _Any
    randomizeDuration: _Any
    vignetteColor: _Any
    vignetteIntensity: _Any
    def initSmokeSlots(self):
        ...
    def readSmokeConfig(self, xmlCtx, section):
        ...
    def _readAttrFactorMods(self, xmlCtx, section):
        ...
    def _readPostEffectTeams(self, _, section):
        ...

class ReconConfigReader(PlaneConfigReader):
    _RECON_SLOTS: _Any
    entitiesToSearch: _Any
    areaRadius: _Any
    scanPointsAmount: _Any
    antepositions: _Any
    lateropositions: _Any
    areaLength: _Any
    areaWidth: _Any
    wwsoundEquipmentUsed: _Any
    def initReconSlots(self):
        ...
    def readReconConfig(self, xmlCtx, section):
        ...
    def __readEntitiesToSearch(self, xmlCtx, section):
        ...

class BuffConfigReader(object):
    _BUFF_SLOTS: tuple
    duration: _Any
    inactivationDelay: _Any
    radius: _Any
    wwsoundEquipmentUsed: _Any
    def initBuffSlots(self):
        ...
    def readBuffConfig(self, xmlCtx, section):
        ...

class InspireConfigReader(BuffConfigReader):
    _INSPIRE_SLOTS: _Any
    increaseFactors: _Any
    def initInspireSlots(self):
        ...
    def readInspireConfig(self, xmlCtx, section):
        ...

class HealPointConfigReader(BuffConfigReader):
    _HEAL_POINT_SLOTS: _Any
    healPerTick: _Any
    expireByDamageReceived: _Any
    healGroup: _Any
    tickInterval: _Any
    height: _Any
    depth: _Any
    def initHealPointSlots(self):
        ...
    def readHealPointConfig(self, xmlCtx, section):
        ...

class ArenaAimLimits(object):
    __slots__: tuple
    insetRadius: _Any
    areaSwitch: _Any
    areaColor: _Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    def _readConfig(self, xmlCtx, section):
        ...
    @staticmethod
    def readConfig(xmlCtx, section, subsection_name):
        ...

class Marker(object):
    __slots__: tuple
    _sectionName: _Any
    name: _Any
    textColor: _Any
    def __init__(self, sectionName):
        ...
    def readConfig(self, xmlCtx, section):
        ...
    def _validate(self):
        ...

class Markers(object):
    __slots__: tuple
    _sectionName: _Any
    ally: _Any
    enemy: _Any
    def __init__(self, sectionName):
        ...
    def readConfig(self, xmlCtx, section):
        ...

class MarkersConfigReader(object):
    _MARKERS_CONFIG_SLOTS: tuple
    markers: _Any
    def initMarkers(self):
        ...
    def readMarkersConfig(self, xmlCtx, section):
        ...

class ArcadeEquipmentConfigReader(object):
    _SHARED_ARCADE_SLOTS: tuple
    minApplyRadius: _Any
    maxApplyRadius: _Any
    applyRadiusVisible: _Any
    cameraPivotPosMin: _Any
    cameraPivotPosMax: _Any
    arenaAimLimits: _Any
    def initArcadeInformation(self):
        ...
    def readArcadeInformation(self, xmlCtx, section):
        ...

class DynamicEquipment(Equipment):
    __slots__: tuple
    _config: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def getLevelIDForVehicle(self, vehicleDescr):
        ...
    def doesDependOnOptionalDevice(self):
        ...
    def getLevelParamsForDevice(self, optionalDevice):
        ...
    def configContainCrewLevelIncrease(self):
        ...
    def updateVehicleAttrFactorsForAspect(self, vehicleDescr, factors, _, *args, **kwargs):
        ...
    def updateVehicleAttrFactorsForLevel(self, factors, levelID):
        ...
    def _readLevelConfig(self, xmlCtx, section):
        ...
    def _updateVehicleAttrFactorsImpl(self, factors, levelParams):
        ...

class FactorBattleBooster(DynamicEquipment):
    __slots__: tuple
    def _readLevelConfig(self, xmlCtx, section):
        ...
    def _updateVehicleAttrFactorsImpl(self, factors, levelParams):
        ...

class AdditiveBattleBooster(DynamicEquipment):
    __slots__: tuple
    def _readLevelConfig(self, xmlCtx, section):
        ...
    def _updateVehicleAttrFactorsImpl(self, factors, levelParams):
        ...

class InvisibilityBattleBooster(DynamicEquipment):
    __slots__: tuple
    def _readLevelConfig(self, xmlCtx, section):
        ...
    def _updateVehicleAttrFactorsImpl(self, factors, levelParams):
        ...

class SkillEquipment(Equipment):
    __slots__: tuple
    skillName: _Any
    perkLevelMultiplier: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateCrewSkill(self, *args):
        ...

class FactorSkillBattleBooster(SkillEquipment):
    __slots__: tuple
    efficiencyFactor: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateCrewSkill(self, a):
        ...

class SixthSenseBattleBooster(SkillEquipment):
    __slots__: tuple
    delay: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateCrewSkill(self, a):
        ...

class PedantBattleBooster(SkillEquipment):
    __slots__: tuple
    ammoBayHealthFactor: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateCrewSkill(self, a):
        ...

class LastEffortBattleBooster(SkillEquipment):
    __slots__: tuple
    durationPerLevel: _Any
    chanceToHitPerLevel: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateCrewSkill(self, a):
        ...

class _OptionalDeviceFilter(object):
    __requiredTags: _Any
    __incompatibleTags: _Any
    def __init__(self, xmlCtx, section):
        ...
    def checkCompatibility(self, vehicleDescr):
        ...
    def checkCompatibilityWithDevice(self, optionalDevice):
        ...

class RageArtillery(Equipment, RageEquipmentConfigReader, ArtilleryConfigReader):
    __slots__: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class RageBomber(Equipment, RageEquipmentConfigReader, BomberConfigReader):
    __slots__: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class ConsumableArtillery(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, ArtilleryConfigReader):
    __slots__: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class ConsumableBomber(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, BomberConfigReader):
    __slots__: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class ConsumableRecon(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, ReconConfigReader):
    __slots__: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class ConsumableSmoke(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, SmokeConfigReader):
    __slots__: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class ConsumableInspire(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, InspireConfigReader):
    __slots__: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class PassiveConsumable(Equipment, TooltipConfigReader):
    __slots__ = TooltipConfigReader._SHARED_TOOLTIPS_CONSUMABLE_SLOTS
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class PassiveEngineering(Equipment, TooltipConfigReader):
    __slots__: _Any
    captureStopping: _Any
    captureBlockBonusTime: _Any
    captureSpeedFactor: _Any
    resupplyCooldownFactor: _Any
    resupplyShellsFactor: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class EpicArtillery(ConsumableArtillery):
    ...

class EpicBomber(ConsumableBomber):
    ...

class EpicRecon(ConsumableRecon):
    ...

class EpicSmoke(ConsumableSmoke):
    ...

class EpicInspire(ConsumableInspire):
    __slots__: tuple
    selfIncreaseFactors: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class FLPassiveEngineering(PassiveEngineering):
    ...

class FortConsumableInspire(ConsumableInspire):
    ...

class AreaOfEffectEquipment(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, ArcadeEquipmentConfigReader, EffectsConfigReader, MarkersConfigReader):
    __slots__: _Any
    delay: _Any
    duration: _Any
    lifetime: _Any
    shotsNumber: _Any
    areaRadius: _Any
    areaLength: _Any
    areaWidth: _Any
    areaVisual: _Any
    areaColor: _Any
    areaColorBlind: _Any
    areaShow: _Any
    areaAccurateCollision: _Any
    areaVisibleToEnemies: _Any
    areaUsedPrefab: _Any
    noOwner: _Any
    attackerType: _Any
    shotSoundPreDelay: _Any
    wwsoundShot: _Any
    wwsoundEquipmentUsed: _Any
    shotEffect: _Any
    actionsConfig: _Any
    explodeDestructible: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _readActionConfig(self, section):
        ...

class AttackBomberEquipment(AreaOfEffectEquipment):
    ...

class AttackArtilleryFortEquipment(AreaOfEffectEquipment):
    __slots__: tuple
    enemyAreaColor: _Any
    enemyAreaColorBlind: _Any
    maxDamage: _Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    @staticmethod
    def __readDamageVehicleAction(section):
        ...

class UpgradableItem(Artefact):
    __upgradeInfo: _Any
    _downgradeInfo: _Any
    _level: _Any
    def __init__(self, typeID, itemID, itemName, compactDescr):
        ...
    @property
    def upgradeInfo(self):
        ...
    @property
    def downgradeInfo(self):
        ...
    @property
    def level(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _readUpgradableConfig(self, xmlCtx, scriptSection):
        ...
    def _initUpgradeInfo(self, xmlCtx, upgradeInfoSection, upgradedCD):
        ...
    def _initDowngradeInfo(self, device):
        ...

class UpgradedItem(Artefact):
    _downgradeInfo: _Any
    _level: _Any
    def __init__(self, typeID, itemID, itemName, compactDescr):
        ...
    @property
    def downgradeInfo(self):
        ...
    @property
    def level(self):
        ...

class UpgradableStaticDevice(StaticOptionalDevice, UpgradableItem):
    ...

class UpgradedStaticDevice(StaticOptionalDevice, UpgradedItem):
    ...

class UpgradableImprovedConfiguration(ImprovedConfiguration, UpgradableItem):
    ...

class UpgradableExtraHealthReserve(ExtraHealthReserve, UpgradableItem):
    ...

class UpgradedImprovedConfiguration(ImprovedConfiguration, UpgradedItem):
    ...

class UpgradedExtraHealthReserve(ExtraHealthReserve, UpgradedItem):
    ...

class UpgradableRotationMechanisms(RotationMechanisms, UpgradableItem):
    ...

class UpgradedRotationMechanisms(RotationMechanisms, UpgradedItem):
    ...

class UpgradableLowNoiseTracks(LowNoiseTracks, UpgradableItem):
    ...

class UpgradedLowNoiseTracks(LowNoiseTracks, UpgradedItem):
    ...

class Bomber(Equipment, TooltipConfigReader, CountableConsumableConfigReader, BomberConfigReader):
    __slots__: _Any
    cooldownTime: _Any
    longDescription: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class Smoke(Equipment, TooltipConfigReader, CountableConsumableConfigReader, SmokeConfigReader):
    __slots__: _Any
    cooldownTime: _Any
    longDescription: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class DOTParams(object):
    __slots__: tuple
    damagePerTick: _Any
    tickInterval: _Any
    restoreHealth: _Any
    canDie: _Any
    groupID: _Any
    attackReasonID: _Any
    def __init__(self, attackReasonID=...):
        ...
    def __repr__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class HOTParams(object):
    __slots__: tuple
    healPerTick: _Any
    healCrew: _Any
    healDevices: _Any
    healGroup: _Any
    tickInterval: _Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class FLRegenerationKit(Equipment, SharedCooldownConsumableConfigReader, TooltipConfigReader):
    __slots__: _Any
    healthRegenPerTick: _Any
    initialHeal: _Any
    healTime: _Any
    healGroup: _Any
    tickInterval: _Any
    expireByDamageReceived: _Any
    resupplyHealthPointsFactor: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class FLAvatarStealthRadar(Equipment, SharedCooldownConsumableConfigReader, CooldownConsumableConfigReader, TooltipConfigReader, InspireConfigReader):
    __slots__: _Any
    passiveCircularVisionRadius: _Any
    detectionTime: _Any
    overridableFactors: _Any
    longDescription: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def readOverFactorsFromConfig(self, xmlCtx, section):
        ...

class MineParams(object):
    __slots__: tuple
    triggerRadius: _Any
    triggerHeight: _Any
    triggerDepth: _Any
    influenceType: _Any
    lifetime: _Any
    damage: _Any
    shell: _Any
    shellLowDamage: _Any
    resistAllyDamage: _Any
    destroyMyMinesOverlappingAlliedMines: _Any
    directDetectionTypes: _Any
    activationDelay: _Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    def _readConfig(self, xmlCtx, section):
        ...

class Minefield(Equipment, TooltipConfigReader, ArcadeEquipmentConfigReader, CountableConsumableConfigReader):
    __slots__: _Any
    bombsPattern: _Any
    mineParams: _Any
    noOwner: _Any
    disableAllyDamage: _Any
    cooldownTime: _Any
    areaLength: _Any
    areaWidth: _Any
    areaVisual: _Any
    areaColor: _Any
    areaMarker: _Any
    longDescription: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class FrontLineMinefield(Equipment, TooltipConfigReader, SharedCooldownConsumableConfigReader, ArcadeEquipmentConfigReader, CooldownConsumableConfigReader):
    __slots__: tuple
    bombsPattern: _Any
    mineParams: _Any
    noOwner: _Any
    areaLength: _Any
    areaWidth: _Any
    areaVisual: _Any
    areaColor: _Any
    areaMarker: _Any
    bombsNumber: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class VisualScriptEquipment(Equipment):
    __slots__: tuple
    visualScript: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _exportSlotsToVSE(self):
        ...
    def isActivationConfirmed(self, args):
        ...

class PointVisualScriptEquipment(VisualScriptEquipment):
    __slots__: tuple
    def isActivationConfirmed(self, args):
        ...

class LevelBasedVisualScriptEquipment(VisualScriptEquipment):
    _LEVEL_BASED_SLOTS: tuple
    radius: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def getRadiusBasedOnSkillLevel(self, skillLevel):
        ...

class DynComponentsGroupEquipment(Equipment):
    __slots__: tuple
    durationSeconds: _Any
    dynComponentsGroups: _Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class PoiRadarEquipment(VisualScriptEquipment):
    __slots__: tuple
    duration: _Any
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class PoiIlluminationFlareEquipment(PointVisualScriptEquipment, BaseMarkerConfigReader):
    __slots__: _Any
    duration: _Any
    delay: _Any
    startRadius: _Any
    endRadius: _Any
    unSpotDuration: _Any
    areaPrefabColorAlly: _Any
    areaPrefabColorEnemy: _Any
    areaPrefabColorEnemyCB: _Any
    startYFlare: _Any
    endYFlare: _Any
    damageIncomeFactor: _Any
    decayPhaseDuration: _Any
    def __init__(self):
        ...
    def initMarkerInformation(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class PoiArtilleryEquipment(PointVisualScriptEquipment, BaseMarkerConfigReader, EffectsConfigReader):
    __slots__: _Any
    delay: _Any
    radius: _Any
    damage: _Any
    stunDuration: _Any
    areaShow: _Any
    duration: _Any
    fraction: _Any
    requireAssists: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class OPT_DEV_TYPE_TAG(object):
    TROPHY_BASIC = 'trophyBasic'
    TROPHY_UPGRADED = 'trophyUpgraded'
    DELUXE = 'deluxe'
    MODERNIZED1 = 'modernized_1'
    MODERNIZED2 = 'modernized_2'
    MODERNIZED3 = 'modernized_3'
    ALL: set
    @staticmethod
    def checkTags(tags):
        ...

class AoeEffects(object):
    START = 'start'
    POSTSTART = 'poststart'
    ACTION = 'action'

class AreaShow(object):
    BEFORE = 'before'
    ALWAYS = 'always'

class Circle(object):
    __slots__: tuple
    abilityRadius: _Any
    safeZoneRadius: _Any
    def __init__(self):
        ...
    def readConfig(self, xmlCtx, section):
        ...

class CGFEquipmentItem(Equipment):
    __slots__: tuple
    durationSeconds: _Any
    prefab: _Any
    filters: _Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

def _readStun(xmlCtx, scriptSection):
    ...
def _readReuseParams(xmlCtx, scriptSection):
    ...
