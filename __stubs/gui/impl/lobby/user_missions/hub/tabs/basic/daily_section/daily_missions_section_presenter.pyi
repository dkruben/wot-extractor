# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/daily_section/daily_missions_section_presenter.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import PremiumConfigs as PremiumConfigs, DAILY_QUESTS_CONFIG as DAILY_QUESTS_CONFIG
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.daily_missions_section_model import DailyMissionsSectionModel as DailyMissionsSectionModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.reward_progress_block_model import RewardProgressTypes as RewardProgressTypes
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.tab_id import TabId as TabId
from gui.impl.lobby.missions.missions_helpers import isPremiumPlusAccount as isPremiumPlusAccount
from gui.impl.lobby.user_missions.hub.tabs.basic.daily_section.presenters.daily_missions_block_presenter import DailyMissionsBlockPresenter as DailyMissionsBlockPresenter
from gui.impl.lobby.user_missions.hub.tabs.basic.daily_section.presenters.premium_daily_missions_block_presenter import PremiumDailyMissionsBlockPresenter as PremiumDailyMissionsBlockPresenter
from gui.impl.lobby.user_missions.hub.tabs.basic.daily_section.presenters.reward_progress_block_presenter import RewardProgressBlockPresenter as RewardProgressBlockPresenter
from gui.impl.lobby.user_missions.hub.update_children_mixin import UpdateChildrenMixin as UpdateChildrenMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.server_events.events_helpers import isDailyQuestsEnable as isDailyQuestsEnable, isPremiumQuestsEnable as isPremiumQuestsEnable
from gui.shared import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import UserMissionsEvent as UserMissionsEvent
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
TAB_ID = TabId.BASIC

# base nao representavel no stub: ViewComponent[...]
class DailyMissionsSectionPresenter(UpdateChildrenMixin):
    LAYOUT_ID: Any
    eventsCache: Any
    itemsCache: Any
    lobbyContext: Any
    _premiumDailyMissionsChild: Any
    _targetQuestId: Any
    _rewardProgressChild: Any
    def __init__(self, targetQuestId=''):
        ...
    @property
    def viewModel(self):
        ...
    def _getListeners(self):
        ...
    def _getEvents(self):
        ...
    def _getChildComponents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __addRewardProgressChild(self):
        ...
    def __updateModel(self):
        ...
    def __onServerSettingsChanged(self, diff=None):
        ...
    def __onTabChange(self, ume):
        ...
