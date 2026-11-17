# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/marathon/marathon_reward_sounds.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import WWISE as WWISE
from shared_utils import CONST_CONTAINER as CONST_CONTAINER

class MarathonVideos(CONST_CONTAINER):
    VEHICLE = 1

class _MarathonVideoEvents(CONST_CONTAINER):
    VIDEO_START: dict
    VIDEO_DONE = 'gui_marathon_video_stop'

class _MarathonVideoStates(CONST_CONTAINER):
    GROUP = 'STATE_video_overlay'
    START = 'STATE_video_overlay_on'
    DONE = 'STATE_video_overlay_off'

def playSound(eventName):
    ...
def onVideoStart(videoId, sourceID=''):
    ...
def onVideoDone():
    ...
