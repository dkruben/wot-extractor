# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/ReplayEvents.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import Event as Event
g_replayEvents: Any

class _ReplayEvents(object):
    onTimeWarpStart: Any
    onTimeWarpFinish: Any
    onPause: Any
    onMuteSound: Any
    onPlaybackSpeedChanged: Any
    onWatcherNotify: Any
    onReplayTerminated: Any
    __isPlaying: Any
    __isRecording: Any
    __isTimeWarp: Any
    __isLastWarpRewind: Any
    @property
    def isPlaying(self):
        ...
    @property
    def isRecording(self):
        ...
    @property
    def isTimeWarp(self):
        ...
    @property
    def isLastWarpRewind(self):
        ...
    def __init__(self):
        ...
    def onRecording(self):
        ...
    def onPlaying(self):
        ...
    def callOnTimeWarpStart(self, isRewind):
        ...
    def callOnTimeWarpFinish(self):
        ...
