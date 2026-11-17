# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/common/battle_royale_artefacts.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Math import Vector3 as Vector3
from constants import IS_CLIENT as IS_CLIENT, ATTACK_REASON as ATTACK_REASON, ATTACK_REASON_INDICES as ATTACK_REASON_INDICES, SERVER_TICK_LENGTH as SERVER_TICK_LENGTH
from items.artefacts import Repairkit as Repairkit, CountableConsumableConfigReader as CountableConsumableConfigReader, Equipment as Equipment, VehicleFactorsXmlReader as VehicleFactorsXmlReader, DOTParams as DOTParams, HOTParams as HOTParams, Bomber as Bomber, ArcadeEquipmentConfigReader as ArcadeEquipmentConfigReader, Smoke as Smoke, TooltipConfigReader as TooltipConfigReader, AreaMarkerConfigReader as AreaMarkerConfigReader, HealPointConfigReader as HealPointConfigReader, PREDEFINED_HEAL_GROUPS as PREDEFINED_HEAL_GROUPS, Minefield as Minefield
from items import _xml as _xml, vehicles as vehicles
from items.components import component_constants as component_constants
from items.stun import g_cfg as stunConfig
from helpers import i18n as i18n
from gui.impl.backport import text as text
from gui.impl.backport.backport_system_locale import getNiceNumberFormat as getNiceNumberFormat, getIntegralFormat as getIntegralFormat
from gui.impl.gen import R as R

class BattleDescriptionConfigReader(object):
    _BATTLE_DESCRIPTION_SLOTS: tuple
    battleDescription: Any
    def initBattleDescriptionSlots(self):
        ...
    def readBattleDescriptionConfig(self, xmlCtx, section):
        ...

class RepairkitBattleRoyale(Repairkit, CountableConsumableConfigReader):
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class AfterburningBattleRoyale(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    consumeSeconds: Any
    enginePowerFactor: Any
    maxSpeedFactor: Any
    vehicleRotationSpeed: Any
    deploySeconds: Any
    rechargeSeconds: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def updateVehicleAttrFactors(self, vehicleDescr, factors, aspect):
        ...
    def _getDescription(self, descr):
        ...
    def _prepareDescription(self, descr):
        ...

class InfluenceZone(object):
    __slots__: tuple
    radius: Any
    height: Any
    depth: Any
    timer: Any
    terrainResistance: Any
    debuffFactors: Any
    dotParams: Any
    hotParams: Any
    influenceType: Any
    fireEffectName: Any
    componentName: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, section):
        ...

class TrapPoint(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    radius: Any
    zonesCount: Any
    influenceZone: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _getDescription(self, descr):
        ...
    def _prepareDescription(self, descr):
        ...

class BomberArcade(Bomber, ArcadeEquipmentConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    influenceZone: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class BomberArcadeWithOwnDamage(Bomber, ArcadeEquipmentConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    abilityRadius: Any
    directHitRadius: Any
    stunRadius: Any
    maxDamage: Any
    minDamage: Any
    maxModuleDamage: Any
    minModuleDamage: Any
    damageSpread: Any
    stunTime: Any
    minStunTime: Any
    longDescription: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def initOwnDamageParams(self):
        ...
    def _readOwnDamageConfig(self, xmlCtx, scriptSection):
        ...
    def _getDescription(self, descr):
        ...
    def _prepareDescription(self, descr):
        ...

class SmokeArcade(Smoke, ArcadeEquipmentConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    orthogonalDir: Any
    cooldownTime: Any
    longDescription: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _prepareDescription(self, descr):
        ...

class SelfBuff(Equipment, TooltipConfigReader, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    duration: Any
    cooldownTime: Any
    increaseFactors: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _getDescription(self, descr):
        ...
    def _prepareDescription(self, descr):
        ...

class Berserker(SelfBuff):
    __slots__: tuple
    dotParams: Any
    cooldownTime: Any
    duration: Any
    increaseFactors: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _prepareDescription(self, descr):
        ...

class _ClientSpawnBotVisuals(object):
    __slots__: tuple
    markerPositionOffset: Any
    markerScale: Any
    deliveringAnimationDuration: Any
    deliveringAnimationStartDelay: Any
    highlightDelay: Any
    def __init__(self, xmlCtx, scriptSection):
        ...

class BRHealPoint(Equipment, TooltipConfigReader, CountableConsumableConfigReader, HealPointConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    cooldownTime: Any
    longDescription: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _prepareDescription(self, descr):
        ...

class RegenerationKit(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__: tuple
    healthRegenPerTick: Any
    initialHeal: Any
    healTime: Any
    healGroup: Any
    tickInterval: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _getDescription(self, descr):
        ...
    def _prepareDescription(self, descr):
        ...

class BRMinefield(Minefield, BattleDescriptionConfigReader):
    __slots__: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...

class ConsumableSpawnBot(Equipment, TooltipConfigReader, CountableConsumableConfigReader, AreaMarkerConfigReader, ArcadeEquipmentConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    botType: Any
    botVehCompDescr: Any
    botLifeTime: Any
    botSpawnPointOffset: Any
    botXRayFactor: Any
    explosionRadius: Any
    explosionDamage: Any
    explosionByShoot: Any
    damageReductionRate: Any
    clientVisuals: Any
    delay: Any
    cooldownTime: Any
    disableAllyDamage: Any
    clientRemovalNotificationDelay: Any
    longDescription: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _prepareDescription(self, descr):
        ...

class ZonesCircle(Equipment):
    __slots__: tuple
    radius: Any
    zonesCount: Any
    vehicleHeightMultiplier: Any
    influenceZone: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _getDescription(self, descr):
        ...

class FireCircle(ZonesCircle, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _getDescription(self, descr):
        ...
    def _prepareDescription(self, descr):
        ...

class CorrodingShot(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    damagePercentAfterShot: Any
    canBeStoppedRepairKit: Any
    increaseFactors: Any
    dotParams: Any
    dotEffectDuration: Any
    tooltipMovie: Any
    effectsIndex: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _getDescription(self, descr):
        ...
    def _prepareDescription(self, descr):
        ...

class AdaptationHealthRestore(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    duration: Any
    restoringCoefficient: Any
    restoringCoefficientTeamMates: Any
    teamMateRestoringRadius: Any
    areaVisual: Any
    posteffectPrefab: Any
    immediatelyRestore: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readBasicConfig(self, xmlCtx, section):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _getDescription(self, descr):
        ...
    def _prepareDescription(self, descr):
        ...

class ThunderStrike(Equipment, ArcadeEquipmentConfigReader, TooltipConfigReader, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    cooldownTime: Any
    canBeStoppedRepairKit: Any
    noOwner: Any
    consumeAmmo: Any
    duration: Any
    damage: Any
    thunderCount: Any
    thunderPeriod: Any
    areaLength: Any
    areaWidth: Any
    areaVisual: Any
    areaColor: Any
    damageRadius: Any
    decreaseFactors: Any
    isDamageAll: Any
    delay: Any
    longDescription: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _prepareDescription(self, descr):
        ...

class ShotPassion(Equipment, CountableConsumableConfigReader, BattleDescriptionConfigReader):
    __slots__: Any
    duration: Any
    damageIncreasePerShot: Any
    maxDamageIncreasePerShot: Any
    cooldownTime: Any
    posteffectPrefab: Any
    increaseFactors: Any
    battleDescription: Any
    def __init__(self):
        ...
    def _readBasicConfig(self, xmlCtx, section):
        ...
    def _readConfig(self, xmlCtx, scriptSection):
        ...
    def _getDescription(self, descr):
        ...
    def _prepareDescription(self, descr):
        ...
