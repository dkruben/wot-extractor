# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/sounds/sound.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import SoundGroups as SoundGroups

class Sound(object):
    __sndTick: Any
    __sndPath: Any
    __isPlaying: Any
    def __init__(self, soundPath):
        ...
    @property
    def isPlaying(self):
        ...
    @property
    def sound(self):
        ...
    def play(self):
        ...
    def stop(self):
        ...

class SoundSequence(object):
    __sounds: Any
    __soundsIter: Any
    __curPlayingSnd: Any
    __beforePlayCB: Any
    __afterPlayCB: Any
    __bwCbID: Any
    def __init__(self, sounds, beforePlayCB=None, afterPlayCB=None):
        ...
    def __del__(self):
        ...
    @property
    def sounds(self):
        ...
    def play(self):
        ...
    def stop(self):
        ...
    def __notifyBeforePlay(self, snd):
        ...
    def __notifyAfterPlay(self, snd):
        ...
    def __clear(self):
        ...
    def __playNextSound(self):
        ...
    def __clearCallback(self):
        ...
    def __finishCallback(self, snd):
        ...
