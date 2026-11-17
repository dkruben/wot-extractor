# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/items/components/c11n_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import reduce as reduce
from future.utils import viewitems as viewitems
from soft_exception import SoftException as SoftException
RENT_DEFAULT_BATTLES = 50
MAX_OUTFIT_LENGTH = 1024
MAX_CAMOUFLAGE_PATTERN_SIZE = 5
MAX_ITEMS_FOR_BUY_OPERATION = 100
HIDDEN_CAMOUFLAGE_ID = 1
TOTAL_COUNTER_TYPE_DESCR = -1
MAX_PROJECTION_DECALS = 9
MAX_SEQUENCES = 5
MAX_ATTACHMENTS = 6
MAX_STAT_TRACKERS = 1
MAX_USERS_PROJECTION_DECALS = 3
MAX_PROJECTION_DECALS_PER_AREA = 3
PROJECTION_DECALS_SCALE_ID_VALUES: tuple
DEFAULT_DECAL_SCALE_FACTORS: tuple
DEFAULT_SCALE_FACTOR_ID = 3
DEFAULT_PALETTE = 0
DEFAULT_DECAL_CLIP_ANGLE = 0.0
DEFAULT_DECAL_TINT_COLOR: tuple
DEFAULT_DECAL_ANCHOR_SHIFT = 0.0
RENT_IS_ALMOST_OVER_VALUE = 3
EMPTY_ITEM_ID = 22222
SLOT_DEFAULT_ALLOWED_MODEL = 'default'
DEFAULT_POSITION: tuple
DEFAULT_ROTATION: tuple
DEFAULT_SCALE: tuple
DEFAULT_GLOSS = 0.509
DEFAULT_METALLIC = 0.23
HANGER_POSTFIX = '_hanger'
CustomizationTypeNames: dict
CustomizationNamesToTypes: dict
SeasonTypeNames: dict
DecalTypeNames: dict
NO_OUTFIT_DATA: tuple
C11N_MAX_REGION_NUM = 3
C11N_GUN_REGION = 0
C11N_MASK_REGION = 2
C11N_GUN_APPLY_REGIONS: dict
CUSTOMIZATION_SLOTS_VEHICLE_PARTS: tuple
UNBOUND_VEH_KEY = 0
CamouflageTilingTypeNames: dict
CamouflageTilingTypeNameToType: dict
EASING_TRANSITION_DURATION = 0.8
IMMEDIATE_TRANSITION_DURATION = 0.0

class CustomizationType(object):
    PAINT = 1
    CAMOUFLAGE = 2
    DECAL = 3
    STYLE = 4
    MODIFICATION = 5
    ITEM_GROUP = 6
    PROJECTION_DECAL = 7
    INSIGNIA = 8
    PERSONAL_NUMBER = 9
    FONT = 10
    SEQUENCE = 11
    ATTACHMENT = 12
    STAT_TRACKER = 13
    RANGE: set
    STYLE_ONLY_RANGE: set
    FULL_RANGE: Any
    APPLIED_TO_TYPES: tuple
    SIMPLE_TYPES: tuple
    SIMPLE_OUTFIT_COMPONENT_TYPES: tuple
    DISMOUNT_TYPE: tuple
    TYPES_FOR_EDITABLE_STYLE: tuple
    COMMON_TYPES: tuple

class CustomizationDisplayType(object):
    HISTORICAL = 0
    NON_HISTORICAL = 1
    FANTASTICAL = 2

class ItemTags(object):
    VEHICLE_BOUND = 'vehicleBound'
    PREMIUM_IGR = 'premiumIGR'
    IGR = 'IGR'
    RARE = 'rare'
    HIDDEN_IN_UI = 'hiddenInUI'
    DIM = 'dim'
    FULL_RGB = 'fullRGB'
    NATIONAL_EMBLEM = 'nationalEmblem'
    STYLE_ONLY = 'styleOnly'
    PROGRESSION_REQUIRED = 'progression_required'
    ADD_NATIONAL_EMBLEM = 'addNationalEmblem'
    DISABLE_VERTICAL_MIRROR = 'disableVerticalMirror'
    STYLE_PROGRESSION = 'styleProgression'
    QUESTS_PROGRESSION = 'questsProgression'
    PROGRESSION_REWIND_ENABLED = 'progression_rewind_enabled'
    ONLY_VERTICAL_MIRROR = 'onlyVerticalMirror'
    HIDE_IF_INCOMPATIBLE = 'hideIfIncompatible'
    STYLE_SERIAL_NUMBER = 'styleSerialNumber'
    LOCKED_ON_VEHICLE = 'lockedOnVehicle'
    IS_3D = 'c11n3D'
    BATTLE_EFFECT = 'battleEffect'
    SHOW_DISABLED = 'showDisabled'

