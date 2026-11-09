# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/events_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
import typing as typing
import operator as operator
import time as time
import BigWorld as BigWorld
from constants import EMAIL_CONFIRMATION_QUEST_ID as EMAIL_CONFIRMATION_QUEST_ID, EVENT_TYPE as EVENT_TYPE
from challenges_common import isChallengeQuest as isChallengeQuest
from customization_quests_common import deserializeToken as deserializeToken, validateToken as validateToken
from gui import makeHtmlString as makeHtmlString
from gui.Scaleform.genConsts.MISSIONS_STATES import MISSIONS_STATES as MISSIONS_STATES
from gui.Scaleform.locale.MENU import MENU as MENU
from gui.Scaleform.locale.QUESTS import QUESTS as QUESTS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS as RES_ICONS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events import formatters as formatters
from gui.server_events.finders import FINAL_PT_TOKEN_PREFIX as FINAL_PT_TOKEN_PREFIX, NO_AWARD_LIST_HONOR_POSTFIX as NO_AWARD_LIST_HONOR_POSTFIX, NO_AWARD_LIST_QUEST_PREFIXES as NO_AWARD_LIST_QUEST_PREFIXES, PT_TOKEN_PREFIX as PT_TOKEN_PREFIX, isPMNoAwardListMilestone as isPMNoAwardListMilestone, isPMPoints as isPMPoints, isPMQuestRegExp as isPMQuestRegExp
from gui.server_events.personal_missions_navigation import PersonalMissionsNavigation as PersonalMissionsNavigation
from gui.shared.gui_items.customization import C11nStyleProgressData as C11nStyleProgressData
from gui.shared.sort_key import SortKey as SortKey
from helpers import dependency as dependency, i18n as i18n, isPlayerAccount as isPlayerAccount, time_utils as time_utils
from shared_utils import CONST_CONTAINER as CONST_CONTAINER, findFirst as findFirst, first as first
from personal_missions import PM_BRANCH_TO_FREE_TOKEN_NAME as PM_BRANCH_TO_FREE_TOKEN_NAME, PMProgressKeys as PMProgressKeys
from skeletons.gui.customization import ICustomizationService as ICustomizationService
from skeletons.gui.game_control import IMarathonEventsController as IMarathonEventsController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.server_events.events_constants import BATTLE_MATTERS_QUEST_ID as BATTLE_MATTERS_QUEST_ID, MARATHON_GROUP_PREFIX as MARATHON_GROUP_PREFIX, PREMIUM_GROUP_PREFIX as PREMIUM_GROUP_PREFIX, DAILY_QUEST_ID_PREFIX as DAILY_QUEST_ID_PREFIX, RANKED_DAILY_GROUP_ID as RANKED_DAILY_GROUP_ID, RANKED_PLATFORM_GROUP_ID as RANKED_PLATFORM_GROUP_ID, BATTLE_ROYALE_GROUPS_ID as BATTLE_ROYALE_GROUPS_ID, EPIC_BATTLE_GROUPS_ID as EPIC_BATTLE_GROUPS_ID, MAPS_TRAINING_GROUPS_ID as MAPS_TRAINING_GROUPS_ID, MAPS_TRAINING_QUEST_PREFIX as MAPS_TRAINING_QUEST_PREFIX, WEEKLY_QUEST_ID_PREFIX as WEEKLY_QUEST_ID_PREFIX, EPIC_QUEST_REWARD_ID as EPIC_QUEST_REWARD_ID
from helpers.i18n import makeString as _ms
from weekly_quests_common.weekly_quests_schema import weeklyQuestsSchema as weeklyQuestsSchema
from gui.server_events.event_items import Quest as Quest
FINISH_TIME_LEFT_TO_SHOW = time_utils.ONE_DAY
START_TIME_LIMIT: Any
AWARDS_PER_PAGE = 3
AWARDS_PER_SINGLE_PAGE = 5
_WQ_TOKEN_QUEST_ID_POS = 2
_WQ_TOKEN_ITEMS_POS: Any
_WQ_MAIN_SEPARATOR = '::'
_WQ_CONDITION_HEAD = 'c:'
_WQ_CONDITION_HEAD_LEN: Any

