# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/sounds/sound_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import enum as enum
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from fort_rush_common.fort_rush_constants import CaptureStates as CaptureStates
FORT_RUSH_PROMO_SOUND_SPACE: Any
FORT_RUSH_PROGRESSION_SOUND_SPACE: Any
CAPTURE_STATE_START_TO_SOUND: dict
CAPTURE_STATE_STOP_TO_SOUND: dict
RTPC_VALUE_THRESHOLD = 50
WIN_POINTS_CAP_STINGER = 'ev_fort_rush_gp_end_battle_score'

class SoundLanguage(CONST_CONTAINER):
    VOICEOVER_LOCALIZATION_SWITCH = 'SWITCH_ext_fort_rush_vo_language'
    VOICEOVER_CN = 'SWITCH_ext_fort_rush_vo_language_CN'
    VOICEOVER_EN = 'SWITCH_ext_fort_rush_vo_language_EN'

class SoundStates(enum.IntEnum):
    NEUTRALIZING = 2

class HangarSounds(CONST_CONTAINER):
    PROMO_SOUND_SPACE = 'fort_rush_promo'
    PROMO_ENTER = 'ev_fort_rush_promo_enter'
    PROMO_EXIT = 'ev_fort_rush_promo_exit'
    PROGRESSION_SOUND_SPACE = 'fort_rush_progression'
    PROGRESSION_ENTER = 'ev_fort_rush_meta_enter'
    PROGRESSION_EXIT = 'ev_fort_rush_meta_exit'
    ENTRY_POINT_CLICK = 'ev_fort_rush_entry_model_click'

class CapturePointSounds(CONST_CONTAINER):
    RTPC = 'RTPC_ext_fort_rush_gp_cap_status'
    CAPTURE_START = 'ev_fort_rush_gp_capture_start'
    CAPTURE_STOP = 'ev_fort_rush_gp_capture_stop'
    CAPTURE_COMPLETE = 'ev_fort_rush_gp_capture_complete'
    NEUTRALIZE_START = 'ev_fort_rush_gp_neutralize_start'
    NEUTRALIZE_STOP = 'ev_fort_rush_gp_neutralize_stop'
    NEUTRALIZE_COMPLETE = 'ev_fort_rush_gp_neutralize_complete'
    CONTESTED_START = 'ev_fort_rush_gp_contested_start'
    CONTESTED_STOP = 'ev_fort_rush_gp_contested_stop'
    HEAL = 'ev_fort_rush_gp_heal'