class ProjectionDecalType(object):
    POSITION = 0
    TAGS = 1

class ProjectionDecalDirectionTags(object):
    PREFIX = 'direction_'
    ANY: Any
    LEFT_TO_RIGHT: Any
    RIGHT_TO_LEFT: Any
    LEFT = 'left'
    RIGHT = 'right'
    FRONT = 'front'
    ALL: tuple

class ProjectionDecalFormTags(object):
    PREFIX = 'formfactor_'
    SQUARE: Any
    RECT1X2: Any
    RECT1X3: Any
    RECT1X4: Any
    RECT1X6: Any
    ALL: tuple

class ProjectionDecalPreferredTags(object):
    PREFIX = 'preferred_'
    SQUARE: Any
    RECT1X2: Any
    RECT1X3: Any
    RECT1X4: Any
    RECT1X6: Any
    ALL: tuple

class ProjectionDecalMatchingTags(object):
    MIMIC = 'mimic'
    COVER = 'cover'
    SAFE = 'safe'
    ALL: tuple

class AttachmentTags(object):
    ROTATABLE = 'rotatable'
    SCALABLE = 'scalable'
    ALL: tuple

class ApplyArea(object):
    NONE = 0
    CHASSIS = 1
    CHASSIS_1 = 2
    CHASSIS_2 = 4
    CHASSIS_3 = 8
    HULL = 16
    HULL_1 = 32
    HULL_2 = 64
    HULL_3 = 128
    TURRET = 256
    TURRET_1 = 512
    TURRET_2 = 1024
    TURRET_3 = 2048
    GUN = 4096
    GUN_1 = 8192
    GUN_2 = 16384
    GUN_3 = 32768
    ALL = 65535
    CHASSIS_REGIONS: tuple
    CHASSIS_PAINT_REGIONS: tuple
    HULL_REGIONS: tuple
    HULL_PAINT_REGIONS: tuple
    HULL_CAMOUFLAGE_REGIONS: tuple
    HULL_EMBLEM_REGIONS: tuple
    HULL_INSCRIPTION_REGIONS: tuple
    HULL_DECAL_REGIONS: Any
    HULL_INSIGNIA_REGIONS: tuple
    HULL_PERSONAL_NUMBER_REGIONS: tuple
    TURRET_REGIONS: tuple
    TURRET_PAINT_REGIONS: tuple
    TURRET_CAMOUFLAGE_REGIONS: tuple
    TURRET_EMBLEM_REGIONS: tuple
    TURRET_INSCRIPTION_REGIONS: tuple
    TURRET_DECAL_REGIONS: Any
    TURRET_INSIGNIA_REGIONS: tuple
    TURRET_PERSONAL_NUMBER_REGIONS: tuple
    GUN_REGIONS: tuple
    GUN_PAINT_REGIONS: tuple
    GUN_CAMOUFLAGE_REGIONS: tuple
    GUN_EMBLEM_REGIONS: tuple
    GUN_INSCRIPTION_REGIONS: tuple
    GUN_DECAL_REGIONS: Any
    GUN_INSIGNIA_REGIONS: tuple
    GUN_PERSONAL_NUMBER_REGIONS: tuple
    RANGE: set
    DECAL_REGIONS: Any
    CAMOUFLAGE_REGIONS: Any
    PAINT_REGIONS: Any
    USER_PAINT_ALLOWED_REGIONS: set
    EMBLEM_REGIONS: Any
    INSCRIPTION_REGIONS: Any
    INSIGNIA_REGIONS: Any
    PERSONAL_NUMBER_REGIONS: Any
    MODIFICATION_REGIONS: tuple
    PAINT_REGIONS_VALUE: Any
    DECAL_REGIONS_VALUE: Any
    CAMOUFLAGE_REGIONS_VALUE: Any
    EMBLEM_REGIONS_VALUE: Any
    INSCRIPTION_REGIONS_VALUE: Any
    INSIGNIA_REGIONS_VALUE: Any
    PERSONAL_NUMBER_REGIONS_VALUE: Any
    CHASSIS_REGIONS_VALUE: Any
    GUN_REGIONS_VALUE: Any
    HULL_REGIONS_VALUE: Any
    TURRET_REGIONS_VALUE: Any
    RANGE_REGIONS_VALUE: Any
    @staticmethod
    def getAppliedCount(appliedTo, appliedRange=...):
        ...

