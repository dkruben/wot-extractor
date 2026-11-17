# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/event_banners/challenges_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import ChallengesMissions as ChallengesMissions
from challenges_common import ChallengeTokenType as ChallengeTokenType
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES as HANGAR_ALIASES
from gui.challenges.challenges_helpers import TIME_BEFORE_END_OF_EXPIRATION as TIME_BEFORE_END_OF_EXPIRATION, getSettings as getSettings, setSettings as setSettings
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.impl.lobby.user_missions.tooltips.challenges_banner_tooltip import ChallengesBannerTooltip as ChallengesBannerTooltip
from gui.server_events.events_dispatcher import showChallenges as showChallenges
from helpers import dependency as dependency, time_utils as time_utils
from shared_utils import findFirst as findFirst
from skeletons.gui.challenges import IChallengesController as IChallengesController
from skeletons.gui.shared import IItemsCache as IItemsCache

class ChallengesEventBanner(StandardEventBanner):
    NAME = HANGAR_ALIASES.CHALLENGES_EVENT_BANNER
    __eventsService: Any
    __challenges: Any
    __state: Any
    __playAppearAnim: Any
    def __init__(self):
        ...
    @property
    def bannerState(self):
        ...
    @property
    def borderColor(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    @property
    def eventEndDate(self):
        ...
    @property
    def showTimerBeforeEventEnd(self):
        ...
    @property
    def timerValue(self):
        ...
    @property
    def playAppearAnim(self):
        ...
    def onAppearAnimationPlayed(self):
        ...
    def createToolTipContent(self, event):
        ...
    def prepare(self):
        ...
    def onClick(self):
        ...
    def onAppear(self):
        ...
    def onDisappear(self):
        ...
    def startPersistentListening(self):
        ...
    def stopPersistentListening(self):
        ...
    def __onUpdate(self, *_):
        ...
    def __getState(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isChallengesBannerAvailable(challenges=None, itemsCache=None):
    ...
