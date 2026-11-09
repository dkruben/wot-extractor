# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/gui_items/__init__.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl import backport as backport
from gui.impl.backport import getNiceNumberFormat as getNiceNumberFormat
from gui.impl.gen import R as R
from gui.shared.items_parameters.param_name_helper import getVehicleParameterText as getVehicleParameterText
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from items import ITEM_TYPE_NAMES as ITEM_TYPE_NAMES, vehicles as vehicles, ITEM_TYPE_INDICES as ITEM_TYPE_INDICES, EQUIPMENT_TYPES as EQUIPMENT_TYPES, getTypeOfCompactDescr as getTypeOfCompactDescr
from gui.shared.money import Currency as Currency
from skeletons.gui.shared.gui_items import IGuiItemsFactory as IGuiItemsFactory
from helpers import dependency as dependency
from typing import Set as Set, FrozenSet as FrozenSet, Union as Union
_logger: Any
CLAN_LOCK = 1
GUI_ITEM_TYPE_NAMES: Any
GUI_ITEM_TYPE_INDICES: dict
VEHICLE_ATTR_TO_KPI_NAME_MAP: dict
CREW_SKILL_TO_KPI_NAME_MAP: dict
AGGREGATE_TO_SINGLE_TYPE_KPI_MAP: dict

class GUI_ITEM_TYPE(CONST_CONTAINER):
    VEHICLE: Any
    CHASSIS: Any
    TURRET: Any
    GUN: Any
    ENGINE: Any
    FUEL_TANK: Any
    RADIO: Any
    TANKMAN: Any
    OPTIONALDEVICE: Any
    SHELL: Any
    EQUIPMENT: Any
    BATTLE_ABILITY: Any
    MODULE_MECHANIC: Any
    VEHICLE_MECHANIC: Any
    CUSTOMIZATION: Any
    CREW_SKINS: Any
    CREW_BOOKS: Any
    PAINT: Any
    CAMOUFLAGE: Any
    MODIFICATION: Any
    DECAL: Any
    EMBLEM: Any
    INSCRIPTION: Any
    OUTFIT: Any
    STYLE: Any
    PROJECTION_DECAL: Any
    INSIGNIA: Any
    PERSONAL_NUMBER: Any
    SEQUENCE: Any
    ATTACHMENT: Any
    STAT_TRACKER: Any
    DEMOUNT_KIT: Any
    RECERTIFICATION_FORM: Any
    MENTORING_LICENSE: Any
    COMMON: Any
    BATTLE_BOOSTER: Any
    ARTEFACTS: tuple
    ACCOUNT_DOSSIER: Any
    VEHICLE_DOSSIER: Any
    TANKMAN_DOSSIER: Any
    ACHIEVEMENT: Any
    SKILL: Any
    BADGE: Any
    LOOT_BOX: Any
    VEH_POST_PROGRESSION: Any
    GUI: tuple
    VEHICLE_MODULES: tuple
    VEHICLE_COMPONENTS: Any
    CUSTOMIZATIONS: tuple
    CUSTOMIZATIONS_WITHOUT_STYLE: tuple
    ATTACHMENT_TYPES: tuple
    COMMON_C11NS: tuple
    COMMON_C11N_COMPATIBLE_WITH_3D_STYLES: tuple

class GUI_ITEM_ECONOMY_CODE(CONST_CONTAINER):
    UNDEFINED = ''
    CENTER_UNAVAILABLE = 'center_unavailable'
    UNLOCK_ERROR = 'unlock_error'
    ITEM_IS_HIDDEN = 'isHidden'
    ITEM_NO_PRICE = 'noPrice'
    ITEM_IS_DUPLICATED = 'duplicatedItem'
    WALLET_NOT_AVAILABLE = 'wallet_not_available'
    RESTORE_DISABLED = 'restore_disabled'
    NO_RENT_PRICE = 'no_rent_price'
    RENTAL_TIME_EXCEEDED = 'rental_time_exceeded'
    RENTAL_DISABLED = 'rental_disabled'
    NOT_ENOUGH_GOLD: Any
    NOT_ENOUGH_CREDITS: Any
    NOT_ENOUGH_CRYSTAL: Any
    NOT_ENOUGH_EVENT_COIN: Any
    NOT_ENOUGH_BPCOIN: Any
    NOT_ENOUGH_EQUIP_COIN: Any
    NOT_ENOUGH_CURRENCIES: tuple
    NOT_ENOUGH_MONEY = 'not_enough_money'
    @classmethod
    def getCurrencyError(cls, currency):
        ...
    @classmethod
    def isCurrencyError(cls, errCode):
        ...

class ItemsCollection(dict):
    def filter(self, criteria):
        ...
    def __repr__(self):
        ...

