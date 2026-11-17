# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/platform/products_fetcher/subscriptions/subscription_descriptors.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_model import SubscriptionTypeEnum as SubscriptionTypeEnum
from gui.impl.gen.view_models.views.lobby.player_subscriptions.wot_subscription_model import WotSubscriptionStateEnum as WotSubscriptionStateEnum, WotTierEnum as WotTierEnum
from gui.platform.products_fetcher.product_descriptor import ProductDescriptor as ProductDescriptor
from helpers import dependency as dependency
from renewable_subscription_common.settings_constants import WotPlusState as WotPlusState, WotPlusTier as WotPlusTier
from skeletons.connection_mgr import IConnectionManager as IConnectionManager
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.offers import IOffersDataProvider as IOffersDataProvider
from skeletons.gui.server_events import IEventsCache as IEventsCache
from gui.server_events.event_items import Quest as Quest
__all__: tuple

class SubscriptionDescriptor(ProductDescriptor):
    _lobbyContext: Any
    _connectionMgr: Any
    _offerToken: Any
    def __init__(self, params):
        ...
    @property
    def type(self):
        ...
    @property
    def isSubscribed(self):
        ...
    @property
    def expirationTime(self):
        ...
    def hasDepotRewards(self):
        ...
    def isRewardsClaimed(self):
        ...
    def getOfferToken(self):
        ...
    def getOfferID(self):
        ...
    def _getEvents(self):
        ...
    def _onServerSettingsChange(self, *args, **kwargs):
        ...

class PrimeGamingDescriptor(SubscriptionDescriptor):
    __PRIME_GAMING_FILTER_STR = 'PrimeGaming'
    __eventsCache: Any
    __offersProvider: Any
    __primeGamingQuest: Any
    _offerToken: Any
    def __init__(self, params):
        ...
    @property
    def isSubscribed(self):
        ...
    @property
    def expirationTime(self):
        ...
    def hasDepotRewards(self):
        ...
    def isRewardsClaimed(self):
        ...
    def getPrimeGamingQuest(self):
        ...
    def getOfferToken(self):
        ...
    def getOfferID(self):
        ...
    def _onServerSettingsChange(self, *args, **kwargs):
        ...
    def __twitchFilterFunc(self, q):
        ...

class WotPlusDescriptor(SubscriptionDescriptor):
    _wotPlusCtrl: Any
    _WOT_PLUS_COMMON_STATE_TO_UI: dict
    _WOT_PLUS_TIER_TO_UI: dict
    _SUBSCRIPTION_TYPE_TO_TIER: dict
    @property
    def type(self):
        ...
    @property
    def expirationTime(self):
        ...
    @property
    def state(self):
        ...
    @property
    def tier(self):
        ...
    @property
    def tierForUi(self):
        ...

class WotPlusProDescriptor(WotPlusDescriptor):
    @property
    def type(self):
        ...
