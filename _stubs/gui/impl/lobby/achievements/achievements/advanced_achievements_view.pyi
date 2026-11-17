# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/achievements/advanced_achievements_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf.view.submodel_presenter import SubModelPresenter as SubModelPresenter
from gui.impl.gen.view_models.views.lobby.achievements.views.achievements.advanced_achievements_view_model import AdvancedAchievementsViewModel as AdvancedAchievementsViewModel
from gui.impl.gen.view_models.views.lobby.achievements.views.achievements.upcoming_model import UpcomingModel as UpcomingModel
from helpers import dependency as dependency
from frameworks.wulf import WindowLayer as WindowLayer, WindowStatus as WindowStatus
from gui.shared.event_dispatcher import showAdvancedAchievementsCatalogView as showAdvancedAchievementsCatalogView, showTrophiesView as showTrophiesView, showAdvancedAchievementsView as showAdvancedAchievementsView
from gui.impl.lobby.achievements.profile_utils import fillAdvancedAchievementModel as fillAdvancedAchievementModel, createAdvancedAchievementsCatalogInitAchievementIDs as createAdvancedAchievementsCatalogInitAchievementIDs, getTrophiesData as getTrophiesData, fillSubcategoryAdvancedAchievementModel as fillSubcategoryAdvancedAchievementModel, getVehicleByName as getVehicleByName
from advanced_achievements_client.constants import AchievementType as AchievementType
from advanced_achievements_client.getters import ROOT_ACHIEVEMENT_IDS as ROOT_ACHIEVEMENT_IDS, getAchievementByID as getAchievementByID, getNearest as getNearest, getLastReceivedAchievements as getLastReceivedAchievements
from uilogging.advanced_achievement.logger import AdvancedAchievementLogger as AdvancedAchievementLogger
from uilogging.advanced_achievement.logging_constants import AdvancedAchievementViewKey as AdvancedAchievementViewKey, AdvancedAchievementButtons as AdvancedAchievementButtons, AdvancedAchievementKeys as AdvancedAchievementKeys, AdvancedAchievementSubcategory as AdvancedAchievementSubcategory
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.game_control import IAchievementsController as IAchievementsController
from skeletons.gui.impl import IGuiLoader as IGuiLoader

class AdvancedAchievementsView(SubModelPresenter):
    __slots__: tuple
    __itemsCache: Any
    __advAchmntCtrl: Any
    __guiLoader: Any
    __RESTRICTED_LAYERS: set
    __ACTIVE_WINDOW_STATUSES: tuple
    __userId: Any
    __achievementList: Any
    __isAnimationInProgress: Any
    __isWindowOverlapped: Any
    __uiLogger: Any
    def __init__(self, achievementsModel, parentView, userId):
        ...
    @property
    def viewModel(self):
        ...
    @property
    def __isOtherPlayer(self):
        ...
    def getParentWindow(self):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def finalize(self):
        ...
    def __onWindowStatusChanged(self, _, newStatus):
        ...
    def __onNewAchievementsEarned(self, _):
        ...
    def __update(self):
        ...
    def __updatePage(self):
        ...
    def __updateTrophies(self, model):
        ...
    def __updateUpcomingAchievements(self, dossierDescr):
        ...
    def __fillUpcomingAchievement(self, achievement):
        ...
    def __setPrevAchievementScore(self):
        ...
    def __setPrevTrophy(self):
        ...
    def __setPrevSubcategoryData(self, prevSubcategories):
        ...
    def __setPrevCategoryProgress(self, value):
        ...
    def __onAnimationInProgress(self, args):
        ...
    def __onAllAnimationEnd(self):
        ...
    def __onCupClick(self):
        ...
    def __onAchievementHover(self, args):
        ...
    def __onSkipAnimation(self, isSkip):
        ...
    def __onOpenDetails(self, args):
        ...
    def __onOpenTrophies(self):
        ...
