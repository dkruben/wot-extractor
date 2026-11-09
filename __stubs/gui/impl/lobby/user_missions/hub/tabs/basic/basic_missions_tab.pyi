# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hub/tabs/basic/basic_missions_tab.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from future.utils import listvalues as listvalues
from PlayerEvents import g_playerEvents as g_playerEvents
from config_schemas.umg_config import umgConfigSchema as umgConfigSchema
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getSuitableVehicles as getSuitableVehicles
from helpers import dependency as dependency
from gui.impl.gen import R as R
from personal_missions import PM_BRANCH as PM_BRANCH, PM_SWITCHES as PM_SWITCHES
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.server_events.events_helpers import isWeeklyQuestsEnable as isWeeklyQuestsEnable
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.basic_missions_tab_model import BasicMissionsTabModel as BasicMissionsTabModel
from gui.impl.lobby.user_missions.hub.tabs.basic.daily_section.daily_missions_section_presenter import DailyMissionsSectionPresenter as DailyMissionsSectionPresenter
from gui.impl.lobby.user_missions.hub.tabs.basic.weekly_missions import WeeklyMissions as WeeklyMissions
from gui.impl.lobby.user_missions.hub.update_children_mixin import UpdateChildrenMixin as UpdateChildrenMixin
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.lobby.user_missions.hub.tabs.basic.personal_missions_widget import PersonalMissionsWindgetPresenter as PersonalMissionsWindgetPresenter
from typing import Callable as Callable, Dict as Dict, List as List

# base nao representavel no stub: ViewComponent[...]
class BasicMissionsTab(UpdateChildrenMixin):
    LAYOUT_ID: Any
    eventsCache: Any
    itemsCache: Any
    lobbyContext: Any
    _targetQuestId: Any
    _hasSuitableVehicles: Any
    __personalMissions: Any
    __pmOperations: Any
    __activeCampaigns: Any
    def __init__(self, targetQuestId):
        ...
    @property
    def viewModel(self):
        ...
    def _finalize(self):
        ...
    def _getChildComponents(self):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _getCallbacks(self):
        ...
    def _getEvents(self):
        ...
    def _updateDailyBlockStatus(self):
        ...
    def __onServerSettingsChanged(self, diff=None):
        ...
    def __onConfigModelUpdated(self, gpKey):
        ...
    def __updatePersonalMissionSection(self):
        ...
    def __onCacheSyncCompleted(self, *_):
        ...
    def __onInventoryCacheSyncCompleted(self, reason, _):
        ...
    def __onVehiclesInventorySyncCompleted(self, _):
        ...
    def __isCampaignCompleted(self):
        ...
    def __isCampaignEnabled(self):
        ...
    def __isCampaignStarted(self):
        ...
    def __isCampaignActive(self, branchNames):
        ...
    def __isPMOperationDisabled(self):
        ...
