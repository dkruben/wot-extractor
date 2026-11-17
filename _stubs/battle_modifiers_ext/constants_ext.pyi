# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_modifiers/scripts/common/battle_modifiers_ext/constants_ext.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from collections import OrderedDict as OrderedDict
from future.utils import viewitems as viewitems, viewvalues as viewvalues, iteritems as iteritems
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT, SHELL_TYPES as SHELL_TYPES, BATTLE_LOG_SHELL_TYPES as BATTLE_LOG_SHELL_TYPES
from items.vehicle_items import Shell as Shell
BATTLE_PARAMS_XML_PATH = 'scripts/item_defs/battle_params.xml'
REMAPPING_XML_PATH = 'scripts/item_defs/remapping.xml'
BATTLE_MODIFIERS_DIR = 'scripts/server_xml/battle_modifiers/'
BATTLE_MODIFIERS_XML = 'battle_modifiers.xml'
USE_VEHICLE_CACHE = True
USE_CONSTANTS_CACHE = True
MAX_VEHICLE_CACHE_LAYER_COUNT = 5
MAX_CONSTANTS_CACHE_LAYER_COUNT = 5
FAKE_PARAM_NAME = 'fakeParam'
DEBUG_MODIFIERS = IS_DEVELOPMENT
ERROR_TEMPLATE = '[BattleModifiers] {} for param {}'

class DataType(object):
    INT = 0
    FLOAT = 1
    STRING = 2
    DICT = 3
    HASHABLE_DICT = 4
    HASHABLE_TYPES: tuple
    ID_TO_NAME: dict
    NAME_TO_ID: dict
    ALL: Any
    NAMES: Any

class UseType(object):
    UNDEFINED = 0
    VAL = 1
    MUL = 2
    ADD = 3
    DIMENSIONAL_TYPES: set
    ID_TO_NAME: dict
    NAME_TO_ID: dict
    ALL: Any
    NAMES: Any
    ALL_WITH_UNDEFINED: Any
    NON_DIMENSIONAL_TYPES: Any

class PhysicalType(object):
    UNDEFINED = 0
    SECONDS = 1
    MINUTES = 2
    MILLIMETERS = 3
    METERS = 4
    METERS_PER_SECOND = 5
    KILOMETERS_PER_HOUR = 6
    METER_PER_SECOND_SQUARED = 7
    DEGREES = 8
    RADIANS = 9
    DEGREES_PER_SECOND = 10
    RADIANS_PER_SECOND = 11
    HIT_POINTS = 12
    HORSEPOWER = 13
    PROBABILITY = 14
    DEVIATION = 15
    LOGIC = 16
    ID_TO_NAME: dict
    NAME_TO_ID: dict
    ALL: Any
    NAMES: Any

class ModifierDomain(object):
    COMMON = 1
    VEH_TYPE = 2
    CHASSIS = 4
    TURRET = 8
    GUN = 16
    SHOT = 32
    SHELL = 64
    SHELL_TYPE = 128
    RADIO = 256
    PHYSICS = 512
    ENGINE = 1024
    HULL = 2048
    VEHICLE = 4096
    CONSTANTS = 8192
    VSE = 16384
    FAKE = 32768
    SHELL_COMPONENTS: Any
    SHOT_COMPONENTS: Any
    GUN_COMPONENTS: Any
    TURRET_COMPONENTS: Any
    VEH_TYPE_COMPONENTS: Any
    VEHICLE_COMPONENTS: Any
    DEFAULT = COMMON
    ID_TO_NAME: dict
    NAME_TO_ID: dict
    ALL: Any
    NAMES: Any

class ClientDomain(object):
    UNDEFINED = 'undefined'
    ACCURACY = 'accuracy'
    ARMOR_PIERCING = 'armorPiercing'
    BATTLE_PARAMS = 'battleParams'
    CONCEALMENT = 'concealment'
    DAMAGE_DEALING = 'damageDealing'
    MOBILITY = 'mobility'
    RANDOMIZATION = 'randomization'
    SUSTAINING = 'sustaining'
    VISIBILITY = 'visibility'
    VITALITY = 'vitality'
    ALL: Any

class GameplayImpact(object):
    UNDEFINED = 0
    POSITIVE = 1
    NEGATIVE = 2
    HIDDEN = 3
    ID_TO_NAME: dict
    NAME_TO_ID: dict
    ALL: Any
    NAMES: Any

class ModifierRestriction(object):
    MIN = 0
    MAX = 1
    USE_TYPES = 2
    LIMITS: tuple
    ID_TO_NAME: dict
    NAME_TO_ID: dict
    ALL: Any
    NAMES: Any

class NodeType(object):
    ROOT = 'root'
    SHELL = 'shell'
    VEHICLE = 'vehicle'
    SUPPORTED_DOMAINS: dict

class Caliber(object):
    AUTO = 'auto'
    SMALL = 'small'
    MEDIUM = 'medium'
    MAIN = 'main'
    LARGE = 'large'
    HUGE = 'huge'
    NAME_TO_CALIBER: Any
    @classmethod
    def get(cls, targetCaliber):
        ...

class GunCaliber(Caliber):
    NAME_TO_CALIBER: Any

class ShellCaliber(Caliber):
    NAME_TO_CALIBER: Any

class ShellKind(object):
    IMPROVED_POSTFIX = SHELL_TYPES.IMPROVED_POSTFIX
    ALL_KEY = 'ALL'
    ALL_REGULAR: set
    ALL_IMPROVED: Any
    @classmethod
    def get(cls, shellDescr, withGold=True):
        ...

class ModifiersWithRemapping(object):
    GUN_EFFECTS = 'gunEffects'
    GUN_MAIN_PREFAB = 'gunMainPrefab'
    SHOT_EFFECTS = 'shotEffects'
    GUN_PREFAB_EFFECTS = 'gunPrefabEffects'
    SHOT_PREFAB_EFFECTS = 'shotPrefabEffects'
    SOUND_NOTIFICATIONS = 'soundNotifications'
    EXHAUST_EFFECTS = 'exhaustEffects'
    ROOT_PREFABS_MECHANIC_EFFECTS = 'rootPrefabsMechanicEffects'
    ALL: set

class RemappingConditionNames(object):
    REMAPPING_NAME = 'remappingName'
    NATION = 'nation'
    OUTFIT = 'outfit'
    GUN_NAME = 'gunName'
    GUN_CALIBER = 'gunCaliber'
    SHELL_KIND = 'shellKind'
    SHELL_SHOTS_COUNT = 'shellShotsCount'
    SHELL_CALIBER = 'shellCaliber'
    ALL: set

class RemappingNames(object):
    TEST = 'test'
    FEP_FALL_TANKS = 'fep_fall_tanks'
    ALL: Any
