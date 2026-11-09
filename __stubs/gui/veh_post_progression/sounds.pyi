# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/veh_post_progression/sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
import WWISE as WWISE
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
PP_VIEW_SOUND_SPACE: Any

class Sounds(CONST_CONTAINER):
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_PP = 'STATE_hangar_place_post_progression'
    COMMON_SOUND_SPACE = 'post_progression_space'
    ENTER = 'ev_pp_enter'
    ENTER_ELITE_VIEW = 'ev_pp_elite_status_acquired'
    MODIFICATION_DESTROY = 'ev_pp_modification_destroy'
    MODIFICATION_MOUNT = 'ev_pp_modification_mount'
    SETUP_SWITCH = 'ev_pp_setup_switch'
    GAMEPLAY_SETUP_SWITCH = 'ev_pp_gameplay_setup_switch'

def playSound(eventName):
    ...