class ACTION_ENTITY_ITEM(object):
    ACTION_NAME_IDX = 0
    ACTION_STEP_IDX = 1
    AFFECTED_ACTIONS_IDX = 2
    ENTITIES_SECTION_NAME = 'actionEntities'
    ACTIONS_SECTION_NAME = 'actions'
    STEPS_SECTION_NAME = 'steps'

class KPI(object):
    __slots__: tuple
    __name: Any
    __value: Any
    __type: Any
    __specValue: Any
    __vehicleTypes: Any
    __isSituational: Any
    class Name(CONST_CONTAINER):
        COMPOUND_KPI = 'compoundKPI'
        VEHICLE_REPAIR_SPEED = 'vehicleRepairSpeed'
        VEHICLE_CHASSIS_REPAIR_SPEED = 'vehicleChassisRepairSpeed'
        VEHICLE_CHASSIS_REPAIR_TIME = 'vehicleChassisRepairTime'
        VEHICLE_ENGINE_POWER = 'vehicleEnginePower'
        VEHICLE_TURRET_ROTATION_SPEED = 'vehicleTurretRotationSpeed'
        VEHICLE_CIRCULAR_VISION_RADIUS = 'vehicleCircularVisionRadius'
        VEHICLE_STILL_CIRCULAR_VISION_RADIUS = 'vehicleStillCircularVisionRadius'
        VEHICLE_STILL_CIRCULAR_VISION_RADIUS_DELUXE = 'vehicleStillCircularVisionRadiusDeluxe'
        VEHICLE_CAMOUFLAGE = 'vehicleCamouflage'
        VEHICLE_STILL_CAMOUFLAGE = 'vehicleStillCamouflage'
        VEHICLE_STILL_CAMOUFLAGE_DELUXE = 'vehicleStillCamouflageDeluxe'
        VEHICLE_FIRE_CHANCE = 'vehicleFireChance'
        VEHICLE_GUN_RELOAD_TIME = 'vehicleGunReloadTime'
        VEHICLE_GUN_AIM_SPEED = 'vehicleGunAimSpeed'
        VEHICLE_GUN_SHOT_DISPERSION = 'vehicleGunShotDispersion'
        VEHICLE_GUN_SHOT_DISPERSION_AFTER_SHOT = 'vehicleGunShotDispersionAfterShot'
        VEHICLE_GUN_SHOT_DISPERSION_CHASSIS_MOVEMENT = 'vehicleGunShotDispersionChassisMovement'
        VEHICLE_GUN_SHOT_DISPERSION_CHASSIS_ROTATION = 'vehicleGunShotDispersionChassisRotation'
        VEHICLE_GUN_SHOT_DISPERSION_TURRET_ROTATION = 'vehicleGunShotDispersionTurretRotation'
        VEHICLE_GUN_SHOT_DISPERSION_WHILE_GUN_DAMAGED = 'vehicleGunShotDispersionWhileGunDamaged'
        VEHICLE_GUN_SHOT_FULL_DISPERSION = 'vehicleGunShotFullDispersion'
        VEHICLE_AMMO_BAY_STRENGTH = 'vehicleAmmoBayStrength'
        VEHICLE_FUEL_TANK_STRENGTH = 'vehicleFuelTankStrength'
        VEHICLE_ENGINE_STRENGTH = 'vehicleEngineStrength'
        VEHICLE_CHASSIS_STRENGTH = 'vehicleChassisStrength'
        VEHICLE_AMMO_BAY_ENGINE_FUEL_STRENGTH = 'vehicleAmmoBayEngineFuelStrength'
        VEHICLE_CHASSIS_FALL_DAMAGE = 'vehicleChassisFallDamage'
        VEHICLE_RAM_DAMAGE_RESISTANCE = 'vehicleRamDamageResistance'
        VEHICLE_DAMAGE_ENEMIES_BY_RAMMING = 'damageEnemiesByRamming'
        VEHICLE_SOFT_GROUND_PASSABILITY = 'vehicleSoftGroundPassability'
        VEHICLE_MEDIUM_GROUND_PASSABILITY = 'vehicleMediumGroundPassability'
        VEHICLE_ENEMY_SPOTTING_TIME = 'vehicleEnemySpottingTime'
        VEHICLE_OWN_SPOTTING_TIME = 'vehicleOwnSpottingTime'
        VEHICLE_INVISIBILITY_AFTER_SHOT = 'vehicleInvisibilityAfterShot'
        VEHICLE_RELOAD_TIME_AFTER_SHELL_CHANGE = 'vehicleReloadTimeAfterShellChange'
        VEHICLE_STRENGTH = 'vehicleStrength'
        VEHICLE_ALL_GROUND_ROTATION_SPEED = 'vehicleAllGroundRotationSpeed'
        VEHICLE_SPEED_GAIN = 'vehicleSpeedGain'
        VEHICLE_TURRET_OR_CUTTING_ROTATION_SPEED = 'vehicleTurretOrCuttingRotationSpeed'
        VEHICLE_FORWARD_MAX_SPEED = 'vehicleForwardMaxSpeed'
        VEHICLE_BACKWARD_MAX_SPEED = 'vehicleBackwardMaxSpeed'
        EQUIPMENT_PREPARATION_TIME = 'equipmentPreparationTime'
        DAMAGE_AND_PIERCING_DISTRIBUTION_LOWER_BOUND = 'damageAndPiercingDistributionLowerBound'
        DAMAGE_AND_PIERCING_DISTRIBUTION_UPPER_BOUND = 'damageAndPiercingDistributionUpperBound'
        PIERCING_HE_SHELLS_DISTRIBUTION_UPPER_BOUND = 'piercingHEShellsDistributionUpperBound'
        PENALTY_TO_DAMAGED_SURVEYING_DEVICE = 'penaltyToDamagedSurveyingDevice'
        STUN_RESISTANCE_EFFECT_FACTOR = 'stunResistanceEffectFactor'
        ART_NOTIFICATION_DELAY_FACTOR = 'artNotificationDelayFactor'
        MEDIUM_GROUND_FACTOR = 'mediumGroundFactor'
        SOFT_GROUND_FACTOR = 'softGroundFactor'
        WHEELS_ROTATION_SPEED = 'wheelsRotationSpeed'
        VEHICLE_FUEL_TANK_LESION_CHANCE = 'vehicleFuelTankLesionChance'
        FOLIAGE_MASKING_FACTOR = 'foliageMaskingFactor'
        ENEMY_MODULES_CREW_CRIT_CHANCE = 'enemyModulesCrewCritChance'
        VEHICLE_RAM_CHASSIS_DAMAGE_RESISTANCE = 'vehicleRamChassisDamageResistance'
        DAMAGED_MODULES_DETECTION_TIME = 'damagedModulesDetectionTime'
        FIRE_EXTINGUISHING_RATE = 'fireExtinguishingRate'
        WOUNDED_CREW_EFFICIENCY = 'woundedCrewEfficiency'
        VEHICLE_HE_SHELL_DAMAGE_RESISTANCE = 'vehicleHEShellDamageResistance'
        VEHICLE_FALLING_DAMAGE_RESISTANCE = 'vehicleFallingDamageResistance'
        VEHICLE_PENALTY_FOR_DAMAGED_ENGINE = 'vehPenaltyForDamagedEngine'
        VEHICLE_PENALTY_FOR_DAMAGED_AMMORACK = 'vehPenaltyForDamagedAmmorack'
        COMMANDER_LAMP_DELAY = 'commanderLampDelay'
        GUN_STABILIZATION = 'gunStabilization'
        HULL_ELEVATION_SPEED = 'hullElevationSpeed'
        ENGINE_HP = 'engineHP'
        FUEL_TANK_HP = 'fuelTankHP'
        VEHICLE_SPEED = 'vehicleSpeed'
        STANDARD_SHELL_PENETRATION = 'standardShellPenetration'
        SPECIAL_SHELL_PENETRATION = 'specialShellPenetration'
        ADDITIONAL_SHELL_AMMO_CAPACITY = 'additionalShellAmmoCapacity'
        NON_HE_SHELL_DAMAGE = 'nonHEShellDamage'
        HE_SHELL_DAMAGE = 'HEShellDamage'
        STANDARD_SHELL_DAMAGE = 'standardShellDamage'
        SPECIAL_SHELL_DAMAGE = 'specialShellDamage'
        ALL_SHELL_DAMAGE = 'allShellDamage'
        BASIC_SHELL_DAMAGE = 'basicShellDamage'
        HE_SHELL_PENETRATION = 'HEShellPenetration'
        GUN_DEPRESSION = 'gunDepression'
        GUN_TRAVERSE = 'gunTraverse'
        TURRET_TRAVERSE = 'turretTraverse'
        GUN_ELEVATION = 'gunElevation'
        STANDARD_SHELL_VELOCITY = 'standardShellVelocity'
        SPECIAL_SHELL_VELOCITY = 'specialShellVelocity'
        RELOAD_TIME_SALVO = 'reloadTimeSalvo'
        RELOAD_TIME_SINGLE = 'reloadTimeSingle'
        RELOAD_TIME_IN_CLIP = 'reloadTimeInClip'
        SHELL_VELOCITY = 'shellVelocity'
        ALL_SHELLS_VELOCITY = 'allShellsVelocity'
        SHELL_MODULE_DAMAGE = 'shellModuleDamage'
        SUSPENSION_DAMAGE_REDUCTION = 'suspensionDamageReduction'
        HP_RECOVER = 'hpRecover'
        COOLING_PER_SEC = 'coolingPerSec'
        HE_SHELL_VELOCITY = 'HEshellVelocity'
        MINIMUM_DAMAGE_AND_PIERCING_POWER = 'minimumDamageAndPiercingPower'
        VEHICLE_CAMOUFLAGE_GROUP = 'vehicleCamouflageGroup'
        VEHICLE_STILL_CAMOUFLAGE_GROUP = 'vehicleStillCamouflageGroup'
        VEHICLE_STILL_CAMOUFLAGE_GROUP_DELUXE = 'vehicleStillCamouflageGroupDeluxe'
        CREW_LEVEL = 'crewLevel'
        CREW_HIT_CHANCE = 'crewHitChance'
        CREW_STUN_DURATION = 'crewStunDuration'
        CREW_REPEATED_STUN_DURATION = 'crewRepeatedStunDuration'
        CREW_SKILL_REPAIR = 'crewSkillRepair'
        CREW_SKILL_FIRE_FIGHTING = 'crewSkillFireFighting'
        CREW_SKILL_CAMOUFLAGE = 'crewSkillCamouflage'
        CREW_SKILL_BROTHERHOOD = 'crewSkillBrotherHood'
        CREW_SKILL_SIXTH_SENSE = 'crewSkillSixthSense'
        CREW_SKILL_SIXTH_SENSE_DELAY = 'crewSkillSixthSenseDelay'
        CREW_SKILL_VIRTUOSO = 'crewSkillVirtuoso'
        CREW_SKILL_SMOOTH_DRIVING = 'crewSkillSmoothRiding'
        CREW_SKILL_RANCOROUS = 'crewSkillRancorous'
        CREW_SKILL_RANCOROUS_DURATION = 'crewSkillRancorousDuration'
        CREW_SKILL_PEDANT = 'crewSkillPedant'
        CREW_SKILL_SMOOTH_TURRET = 'crewSkillSmoothTurret'
        CREW_SKILL_PRACTICAL = 'crewSkillPractical'
        CREW_SKILL_STUN_RESISTANCE = 'crewSkillStunResistance'
        DEMASK_FOLIAGE_FACTOR = 'demaskFoliageFactor'
        DEMASK_MOVING_FACTOR = 'demaskMovingFactor'
        GAME_XP = 'gameXp'
        GAME_FREE_XP = 'gameFreeXp'
        GAME_CREW_XP = 'gameCrewXp'
        GAME_CREDITS = 'gameCredits'
        GAME_FL_XP = 'gameFlXp'
        GAME_FREE_XP_AND_CREW_XP = 'gameFreeXpAndCrewXp'
        VALUE = 'value'
    class Type(CONST_CONTAINER):
        MUL = 'mul'
        ADD = 'add'
        BOOST_SKILL = 'boostSkill'
        ONE_OF = 'oneOf'
        AGGREGATE_MUL = 'aggregateMul'
    def __init__(self, kpiName, kpiValue, kpiType=..., specValue=None, vehicleTypes=None, situational=False):
        ...
    @property
    def name(self):
        ...
    @property
    def value(self):
        ...
    @property
    def specValue(self):
        ...
    @property
    def type(self):
        ...
    @property
    def vehicleTypes(self):
        ...
    @property
    def situational(self):
        ...
    @property
    def isDebuff(self):
        ...
    @property
    def isPositive(self):
        ...
    def getDescriptionR(self):
        ...
    def getLongDescriptionR(self):
        ...

def getItemTypeID(bonusName):
    ...
def formatMoneyError(currency):
    ...
def getVehicleComponentsByType(vehicle, itemTypeIdx):
    ...
def getVehicleSuitablesByType(vehDescr, itemTypeId, turretPID=0):
    ...
def getItemIconName(itemName):
    ...
def checkForTags(vTags, tags):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isItemVehicleHull(intCD, vehicle, itemsFactory=None):
    ...
def kpiAddEnding(kpiName, text):
    ...
def kpiFormatValue(kpiName, value, addEnding=True):
    ...
def kpiFormatNoSignValue(kpiName, value, addEnding=True):
    ...
def kpiFormatValueRange(kpiName, valueRange, addEnding=True):
    ...
def getKpiValueString(kpi, value, addEnding=True):
    ...
def getKpiFormatDescription(kpi):
    ...
def mergeAggregateKpi(aggregateKpi):
    ...
def collectKpi(descriptor, vehicle=None):
    ...
