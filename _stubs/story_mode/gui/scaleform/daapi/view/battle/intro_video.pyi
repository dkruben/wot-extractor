# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/scaleform/daapi/view/battle/intro_video.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BattleReplay as BattleReplay
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from gui.game_loading import loading as loading
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from story_mode.gui.fade_in_out import UseStoryModeFading as UseStoryModeFading
from story_mode.gui.scaleform.daapi.view.common.base_video import BaseVideo as BaseVideo
from story_mode.gui.scaleform.daapi.view.model.video_settings_model import getIntroVideoSettings as getIntroVideoSettings
from story_mode.gui.shared.event_dispatcher import showPrebattleWindow as showPrebattleWindow
from story_mode.uilogging.story_mode.loggers import IntroVideoLogger as IntroVideoLogger

class IntroVideo(BaseVideo, IArenaLoadController):
    _sessionProvider: Any
    def spaceLoadCompleted(self):
        ...
    # decorador original: @UseStoryModeFading(...)
    def onVideoComplete(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _getSettings(self):
        ...
    def _getLogger(self):
        ...
