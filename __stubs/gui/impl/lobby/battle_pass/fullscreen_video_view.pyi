# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/battle_pass/fullscreen_video_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import BigWorld as BigWorld
import SoundGroups as SoundGroups
import Windowing as Windowing
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.battle_pass.sounds import BattlePassSounds as BattlePassSounds
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.battle_pass.fullscreen_video_view_model import FullscreenVideoViewModel as FullscreenVideoViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyWindow as LobbyWindow
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from gui.sounds.filters import switchVideoOverlaySoundFilter as switchVideoOverlaySoundFilter
_logger: Any

class FullscreenVideoView(ViewImpl):
    __slots__: tuple
    __appFactory: Any
    __onVideoClosedHandle: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def onClose(self):
        ...
    def _onLoading(self, videoName, audioName, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __hideBack(self):
        ...
    def __showBack(self):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __setWindowAccessible(self, model=None):
        ...
    def __onWindowAccessibilityChanged(self, _):
        ...

class FullscreenVideoWindow(LobbyWindow):
    __slots__: tuple
    def __init__(self, *args, **kwargs):
        ...
