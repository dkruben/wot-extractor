# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/common/settings/acoustic_presets.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
from collections import namedtuple as namedtuple
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from debug_utils import LOG_WARNING as LOG_WARNING, LOG_ERROR as LOG_ERROR
from gui.Scaleform.genConsts.ACOUSTICS import ACOUSTICS as ACOUSTICS
from shared_utils import findFirst as findFirst
_SOUND_DELAY = 0.5
PresetItem: Any
_PRESETS: dict

class AcousticPresetsPlayer(object):
    __view: Any
    __cursor: Any
    __items: Any
    __sound: Any
    __isPlaying: Any
    __isPlayRound: Any
    __callbackID: Any
    def __init__(self, view, items):
        ...
    def clear(self):
        ...
    def setupInitState(self):
        ...
    def play(self):
        ...
    def pause(self):
        ...
    def reset(self):
        ...
    def click(self, speakerID):
        ...
    def __lockView(self):
        ...
    def __unlockView(self, pause=False):
        ...
    def __hasNextSound(self):
        ...
    def __playNextSound(self):
        ...
    def __playSound(self, item):
        ...
    def __stopSound(self):
        ...
    def __onSoundStop(self, _):
        ...
    def __clearCallback(self):
        ...
    def __setCallback(self):
        ...
    def __handleCallback(self):
        ...

def createPlayer(view, acousticType):
    ...
