# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/reserve_stock_feature.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import PREMIUM_TYPE as PREMIUM_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.game_control.wot_plus.utils import getMaxGoldReserveCapacityFromAllTiers as getMaxGoldReserveCapacityFromAllTiers
from gui.impl.lobby.account_dashboard.features.base import FeatureItem as FeatureItem
from gui.impl.lobby.premacc.premacc_helpers import PiggyBankConstants as PiggyBankConstants, getOpenTimeHelper as getOpenTimeHelper
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showPiggyBankView as showPiggyBankView
from helpers import dependency as dependency
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from renewable_subscription_common.settings_constants import RS_TIER as RS_TIER
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.wot_plus.loggers import WotPlusAccountDashboardWidgetLogger as WotPlusAccountDashboardWidgetLogger
from uilogging.wot_plus.logging_constants import AccountDashboardFeature as AccountDashboardFeature
from typing import Dict as Dict
from gui.impl.gen.view_models.views.lobby.account_dashboard.reserve_stock_model import ReserveStockModel as ReserveStockModel

class ReserveStockFeature(FeatureItem):
    _itemsCache: Any
    _lobbyContext: Any
    _gameSession: Any
    _wotPlus: Any
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _fillModel(self, model):
        ...
    def _updateCredits(self, credits=None):
        ...
    def _updateGold(self, gold=None):
        ...
    def _onPremiumNotify(self, *_):
        ...
    def _onWotPlusChanged(self, data):
        ...
    def _updateLastSmashTimestamp(self, _):
        ...
    def _onPiggyBankChanged(self, _):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    # decorador original: @replaceNoneKwargsModel
    def _update(self, credits=None, gold=None, model=None):
        ...
    def __onClick(self):
        ...
    def __isTankPremiumActive(self):
        ...
    def __isWotPlusActive(self):
        ...
