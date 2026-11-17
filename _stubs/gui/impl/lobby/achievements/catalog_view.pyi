# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/achievements/catalog_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from advanced_achievements_client.constants import TROPHIES_ACHIEVEMENT_ID as TROPHIES_ACHIEVEMENT_ID
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, WindowFlags as WindowFlags, WindowLayer as WindowLayer
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.view.lobby.storage.storage_helpers import getVehicleCDForStyle as getVehicleCDForStyle
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.impl.gen import R as R
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.catalog_view_model import CatalogViewModel as CatalogViewModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.breadcrumb_model import BreadcrumbModel as BreadcrumbModel
from gui.impl.lobby.achievements.profile_utils import fillDetailsModel as fillDetailsModel, fillBreadcrumbModel as fillBreadcrumbModel, fillAchievementCardModel as fillAchievementCardModel, getTrophiesData as getTrophiesData, createBackportTooltipDecorator as createBackportTooltipDecorator, createTooltipContentDecorator as createTooltipContentDecorator
from gui.shared.event_dispatcher import showAdvancedAchievementsCatalogView as showAdvancedAchievementsCatalogView, showAdvancedAchievementsView as showAdvancedAchievementsView, showStylePreview as showStylePreview, showAnimatedDogTags as showAnimatedDogTags, showVehicleHubModules as showVehicleHubModules
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from helpers import dependency as dependency
from skeletons.gui.game_control import IAchievementsController as IAchievementsController
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from uilogging.advanced_achievement.logger import AdvancedAchievementLogger as AdvancedAchievementLogger
from uilogging.advanced_achievement.logging_constants import AdvancedAchievementViewKey as AdvancedAchievementViewKey, AdvancedAchievementButtons as AdvancedAchievementButtons
from gui.Scaleform.daapi.view.lobby.profile.sound_constants import ACHIEVEMENTS_SOUND_SPACE as ACHIEVEMENTS_SOUND_SPACE
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.details_model import DetailsModel as DetailsModel

class CatalogView(ViewImpl):
    __slots__: tuple
    __achievementsController: Any
    __customizationService: Any
    __appLoader: Any
    _COMMON_SOUND_SPACE = ACHIEVEMENTS_SOUND_SPACE
    __tooltipData: Any
    __achievementCategory: Any
    __closeCallback: Any
    __breadcrumbAchievementIDs: Any
    __uiParentScreen: Any
    __uiLogging: Any
    __mainViewCallback: Any
    def __init__(self, initAchievementIDs, achievementCategory, closeCallback, uiParentScreen, mainViewCallback=None, *args, **kwargs):
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
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def __updatePage(self):
        ...
    def __updateAchievementScore(self, model):
        ...
    def __updateBreadcrumbs(self, model):
        ...
    def __updateAchievements(self, model):
        ...
    def __updateDescription(self, model, descriptionAchievement):
        ...
    def __updateTrophiesDescription(self, model):
        ...
    def __updateAchievementsList(self, model, achievements):
        ...
    def __getAchievementBubbles(self, achievement):
        ...
    def __navigateToBreadcrumb(self, achievementID):
        ...
    def __addBreadcrumb(self, achievementID):
        ...
    def __onClose(self):
        ...
    def __onBreadcrumbClick(self, args):
        ...
    def __onCatalogClick(self):
        ...
    def __onStylePreview(self, args):
        ...
    # decorador original: @args2params(...)
    def __onPurchaseVehicleClick(self, intCD):
        ...
    def __onCardClick(self, args):
        ...
    def __onHintClose(self):
        ...
    def __onCardHover(self, args):
        ...
    def __onDogTagPreview(self, args):
        ...

class CatalogViewWindow(WindowImpl):
    __slots__: tuple
    def __init__(self, initAchievementIDs, achievementCategory, closeCallback, uiParentScreen, parent=None, *args, **kwargs):
        ...

def _getPreviewCallback(appLoader, initAchievementIDs, achievementCategory, closeCallback, parentScreen):
    ...
