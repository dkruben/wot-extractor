# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/uilogging/player_satisfaction_rating/logging_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from chat_commands_consts import BATTLE_CHAT_COMMAND_NAMES as BATTLE_CHAT_COMMAND_NAMES
from gui.Scaleform.daapi.view.lobby.lobby_constants import USER as USER
from gui.shared.denunciator import DENUNCIATIONS as DENUNCIATIONS
FEATURE = 'battle_rating'
MIN_VIEW_TIME = 2.0
NO_MIN_VIEW_TIME = 0.0
ARENA_PERIOD_TO_KEY: dict
RADIAL_MENU_ACTIONS_TO_LOGGING_ACTIONS: dict
POST_BATTLE_CM_ACTION_TO_PLAYER_SATISFACTION_CM_ACTION: dict

class PlayerSatisfactionRatingLogActions(Enum):
    OPENED = 'opened'
    CLICK = 'click'
    VIEWED = 'viewed'

class PlayerSatisfactionRatingCMActions(Enum):
    NO_ACTION = 'no_action'
    UNTRACKED_ACTION = 'untracked_action'
    FRIEND_ACTION = 'friend_action'
    SEND_MESSAGE = 'send_message'
    CREATE_PLATOON = 'create_platoon'
    CREATE_UNIT = 'create_unit'
    COMPLAIN = 'complain'
    BLACKLIST = 'blacklist'
    VOICE_MESSAGES = 'voice_messages'
    COMMENDATION = 'commendation'

class PlayerSatisfactionRatingKeys(Enum):
    CONTEXT_MENU = 'context_menu'
    TEAM_SCORE_TAB = 'team_score_tab'
    TEAM_VIEW = 'team_view'
    BATTLE_GUI = 'battle_gui'
    CREATE_PLATOON = 'create_platoon'
    COMMAND_WHEEL = 'command_wheel'
    HOT_KEY = 'hot_key'
    RESPONSE = 'response'

class PlayerSatisfationRatingInviteSource(object):
    FULL_STATS_VIEW = 'full_stats_view'
    IN_BATTLE_GUI = 'in_battle_gui'

class PlayerSatisfactionRatingInfoKeys(object):
    ARENA_ID_KEY = 'arena_id'
    BATTLE_PHASE_KEY = 'battle_phase'
    PHASE_TIME_KEY = 'phase_time'
    IS_ALIVE_KEY = 'is_alive'
    PREBATTLE_ID_KEY = 'prebattle_id'

class PlayerSatisfactionRatingRadialMenuActions(Enum):
    NO_ACTION = 'no_action'
    UNTRACKED_ACTION = 'untracked_action'
    HELP_PROVIDE = 'help_provide'
    HELP_ASKED = 'help_asked'
    THANK_YOU = 'thank_you'
    RETREAT = 'retreat'
