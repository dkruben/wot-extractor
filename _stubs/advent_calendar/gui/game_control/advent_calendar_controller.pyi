# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/game_control/advent_calendar_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import re as re
import Event as Event
from BWUtil import AsyncReturn as AsyncReturn
from adisp import adisp_process as adisp_process
from constants import SECONDS_IN_DAY as SECONDS_IN_DAY, Configs as Configs
from shared_utils import first as first, nextTick as nextTick
from wg_async import BrokenPromiseError as BrokenPromiseError, TimeoutError as TimeoutError, await_callback as await_callback, wg_async as wg_async
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from skeletons.gui.shared.utils import IHangarSpace as IHangarSpace
from advent_calendar.gui.feature.constants import ADVENT_CALENDAR_PROGRESSION_QUEST_PREFIX as ADVENT_CALENDAR_PROGRESSION_QUEST_PREFIX, ADVENT_CALENDAR_QUEST_POSTFIX as ADVENT_CALENDAR_QUEST_POSTFIX, ADVENT_CALENDAR_QUEST_PREFIX as ADVENT_CALENDAR_QUEST_PREFIX, ADVENT_CALENDAR_QUEST_RE_PATTERN as ADVENT_CALENDAR_QUEST_RE_PATTERN, ADVENT_CALENDAR_TOKEN as ADVENT_CALENDAR_TOKEN
from advent_calendar.gui.impl.lobby.feature.advent_helper import getProgressionRewardType as getProgressionRewardType, getQuestNeededTokensCount as getQuestNeededTokensCount
from advent_calendar.gui.impl.lobby.feature.bonus_grouper import AdventCalendarQuestsBonusGrouper as AdventCalendarQuestsBonusGrouper, QuestRewardsGroups as QuestRewardsGroups
from advent_calendar.helpers.server_settings import AdventCalendarConfig as AdventCalendarConfig
from advent_calendar.skeletons.game_controller import IAdventCalendarController as IAdventCalendarController
from advent_calendar_common.advent_calendar_constants import GAME_PARAMS_KEY as GAME_PARAMS_KEY
from gui import SystemMessages as SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager as g_clientUpdateManager
from gui.SystemMessages import SM_TYPE as SM_TYPE
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.bonuses import LootBoxTokensBonus as LootBoxTokensBonus
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.utils.scheduled_notifications import SimpleNotifier as SimpleNotifier
from helpers import dependency as dependency, time_utils as time_utils
from helpers.server_settings import LootBoxesTooltipConfig as LootBoxesTooltipConfig
_logger: Any
_TRACKING_CONFIGS: tuple
OPEN_DOOR_COMPLETED_TIMEOUT = 5

class AdventCalendarController(IAdventCalendarController):
    __lobbyContext: Any
    __itemsCache: Any
    __eventsCache: Any
    __hangarSpace: Any
    __em: Any
    onConfigChanged: Any
    onDoorsStateChanged: Any
    onDoorOpened: Any
    onLootBoxesConfigChanged: Any
    __doorChangingNotifier: Any
    __phaseChangedNotifier: Any
    __awaitedQuestId: Any
    __completedAwardsQuests: Any
    __progressionRewardsQuestsOrdered: Any
    __isEnabledPrev: Any
    def __init__(self):
        ...
    @property
    def isActive(self):
        ...
    @property
    def isEnabled(self):
        ...
    @property
    def startDate(self):
        ...
    @property
    def postEventStartDate(self):
        ...
    @property
    def postEventEndDate(self):
        ...
    @property
    def getCurrentTime(self):
        ...
    @property
    def completedAwardsQuests(self):
        ...
    @property
    def progressionRewardQuestsOrdered(self):
        ...
    @property
    def config(self):
        ...
    @property
    def lootBoxesTooltipConfig(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onDisconnected(self):
        ...
    def fini(self):
        ...
    def isInActivePhase(self):
        ...
    def isAvailableAndActivePhase(self):
        ...
    def isAvailableAndPostActivePhase(self):
        ...
    def isAvailable(self):
        ...
    def isInPostActivePhase(self):
        ...
    def isFirstEventDay(self):
        ...
    def getCurrentDayNumber(self):
        ...
    def getDoorOpenTimeUI(self, doorId):
        ...
    def getDoorOpenTokenName(self, day=1):
        ...
    def getDoorOpenQuestName(self, day=1):
        ...
    def progressionQuestMayBeCompleted(self, openedDoorsAmount=None):
        ...
    # decorador original: @wg_async
    def awaitDoorOpenQuestCompletion(self, dayID, currency):
        ...
    def isDoorOpened(self, dayID):
        ...
    def getQuestByDayId(self, dayId):
        ...
    def getAdventCalendarGroupedQuestsRewards(self):
        ...
    def getRewardsLootBox(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def __isEnableChanged(self):
        ...
    def __update(self):
        ...
    def __getTimeToNextDoor(self):
        ...
    def __onNotifyDoorChanged(self):
        ...
    def __onConfigChanged(self):
        ...
    @staticmethod
    def __filterFunc(quest):
        ...
    def __onDoorSuccessfulOpened(self):
        ...
    def __onTokensUpdate(self, diff):
        ...
    def __getProgressionRewardQuestsOrdered(self):
        ...
    def __startNotifiers(self):
        ...
    def __getTimeTillPhaseChange(self):
        ...
    # decorador original: @nextTick
    def __onEventsCacheSynced(self, *args, **kwargs):
        ...
    # decorador original: @adisp_process
    def __openAdventCalendarDoor(self, dayID, currency, callback=None):
        ...
