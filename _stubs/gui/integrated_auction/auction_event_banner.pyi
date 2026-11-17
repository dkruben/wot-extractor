# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/integrated_auction/auction_event_banner.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import INTEGRATED_AUCTION_FIRST_APPEARANCE_TIMESTAMP as INTEGRATED_AUCTION_FIRST_APPEARANCE_TIMESTAMP, INTEGRATED_AUCTION_INTRO_CLICK_TIMESTAMP as INTEGRATED_AUCTION_INTRO_CLICK_TIMESTAMP
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getIntegratedAuctionUrl as getIntegratedAuctionUrl
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.constants.event_banner_state import EventBannerState as EventBannerState
from gui.impl.lobby.user_missions.hangar_widget.event_banners.event_banners_container import EventBannersContainer as EventBannersContainer
from gui.impl.lobby.user_missions.hangar_widget.event_banners.standard_event_banner import StandardEventBanner as StandardEventBanner
from gui.impl.lobby.user_missions.hangar_widget.services import IEventsService as IEventsService
from gui.integrated_auction.constants import AUCTION_ENTRY_POINT_NAME as AUCTION_ENTRY_POINT_NAME
from gui.integrated_auction.tooltips.event_banner_tooltip import EventBannerTooltip as EventBannerTooltip
from gui.shared.event_dispatcher import showShop as showShop
from gui.shared.utils.scheduled_notifications import Notifiable as Notifiable, SimpleNotifier as SimpleNotifier
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime, getTimestampByStrDate as getTimestampByStrDate

class IntegratedAuctionEventBanner(Notifiable, StandardEventBanner):
    NAME = AUCTION_ENTRY_POINT_NAME
    __eventsService: Any
    __entry: Any
    __state: Any
    __timerValue: Any
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
    def timerValue(self):
        ...
    @property
    def playAppearAnim(self):
        ...
    @property
    def timerText(self):
        ...
    def createToolTipContent(self, event):
        ...
    def onClick(self):
        ...
    def onAppearAnimationPlayed(self):
        ...
    def prepare(self):
        ...
    def onDisappear(self):
        ...
    def __auctionStart(self):
        ...
    def __timeRemaining(self):
        ...
    def __getState(self):
        ...
    def __onUpdate(self, *_):
        ...
    def __getTimeToUpdate(self):
        ...

# decorador original: @dependency.replace_none_kwargs(...)
def isAuctionEventBannerAvailable(eventService=None):
    ...
