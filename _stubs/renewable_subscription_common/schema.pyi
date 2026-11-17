# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/renewable_subscription_common/schema.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from future.utils import iteritems as iteritems
import constants as constants
from account_shared import validateCustomizationItem as validateCustomizationItem
from battle_pass_integration import getAllIntergatedGameModes as getAllIntergatedGameModes
from constants import ARENA_BONUS_TYPE_NAMES as ARENA_BONUS_TYPE_NAMES, IS_CLIENT as IS_CLIENT, VEHICLE_CLASSES as VEHICLE_CLASSES, MIN_VEHICLE_LEVEL as MIN_VEHICLE_LEVEL, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL
from dict2model import fields as d2m_fields, models as models, schemas as schemas, validate as validate, exceptions as exceptions
from game_params_common.schema import GameParamsSchema as GameParamsSchema
from game_params_common.scope import GameParamsScopeFlags as GameParamsScopeFlags, clientFilter as clientFilter
from items import vehicles as vehicles
_logger: Any
_customCompensationSchema: Any
_customizationSchema: Any
_exclusiveVehicleSchema: Any
_tierFeatureSchema: Any
_tierSchema: Any
_bonusFactorsSchema: Any
_battleBonusesFeatureSchema: Any
_badgesFeatureSchema: Any
_excludedMapFeatureSchema: Any
_reserveGainsPerBattleTypeSchema: Any
_goldReserveFeatureSchema: Any
_compatibleVehiclesSchema: Any
_proBoostFeatureSchema: Any
_freeEquipmentDemountingFeatureSchema: Any
_passiveCrewXPFeatureSchema: Any
_dailyAttendanceFeatureSchema: Any
_additionalXPBonusFeatureSchema: Any
_exclusiveVehicleFeatureSchema: Any
_optionalDevicesAssistantFeatureSchema: Any
_crewAssistantFeatureSchema: Any
_bpPointsOverrideSchema: Any
_bpPointsSchema: Any
_battlePassFeatureSchema: Any
_serviceRecordCustomizationFeatureSchema: Any
_SubscriptionFeaturesModelType: Any
_subscriptionFeaturesSchema: Any
renewableSubscriptionsConfigSchema: Any

class Features(object):
    BATTLE_BONUSES = 1
    BADGES = 2
    EXCLUDED_MAP = 3
    GOLD_RESERVE = 4
    PRO_BOOST = 5
    FREE_EQUIPMENT_DEMOUNTING = 6
    PASSIVE_CREW_XP = 7
    DAILY_ATTENDANCE = 8
    ADDITIONAL_XP = 9
    EXCLUSIVE_VEHICLE = 10
    OPTIONAL_DEVICES_ASSISTANT = 11
    CREW_ASSISTANT = 12
    BATTLE_PASS = 13
    SERVICE_RECORD_CUSTOMIZATION = 14
    ALL: tuple

class _CustomCompensation(models.Model):
    __slots__: tuple
    credits: Any
    gold: Any
    def __init__(self, credits, gold):
        ...

class _Customization(models.Model):
    __slots__: tuple
    styleId: Any
    customCompensation: Any
    def __init__(self, styleId, customCompensation):
        ...

class _ExclusiveVehicle(models.Model):
    __slots__: tuple
    vehicleName: Any
    noCrew: Any
    customization: Any
    _vehicleIntCD: Any
    def __init__(self, vehicleName, noCrew, customization):
        ...
    def getVehicleIntCD(self):
        ...

class _FeatureModel(models.Model):
    __slots__: tuple
    enabled: Any
    _available: Any
    def __init__(self, enabled, *args, **kwargs):
        ...
    @property
    def available(self):
        ...
    def setAvailable(self, value):
        ...
    def getFeatureID(self):
        ...

class _TierFeatureModel(models.Model):
    __slots__: tuple
    name: Any
    overriddenParams: Any
    class _ForbiddenOverride(object):
        ENABLED = 'enabled'
        XP_PER_MINUTE_FACTOR = 'xpPerMinute'
    def __init__(self, name, overriddenParams):
        ...
    @classmethod
    def validateOverrideFields(cls, oParams):
        ...

