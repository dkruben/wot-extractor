# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/lobby/views/frontline_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers.AccountSettings import AccountSettings as AccountSettings, FRONTLINE_BANNER_FIRST_APPEARANCE_TIMESTAMP as FRONTLINE_BANNER_FIRST_APPEARANCE_TIMESTAMP, FRONTLINE_BANNER_INTRO_CLICK_TIMESTAMP as FRONTLINE_BANNER_INTRO_CLICK_TIMESTAMP
from frontline.gui.frontline_helpers import isHangarAvailable as isHangarAvailable, getFrontlineState as getFrontlineState
from frontline.gui.impl.gen.view_models.views.lobby.views.frontline_const import FrontlineState as FrontlineState
from frontline.gui.impl.lobby.tooltips.banner_tooltip import BannerTooltipView as BannerTooltipView
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.Scaleform.genConsts.EPICBATTLES_ALIASES import EPICBATTLES_ALIASES as EPICBATTLES_ALIASES
from gui.periodic_battles.models import PrimeTimeStatus as PrimeTimeStatus
from gui.shared.event_dispatcher import showEpicRewardsSelectionWindow as showEpicRewardsSelectionWindow
from helpers import dependency as dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController as IEpicBattleMetaGameController
from frontline.constants.common import STATES_MAP as STATES_MAP

class FrontlineEventBanner(StandardEventBanner):
    NAME = EPICBATTLES_ALIASES.EPIC_BATTLES_ENTRY_POINT
    __epicController: Any
    __eventsService: Any
    _state: Any
    _eventStartDate: Any
    _eventEndDate: Any
    _timerValue: Any
    _playAppearAnim: Any
    def __init__(self):
        ...
    @property
    def isMode(self):
        ...
    @property
    def hasRewards(self):
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
    def eventStartDate(self):
        ...
    @property
    def eventEndDate(self):
        ...
    @property
    def playAppearAnim(self):
        ...
    def createToolTipContent(self, event):
        ...
    def onClick(self):
        ...
    def onAppearAnimationPlayed(self):
        ...
    def prepare(self):
        ...
    def onAppear(self):
        ...
    def onDisappear(self):
        ...
    def __onUpdate(self, *_):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isEpicBattlesEntryPointAvailable(epicController=None):
    ...
