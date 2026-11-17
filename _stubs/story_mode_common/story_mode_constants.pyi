# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/common/story_mode_common/story_mode_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import constants as constants
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, ARENA_GUI_TYPE as ARENA_GUI_TYPE
from constants_utils import ConstInjector as ConstInjector
EXTENSION_NAME = 'story_mode'
LOGGER_NAME = 'story_mode'
DEFAULT_BATTLES_LIMIT = 500
MM_STORY_MODE_STATS_KEY = 'stats/story_mode/'
BATTLES_LIMIT_KEY: Any
SM_CONGRATULATIONS_MESSAGE = 'StoryModeCongratulationsMessage'
STORY_MODE_BONUS_TYPES: tuple
STORY_MODE_GUI_TYPE_BY_BONUS_TYPE: dict
VEHICLE_BUNKER_TURRET_TAG = 'bunkerTurret'
PROGRESS_PDATA_KEY = 'progress'
STORY_MODE_PDATA_KEY = 'storyMode'
LONG_INT_HALF_SHIFT = 32
STORY_MODE_AB_FEATURE = 'storyMode'
DISABLE_REGULAR_OPERATIONS = 'disableRegularOperations'
RECON_ABILITY = 'smn_recon_ability'
DISTRACTION_ABILITY = 'smn_distraction_ability'
SCC_AIRSTRIKE_ABILITY = 'sm_scc_airstrike'
SCC_AIRSTRIKE_ABILITY_HARD = 'sm_scc_airstrike_hard'
PLAYER_TEAM = 1
DEFAULT_SPAWN_GROUP = 0

class PRIORITY(enum.IntEnum):
    HIGH = 0
    MEDIUM = 1
    LOW = 2

# decorador original: @enum.unique
class MissionsDifficulty(str, enum.Enum):
    UNDEFINED = ''
    NORMAL = 'normal'
    HARD = 'hard'
    VERY_HARD = 'very_hard'

class EventMissionSelector(str, enum.Enum):
    DEFAULT = 'default'
    WITH_UNLOCK_MISSION = 'withUnlockMission'
    BATTLES_COUNT = 'battlesCount'

class MissionType(str, enum.Enum):
    ONBOARDING = 'onboarding'
    REGULAR = 'regular'
    EVENT = 'event'

class AwarenessState(enum.IntEnum):
    SPOTTED = 0
    SPOTTING = 1
    NOT_SPOTTED = 2

class EQUIPMENT_STAGES(constants.EQUIPMENT_STAGES, ConstInjector):
    ACTIVATING = 101
    DEACTIVATING = 102

class MissionLockCondition(str, enum.Enum):
    BY_MISSION = 'byMission'
    BATTLES_COUNT = 'battlesCount'

class MissionId(enum.IntEnum):
    UNDEFINED = -1
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7

class TaskId(enum.IntEnum):
    ONE = 1
    TWO = 2
    THREE = 3

class MM_STORY_MODE_STATS(object):
    PLAYERS_COUNT_KEY: Any
    BATTLES_COUNT_KEY: Any
    AVG_WAIT_TIME_KEY: Any
    ALL: tuple
