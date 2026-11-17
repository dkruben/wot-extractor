# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/battle/epilogue_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import typing as typing
import SoundGroups as SoundGroups
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings
from gui.app_loader import app_getter as app_getter
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl, ViewImpl as ViewImpl
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from story_mode.gui.fade_in_out import UseStoryModeFading as UseStoryModeFading
from story_mode.gui.impl.battle.lore_settings_model import getLoreSettings as getLoreSettings
from story_mode.gui.impl.gen.view_models.views.battle.epilogue_window_view_model import EpilogueWindowViewModel as EpilogueWindowViewModel
from story_mode.gui.impl.mixins import DestroyWindowOnDisconnectMixin as DestroyWindowOnDisconnectMixin
from story_mode.gui.shared.event_dispatcher import showCongratulationsWindow as showCongratulationsWindow, sendViewLoadedEvent as sendViewLoadedEvent
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.consts import LogWindows as LogWindows, LogButtons as LogButtons
from story_mode.uilogging.story_mode.loggers import WindowLogger as WindowLogger
from gui.Scaleform.framework.application import AppEntry as AppEntry

class EpilogueView(ViewImpl):
    __slots__: tuple
    LAYOUT_ID: Any
    _storyModeCtrl: Any
    _appLoader: Any
    _uiLogger: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @UseStoryModeFading(...)
    def _onCloseHandler(self):
        ...
    # decorador original: @UseStoryModeFading(...)
    def _goToHangarAnimated(self):
        ...

class EpilogueWindow(DestroyWindowOnDisconnectMixin, WindowImpl):
    __slots__: tuple
    def __init__(self):
        ...
    # decorador original: @app_getter
    def app(self):
        ...
    def _onContentReady(self):
        ...
