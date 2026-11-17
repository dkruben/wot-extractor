# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/sounds/epic_sound_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from gui.Scaleform.genConsts.GAME_MESSAGES_CONSTS import GAME_MESSAGES_CONSTS as GAME_MESSAGES_CONSTS
from epic_constants import EPIC_BATTLE_TEAM_ID as EPIC_BATTLE_TEAM_ID

class EPIC_TIME_WWEVENTS(object):
    EB_RESPAWN_COUNT_DOWN_SOUND_ID: dict
    EB_TIME_OVER = 'time_over'

class EPIC_OVERTIME_SOUND_NOTIFICATIONS(object):
    EB_OVERTIME_COUNTDOWN = 'eb_overtime_countdown'
    EB_OVERTIME_COUNTDOWN_STOP = 'eb_overtime_countdown_stop'
    BF_EB_OVERTIME: dict
    BF_EB_OVERTIME_START = 'eb_overtime_start'

class EPIC_METAGAME_WWISE_SOUND_EVENTS(object):
    EB_ACHIEVED_RANK = 'eb_achieved_rank'
    EB_LEVEL_REACHED = 'eb_level_reached'
    EB_PROGRESS_BAR_START = 'gui_progress_bar'
    EB_PROGRESS_BAR_STOP = 'gui_progress_bar_stop'
    EB_LEVEL_REACHED_MAX = 'eb_level_reached_maximum'

