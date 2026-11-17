# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/subscriptions_feature.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PLAYER_SUBSCRIPTIONS_CONFIG as PLAYER_SUBSCRIPTIONS_CONFIG
from gui.impl.gen.view_models.views.lobby.account_dashboard.subscriptions_entry_point_model import SubscriptionsEntryPointModel as SubscriptionsEntryPointModel
from gui.impl.lobby.account_dashboard.features.base import FeatureItem as FeatureItem
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showSubscriptionsPage as showSubscriptionsPage
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from uilogging.wot_plus.loggers import WotPlusAccountDashboardWidgetLogger as WotPlusAccountDashboardWidgetLogger
from uilogging.wot_plus.logging_constants import AccountDashboardFeature as AccountDashboardFeature

class SubscriptionsFeature(FeatureItem):
    __lobbyContext: Any
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _fillModel(self, model):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __update(self, model=None):
        ...
    def __onServerSettingsChanged(self, diff):
        ...
    @staticmethod
    def __onClick():
        ...
