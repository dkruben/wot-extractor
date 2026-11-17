# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/premium_account_feature.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from constants import PREMIUM_TYPE as PREMIUM_TYPE
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPremiumUrl as getBuyPremiumUrl
from gui.impl.lobby.account_dashboard.features.base import FeatureItem as FeatureItem
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.shared.event_dispatcher import showShop as showShop
from helpers import dependency as dependency, time_utils as time_utils
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.impl.gen.view_models.views.lobby.account_dashboard.premium_account_model import PremiumAccountModel as PremiumAccountModel

class PremiumAccountFeature(FeatureItem):
    __slots__: tuple
    __itemsCache: Any
    __lobbyContext: Any
    __gameSession: Any
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
    def __onSettingsChange(self, diff):
        ...
    def __onStatsChanged(self, *_):
        ...
    def __onPremiumStatusChanged(self, *_):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __setPremBonusValues(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updatePremState(self, model=None):
        ...
    def __getTimeLeft(self, premType):
        ...
    def __getStatsRequester(self):
        ...
    @staticmethod
    def __toPercents(value):
        ...
    @staticmethod
    def __onClick():
        ...
