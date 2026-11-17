# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/client/battle_modifiers/gui/impl/gen/view_models/views/lobby/feature/modifier_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from battle_modifiers.gui.impl.gen.view_models.views.lobby.feature.limit_model import LimitModel as LimitModel

class ModType(Enum):
    FAKE_MODIFIER = 'fakeModifier'
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
    INVISIBILITY_FACTOR_AT_SHOT = 'invisibilityFactorAtShot'
    VEHICLE_AOI_RADIUS = 'vehicleAoIRadius'
    DEVICE_DAMAGE_FIRST = 'deviceDamageFirst'
    AMMO_BAY_HEALTH = 'ammoBayHealth'
    ENGINE_HEALTH = 'engineHealth'
    FUEL_TANK_HEALTH = 'fuelTankHealth'
    TURRET_ROTATOR_HEALTH = 'turretRotatorHealth'
    SURVEYING_DEVICE_HEALTH = 'surveyingDeviceHealth'
    CHASSIS_HEALTH = 'chassisHealth'
    GUN_HEALTH = 'gunHealth'

class ModPhysType(Enum):
    UNDEFINED = 'undefined'
    METERS_PER_SECOND = 'metersPerSecond'
    KILOMETERS_PER_HOUR = 'km_per_hour'
    RADIANS = 'radians'
    DEGREES = 'degrees'
    DEGREES_PER_SECOND = 'degrees_per_second'
    HIT_POINTS = 'hitPoints'
    MILLIMETERS = 'millimeters'
    METERS = 'meters'
    SECONDS = 'seconds'
    MINUTES = 'minutes'
    RADIANS_PER_SECOND = 'radians_per_second'
    METER_PER_SECOND_SQUARED = 'meter_per_second_squared'
    PROBABILITY = 'probability'
    DEVIATION = 'deviation'
    LOGIC = 'logic'
    HORSEPOWER = 'horsepower'

class ModUseType(Enum):
    UNDEFINED = 'undefined'
    VAL = 'val'
    MUL = 'mul'
    ADD = 'add'

class ModGameplayImpact(Enum):
    UNDEFINED = 'undefined'
    POSITIVE = 'positive'
    NEGATIVE = 'negative'

class ModifierModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=7, commands=0):
        ...
    def getModificationType(self):
        ...
    def setModificationType(self, value):
        ...
    def getResName(self):
        ...
    def setResName(self, value):
        ...
    def getValue(self):
        ...
    def setValue(self, value):
        ...
    def getPhysicalType(self):
        ...
    def setPhysicalType(self, value):
        ...
    def getUseType(self):
        ...
    def setUseType(self, value):
        ...
    def getGameplayImpact(self):
        ...
    def setGameplayImpact(self, value):
        ...
    def getLimits(self):
        ...
    def setLimits(self, value):
        ...
    @staticmethod
    def getLimitsType():
        ...
    def _initialize(self):
        ...
