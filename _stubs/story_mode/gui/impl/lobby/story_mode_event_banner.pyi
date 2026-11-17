# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/lobby/story_mode_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from helpers import dependency as dependency
from helpers.time_utils import getTimestampFromUTC as getTimestampFromUTC, getServerUTCTime as getServerUTCTime, ONE_DAY as ONE_DAY, ONE_MINUTE as ONE_MINUTE
from story_mode.account_settings import setEventEntryPointShown as setEventEntryPointShown, getEventEntryPointShown as getEventEntryPointShown, getEventVisited as getEventVisited, getNewbieEntryPointAnimationSeenId as getNewbieEntryPointAnimationSeenId, setNewbieEntryPointAnimationSeenId as setNewbieEntryPointAnimationSeenId
from story_mode.gui.impl.lobby.event_banner_tooltip import EventBannerTooltip as EventBannerTooltip
from story_mode.gui.impl.lobby.newbie_banner_tooltip import NewbieBannerTooltip as NewbieBannerTooltip
from story_mode.skeletons.story_mode_controller import IStoryModeController as IStoryModeController
from story_mode.uilogging.story_mode.loggers import EntryPointLogger as EntryPointLogger, NewbieEntryPointLogger as NewbieEntryPointLogger
from story_mode_common.configs.story_mode_settings import settingsSchema as settingsSchema
from frameworks.wulf import ViewEvent as ViewEvent

class StoryModeNewbieBanner(StandardEventBanner):
    NAME = 'StoryModeNewbieEntryPoint'
    _controller: Any
    _uiLogger: Any
    def __init__(self):
        ...
    @property
    def isMode(self):
        ...
    @property
    def borderColor(self):
        ...
    @property
    def bannerState(self):
        ...
    @property
    def playAppearAnim(self):
        ...
    @property
    def introDescription(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    def createToolTipContent(self, event):
        ...
    def onClick(self):
        ...

class StoryModeEventBanner(StandardEventBanner):
    NAME = 'StoryModeEventEntryPoint'
    _controller: Any
    _uiLogger: Any
    def __init__(self):
        ...
    @property
    def isMode(self):
        ...
    @property
    def borderColor(self):
        ...
    @property
    def bannerState(self):
        ...
    @property
    def timerValue(self):
        ...
    @property
    def showTimerBeforeEventEnd(self):
        ...
    @property
    def playAppearAnim(self):
        ...
    @property
    def introDescription(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    def createToolTipContent(self, event):
        ...
    def onClick(self):
        ...
    def onAppear(self):
        ...
    def onDisappear(self):
        ...
    def _onSettingsUpdated(self):
        ...