class _TierModel(models.Model):
    __slots__: tuple
    id: Any
    productCodes: Any
    productEnabledForSteam: Any
    features: Any
    def __init__(self, id, productCodes, productEnabledForSteam, features):
        ...
    @classmethod
    def checkUniqFeatures(cls, modelsList):
        ...

class _BonusFactors(models.Model):
    __slots__: tuple
    xpFactor: Any
    creditsFactor: Any
    crewXPFactor: Any
    freeXPFactor: Any
    def __init__(self, xpFactor, creditsFactor, crewXPFactor, freeXPFactor):
        ...

class _BattleBonusesFeatureModel(_FeatureModel):
    __slots__: tuple
    bonusFactors: Any
    def __init__(self, enabled, bonusFactors):
        ...
    def getFeatureID(self):
        ...

class _BadgesFeatureModel(_FeatureModel):
    __slots__: tuple
    badgeIDs: Any
    def __init__(self, enabled, badgeIDs):
        ...
    def getFeatureID(self):
        ...

class _ExcludedMapFeatureModel(_FeatureModel):
    __slots__: tuple
    count: Any
    def __init__(self, enabled, count):
        ...
    def getFeatureID(self):
        ...

class _ReserveGainsPerBattle(models.Model):
    __slots__: tuple
    arenaBonusType: Any
    win: Any
    loss: Any
    draw: Any
    minLevel: Any
    minTop: Any
    topType: Any
    def __init__(self, arenaBonusType, win, loss, draw, minLevel, minTop, topType):
        ...

class _GoldReserveFeatureModel(_FeatureModel):
    __slots__: tuple
    maxCapacity: Any
    reserveGainsPerBattleType: Any
    def __init__(self, enabled, maxCapacity, reserveGainsPerBattleType):
        ...
    def getArenaTypeToGain(self):
        ...
    @classmethod
    def checkUniqArenaBonusTypes(cls, modelsList):
        ...
    def getFeatureID(self):
        ...

class _CompatibleVehicles(models.Model):
    __slots__: tuple
    tankClass: Any
    excludedLevels: Any
    def __init__(self, tankClass, excludedLevels):
        ...

class _ProBoostFeatureModel(_FeatureModel):
    __slots__: tuple
    applicableVehiclesLimit: Any
    cooldown: Any
    bonusFactors: Any
    excludedTags: Any
    compatibleVehicles: Any
    def __init__(self, enabled, applicableVehiclesLimit, cooldown, bonusFactors, excludedTags, compatibleVehicles):
        ...
    @classmethod
    def checkUniqueTankClasses(cls, modelsList):
        ...
    def getFeatureID(self):
        ...

class _FreeEquipmentDemountingFeatureModel(_FeatureModel):
    __slots__: tuple
    deluxeEnabled: Any
    def __init__(self, enabled, deluxeEnabled):
        ...
    def getFeatureID(self):
        ...

class _PassiveCrewXPFeatureModel(_FeatureModel):
    __slots__: tuple
    xpPerMinute: Any
    def __init__(self, enabled, xpPerMinute):
        ...
    def getFeatureID(self):
        ...

class _DailyAttendanceFeatureModel(_FeatureModel):
    __slots__: tuple
    questPrefix: Any
    def __init__(self, enabled, questPrefix):
        ...
    def getFeatureID(self):
        ...

class _AdditionalXPBonusFeatureModel(_FeatureModel):
    __slots__: tuple
    applyCount: Any
    def __init__(self, enabled, applyCount):
        ...
    def getFeatureID(self):
        ...

class _ExclusiveVehicleFeatureModel(_FeatureModel):
    __slots__: tuple
    exclusiveVehicles: Any
    def __init__(self, enabled, exclusiveVehicles):
        ...
    def getFeatureID(self):
        ...

