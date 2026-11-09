# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/feature/fun_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
FUN_PROGRESSION_SOUND_SPACE: Any
FUN_REWARD_SCREEN_SOUND_SPACE: Any
FUN_TIER_LIST_SOUND_SPACE: Any
FUN_BATTLE_RESULTS_SOUND_SPACE: Any

class FunSounds(CONST_CONTAINER):
    HANGAR_PLACE_STATE = 'STATE_hangar_place'
    HANGAR_PLACE_TASKS = 'STATE_hangar_place_fep'
    OVERLAY_HANGAR_STATE = 'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_STATE_ON = 'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_STATE_OFF = 'STATE_overlay_hangar_general_off'
    PROGRESSION_SPACE_NAME = 'fun_progression_view'
    PROGRESSION_ENTER_EVENT = 'ev_fep_meta_enter'
    PROGRESSION_EXIT_EVENT = 'ev_fep_meta_exit'
    REWARDS_SPACE_NAME = 'fun_rewards_view'
    REWARDS_SCREEN_GENERAL = 'gui_reward_screen_general'
    TIER_LIST_SPACE_NAME = 'fun_tier_list'
    TIER_LIST_ENTER = 'ev_fep_infopage_enter'
    TIER_LIST_EXIT = 'ev_fep_infopage_exit'
    BATTLE_RESULTS_SPACE_NAME = 'fun_postbattle_view'
    GAMEPLACE_STATE = 'STATE_gameplace'
    GAMEPLACE_BATTLE_RESULTS_STATE = 'STATE_gameplace_result'
    GAMEPLACE_HANGAR_STATE = 'STATE_gameplace_hangar'
    BATTLE_RESULTS_ENTER_EVENT = 'gui_hangar_neutral_screen'
