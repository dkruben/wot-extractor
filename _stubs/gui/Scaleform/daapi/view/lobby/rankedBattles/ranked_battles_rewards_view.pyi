# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/rankedBattles/ranked_battles_rewards_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import RANKED_STYLED_VEHICLES_POOL as RANKED_STYLED_VEHICLES_POOL, RANKED_AWARDS_COUNTER as RANKED_AWARDS_COUNTER, RANKED_CURRENT_AWARDS_BUBBLE_YEAR_REACHED as RANKED_CURRENT_AWARDS_BUBBLE_YEAR_REACHED, RANKED_AWARDS_BUBBLE_YEAR_REACHED as RANKED_AWARDS_BUBBLE_YEAR_REACHED
from gui.Scaleform.daapi.view.lobby.rankedBattles.ranked_battles_page import IResetablePage as IResetablePage
from gui.Scaleform.daapi.view.meta.RankedBattlesRewardsLeaguesMeta import RankedBattlesRewardsLeaguesMeta as RankedBattlesRewardsLeaguesMeta
from gui.Scaleform.daapi.view.meta.RankedBattlesRewardsMeta import RankedBattlesRewardsMeta as RankedBattlesRewardsMeta
from gui.Scaleform.daapi.view.meta.RankedBattlesRewardsRanksMeta import RankedBattlesRewardsRanksMeta as RankedBattlesRewardsRanksMeta
from gui.Scaleform.daapi.view.meta.RankedBattlesRewardsYearMeta import RankedBattlesRewardsYearMeta as RankedBattlesRewardsYearMeta
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES as RANKEDBATTLES_ALIASES
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as _RBC
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles.constants import FINAL_QUEST_PATTERN as FINAL_QUEST_PATTERN, STANDARD_POINTS_COUNT as STANDARD_POINTS_COUNT, YEAR_AWARDS_ORDER as YEAR_AWARDS_ORDER
from gui.ranked_battles.ranked_builders import rewards_vos as rewards_vos
from gui.ranked_battles.ranked_formatters import getRankedAwardsFormatter as getRankedAwardsFormatter
from gui.ranked_battles.ranked_helpers import getDataFromFinalTokenQuestID as getDataFromFinalTokenQuestID
from gui.ranked_battles.ranked_helpers.sound_manager import AmbientType as AmbientType
from gui.shared.event_dispatcher import showStylePreview as showStylePreview, showRankedSelectableReward as showRankedSelectableReward
from gui.shared.formatters import text_styles as text_styles
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.shared.utils.scheduled_notifications import AcyclicNotifier as AcyclicNotifier
from helpers import dependency as dependency, time_utils as time_utils
from items import parseIntCompactDescr as parseIntCompactDescr
from items.vehicles import VehicleDescriptor as VehicleDescriptor, getVehicleType as getVehicleType
from shared_utils import findFirst as findFirst, first as first
from skeletons.gui.game_control import IRankedBattlesController as IRankedBattlesController
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.ranked_battles.ranked_builders import main_page_vos as main_page_vos
_logger: Any
_REWARDS_COMPONENTS: tuple
_DEFAULT_STYLED_VEHICLES: tuple

class RankedBattlesRewardsView(RankedBattlesRewardsMeta, IResetablePage):
    __rankedController: Any
    _selectedViewID: Any
    def __init__(self):
        ...
    def reset(self):
        ...
    def onTabChanged(self, viewId):
        ...
    def setActiveTab(self, linkage=None):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def _update(self):
        ...
    def _updateSounds(self):
        ...
    def _updateYearRewardCounters(self):
        ...
    def _updateCounters(self):
        ...

class RankedRewardsSeasonOffView(RankedBattlesRewardsView):
    __rankedController: Any
    def reset(self):
        ...
    def setActiveTab(self, linkage=None):
        ...
    def _update(self):
        ...
    def _updateSounds(self):
        ...

class RankedRewardsSeasonOnView(RankedBattlesRewardsView):
    __rankedController: Any
    def reset(self):
        ...
    def setActiveTab(self, linkage=None):
        ...
    def _updateSounds(self):
        ...
    def onTabChanged(self, viewId):
        ...

class RankedBattlesRewardsRanksView(RankedBattlesRewardsRanksMeta, IResetablePage):
    __rankedController: Any
    __selectedDivisionIdx: Any
    __bonusFormatter: Any
    def __init__(self):
        ...
    def onRequestData(self, index, iconSizeID, rewardsCount):
        ...
    def reset(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __getRankRewards(self, rank, iconSize):
        ...
    def __getDivisionsData(self):
        ...
    def __getSelectedDivision(self):
        ...
    def __getRewardsData(self, division, iconSize, rewardsCount):
        ...
    def __onUpdate(self, immediately=False):
        ...
    def __updateSounds(self):
        ...

class RankedBattlesRewardsLeaguesView(RankedBattlesRewardsLeaguesMeta, IResetablePage):
    __rankedController: Any
    __itemsCache: Any
    __styleDescriptions: Any
    def __init__(self):
        ...
    def onStyleClick(self, styleID):
        ...
    def reset(self):
        ...
    @classmethod
    def _backToLeaguesCallback(cls):
        ...
    def _populate(self):
        ...
    def __getLeaguesData(self):
        ...
    def __showStylePreview(self, styleID):
        ...

class RankedBattlesRewardsYearView(RankedBattlesRewardsYearMeta, IResetablePage):
    __eventsCache: Any
    __rankedController: Any
    __acyclicNotifier: Any
    def __init__(self):
        ...
    def reset(self):
        ...
    def onChooseRewardBtnClick(self):
        ...
    def _populate(self):
        ...
    def _dispose(self):
        ...
    def __update(self):
        ...
    def __getAwardingStatus(self, currentPoints):
        ...
    def __getAwardsData(self, points, rewardingComplete, isAwarded):
        ...
    def __getStandardFinalQuest(self):
        ...
    def __getTillUpdateTime(self):
        ...
