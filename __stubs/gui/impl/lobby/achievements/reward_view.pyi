# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/reward_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import SoundGroups as SoundGroups
from gui.server_events.bonuses import DogTagComponentBonus as DogTagComponentBonus
from gui.shared.event_dispatcher import showAdvancedAchievementsRewardView as showAdvancedAchievementsRewardView, showAdvancedAchievementsView as showAdvancedAchievementsView
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.shared.event_dispatcher import showAdvancedAchievementsCatalogView as showAdvancedAchievementsCatalogView, showAnimatedDogTags as showAnimatedDogTags
from gui.shared.tutorial_helper import getTutorialGlobalStorage as getTutorialGlobalStorage
from gui.impl.lobby.achievements.profile_utils import createAdvancedAchievementsCatalogInitAchievementIDs as createAdvancedAchievementsCatalogInitAchievementIDs, fillAdvancedAchievementModel as fillAdvancedAchievementModel, createBackportTooltipDecorator as createBackportTooltipDecorator, createTooltipContentDecorator as createTooltipContentDecorator, getRewardViewBonusPacker as getRewardViewBonusPacker
from gui.impl.gen.view_models.views.lobby.achievements.views.reward_view_model import RewardViewModel as RewardViewModel
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.pub import ViewImpl as ViewImpl
from gui.impl.pub.lobby_window import LobbyNotificationWindow as LobbyNotificationWindow
from gui.Scaleform.daapi.view.lobby.profile.sound_constants import ACHIEVEMENTS_REWARD_SCREEN_EXIT_EVENT as ACHIEVEMENTS_REWARD_SCREEN_EXIT_EVENT
from helpers import dependency as dependency
from PlayerEvents import g_playerEvents as g_playerEvents
from skeletons.gui.game_control import IAchievementsController as IAchievementsController
from tutorial.control.context import GLOBAL_FLAG as GLOBAL_FLAG
from uilogging.advanced_achievement.logger import AdvancedAchievementRewardLogger as AdvancedAchievementRewardLogger
from uilogging.advanced_achievement.logging_constants import AdvancedAchievementViewKey as AdvancedAchievementViewKey, AdvancedAchievementButtons as AdvancedAchievementButtons
from advanced_achievements_client.getters import BonusTuple as BonusTuple
from typing import List as List

class RewardView(ViewImpl):
    __slots__: tuple
    __MAX_REWARDS_PER_SCREEN = 3
    __achievementsController: Any
    __bonusTuples: Any
    __isFirstEntry: Any
    __haveNewAnimatedDogTag: Any
    __tooltipData: Any
    __uiLogger: Any
    def __init__(self, bonusTuples, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self):
        ...
    def _finalize(self):
        ...
    def __getIsFirstEntry(self):
        ...
    def __hasAnimatedDogtag(self):
        ...
    def __fillModel(self):
        ...
    def __getBonusTuples(self):
        ...
    def __getNextBonusTuple(self):
        ...
    def __updateAchievements(self, model, bonusTuples):
        ...
    def __updateRewards(self, model, bonusTuples):
        ...
    def __onClose(self):
        ...
    def __goToDogTag(self, args):
        ...
    def __onOpenAchievement(self, args):
        ...
    def __onOpenNextReward(self):
        ...
    def __onOpenAchievementsPage(self):
        ...

class RewardViewWindow(LobbyNotificationWindow):
    __slots__: tuple
    def __init__(self, bonusTuples, parent=None, *args, **kwargs):
        ...
