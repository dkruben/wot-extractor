# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/lobby/comp7_helpers/comp7_lobby_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
import SoundGroups as SoundGroups
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
from comp7.gui.impl.gen.view_models.views.lobby.enums import MetaRootViews as MetaRootViews
from sound_gui_manager import CommonSoundSpaceSettings as CommonSoundSpaceSettings

class MetaViewSounds(Enum):
    ENTER_EVENT = 'comp_7_progression_enter'
    EXIT_EVENT = 'comp_7_progression_exit'
    ENTER_TAB_EVENTS: dict
    EXIT_TAB_EVENTS: dict

class FlybySounds(Enum):
    START = 'comp_7_shop_purchase_anim_start'
    STOP = 'comp_7_shop_purchase_anim_stop'

class VehicleVideoSounds(CONST_CONTAINER):
    START = 'comp_7_video_reward_style_start'
    PAUSE = 'comp_7_video_reward_style_pause'
    RESUME = 'comp_7_video_reward_style_resume'
    END = 'comp_7_video_reward_style_stop'

def getComp7MetaSoundSpace():
    ...
def playComp7MetaViewTabSound(tabId, prevTabId=None):
    ...
def playSound(eventName):
    ...
