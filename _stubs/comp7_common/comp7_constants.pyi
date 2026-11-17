# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/common/comp7_common/comp7_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
import UnitBase as UnitBase
import constants as constants
from constants_utils import ConstInjector as ConstInjector
DEFAULT_ASSETS_PACK = 'undefined'
DEFAULT_SETTINGS_KEY = 'undefined'
DEFAULT_PRIORITY = 0
UNKNOWN_EVENT_ID = 0
UNKNOWN_EVENT_NAME = 'unknown_event'
UNKNOWN_WWISE_REMAPPING = 'unknownRemapping'
COMP7_INBATTLE_CONFIGS: tuple
BATTLE_MODE_VEH_TAGS_EXCEPT_COMP7: Any

class Configs(enum.Enum):
    COMP7_CONFIG = 'comp7_config'
    COMP7_RANKS_CONFIG = 'comp7_ranks_config'
    COMP7_REWARDS_CONFIG = 'comp7_rewards_config'

class ARENA_GUI_TYPE(constants.ARENA_GUI_TYPE, ConstInjector):
    COMP7 = 30
    TOURNAMENT_COMP7 = 33
    TRAINING_COMP7 = 34
    COMP7_RANGE: tuple

class UNIT_MGR_FLAGS(UnitBase.UNIT_MGR_FLAGS, ConstInjector):
    COMP7 = 262144

class ROSTER_TYPE(UnitBase.ROSTER_TYPE, ConstInjector):
    COMP7_ROSTER: Any

class PREBATTLE_TYPE(constants.PREBATTLE_TYPE, ConstInjector):
    COMP7 = 24
    TRAINING_COMP7 = 26

class INVITATION_TYPE(constants.INVITATION_TYPE, ConstInjector):
    COMP7 = PREBATTLE_TYPE.COMP7

class CLIENT_UNIT_CMD(UnitBase.CLIENT_UNIT_CMD, ConstInjector):
    SET_SQUAD_SIZE = 4301

class GameSeasonType(constants.GameSeasonType, ConstInjector):
    COMP7 = 7

class BATTLE_PROGRESS_CATEGORY(constants.BATTLE_PROGRESS_CATEGORY, ConstInjector):
    COMP7_WEEKLY_QUESTS = 8
    COMP7_CUSTOMISATION_QUESTS = 9