class EventInfoModel(object):
    NO_BONUS_COUNT = -1
    event: Any
    def __init__(self, event):
        ...
    def getTimerMsg(self, key=None):
        ...
    def _getStatus(self, pCur=None):
        ...
    @classmethod
    def _getTillTimeString(cls, timeValue):
        ...
    @classmethod
    def _getDailyProgressResetTimeUTC(cls):
        ...
    @classmethod
    def _getWeeklyProgressResetTimeUTC(cls):
        ...
    @classmethod
    def getDailyProgressResetTimeDelta(cls):
        ...
    def _getActiveDateTimeString(self):
        ...
    @classmethod
    def _getDateTimeString(cls, timeValue):
        ...

class QuestInfoModel(EventInfoModel):
    def _getActiveDateTimeString(self):
        ...
    def getTimerMsg(self, key='comeToEndInMinutes'):
        ...
    def _getDailyResetStatus(self, resetLabelKey, labeFormatter):
        ...
    def _getWeeklyResetStatus(self, resetLabelKey, labeFormatter):
        ...
    def _getCompleteDailyStatus(self, completeKey):
        ...
    def _getCompleteWeeklyStatus(self, completeKey):
        ...
    def _getCompleteKey(self):
        ...
    def _getCompleteWeeklyKey(self):
        ...

class EVENT_STATUS(CONST_CONTAINER):
    COMPLETED = 'done'
    NOT_AVAILABLE = 'notAvailable'
    WRONG_TIME = 'wrongTime'
    NONE = ''

class AwardSheetPresenter(object):
    __navigation: Any
    class Size(CONST_CONTAINER):
        TINY = 'tiny'
        SMALL = 'small'
        MID = 'mid'
        BIG = 'big'
        X_16 = 'x16'
    @classmethod
    def getIcon(cls, size, branch=None):
        ...
    @classmethod
    def getPawnedIcon(cls, branch=None):
        ...

class WeeklyQuestInfo(object):
    id: Any
    conditions: Any
    def __init__(self, token):
        ...
    def getMainConditionId(self):
        ...
    def getSpecialConditionIds(self):
        ...
    @staticmethod
    def _isCondition(token):
        ...
    @staticmethod
    def _getCondition(token):
        ...

class PremMissionsSortKey(SortKey):
    __slots__: tuple
    item: Any
    def __init__(self, item):
        ...
    def _cmp(self, other):
        ...

def getMinutesRoundByTime(timeLeft):
    ...
def missionsSortFunc(q):
    ...
def premMissionsSortFunc(a, b):
    ...
def dailyQuestsSortFunc(q):
    ...
def hasAnySavedProgresses(savedProgresses):
    ...
def questsSortFunc(q):
    ...
def getBoosterQuests():
    ...
def hasAtLeastOneAvailableQuest(quests):
    ...
def hasAtLeastOneCompletedQuest(quests):
    ...
def isAllQuestsCompleted(quests):
    ...
def isSuitableForPM(diff):
    ...
def getMarathonPrefix(eventID):
    ...
def isMarathon(eventID):
    ...
def isMapsTraining(groupID):
    ...
def isMapsTrainingQuest(eventID):
    ...
def isBattleMattersQuestID(questID):
    ...
def isPremium(eventID):
    ...
def isDailyEpicReward(eventID):
    ...
def isDailyEpic(eventID):
    ...
def isBattleRoyale(eventID):
    ...
def isRankedDaily(eventID):
    ...
def isRankedPlatform(eventID):
    ...
def isDailyQuest(eventID):
    ...
def isWeeklyQuest(eventID):
    ...
def isACEmailConfirmationQuest(eventID):
    ...
def isPMAdvancedOperationFinishedQuest(eventID):
    ...
def isRegularQuest(eventID, additionalCheckers):
    ...
def isCommonBattleQuest(event):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isC11nQuest(eventID, c11nService=None):
    ...
def getDataByC11nQuest(quest):
    ...
def parseC11nProgressToken(token):
    ...
def getIdxFromQuest(quest):
    ...
def getIdxFromQuestID(questID):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getLootboxesFromBonuses(bonuses, itemsCache=None):
    ...
def getTankmanRewardQuests():
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getPremiumGroup(eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getDailyEpicGroup(eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getDailyBattleRoyaleGroup(eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRankedDailyGroup(eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRankedPlatformGroup(eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isPremiumQuestsEnable(lobbyContext=None, eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isDailyQuestsEnable(lobbyContext=None, eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRerollTimeout(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isRerollEnabled(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isEpicQuestEnabled(lobbyContext=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isWeeklyQuestsEnable(lobbyContext=None, eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getWeeklyRerollTimeout(lobbyContext=None):
    ...
def getEventsData(eventsTypeName):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getC11nQuestsConfig(lobbyContext=None):
    ...
