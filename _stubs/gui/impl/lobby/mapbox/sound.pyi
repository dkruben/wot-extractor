# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/mapbox/sound.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings
import WWISE as WWISE

class Sounds(Enum):
    OVERLAY_HANGAR_GENERAL = 'STATE_overlay_hangar_general'
    OVERLAY_HANGAR_GENERAL_ON = 'STATE_overlay_hangar_general_on'
    OVERLAY_HANGAR_GENERAL_OFF = 'STATE_overlay_hangar_general_off'

class MapBoxSounds(Enum):
    REWARD_SCREEN = 'bp_reward_screen'

def getMapboxViewSoundSpace(enterEvent='', exitEvent=''):
    ...
def playSound(eventName):
    ...
