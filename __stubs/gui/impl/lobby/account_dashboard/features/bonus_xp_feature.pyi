# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/bonus_xp_feature.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from PlayerEvents import g_playerEvents as g_playerEvents
from constants import PremiumConfigs as PremiumConfigs, PREMIUM_TYPE as PREMIUM_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.impl.lobby.account_dashboard.features.base import FeatureItem as FeatureItem
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showDailyExpPageView as showDailyExpPageView
from helpers import dependency as dependency
from renewable_subscription_common.schema import renewableSubscriptionsConfigSchema as renewableSubscriptionsConfigSchema
from renewable_subscription_common.settings_constants import RS_TIER as RS_TIER
from skeletons.gui.game_control import IGameSessionController as IGameSessionController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen.view_models.views.lobby.account_dashboard.bonus_xp_model import BonusXpModel as BonusXpModel

class BonusXPFeature(FeatureItem):
    __itemsCache: Any
    __lobbyContext: Any
    __gameSession: Any
    __wotPlusController: Any
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _fillModel(self, model):
        ...
    def __startListening(self):
        ...
    def __stopListening(self):
        ...
    def __onUpdate(self, *_):
        ...
    def _onServerSettingsChange(self, diff):
        ...
    def _onConfigModelUpdated(self, gpKey):
        ...
    def _onWotPlusChange(self, data):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateModel(self, model=None):
        ...
    def __onClick(self):
        ...
