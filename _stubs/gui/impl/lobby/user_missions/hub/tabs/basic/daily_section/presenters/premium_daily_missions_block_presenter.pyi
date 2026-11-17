# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/presenters/premium_daily_missions_block_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PremiumConfigs as PremiumConfigs
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getBuyPremiumUrl as getBuyPremiumUrl
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.premium_daily.premium_daily_mission_model import PremiumDailyMissionModel as PremiumDailyMissionModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.premium_daily.premium_daily_missions_block_model import PremiumDailyMissionsBlockModel as PremiumDailyMissionsBlockModel
from gui.impl.lobby.missions.missions_helpers import isPremiumPlusAccount as isPremiumPlusAccount, markQuestProgressAsViewed as markQuestProgressAsViewed
from gui.impl.lobby.missions.missions_helpers import needToUpdateQuestsInModelByIds as needToUpdateQuestsInModelByIds
from gui.impl.lobby.user_missions.hub.tabs.basic.daily_section.presenters.base_missions_block_presenter import BaseMissionsBlockPresenter as BaseMissionsBlockPresenter
from gui.server_events.events_helpers import isPremiumQuestsEnable as isPremiumQuestsEnable, PremMissionsSortKey as PremMissionsSortKey
from gui.server_events.settings import visitEventsGUI as visitEventsGUI
from gui.shared.event_dispatcher import showShop as showShop
from helpers import dependency as dependency
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache

# base nao representavel no stub: BaseMissionsBlockPresenter[...]
class PremiumDailyMissionsBlockPresenter:
    eventsCache: Any
    gameSession: Any
    lobbyContext: Any
    _isBlockEnabled: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _markQuestsAsVisited(self):
        ...
    def _onSyncCompleted(self, *_):
        ...
    def _getEvents(self):
        ...
    def _updateModel(self, model):
        ...
    def _onServerSettingsChanged(self, diff=None):
        ...
    def _onPremiumTypeChanged(self, *_):
        ...
    def __onBuyPremiumBtn(self, *args):
        ...
