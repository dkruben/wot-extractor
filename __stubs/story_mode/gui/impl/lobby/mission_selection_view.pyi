# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/mission_selection_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import json as json
import logging as logging
import typing as typing
from datetime import datetime as datetime
from future.utils import viewitems as viewitems
import ResMgr as ResMgr
from PlayerEvents import g_playerEvents as g_playerEvents
from frameworks.wulf import ViewStatus as ViewStatus, WindowLayer as WindowLayer
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.impl import backport as backport
from gui.impl.backport import BackportTooltipWindow as BackportTooltipWindow, createTooltipData as createTooltipData
from gui.impl.gen import R as R
from gui.impl.lobby.common.tooltips.extended_text_tooltip import ExtendedTextTooltip as ExtendedTextTooltip
from gui.impl.lobby.hangar.presenters.utils import navigateTo as navigateTo, getSharedMenuItems as getSharedMenuItems
from gui.impl.lobby.hangar.presenters.main_menu_presenter import MainMenuPresenter as MainMenuPresenter
from gui.prb_control.events_dispatcher import g_eventDispatcher as g_eventDispatcher
from gui.server_events.bonuses import getNonQuestBonuses as getNonQuestBonuses
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from gui.shared.utils.graphics import isLowPreset as isLowPreset
from helpers import i18n as i18n, dependency as dependency
from ids_generators import SequenceIDGenerator as SequenceIDGenerator
from items import vehicles as vehicles
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.shared import IItemsCache as IItemsCache
from story_mode.account_settings import setUnlockedTaskShown as setUnlockedTaskShown, isUnlockedTaskShown as isUnlockedTaskShown, isWelcomeScreenSeen as isWelcomeScreenSeen, getEventVisited as getEventVisited, setEventVisited as setEventVisited
from story_mode.gui.impl.gen.view_models.views.lobby.mission_model import MissionModel as MissionModel
from story_mode.gui.impl.gen.view_models.views.lobby.mission_selection_view_model import MissionSelectionViewModel as MissionSelectionViewModel, TabsEnum as TabsEnum
from story_mode.gui.impl.gen.view_models.views.lobby.task_model import TaskModel as TaskModel, TaskStateEnum as TaskStateEnum
from story_mode.gui.impl.lobby.base_prb_view import BasePrbView as BasePrbView
from story_mode.gui.impl.lobby.difficulty_tooltip import DifficultyTooltip as DifficultyTooltip
from story_mode.gui.impl.lobby.mission_tooltip import MissionTooltip as MissionTooltip
from story_mode.gui.shared.event_dispatcher import sendViewLoadedEvent as sendViewLoadedEvent, showEventWelcomeWindow as showEventWelcomeWindow
from story_mode.gui.shared.utils import formatAndFillRewards as formatAndFillRewards
from story_mode.gui.story_mode_gui_constants import VIEW_ALIAS as VIEW_ALIAS, INFO_PAGE_STORY_MODE as INFO_PAGE_STORY_MODE
from story_mode.gui.sound_constants import STORY_MODE_SOUND_SPACE as STORY_MODE_SOUND_SPACE
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.consts import LogButtons as LogButtons
from story_mode.uilogging.story_mode.loggers import SelectMissionWindow as SelectMissionWindow
from story_mode_common.helpers import isTaskCompleted as isTaskCompleted
from story_mode_common.story_mode_constants import MissionId as MissionId, LOGGER_NAME as LOGGER_NAME
from story_mode_common.configs.story_mode_missions import MissionModel as ConfigMissionModel
from gui.shared.gui_items import Vehicle as Vehicle
from story_mode.gui.impl.gen.view_models.views.lobby.parallax_model import ParallaxModel as ParallaxModel
_logger: Any
PATH_TO_CONFIGS = 'story_mode/gui/parallax/configs.json'
PARALLAX_DEFAULT_SCALE = 1
NOT_UI_CONDITIONS: tuple

class MissionSelectionView(BasePrbView):
    LAYOUT_ID: Any
    MODEL_CLASS = MissionSelectionViewModel
    _COMMON_SOUND_SPACE = STORY_MODE_SOUND_SPACE
    _MAX_BONUSES_IN_VIEW = 5
    _HIDDEN_REWARDS: tuple
    _gui: Any
    _itemsCache: Any
    _storyModeCtrl: Any
    _animationCounter: Any
    _isBackgroundLoaded: Any
    _uiLogger: Any
    __isAnimationPlayedAfterWindowMap: Any
    __idGen: Any
    __bonusCache: Any
    _isParallaxEnabled: Any
    _parallaxConfig: Any
    def __init__(self, *args, **kwargs):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def createToolTip(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _initialize(self):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def _setComponents(self):
        ...
    def _onBackgroundLoaded(self):
        ...
    def _quit(self):
        ...
    def __onViewStatusChanged(self, uniqueID, newState):
        ...
    def __selectMission(self, missionId, updateMissions):
        ...
    def __onMissionSelect(self, args):
        ...
    def __onChangeTab(self, args):
        ...
    def __onMissionsDataUpdated(self):
        ...
    def __onSettingsUpdated(self):
        ...
    def __updateSelectedMission(self, model, updateMissions=True):
        ...
    def __onTaskUnlocked(self, args):
        ...
    def __updateSelectedMissionModel(self, model, missionConfig):
        ...
    def __updateMissionsModels(self, model, currentTab):
        ...
    def __updateTasks(self, model, missionConfig):
        ...
    def __openAbout(self):
        ...
    def __updateTaskRewards(self, task, taskModel):
        ...
    def __getTaskState(self, missionId, task):
        ...
    def __onDossiersResync(self, *args):
        ...
    def __readParallaxConfig(self, missionId, model, isParallaxEnabled):
        ...

def _totalSeconds(endDate):
    ...
def _readSection(path):
    ...
def _toJson(inputData):
    ...
def _getChunks(count, name, path):
    ...
