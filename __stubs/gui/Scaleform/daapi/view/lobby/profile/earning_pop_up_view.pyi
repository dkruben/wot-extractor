# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/profile/earning_pop_up_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import deque as deque
from functools import partial as partial
from frameworks.wulf import ViewFlags as ViewFlags
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.meta.EarningPopUpViewMeta import EarningPopUpViewMeta as EarningPopUpViewMeta
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.Scaleform.framework.managers.view_lifecycle_watcher import IViewLifecycleHandler as IViewLifecycleHandler, ViewLifecycleWatcher as ViewLifecycleWatcher
from gui.impl.gen import R as R
from gui.impl.lobby.achievements.profile_utils import fillAdvancedAchievementModel as fillAdvancedAchievementModel, createAdvancedAchievementsCatalogInitAchievementIDs as createAdvancedAchievementsCatalogInitAchievementIDs
from gui.shared import events as events, g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen.view_models.views.lobby.achievements.views.achievements_earning_view_model import AchievementsEarningViewModel as AchievementsEarningViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.event_dispatcher import showAdvancedAchievementsCatalogView as showAdvancedAchievementsCatalogView, showAdvancedAchievementsView as showAdvancedAchievementsView, showTrophiesView as showTrophiesView
from gui.shared.tutorial_helper import getTutorialGlobalStorage as getTutorialGlobalStorage
from helpers import dependency as dependency
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from skeletons.gui.game_control import IAchievementsController as IAchievementsController
from tutorial.control.context import GLOBAL_FLAG as GLOBAL_FLAG
from uilogging.advanced_achievement.logger import AdvancedAchievementEarningLogger as AdvancedAchievementEarningLogger
from uilogging.advanced_achievement.logging_constants import AdvancedAchievementViewKey as AdvancedAchievementViewKey, AdvancedAchievementKeys as AdvancedAchievementKeys

class EarningPopUpView(EarningPopUpViewMeta):
    __view: Any
    def __init__(self):
        ...
    def _makeInjectView(self):
        ...

class _NonOverlappingViewsLifecycleHandler(IViewLifecycleHandler):
    __NON_OVERLAPPING_VIEWS: tuple
    __stopAnimationCallback: Any
    def __init__(self, stopAnimationCallback):
        ...
    def onViewCreated(self, view):
        ...

class _EarningPopUpView(ViewImpl):
    __appLoader: Any
    __achievementsController: Any
    __slots__: tuple
    __achievementQueue: Any
    __uiLogging: Any
    __viewLifecycleWatcher: Any
    def __init__(self, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getListeners(self):
        ...
    def _getEvents(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __achEarnedEventHandler(self, event):
        ...
    def __onStopAnimation(self):
        ...
    def __startAnimation(self, data):
        ...
    def __onShown(self):
        ...
    def __onGoToAchievement(self, args):
        ...
    def __achievementCloseCallback(self):
        ...
