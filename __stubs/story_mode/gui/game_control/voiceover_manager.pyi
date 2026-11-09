# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/game_control/voiceover_manager.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import typing as typing
from account_helpers.settings_core.settings_constants import SOUND as SOUND
import BigWorld as BigWorld
import SoundGroups as SoundGroups
import WWISE as WWISE
from Event import Event as Event
from PlayerEvents import g_playerEvents as g_playerEvents
from account_helpers import AccountSettings as AccountSettings
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
from helpers import i18n as i18n, dependency as dependency
from story_mode.skeletons.voiceover_controller import IVoiceoverManager as IVoiceoverManager
_UPDATE_PERIOD = 0.1

class VoiceoverManager(IVoiceoverManager):
    __slots__: tuple
    onSubtitleShow: Any
    onSubtitleHide: Any
    onStarted: Any
    onStopped: Any
    _currentSound: Any
    _currentSubtitle: Any
    _callbackId: Any
    _currentCtx: Any
    _delay: Any
    _onEndCallbackId: Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
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
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def _onAvatarBecomeNonPlayer(self):
        ...
    def _update(self):
        ...
    def _onEndEvent(self, onEnd):
        ...
    def _soundMarkerHandler(self, marker):
        ...

def debugSubtitle(text=''):
    ...
