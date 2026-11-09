# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/component_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import collections as collections
import enum as enum
from soft_exception import SoftException as SoftException
from wrapped_reflection_framework import reflectedNamedTuple as reflectedNamedTuple
from Math import Vector3 as Vector3
Autoreload: Any
AutoShoot: Any
DualGun: Any
DualAccuracy: Any
TwinGun: Any
MultiGunState: Any
ControllableReload: Any
UNDEFINED_ITEM_TYPE_ID = 0
ZERO_FLOAT = 0.0
ZERO_INT = 0
ZERO_TUPLE2: tuple
ZERO_VECTOR3: Any
ONE_INT = 1
ONE_FLOAT = 1.0
EMPTY_STRING = ''
EMPTY_TUPLE: tuple
EMPTY_LIST: list
INFLUENCE_ALL = 0
INFLUENCE_ALLY = 1
INFLUENCE_ENEMY = 2
EMPTY_DICT: Any
EMPTY_TAGS: Any
LEVEL = 1
DEFAULT_ARMOR_HOMOGENIZATION = 1.0
DEFAULT_GUN_AUTORELOAD: Any
DEFAULT_GUN_BURST: tuple
DEFAULT_GUN_CLIP: tuple
DEFAULT_GUN_DUALGUN: Any
DEFAULT_GUN_DUAL_ACCURACY: Any
DEFAULT_GUN_AUTOSHOOT: Any
DEFAULT_GUN_TWINGUN: Any
DEFAULT_FAKE_TURRETS: dict
DEFAULT_HULL_VARIANT_MATCH: tuple
DEFAULT_PREMIUM_VEHICLE_XP_FACTOR = 0.0
DEFAULT_SPECIFIC_FRICTION = 0.6867000000000001
DEFAULT_INVISIBILITY_FACTOR = 1.0
DEFAULT_DAMAGE_RANDOMIZATION = 0.25
DEFAULT_PIERCING_POWER_RANDOMIZATION = 0.25
DEFAULT_MODERN_HE_OBSTACLE_PENETRATION = True
DEFAULT_MODERN_HE_SHIELD_PENETRATION = True
DEFAULT_PIERCING_SPALLS = True
MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_DESTRUCTIBLES = 1.0
MODERN_HE_PIERCING_POWER_REDUCTION_FACTOR_FOR_SHIELDS = 3.0
MODERN_HE_DAMAGE_ABSORPTION_FACTOR = 0.0
DEFAULT_ENABLE_TRACE_RICOCHET = True
KMH_TO_MS = 0.27778
MS_TO_KMH = 3.5999712
KG_TO_NEWTON = 9.81
HP_TO_WATTS = 735.5
ALLOWED_EMBLEM_SLOTS: tuple
ALLOWED_PROJECTION_DECALS_ANCHORS: tuple
ALLOWED_MISC_SLOTS: tuple
ALLOWED_SLOTS_ANCHORS: tuple
ALLOWED_ATTACHMENT_SLOTS: tuple
TANKMEN_GROUPS: tuple
MAIN_TRACK_PAIR_IDX = 0
DEFAULT_TRACK_HIT_VECTOR: Any
TrackState: Any
DynamicShotEffect: Any
DYNAMIC_SHOT_MAX_COUNT = 10000
ShootImpulse: Any
INVALID_EFFECT_INDEX = 255

class _ReadOnlyDict(dict):
    def __setitem__(self, key, value):
        ...
    def update(self, E=None, **F):
        ...

class ObjectSlotType(object):
    ATTACHMENT = 'attachment'
    ALL: tuple

class MuzzleBrakeType(enum.IntEnum):
    NONE = 0
    HORIZONTAL = 1
    VERTICAL = 2
    RADIAL = 3
    ANGLED = 4
