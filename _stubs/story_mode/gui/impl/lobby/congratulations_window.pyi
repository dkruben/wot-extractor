# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/congratulations_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import typing as typing
import SoundGroups as SoundGroups
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings, View as View, WindowLayer as WindowLayer
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl, ViewImpl as ViewImpl
from helpers import dependency as dependency
from story_mode.gui.impl.gen.view_models.views.lobby.congratulations_window_view_model import CongratulationsWindowViewModel as CongratulationsWindowViewModel
from story_mode.gui.impl.gen.view_models.views.lobby.medal_tooltip_view_model import MedalTooltipViewModel as MedalTooltipViewModel
from story_mode.gui.impl.lobby.badge_tooltip import BadgeTooltip as BadgeTooltip
from story_mode.gui.impl.mixins import DestroyWindowOnDisconnectMixin as DestroyWindowOnDisconnectMixin
from story_mode.gui.shared.event_dispatcher import sendViewLoadedEvent as sendViewLoadedEvent
from story_mode.gui.sound_constants import CONGRATULATION_MUSIC as CONGRATULATION_MUSIC
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.consts import LogWindows as LogWindows, LogButtons as LogButtons
from story_mode.uilogging.story_mode.loggers import WindowLogger as WindowLogger
from wg_async import wg_async as wg_async, wg_await as wg_await, forwardAsFuture as forwardAsFuture

class CongratulationsView(ViewImpl):
    __slots__: tuple
    LAYOUT_ID: Any
    _storyModeCtrl: Any
    _onClose: Any
    _isCloseVisible: Any
    _uiLogger: Any
    _awardData: Any
    _missionId: Any
    def __init__(self, isCloseVisible=False, onClose=None, awardData=None):
        ...
    @property
    def viewModel(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def _finalize(self):
        ...
    # decorador original: @wg_async
    def _closeHandler(self):
        ...

class CongratulationsWindow(DestroyWindowOnDisconnectMixin, WindowImpl):
    __slots__: tuple
    def __init__(self, isCloseVisible=False, onClose=None, awardData=None):
        ...
