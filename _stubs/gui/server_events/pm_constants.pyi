# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/pm_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from personal_missions import PM_BRANCH as PM_BRANCH
_SOUNDS_PRIORITIES: tuple
PERSONAL_MISSIONS_SOUND_SPACE: Any
PERSONAL_MISSIONS_SILENT_SOUND_SPACE: Any
PAUSABLE_OPERATIONS_IDS: tuple
DISCARDABLE_OPERATIONS_IDS: tuple
PM_SUIT_OP_PLUGIN_ERR_RESPONSE = 'WRONG_OPERATION'

class SOUNDS(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'personalMissions'
    FIRST_RUN_AWARD_APPEARANCE = 'pm_appearance_of_reward'
    AMBIENT = 'pm_ambient'
    MUSIC = 'pm_music'
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_GARAGE = 'STATE_hangar_place_garage'
    STATE_PLACE_MISSIONS = 'STATE_hangar_place_personalMissions'
    RTCP_MISSIONS_NUMBER = 'RTPC_ext_mission_number'
    RTCP_MISSIONS_ZOOM = 'RTPC_ext_mission_zoom'
    RTCP_DEBRIS_CONTROL = 'RTPC_ext_mission_debris_control'
    OPERATION_NAV_CLICK = 'tank_selection'
    OPERATION_NAV_CLICK_ANIMATION = 'pm_tank_select_animation'
    CHAIN_NAV_CLICK = 'pm_type_select_animation'
    REGION_CLICK = 'tabb'
    FREE_AWARD_LIST_SPENT = 'pm_reward_list_spend'
    AWARD_WINDOW = 'pm_standard_greeting'
    AWARD_LIST_AWARD_WINDOW = 'pm_special_greeting'
    WOMAN_AWARD_WINDOW = 'pm_special_greeting_woman'
    TANK_AWARD_WINDOW = 'pm_special_greeting_tank'
    RTCP_OVERLAY = 'RTPC_ext_greeting_overlay'
    ONE_AWARD_LIST_RECEIVED = 'pm_greeting_order_form'
    ONE_AWARD_LIST_RECEIVED_CONFIRM = 'pm_greeting_order_form_confirm'
    FOUR_AWARD_LISTS_RECEIVED = 'pm_conversion_order_form'
    RTCP_MISSION_BRANCH: dict
    BRANCH_DEFAULT = 0
    BRANCH_SELECTED = 100
    MIN_MISSIONS_ZOOM = 0
    MAX_MISSIONS_ZOOM = 100

class PM_TUTOR_FIELDS(CONST_CONTAINER):
    FIRST_ENTRY_AWARDS_SHOWN = 'pm_first_entry_awards_shown'
    INITIAL_FAL_COUNT = 'pm_initial_free_award_lists_count'
    ONE_FAL_SHOWN = 'pm_first_free_award_list_shown'
    MULTIPLE_FAL_SHOWN = 'pm_four_free_award_lists_shown'
    PM2_ONE_FAL_SHOWN = 'pm2_first_free_award_list_shown'
    PM2_MULTIPLE_FAL_SHOWN = 'pm2_four_free_award_lists_shown'
