# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dog_tags/dog_tags_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from collections import defaultdict as defaultdict
from operator import attrgetter as attrgetter
import typing as typing
import BigWorld as BigWorld
import WWISE as WWISE
from constants import DOG_TAGS_CONFIG as DOG_TAGS_CONFIG
from dog_tags_common.components_config import componentConfigAdapter as componentConfigAdapter
from dog_tags_common.config.common import ComponentViewType as ComponentViewType, ComponentPurpose as ComponentPurpose
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.lobby_entry import getLobbyStateMachine as getLobbyStateMachine
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.dog_tags.dedication_tooltip_model import DedicationTooltipModel as DedicationTooltipModel
from gui.impl.gen.view_models.views.lobby.dog_tags.dog_tags_view_model import DogTagsViewModel as DogTagsViewModel
from gui.impl.gen.view_models.views.lobby.dog_tags.three_months_tooltip_model import ThreeMonthsTooltipModel as ThreeMonthsTooltipModel
from gui.impl.gen.view_models.views.lobby.dog_tags.triumph_tooltip_model import TriumphTooltipModel as TriumphTooltipModel
from gui.impl.gui_decorators import args2params as args2params
from gui.impl.lobby.dog_tags.animated_dog_tag_composer import AnimatedDogTagComposer as AnimatedDogTagComposer
from gui.impl.lobby.dog_tags.dog_tag_composer import DogTagComposerLobby as DogTagComposerLobby
from gui.impl.lobby.dog_tags.ranked_efficiency_tooltip import RankedEfficiencyTooltip as RankedEfficiencyTooltip
from gui.impl.pub import ViewImpl as ViewImpl
from gui.server_events import settings as userSettings
from gui.shared import events as events
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.event_dispatcher import showBrowserOverlayView as showBrowserOverlayView
from gui.sounds.filters import switchHangarOverlaySoundFilter as switchHangarOverlaySoundFilter
from helpers import dependency as dependency
from helpers.time_utils import getCurrentLocalServerTimestamp as getCurrentLocalServerTimestamp, getTimeStructInLocal as getTimeStructInLocal
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.web import IWebController as IWebController
from uilogging.dog_tags.logger import DogTagsViewLogger as DogTagsViewLogger
from uilogging.dog_tags.logging_constants import DogTagsViewKeys as DogTagsViewKeys
from account_helpers.dog_tags import DogTags as DogTagsAccountHelper
from typing import Dict as Dict, Callable as Callable, Optional as Optional, Union as Union
from frameworks.wulf import View as View, ViewEvent as ViewEvent
_logger: Any
DEFAULT_DOG_TAGS_TAB: Any
DOG_TAG_INFO_PAGE_KEY = 'infoPage'

class DogTagsView(ViewImpl):
    _webCtrl: Any
    lobbyContext: Any
    _dogTagsHelper: Any
    _composer: Any
    _animatedComposer: Any
    __selectedEngraving: Any
    __selectedBackground: Any
    _tooltipModelFactories: Any
    __uiLogging: Any
    def __init__(self, layoutID=..., *args, **kwargs):
        ...
    def highlightComponent(self, highlightedComponentId):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def getCurrentDogTag(self):
        ...
    def setSelectedToEquippedDogTag(self):
        ...
    @property
    def selectedEngraving(self):
        ...
    @property
    def selectedBackground(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onLoading(self, highlightedComponentId=-1, makeTopView=False):
        ...
    @staticmethod
    def _soundsOnExit():
        ...
    def _markComponentAsViewed(self, compId):
        ...
    def __isAnimatedDogTagEquipped(self):
        ...
    def __update(self, highlightedComponentId=-1):
        ...
    @staticmethod
    def __getSelectedTabIdx(highlightedComponentId):
        ...
    @staticmethod
    def __getComponentTabIdx(compId):
        ...
    def __onBack(self):
        ...
    # decorador original: @args2params(...)
    def __onTabSelected(self, newTab):
        ...
    def __switchTab(self, newTab):
        ...
    def __onInfoButtonClicked(self):
        ...
    def __updateNotificationCounters(self, model):
        ...
    def __onEquip(self):
        ...
    # decorador original: @args2params(...)
    def __onPlayVideo(self, urlKey):
        ...
    def __onOnboardingCloseClick(self):
        ...
    # decorador original: @args2params(...)
    def __onNewComponentHover(self, compId):
        ...
    def __onDogTagDataChanged(self, diff):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    # decorador original: @args2params(...)
    def __onUpdateSelectedDT(self, background=None, engraving=None):
        ...

class GradesTooltip(ViewImpl):
    def __init__(self, contentId, contentModel, *args, **kwargs):
        ...
    def _onLoading(self, engravingId):
        ...

class DedicationTooltip(GradesTooltip):
    def __init__(self, *args, **kwargs):
        ...

class TriumphTooltip(GradesTooltip):
    def __init__(self, *args, **kwargs):
        ...

class ThreeMonthsTooltip(ViewImpl):
    def __init__(self, *args, **kwargs):
        ...
    def _onLoading(self, engravingId):
        ...
    @staticmethod
    def _getMonthRes(monthNum):
        ...
