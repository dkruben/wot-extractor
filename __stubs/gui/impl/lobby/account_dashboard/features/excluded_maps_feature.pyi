# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/excluded_maps_feature.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import ArenaType as ArenaType
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import PremiumConfigs as PremiumConfigs, PREMIUM_TYPE as PREMIUM_TYPE, EMPTY_GEOMETRY_ID as EMPTY_GEOMETRY_ID
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.game_control.wot_plus.utils import getExcludedMapsPromoData as getExcludedMapsPromoData
from gui.impl.gen.view_models.views.lobby.account_dashboard.map_model import MapModel as MapModel, SlotStateEnum as SlotStateEnum
from gui.impl.lobby.account_dashboard.features.base import FeatureItem as FeatureItem
from gui.impl.lobby.maps_blacklist.maps_blacklist_view import buildSlotsMap as buildSlotsMap
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showMapsBlacklistView as showMapsBlacklistView
from helpers import dependency as dependency, time_utils as time_utils
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from renewable_subscription_common.settings_constants import RS_TIER as RS_TIER
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from uilogging.wot_plus.loggers import WotPlusAccountDashboardWidgetLogger as WotPlusAccountDashboardWidgetLogger
from uilogging.wot_plus.logging_constants import AccountDashboardFeature as AccountDashboardFeature
from typing import Dict as Dict
from gui.impl.gen.view_models.views.lobby.account_dashboard.excluded_maps_model import ExcludedMapsModel as ExcludedMapsModel
_logger: Any

class ExcludedMapsFeature(FeatureItem):
    __itemsCache: Any
    __lobbyContext: Any
    __gameSession: Any
    __wotPlus: Any
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _fillModel(self, model):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def __onPreferredMapsChanged(self, _):
        ...
    def __onPremiumNotify(self, *_):
        ...
    def __onWotPlusChanged(self, data):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __update(self, model=None):
        ...
    @staticmethod
    def __onClick():
        ...
