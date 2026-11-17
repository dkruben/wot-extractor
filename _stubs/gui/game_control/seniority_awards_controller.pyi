# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/game_control/seniority_awards_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import re as re
from enum import Enum as Enum
from future.utils import viewitems as viewitems
from typing import TYPE_CHECKING as TYPE_CHECKING
import BigWorld as BigWorld
import Event as Event
from constants import Configs as Configs
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.items_cache import CACHE_SYNC_REASON as CACHE_SYNC_REASON
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from helpers import dependency as dependency, time_utils as time_utils
from helpers.server_settings import SeniorityAwardsConfig as SeniorityAwardsConfig
from skeletons.gui.game_control import ISeniorityAwardsController as ISeniorityAwardsController, IHangarLoadingController as IHangarLoadingController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from gui.server_events.event_items import Quest as Quest
from typing import Dict as Dict, Iterable as Iterable, Optional as Optional
REG_EXP_QUEST_YEAR_TIER = ':([Y, y]\\d+):'
REG_EXP_QUEST_TEST_GROUP = ':([A,a,B,b][T,t])'
WDR_CURRENCY = 'wdrcoin'
CLAIM_REWARD_TIMEOUT = 20
SELECT_REWARD_TIMEOUT = 20
NEWBIE_REWARD_BATTLES_COUNT = 15
NEWBIE_BULLET_BATTLES_COUNT = 4
_logger: Any

class VehicleSelectionState(Enum):
    RECIEVED = 0
    SELECTION_FAILED = 1
    HAS_CLIENT_TOKENS = 2

class VehiclesForSelectionState(Enum):
    STATE_CHANGED = 0
    VEHICLES_CHANGED = 1

class SeniorityAwardsController(ISeniorityAwardsController):
    __lobbyContext: Any
    __itemsCache: Any
    __hangarSpace: Any
    __eventsCache: Any
    __hangarLoadingController: Any
    __em: Any
    onUpdated: Any
    onVehicleSelectionChanged: Any
    onQuestsReceived: Any
    __claimTimeoutId: Any
    __years: Any
    __yearTier: Any
    __rewardCategory: Any
    __testGroup: Any
    __seniorityAwardsCompletedQuests: Any
    __vehiclesForSelection: Any
    __endTimestamp: Any
    __clockOnNotification: Any
    def __init__(self):
        ...
    @property
    def config(self):
        ...
    @property
    def isEnabled(self):
        ...
    @property
    def isActive(self):
        ...
    @property
    def isAvailable(self):
        ...
    @property
    def timeLeft(self):
        ...
    @property
    def endTime(self):
        ...
    @property
    def isVehicleSelectionAvailable(self):
        ...
    @property
    def yearsInGame(self):
        ...
    @property
    def getVehiclesForSelectionCount(self):
        ...
    @property
    def isRewardReceived(self):
        ...
    @property
    def seniorityQuestPrefix(self):
        ...
    @property
    def vehicleSelectionQuestPattern(self):
        ...
    @property
    def vehicleSelectionQuestPrefix(self):
        ...
    @property
    def vehicleSelectionToken(self):
        ...
    @property
    def categories(self):
        ...
    @property
    def maxCategory(self):
        ...
    @property
    def showRewardHangarNotification(self):
        ...
    @property
    def showRewardNotification(self):
        ...
    @property
    def isEligibleToReward(self):
        ...
    @property
    def isNeedToShowRewardNotification(self):
        ...
    @property
    def isNeedToShowNotificationBullet(self):
        ...
    @property
    def clockOnNotification(self):
        ...
    def getSACoin(self):
        ...
    @property
    def claimVehicleRewardTokenPattern(self):
        ...
    @property
    def pendingReminderTimestamp(self):
        ...
    @property
    def completedSeniorityAwardsQuests(self):
        ...
    @property
    def vehiclesForSelection(self):
        ...
    @property
    def rewardCategory(self):
        ...
    @property
    def testGroup(self):
        ...
    @property
    def yearTier(self):
        ...
    def isVehicleSelectionQuestCompleted(self, vehicleRewardId):
        ...
    def getVehicleSelectionRewards(self):
        ...
    def getAvailableVehicleSelectionRewards(self):
        ...
    def getVehicleSelectionQuestReward(self, vehicleRewardId):
        ...
    def claimReward(self):
        ...
    def markRewardReceived(self):
        ...
    @staticmethod
    def getSeniorityLevel(completedQuests, regexp):
        ...
    def onAccountBecomePlayer(self):
        ...
    def onAccountBecomeNonPlayer(self):
        ...
    def fini(self):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def __onHangarLoaded(self):
        ...
    def __clear(self):
        ...
    def __clearCachedValues(self):
        ...
    def __removeListeners(self):
        ...
    def __onTokensUpdate(self, diff):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __scheduleClaimTimeout(self):
        ...
    def __cancelClaimTimeout(self):
        ...
    def __onClaimRewardFailed(self):
        ...
    @staticmethod
    def __showWaiting():
        ...
    @staticmethod
    def __hideWaiting():
        ...
    def __update(self):
        ...
    def __filterFunc(self, quest):
        ...
    def __onEventsCacheSynced(self, *_, **__):
        ...
    def __hasClientTokens(self):
        ...
    def __onItemsCacheUpdated(self, reason, diff):
        ...
    def __onVehicleSelectionStateChanged(self):
        ...
