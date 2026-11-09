# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/seniority_awards/seniority_awards_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import WWISE as WWISE
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
from gui.sounds.filters import StatesGroup as StatesGroup, States as States
SENIORITY_REWARD_SOUND_SPACE: Any

class LootBoxViewEvents(CONST_CONTAINER):
    ENTRY_VIEW_ENTER = 'gui_lootbox_logistic_center_ambience_on'
    ENTRY_VIEW_EXIT = 'gui_lootbox_logistic_center_ambience_off'
    BENGAL_FIRE_OFF = 'gui_lootbox_logistic_center_bengal_fire_off'

def playSound(eventName):
    ...
