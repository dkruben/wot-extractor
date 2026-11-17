# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/skeletons/voiceover_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from skeletons.gui.game_control import IGameController as IGameController
from Event import Event as Event

class IVoiceoverManager(IGameController):
    onSubtitleShow = None
    onSubtitleHide = None
    onStarted = None
    onStopped = None
    @property
    def currentSubtitle(self):
        ...
    @property
    def currentCtx(self):
        ...
    @property
    def isPlaying(self):
        ...
    def stopVoiceover(self):
        ...
    def playVoiceover(self, voiceoverId, ctx=None, delay=None):
        ...