class _OptionalDevicesAssistantFeature(_FeatureModel):
    def getFeatureID(self):
        ...

class _CrewAssistantFeature(_FeatureModel):
    def getFeatureID(self):
        ...

class _BattlePassFeature(_FeatureModel):
    __slots__: tuple
    points: Any
    _bonusTypeToPoints: Any
    def __init__(self, enabled, points):
        ...
    def getFeatureID(self):
        ...
    def getVehiclePointListsForMode(self, bonusType, vehTypeCompDescr):
        ...
    @classmethod
    def checkUniqArenaBonusTypes(cls, modelsList):
        ...
    @classmethod
    def checkBPIntegratedModes(cls, modelsList):
        ...
    @classmethod
    def _getArenaBonusTypeIdByName(cls, model):
        ...

class _BPpointsOverride(models.Model):
    __slots__: tuple
    vehicle: Any
    win: Any
    loss: Any
    def __init__(self, vehicle, win, loss):
        ...

class _BPpoints(models.Model):
    __slots__: tuple
    arenaBonusType: Any
    win: Any
    loss: Any
    overrides: Any
    _vehicleIntCDtoPoints: Any
    def __init__(self, arenaBonusType, win, loss, overrides):
        ...
    def getPointsForVehicle(self, vehTypeCompDescr):
        ...

class _ServiceRecordCustomizationFeature(_FeatureModel):
    def getFeatureID(self):
        ...

class _SubscriptionFeaturesModel(models.Model):
    __slots__: tuple
    goldReserveFeature: Any
    excludedMapFeature: Any
    badgesFeature: Any
    battleBonusesFeature: Any
    freeEquipmentDemountingFeature: Any
    passiveCrewXPFeature: Any
    dailyAttendanceFeature: Any
    additionalXPBonusFeature: Any
    exclusiveVehicleFeature: Any
    proBoostFeature: Any
    optionalDevicesAssistantFeature: Any
    crewAssistantFeature: Any
    battlePassFeature: Any
    serviceRecordCustomizationFeature: Any
    _availableFeatures: Any
    def __init__(self, goldReserveFeature, excludedMapFeature, badgesFeature, battleBonusesFeature, freeEquipmentDemountingFeature, passiveCrewXPFeature, dailyAttendanceFeature, additionalXPBonusFeature, exclusiveVehicleFeature, proBoostFeature, optionalDevicesAssistantFeature, crewAssistantFeature, battlePassFeature, serviceRecordCustomizationFeature):
        ...
    def getAvailableFeatures(self):
        ...

# base nao representavel no stub: GameParamsSchema[...]
class _SubscriptionFeaturesSchema:
    def __init__(self, fields=None, modelClass=..., checkUnknown=True, serializedValidators=None, deserializedValidators=None, readers=None):
        ...

class _SubscriptionFullModel(_SubscriptionFeaturesModel):
    __slots__: tuple
    enabled: Any
    enabledForSteam: Any
    tiers: Any
    _overriddenTiers: Any
    _tierProductCodes: Any
    def __init__(self, enabled, enabledForSteam, goldReserveFeature, excludedMapFeature, badgesFeature, battleBonusesFeature, freeEquipmentDemountingFeature, passiveCrewXPFeature, dailyAttendanceFeature, additionalXPBonusFeature, exclusiveVehicleFeature, proBoostFeature, optionalDevicesAssistantFeature, crewAssistantFeature, tiers, battlePassFeature, serviceRecordCustomizationFeature):
        ...
    def getAllProductCodes(self):
        ...
    def getTierProductCodes(self, tierID):
        ...
    def getTierSettingsById(self, tierID):
        ...
    def _initOverriddenTiers(self):
        ...
    def _initTierSubscriptionCodes(self):
        ...

def _checkUniqListItems(modelsList, fieldGetter):
    ...
def _validateVehicle(strDescriptor):
    ...
def _validateStyle(styleId):
    ...
def _createBPpointsListField():
    ...
