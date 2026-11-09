# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/game_control/story_mode_fading_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from future.utils import viewvalues as viewvalues
from gui.impl.common.fade_manager import FadeManager as FadeManager, DefaultFadingCover as DefaultFadingCover
from story_mode.gui.story_mode_gui_constants import STORY_MODE_FADE_IN_DURATION as STORY_MODE_FADE_IN_DURATION, STORY_MODE_FADE_OUT_DURATION as STORY_MODE_FADE_OUT_DURATION, IS_STORY_MODE_FADE_IN_OUT_ON as IS_STORY_MODE_FADE_IN_OUT_ON
from story_mode.skeletons.story_mode_fading_controller import IStoryModeFadingController as IStoryModeFadingController
from wg_async import wg_await as wg_await, wg_async as wg_async

class StoryModeFadingCover(DefaultFadingCover):
    def __init__(self):
        ...

class StoryModeFadingController(IStoryModeFadingController):
    _managerByLayer: Any
    def __init__(self):
        ...
    # decorador original: @wg_async
    def show(self, layerID):
        ...
    # decorador original: @wg_async
    def hide(self, layerID):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onAccountBecomePlayer(self):
        ...
    def _hideImmediately(self):
        ...
    def _getFadeManager(self, layerID):
        ...
