# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/account_dashboard/features/premium_quests_feature.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from Event import Event as Event
from constants import PremiumConfigs as PremiumConfigs, PREMIUM_TYPE as PREMIUM_TYPE
from gui.impl.gen.view_models.views.lobby.account_dashboard.premium_quests_model import PremiumQuestsModel as PremiumQuestsModel
from gui.impl.lobby.account_dashboard.features.base import FeatureItem as FeatureItem
from gui.impl.lobby.user_missions.hub.hub_view import DailyTabs as DailyTabs
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.server_events.events_dispatcher import showDailyQuests as showDailyQuests
from gui.server_events.events_helpers import isPremiumQuestsEnable as isPremiumQuestsEnable, premMissionsSortFunc as premMissionsSortFunc
from helpers import dependency as dependency
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache

class PremQuestsController(object):
    eventsCache: Any
    gameSession: Any
    onPremiumQuestsStageChange: Any
    _completedQuestsCount: Any
    def __init__(self):
        ...
    def getCompletedQuestsCount(self):
        ...
    def initialise(self):
        ...
    def finalize(self):
        ...
    def update(self, *args):
        ...

class PremiumQuestsFeature(FeatureItem):
    NO_PREMIUM = -1
    _itemsCache: Any
    _lobbyContext: Any
    _gameSession: Any
    _questController: Any
    def __init__(self, viewModel):
        ...
    def initialize(self, *args, **kwargs):
        ...
    def finalize(self):
        ...
    def _fillModel(self, model):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateModel(self, model=None):
        ...
    def __onPremiumChange(self, *_):
        ...
    def __onServerSettingsChange(self, diff=None):
        ...
    @staticmethod
    def onClick():
        ...