class SeasonType(object):
    UNDEFINED = 0
    WINTER = 1
    SUMMER = 2
    DESERT = 4
    EVENT = 8
    ALL: Any
    RANGE: tuple
    SEASONS: tuple
    COMMON_SEASONS: tuple
    REGULAR: Any
    @staticmethod
    def fromArenaKind(arenaKind):
        ...

class ModificationType(object):
    UNDEFINED = 0
    PAINT_AGE = 1
    CAMOUFLAGE_AGE = 2
    PAINT_FADING = 3
    GLOSS = 4
    METALLIC = 5
    USE_NEW_WEAR = 6

class DecalType(object):
    EMBLEM = 1
    INSCRIPTION = 2
    ALL: tuple

class StyleFlags(object):
    ENABLED = 1
    INSTALLED = 2
    EMPTY = 0
    ACTIVE: Any

class Options:
    NONE = 0
    MIRRORED_HORIZONTALLY = 1
    MIRRORED_VERTICALLY = 2
    COMBO_MIRRORED: Any
    RANGE: tuple
    PROJECTION_DECALS_ALLOWED_OPTIONS: tuple
    PROJECTION_DECALS_ALLOWED_OPTIONS_VALUE: Any

class ImageOptions:
    NONE = 0
    FULL_RGB = 1

class CamouflageTilingType(object):
    NONE = 0
    LEGACY = 1
    RELATIVE = 2
    RELATIVEWITHFACTOR = 3
    ABSOLUTE = 4
    RANGE = None

class SLOT_TYPE_NAMES(object):
    PAINT = 'paint'
    CAMOUFLAGE = 'camouflage'
    INSCRIPTION = 'inscription'
    EMBLEM = 'player'
    STYLE = 'style'
    EFFECT = 'effect'
    PROJECTION_DECAL = 'projectionDecal'
    INSIGNIA = 'insignia'
    ATTACHMENT = 'attachment'
    STAT_TRACKER = 'statTracker'
    FIXED_EMBLEM = 'fixedEmblem'
    FIXED_INSCRIPTION = 'fixedInscription'
    FIXED_PROJECTION_DECAL = 'fixedProjectionDecal'
    EDITABLE_STYLE_DELETABLE: tuple
    DECALS: tuple
    FIXED: tuple
    ALL: tuple

class EDITING_STYLE_REASONS(object):
    IS_EDITABLE = 'isEditable'
    NOT_EDITABLE = 'notEditable'
    NOT_REACHED_LEVEL = 'notReachedLevel'
    NOT_HAVE_ANY_PROGRESSIVE_DECALS = 'notHaveAnyProgressiveDecals'
    ENABLED: tuple
    DISABLED: tuple

class Rarity(object):
    UNKNOWN = ''
    RARE = 'rare'
    EPIC = 'epic'
    LEGENDARY = 'legendary'
    FILTERABLE: tuple
    UI_EFFECT: tuple
    ALL: Any

class AttachmentLogic(object):
    UNKNOWN = ''
    FLAG_PART = 'flagPart'
    FLAG_ANIMATION = 'flagAnimation'
    PREFAB = 'prefab'
    FLAGS: tuple
    ALL: tuple

class AttachmentType(object):
    UNKNOWN = ''
    UNIVERSAL = 'universal'
    TURRET = 'turret'
    GUN_MANTLET = 'gunMantlet'
    GUN = 'gun'
    GUN_STATIC = 'gunStatic'
    GUN_RIGHT = 'gunRight'
    GUN_LEFT = 'gunLeft'
    GUN_SLOTS: tuple
    ALL: tuple

class AttachmentSize(object):
    UNKNOWN = ''
    SMALL = 'small'
    MEDIUM = 'medium'
    LARGE = 'large'
    ALL: tuple
    DEFAULT = MEDIUM

class StatTrackerStatistic(object):
    KILLS = 'kills'
    ALL: tuple
