# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/daily_experience/daily_experience_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import PREMIUM_TYPE as PREMIUM_TYPE, PremiumConfigs as PremiumConfigs
from frameworks.wulf import ViewSettings as ViewSettings, ViewFlags as ViewFlags
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPremiumUrl as getBuyPremiumUrl, getWotPlusShopUrl as getWotPlusShopUrl
from gui.game_control.wot_plus.utils import getAdditionalXPPromoData as getAdditionalXPPromoData
from gui.impl.gen.view_models.views.lobby.account_dashboard.daily_experience_view_model import DailyExperienceViewModel as DailyExperienceViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.event_dispatcher import showWotPlusInfoPage as showWotPlusInfoPage, showShop as showShop, showTankPremiumAboutPage as showTankPremiumAboutPage
from helpers import dependency as dependency
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from renewable_subscription_common.settings_constants import RS_TIER as RS_TIER
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.wot_plus.logging_constants import WotPlusInfoPageSource as WotPlusInfoPageSource
from gui.game_control.wot_plus_controller import WotPlusController as WotPlusController

class DailyExperienceView(ViewImpl):
    __itemsCache: Any
    __lobbyContext: Any
    __gameSession: Any
    __wotPlusController: Any
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def __updateViewModel(self):
        ...
    def _onPremiumNotify(self, *args):
        ...
    def _onStatsUpdated(self, *args):
        ...
    def _getEvents(self):
        ...
    def _getCallbacks(self):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def __onWotPlusChange(self, data):
        ...
    def __onClose(self):
        ...
    def __onWotPlusSubscribeBtnClick(self):
        ...
    def __onWotPremiumDetailsBtnClick(self):
        ...
    def __onWotPremiumUpgradeBtnClick(self):
        ...
    def __onWotPlusDetailsBtnClick(self):
        ...
