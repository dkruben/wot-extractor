# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/player_subscriptions/player_subscriptions_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
from constants import IS_CHINA as IS_CHINA
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui import GUI_SETTINGS as GUI_SETTINGS
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getWotPlusShopUrl as getWotPlusShopUrl, getWotPlusPro12ShopUrl as getWotPlusPro12ShopUrl, getWotPlusPro6ShopUrl as getWotPlusPro6ShopUrl
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.player_subscriptions.external_subscription_model import ExternalSubscriptionModel as ExternalSubscriptionModel
from gui.impl.gen.view_models.views.lobby.player_subscriptions.player_subscriptions_model import PlayerSubscriptionsModel as PlayerSubscriptionsModel
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_model import SubscriptionTypeEnum as SubscriptionTypeEnum
from gui.impl.gen.view_models.views.lobby.player_subscriptions.wot_subscription_model import WotPlusPeriodicityEnum as WotPlusPeriodicityEnum
from gui.impl.gen.view_models.views.lobby.player_subscriptions.wot_subscription_model import WotSubscriptionModel as WotSubscriptionModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.platform.products_fetcher.fetch_result import FetchResult as FetchResult
from gui.platform.products_fetcher.subscriptions.subscription_descriptors import WotPlusDescriptor as WotPlusDescriptor
from gui.shared.event_dispatcher import showOfferGiftsWindow as showOfferGiftsWindow, showBrowserOverlayView as showBrowserOverlayView, showShop as showShop, showWotPlusInfoPage as showWotPlusInfoPage, showWotPlusProductPage as showWotPlusProductPage, showWotPlusSteamSubscriptionManagementPage as showWotPlusSteamSubscriptionManagementPage
from helpers import dependency as dependency
from renewable_subscription_common.settings_constants import RS_TIER as RS_TIER, WotPlusTier as WotPlusTier
from skeletons.gui.game_control import IExternalLinksController as IExternalLinksController, ISteamCompletionController as ISteamCompletionController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.platform.product_fetch_controller import ISubscriptionProductsFetchController as ISubscriptionProductsFetchController
from uilogging.wot_plus.loggers import WotPlusSubscriptionViewLogger as WotPlusSubscriptionViewLogger
from uilogging.wot_plus.logging_constants import WotPlusInfoPageSource as WotPlusInfoPageSource, SubscriptionPageKeys as SubscriptionPageKeys
from wg_async import wg_await as wg_await, wg_async as wg_async
from typing import Optional as Optional, Dict as Dict, Any as Any, List as List, Union as Union
from gui.game_control.wot_plus_controller import WotPlusController as WotPlusController
from gui.platform.products_fetcher.subscriptions.subscription_descriptors import SubscriptionDescriptor as SubscriptionDescriptor
from gui.platform.products_fetcher import SubscriptionProductsFetchController as SubscriptionProductsFetchController
from gui.impl.gen.view_models.views.lobby.player_subscriptions.subscription_model import SubscriptionModel as SubscriptionModel
from gui.platform.products_fetcher.subscriptions.subscription_descriptors import WotPlusProDescriptor as WotPlusProDescriptor
_logger: _Any
_SUBSCRIPTION_TYPE_FACTORIES: dict

class BaseSubscriptionModelFactory(object):
    def type(self):
        ...
    def fill(self, subscriptionDescr):
        ...

class ExternalSubscriptionModelFactory(BaseSubscriptionModelFactory):
    def type(self):
        ...
    def fill(self, subscriptionDescr):
        ...

class WotPlusCoreSubscriptionModelFactory(BaseSubscriptionModelFactory):
    _steamCompletionCtrl: _Any
    def type(self):
        ...
    def fill(self, subscriptionDescr):
        ...

class WotPlusProSubscriptionModelFactory(WotPlusCoreSubscriptionModelFactory):
    _wotPlusCtrl: _Any
    def fill(self, subscriptionDescr):
        ...

class PlayerSubscriptionsView(ViewImpl):
    _subscriptionProductsFetchController: _Any
    _externalBrowser: _Any
    _lobbyContext: _Any
    _steamCompletionCtrl: _Any
    _wotPlusCtrl: _Any
    __slots__: tuple
    __subscriptionsFetchResult: _Any
    __subscriptions: _Any
    _wotPlusUILogger: _Any
    def __init__(self, layoutID=...):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    # decorador original: @wg_async
    def __fetchExternalSubs(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onWotPlusStatusChanged(self, args):
        ...
    def __updateViewModel(self):
        ...
    def __getSortedProducts(self, products):
        ...
    def __onBackClick(self):
        ...
    def __onCardClick(self, args):
        ...
    def __onButtonClick(self, args):
        ...
    def __onWotPlusButtonClick(self, isCoreSubRequested):
        ...
    def __showWotPlusPageForSubscriber(self, isCoreSubRequested):
        ...
    def __showWotPlusShopForNonSubscriber(self, isCoreSubRequested):
        ...
    def __onExternalSubscriptionButtonClick(self, id_):
        ...
    def __onServerSettingsChange(self, *args, **kwargs):
        ...
    def isSubscriptionProductAvailable(self, subscription):
        ...

def _isWotPlus(subscriptionType):
    ...
