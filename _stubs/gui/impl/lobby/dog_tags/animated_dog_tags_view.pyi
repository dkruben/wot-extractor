# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dog_tags/animated_dog_tags_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from functools import partial as partial
import BigWorld as BigWorld
import WWISE as WWISE
from constants import DOG_TAGS_CONFIG as DOG_TAGS_CONFIG
from dog_tags_common.dog_tags_storage import UnlockedComponentsStorage as UnlockedComponentsStorage, PlayerDogTagStorage as PlayerDogTagStorage
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.impl import backport as backport
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.dog_tags.animated_dog_tags_view_model import AnimatedDogTagsViewModel as AnimatedDogTagsViewModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.achievements.profile_utils import createAdvancedAchievementsCatalogInitAchievementIDs as createAdvancedAchievementsCatalogInitAchievementIDs
from gui.impl.lobby.dog_tags.animated_dog_tag_composer import AnimatedDogTagComposer as AnimatedDogTagComposer
from gui.impl.lobby.dog_tags.catalog_animated_dog_tag_tooltip import CatalogAnimatedDogTagTooltip as CatalogAnimatedDogTagTooltip
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events import settings as userSettings
from gui.shared import events as events
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView, showAdvancedAchievementsCatalogView as showAdvancedAchievementsCatalogView, showAnimatedDogTags as showAnimatedDogTags
from gui.impl.lobby.account_dashboard.sound_constants import ACC_DASHBOARD_SOUND_SPACE as ACC_DASHBOARD_SOUND_SPACE
from helpers import dependency as dependency
from skeletons.gui.impl import IGuiLoader as IGuiLoader
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.web import IWebController as IWebController
from uilogging.dog_tags.logger import AnimatedDogTagsViewLogger as AnimatedDogTagsViewLogger
from uilogging.dog_tags.logging_constants import DogTagButtons as DogTagButtons, DogTagsViewKeys as DogTagsViewKeys, DogTagKeys as DogTagKeys
from gui.Scaleform.Waiting import Waiting as Waiting
from account_helpers.dog_tags import DogTags as DogTagsAccountHelper
_logger: Any

class AnimatedDogTagsView(ViewImpl):
    __slots__: tuple
    _webCtrl: Any
    lobbyContext: Any
    _COMMON_SOUND_SPACE = ACC_DASHBOARD_SOUND_SPACE
    __initBackgroundId: Any
    __initEngravingId: Any
    _dogTagsHelper: Any
    _composer: Any
    __uiLogger: Any
    def __init__(self, layoutID=..., initBackgroundId=0, initEngravingId=0, *args, **kwargs):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    def __onClose(self):
        ...
    def __update(self):
        ...
    def __onInfoButtonClicked(self):
        ...
    # decorador original: @args2params(...)
    def __onEquip(self, background, engraving):
        ...
    # decorador original: @args2params(...)
    def __onGoToAchievement(self, achievementId, category, background, engraving):
        ...
    # decorador original: @args2params(...)
    def __onPlayVideo(self, urlKey):
        ...
    def __onOnboardingCloseClick(self):
        ...
    # decorador original: @args2params(...)
    def __onHideNewBubble(self, background, engraving):
        ...
    def __onDogTagDataChanged(self, diff):
        ...
    def __onServerSettingsChange(self, diff):
        ...

def _getCatalogCallback(backgroundId, engravingId):
    ...
