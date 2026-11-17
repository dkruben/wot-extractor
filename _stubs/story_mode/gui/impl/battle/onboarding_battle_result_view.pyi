# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/battle/onboarding_battle_result_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import typing as typing
from frameworks.wulf import WindowFlags as WindowFlags, ViewSettings as ViewSettings
from gui.app_loader import app_getter as app_getter
from gui.impl.gen import R as R
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from helpers import dependency as dependency
from story_mode.gui.fade_in_out import UseStoryModeFading as UseStoryModeFading
from story_mode.gui.impl.gen.view_models.views.battle.onboarding_battle_result_view_model import OnboardingBattleResultViewModel as OnboardingBattleResultViewModel
from story_mode.gui.impl.mixins import DestroyWindowOnDisconnectMixin as DestroyWindowOnDisconnectMixin
from story_mode.gui.shared.event_dispatcher import showPrebattleAndGoToQueue as showPrebattleAndGoToQueue, sendViewLoadedEvent as sendViewLoadedEvent
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.consts import LogButtons as LogButtons
from story_mode.uilogging.story_mode.loggers import PostBattleWindowLogger as PostBattleWindowLogger
from gui.Scaleform.framework.application import AppEntry as AppEntry

class OnboardingBattleResultView(ViewImpl):
    __slots__: tuple
    LAYOUT_ID: Any
    _storyModeCtrl: Any
    _finishReason: Any
    _missionId: Any
    _uiLogger: Any
    def __init__(self, finishReason, missionId):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @UseStoryModeFading(...)
    def __onContinueButtonClick(self):
        ...

class OnboardingBattleResultWindow(DestroyWindowOnDisconnectMixin, WindowImpl):
    __slots__: tuple
    # decorador original: @app_getter
    def app(self):
        ...
    def __init__(self, finishReason, missionId):
        ...
    def _onContentReady(self):
        ...
