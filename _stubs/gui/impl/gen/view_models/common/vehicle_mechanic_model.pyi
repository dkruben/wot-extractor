# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/common/vehicle_mechanic_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class MechanicsEnum(Enum):
    UNKNOWN = 'unknown'
    MAGAZINE_GUN = 'magazineGun'
    AUTO_LOADER_GUN = 'autoLoaderGun'
    AUTO_LOADER_GUN_BOOST = 'autoLoaderGunBoost'
    DAMAGE_MUTABLE = 'damageMutable'
    DUAL_GUN = 'dualGun'
    HYDRAULIC_CHASSIS = 'hydraulicChassis'
    TRACK_WITHIN_TRACK = 'trackWithinTrack'
    SIEGE_MODE = 'siegeMode'
    STUN = 'stun'
    HYDRAULIC_WHEELED_CHASSIS = 'hydraulicWheeledChassis'
    TURBOSHAFT_ENGINE = 'turboshaftEngine'
    ROCKET_ACCELERATION = 'rocketAcceleration'
    TARGET_DESIGNATOR = 'targetDesignator'
    DUAL_ACCURACY = 'dualAccuracy'
    AUTO_SHOOT_GUN = 'autoShootGun'
    TWIN_GUN = 'twinGun'
    IMPROVED_RAMMING = 'improvedRamming'
    CONCENTRATION_MODE = 'concentrationMode'
    BATTLE_FURY = 'battleFury'
    EXTRA_SHOT_CLIP = 'extraShotClip'
    POWER_MODE = 'powerMode'
    ACCURACY_STACKS = 'accuracyStacks'
    SUPPORT_WEAPON = 'supportWeapon'
    PILLBOX_SIEGE_MODE = 'pillboxSiegeMode'
    CHARGEABLE_BURST = 'chargeableBurst'
    SHELL_CALIBRATION = 'shellCalibration'
    RECHARGEABLE_NITRO = 'rechargeableNitro'
    CHARGE_SHOT = 'chargeShot'
    OVERHEAT_STACKS = 'overheatStacks'
    SIGHT_POINTER = 'sightPointer'
    STANCE_DANCE = 'stanceDance'
    AUTORELOADER_SURGE = 'autoreloaderSurge'
    STATIONARY_RELOAD = 'stationaryReload'
    OVERHEAT_GUN = 'overheatGun'
    HEATING_ZONES_GUN = 'heatingZonesGun'
    LOW_CHARGE_SHOT = 'lowChargeShot'
    STAGED_JET_BOOSTERS = 'stagedJetBoosters'
    PROPELLANT_GUN = 'propellantAfterburnerGun'
    WHEELED_DASH = 'wheeledDash'
    AUXILIARY_ROCKET_LAUNCHER = 'auxiliaryRocketLauncher'
    SHELL_PARAMS_SWITCHER = 'shellParamsSwitcher'
    BUSTLE_FEED = 'bustleFeed'
    COMBAT_THROTTLE = 'combatThrottle'

class MechanicsRank(Enum):
    UNDEFINED = 'undefined'
    SILVER = 'silver'
    GOLD = 'gold'

class VehicleMechanicModel(ViewModel):
    __slots__: tuple
    MIN_SPECIAL_PRIORITY = 1
    def __init__(self, properties=4, commands=0):
        ...
    def getName(self):
        ...
    def setName(self, value):
        ...
    def getPriority(self):
        ...
    def setPriority(self, value):
        ...
    def getRank(self):
        ...
    def setRank(self, value):
        ...
    def getHasVideo(self):
        ...
    def setHasVideo(self, value):
        ...
    def _initialize(self):
        ...
