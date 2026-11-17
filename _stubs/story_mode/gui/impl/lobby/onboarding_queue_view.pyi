# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/onboarding_queue_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import typing as typing
import BigWorld as BigWorld
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings
from gui.game_loading import loading as loading
from gui.game_loading.resources.consts import Milestones as Milestones
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl
from gui.prb_control import prbEntityProperty as prbEntityProperty
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE, events as events
from helpers import dependency as dependency
from story_mode.gui.fade_in_out import UseStoryModeFading as UseStoryModeFading
from story_mode.gui.impl.base_queue_view import BaseWaitQueueView as BaseWaitQueueView
from story_mode.gui.impl.battle.prebattle_window import getOpenedPrebattleView as getOpenedPrebattleView
from story_mode.gui.impl.gen.view_models.views.lobby.onboarding_queue_view_model import OnboardingQueueViewModel as OnboardingQueueViewModel
from story_mode.gui.impl.mixins import DestroyWindowOnDisconnectMixin as DestroyWindowOnDisconnectMixin
from story_mode.gui.shared.event_dispatcher import sendViewLoadedEvent as sendViewLoadedEvent
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.consts import LogWindows as LogWindows, LogButtons as LogButtons
from story_mode.uilogging.story_mode.loggers import WindowBehindGameLoadingLogger as WindowBehindGameLoadingLogger

class OnboardingQueueView(BaseWaitQueueView):
    __slots__: tuple
    LAYOUT_ID: Any
    _storyModeCtrl: Any
    _isButtonVisible: Any
    _hideGameLoadingCallbackId: Any
    _uiLogger: Any
    def __init__(self, isButtonVisible=False):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @prbEntityProperty
    def prbEntity(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _onWaitQueueTimeout(self):
        ...
    def _onQuitButtonClick(self):
        ...
    def _hideGameLoading(self):
        ...
    # decorador original: @UseStoryModeFading(...)
    def _handleBattleLoading(self, *_):
        ...

class OnboardingQueueWindow(DestroyWindowOnDisconnectMixin, WindowImpl):
    __slots__: tuple
    def __init__(self, isButtonVisible=False):
        ...
