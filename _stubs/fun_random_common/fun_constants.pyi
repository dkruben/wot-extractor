# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/common/fun_random_common/fun_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
import UnitBase as UnitBase
from constants_utils import ConstInjector as ConstInjector
DEFAULT_ASSETS_PACK = 'undefined'
DEFAULT_SETTINGS_KEY = 'undefined'
DEFAULT_PRIORITY = 0
FUN_EVENT_ID_KEY = 'funEventID'
UNKNOWN_EVENT_ID = 0
UNKNOWN_EVENT_NAME = 'unknown_event'
UNKNOWN_WWISE_REMAPPING = 'unknownRemapping'
FUN_GAME_PARAMS_KEY = 'fun_random_config'
BATTLE_MODE_VEH_TAGS_EXCEPT_FUN: Any

class FunSubModeImpl(object):
    UNDEFINED = 0
    DEFAULT = 1
    DEV_TEST = 2
    ALL: Any

class FunProgressionCondition(object):
    BATTLES = 'battles'
    DAMAGE = 'damage'
    TOP = 'top'
    WIN = 'win'
    ALL: tuple

class FunEfficiencyParameter(object):
    KILLS = 'kills'
    SPOTTED = 'spotted'
    STUN = 'damageAssistedStun'
    DAMAGE_DEALT = 'damageDealt'
    DAMAGE_ASSISTED = 'damageAssisted'
    DAMAGE_BLOCKED_BY_ARMOR = 'damageBlockedByArmor'
    CAPTURE_POINTS = 'capturePoints'
    DROPPED_CAPTURE_POINTS = 'droppedCapturePoints'
    ALL: tuple

class FunPerformanceParameter(object):
    RECOMMENDED_GRAPHICS_PRESET = 'recommendedGraphicsPreset'
    RENDER_PIPELINE = 'renderPipeline'
    MEDIUM_RISK = 'mediumRisk'
    HIGH_RISK = 'highRisk'
    ALL: tuple

class FunEfficiencyParameterCount(object):
    MIN = 3
    MAX = 5

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    FUN_RANDOM = 29
    FUN_RANDOM_RANGE: tuple

class ARENA_BONUS_TYPE(constants.ARENA_BONUS_TYPE, ConstInjector):
    FUN_RANDOM = 42

class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    FUN_RANDOM = 131072

class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    FUN_RANDOM_ROSTER: Any

class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    FUN_RANDOM = constants.PREBATTLE_TYPE.FUN_RANDOM

class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    CHANGE_FUN_EVENT_ID = 29
