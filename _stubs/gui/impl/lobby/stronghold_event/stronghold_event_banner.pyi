# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/stronghold_event/stronghold_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import Tuple as Tuple
from account_helpers.AccountSettings import StrongholdEvent as StrongholdEvent
from constants import ClansConfig as ClansConfig
from gui.Scaleform.daapi.view.lobby.clans.clan_helpers import getStrongholdEventEnabled as getStrongholdEventEnabled, getStrongholdEventUrl as getStrongholdEventUrl
from gui.Scaleform.genConsts.HANGAR_ALIASES import HANGAR_ALIASES as HANGAR_ALIASES
from gui.clans.clan_cache import g_clanCache as g_clanCache
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.stronghold_event.stronghold_event_helpers import getSettings as getSettings, setSettings as setSettings
from gui.impl.lobby.stronghold_event.tooltips.stronghold_event_banner_tooltip import StrongholdEventBannerTooltip as StrongholdEventBannerTooltip
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.shared.event_dispatcher import showStrongholds as showStrongholds
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from helpers import dependency as dependency, time_utils as time_utils
from helpers.server_settings import serverSettingsChangeListener as serverSettingsChangeListener
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext

class StrongholdEventBanner(Notifiable, StandardEventBanner):
    NAME = HANGAR_ALIASES.STRONGHOLD_EVENT_BANNER
    __eventsService: Any
    __lobbyContext: Any
    __settingsCore: Any
    __eventSettings: Any
    _state: Any
    _timerValue: Any
    _playAppearAnim: Any
    def __init__(self):
        ...
    @property
    def bannerState(self):
        ...
    @property
    def isMode(self):
        ...
    @property
    def borderColor(self):
        ...
    @property
    def introDescription(self):
        ...
    @property
    def inProgressDescription(self):
        ...
    @property
    def timerValue(self):
        ...
    @property
    def eventStartDate(self):
        ...
    @property
    def eventEndDate(self):
        ...
    @property
    def playAppearAnim(self):
        ...
    @property
    def showTimerBeforeEventEnd(self):
        ...
    def createToolTipContent(self, event):
        ...
    def onClick(self):
        ...
    def prepare(self):
        ...
    def onAppear(self):
        ...
    def onDisappear(self):
        ...
    def __getState(self):
        ...
    def __onUpdate(self, *_):
        ...
    # decorador original: @serverSettingsChangeListener(...)
    def __onServerSettingsChanged(self, _):
        ...
    def __onDataFailed(self, _):
        ...
    def __isEventActive(self):
        ...
    def __getCurrentPrimeTime(self):
        ...
    def __getTimeToNextAction(self):
        ...