class EPIC_SOUND(object):
    HANGAR = 'frontline_hangar'
    GAMEMODE_GROUP = 'STATE_gamemode'
    GAMEMODE_STATE = 'STATE_gamemode_frontline'
    GAMEMODE_DEFAULT = 'STATE_gamemode_default'
    PROGRESS_PAGE_ENTER = 'eb_ambient_progress_page_enter'
    PROGRESS_PAGE_EXIT = 'eb_ambient_progress_page_exit'
    GUI_REWARD_SCREEN = 'gui_reward_screen_general'
    GUI_MAIN_AWARD = 'gui_hangar_reward_main_icon'
    EPIC_MSG_SOUNDS_ENABLED = True
    BF_EB_EQUIPMENT_SOUND_LIST: tuple
    EB_READY_FOR_DEPLOYMENT = 'eb_ready_for_deployment'
    BF_EB_START_BATTLE: dict
    BF_EB_GLOBAL_MESSAGE = 'eb_general_message'
    BF_EB_WPN_ZONE_PROTECTION = 'eb_warships_firing'
    BF_EB_BASE_CAPTURE_SIREN_SOUND = 'eb_zone_capture'
    BF_EB_ENTER_CLOSED_ZONE = 'eb_enter_closed_zone'
    BF_EB_ENTER_PROTECTION_ZONE = 'eb_enter_landing_zone'
    BF_EB_AIR_STRIKE_WARNING = 'eb_airstrike_warning_defender'
    BF_EB_LANDING_ZONE_PROTECTION = 'eb_closed_zone_artillery_fire'
    BF_EB_CLOSED_ZONE_ARTILLERY = 'eb_closed_zone_artillery_fire'
    BF_EB_RECOVERY_REQUESTED = 'eb_recovery_requested'
    BF_EB_RECOVERY_SUCCESSFUL = 'eb_recovery_successful'
    BF_EB_RECOVERY_CANCELED = 'eb_recovery_canceled'
    BF_EB_NEW_OBJECTIVE = 'eb_new_battle_objective'
    BF_EB_SPECIFIC_TIME = 'eb_specific_time'
    BF_EB_GENERAL = 'eb_general'
    BF_EB_RANK_UP: dict
    BF_EB_RETREAT_SUCCESSFUL = 'eb_retreat_successful'
    BF_EB_ZONE_CONTESTED_ATK: dict
    BF_EB_ZONE_CONTESTED_DEF: dict
    BF_EB_ZONE_CAPTURED_ATK: dict
    BF_EB_ZONE_CAPTURED_DEF: dict
    BF_EB_AIRSTRIKE_ATK = 'eb_airstrike_ATK'
    BF_EB_AIRSTRIKE_DEF = 'eb_airstrike_DEF'
    BF_EB_AIR_SUPPORT: dict
    BF_EB_MAIN_OBJECTIVES_REACHED_ATK: dict
    BF_EB_MAIN_OBJECTIVES_REACHED_DEF: dict
    BF_EB_OBJECTIVE_UNDER_ATTACK_ATK: dict
    BF_EB_OBJECTIVE_UNDER_ATTACK_DEF: dict
    BF_EB_MAIN_OBJECTIVES_ONE_DESTROYED = 'eb_objective_destroyed'
    BF_EB_MAIN_OBJECTIVES_ONLY_ONE_LEFT = 'eb_main_objectives_only_one_left'
    BF_EB_MAIN_OBJECTIVES_ALL_DOWN = 'eb_main_objectives_all_down'
    BF_EB_HQ_DESTROYED_ATK_OR_DEF: dict
    BF_EB_REINFORCEMENTS_ARRIVED = 'eb_reinforcements_arrived'
    BF_EB_REINFORCEMENTS_CEASED = 'eb_reinforcements_ceased'
    BF_EB_TIME_OUT: dict
    BF_EB_ALL_ENEMIES_DESTROYED: dict
    BF_EB_STOP_TICKING = 'time_countdown_stop'
    BF_EB_VO_MESSAGES: dict
    EB_UI_REPPAIR_POINT_COMPLETED = 'eb_ui_repair_point'
    EB_UI_REPPAIR_POINT_PROGRESS = 'eb_ui_repair_point_progress'
    EB_UI_REPPAIR_POINT_PROGRESS_STOP = 'eb_ui_repair_point_progress_stop'
    EB_ABILITY_MINEFIELD_BLOCK = 'eb_ability_minefield_block'
    EB_ABILITY_MINEFIELD_APPLY = 'eb_ability_minefield_apply'
    EB_ABILITY_MINEFIELD_HITS_TARGET = 'eb_ability_minefield_hits_target'
    EB_ABILITY_STEALTH_START = 'eb_ability_stealth_start'
    EB_ABILITY_STEALTH_STOP = 'eb_ability_stealth_stop'
    EB_ABILITY_RENOVATION_COMPLETED = 'eb_ability_renovation_completed'
    EQUIPMENT_ACTIVATED: dict
    EB_VO_RESERVE_UPGRADED = 'vo_eb_reserve_improving'
    EB_VO_RESERVE_UNLOCKED = 'vo_eb_reserve_unlock'
    EB_VO_TANKS_UNLOCKED = 'vo_eb_unlock_tier_9_tanks'
    EB_TANKS_UNLOCKED = 'eb_tanks_9lvl_unlocked'
    EB_UI_ADD_TIME_EMERGENCE = 'eb_ui_add_time_emergence'
    EB_UI_CANNON_DESTRUCTION_EMERGENCE = 'eb_ui_cannon_destruction_emergence'
    EB_UI_CANNON_DESTRUCTION_CROSS = 'eb_ui_cannon_destruction_cross'
    EB_UI_CANNON_DESTRUCTION_DISAPPEARANCE = 'eb_ui_cannon_destruction_disappearance'

class BF_EB_MAIN_OBJECTIVES_SOUND_NOTIFICATIONS(object):
    ONE_DESTROYED = EPIC_SOUND.BF_EB_MAIN_OBJECTIVES_ONE_DESTROYED
    ONLY_ONE_LEFT = EPIC_SOUND.BF_EB_MAIN_OBJECTIVES_ONLY_ONE_LEFT
    ALL_DOWN = EPIC_SOUND.BF_EB_MAIN_OBJECTIVES_ALL_DOWN
