# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/maps_training/sound_constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
MAPS_TRAINING_SOUND_SPACE: Any

class MapsTrainingSound(CONST_CONTAINER):
    COMMON_SOUND_SPACE = 'Lobby_music_garage_maps_training'
    GAMEMODE_GROUP = 'STATE_gamemode'
    GAMEMODE_STATE = 'STATE_gamemode_maps_training'
    GAMEMODE_DEFAULT = 'STATE_gamemode_default'
    HANGAR_GROUP = 'STATE_hangar_place'
    HANGAR_STATE = 'STATE_hangar_place_garage'
    ENTER_EVENT = 'mt_mode_enter'
    EXIT_EVENT = 'mt_mode_exit'
    MAP_CHOICE_ENTER = 'mt_map_choice_enter'
    MAP_CHOICE_EXIT = 'mt_map_choice_exit'
    COMPLETE_ITEM = 'mt_anim_scenario_complete'
    @staticmethod
    def onSelectedMap(isSelected):
        ...
