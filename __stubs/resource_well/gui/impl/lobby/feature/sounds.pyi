# wot-extractor: STUB (.pyi) gerado a partir de sources/res/resource_well/scripts/client/resource_well/gui/impl/lobby/feature/sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.sounds.filters import StatesGroup as StatesGroup, States as States
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
RESOURCE_WELL_SOUND_SPACE: Any
RESOURCE_WELL_PREVIEW_SOUND_SPACE: Any

class SOUNDS(CONST_CONTAINER):
    SPACE = 'resource_well_space'
    COMMON_ENTER = 'resources_well_enter'
    COMMON_EXIT = 'resources_well_exit'
    PREVIEW_SPACE = 'resource_well_preview_space'
    PREVIEW_ENTER = 'resources_well_preview_enter'
    PREVIEW_EXIT = 'resources_well_preview_exit'
    STATE_PLACE = 'STATE_hangar_place'
    STATE_PLACE_GARAGE = 'STATE_hangar_place_garage'
