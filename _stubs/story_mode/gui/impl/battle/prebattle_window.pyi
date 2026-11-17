# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/battle/prebattle_window.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from logging import getLogger as getLogger
import typing as typing
import WWISE as WWISE
import BattleReplay as BattleReplay
import BigWorld as BigWorld
import SoundGroups as SoundGroups
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.app_loader import app_getter as app_getter
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.arena_info.interfaces import IArenaLoadController as IArenaLoadController
from gui.game_loading import loading as loading
from gui.impl.gen import R as R
from gui.impl.pub import WindowImpl as WindowImpl
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from story_mode.gui.fade_in_out import UseStoryModeFading as UseStoryModeFading
from story_mode.gui.impl.base_queue_view import BaseWaitQueueView as BaseWaitQueueView
from story_mode.gui.impl.battle.lore_settings_model import getLoreSettings as getLoreSettings
from story_mode.gui.impl.gen.view_models.views.battle.prebattle_window_view_model import PrebattleWindowViewModel as PrebattleWindowViewModel
from story_mode.gui.impl.mixins import DestroyWindowOnDisconnectMixin as DestroyWindowOnDisconnectMixin
from story_mode.gui.shared.event_dispatcher import showQueueWindow as showQueueWindow, sendViewLoadedEvent as sendViewLoadedEvent
from story_mode.gui.sound_constants import GAMEMODE_GROUP as GAMEMODE_GROUP, GAMEMODE_STATE as GAMEMODE_STATE
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.consts import LogWindows as LogWindows, LogButtons as LogButtons
from story_mode.uilogging.story_mode.loggers import MissionWindowLogger as MissionWindowLogger
from story_mode_common.story_mode_constants import LOGGER_NAME as LOGGER_NAME
from gui.Scaleform.framework.application import AppEntry as AppEntry
_logger: Any

class PrebattleView(BaseWaitQueueView, IArenaLoadController):
    __slots__: tuple
    LAYOUT_ID: Any
    _storyModeCtrl: Any
    _sessionProvider: Any
    missionId: Any
    _uiLogger: Any
    _missionLoreSettings: Any
    def __init__(self, missionId):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @app_getter
    def app(self):
        ...
    def spaceLoadCompleted(self):
        ...
    # decorador original: @UseStoryModeFading(...)
    def arenaLoadCompleted(self):
        ...
    def restart(self):
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
    def _gotoBattleHandler(self):
        ...
    # decorador original: @UseStoryModeFading(...)
    def _onWaitQueueTimeout(self):
        ...

class PrebattleWindow(DestroyWindowOnDisconnectMixin, WindowImpl):
    __slots__: tuple
    def __init__(self, missionId):
        ...

def _hideCursor():
    ...
def getOpenedPrebattleView():
    ...
