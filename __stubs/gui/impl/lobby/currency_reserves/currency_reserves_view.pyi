# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/currency_reserves/currency_reserves_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import logging as logging
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import PremiumConfigs as PremiumConfigs, PREMIUM_TYPE as PREMIUM_TYPE
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getWotPlusShopUrl as getWotPlusShopUrl, getBuyPremiumUrl as getBuyPremiumUrl
from gui.game_control.wot_plus.utils import getMaxGoldReserveCapacityFromAllTiers as getMaxGoldReserveCapacityFromAllTiers
from gui.impl.gen.view_models.views.lobby.currency_reserves.currency_reserve_model import CurrencyEnum as CurrencyEnum
from gui.impl.gen.view_models.views.lobby.currency_reserves.currency_reserves_view_model import CurrencyReservesViewModel as CurrencyReservesViewModel
from gui.impl.lobby.premacc.premacc_helpers import PiggyBankConstants as PiggyBankConstants, getDeltaTimeHelper as getDeltaTimeHelper
from gui.impl.pub import ViewImpl as ViewImpl
from gui.shared.event_dispatcher import showWotPlusInfoPage as showWotPlusInfoPage, showTankPremiumAboutPage as showTankPremiumAboutPage, showShop as showShop
from helpers import dependency as dependency
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from renewable_subscription_common.settings_constants import RS_TIER as RS_TIER
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.wot_plus.loggers import WotPlusReservesLogger as WotPlusReservesLogger
from uilogging.wot_plus.logging_constants import WotPlusInfoPageSource as WotPlusInfoPageSource, ReservesKeys as ReservesKeys
from typing import Dict as Dict, Any as Any
_logger: _Any

class CurrencyReservesView(ViewImpl):
    _itemsCache: _Any
    _gameSession: _Any
    _lobbyContext: _Any
    _wotPlusCtrl: _Any
    __slots__: tuple
    _creditReserveInfo: _Any
    _creditReserveConfig: _Any
    _serverSettings: _Any
    _wotPlusUILogger: _Any
    def __init__(self, layoutID):
        ...
    @property
    def viewModel(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _onPremiumNotify(self, *args):
        ...
    def _onLoading(self, highlightedComponentId=-1, makeTopView=False):
        ...
    def _onPiggyBankChanged(self, *args):
        ...
    def _updateTimeToOpen(self):
        ...
    def _updateCreditReserve(self):
        ...
    def _updateGoldReserve(self):
        ...
    def _onServerSettingsChange(self, diff):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def _onWotPlusDataChanged(self, data):
        ...
    def _onClose(self):
        ...
    def _isPremiumPlusActive(self):
        ...
    def _onGoldReserveInfoButtonClick(self):
        ...
    def _onGoldReserveActionButtonClick(self):
        ...
    def _onCreditReserveInfoButtonClick(self):
        ...
    def _onCreditReserveActionButtonClick(self):
        ...
