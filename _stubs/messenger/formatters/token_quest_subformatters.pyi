# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/formatters/token_quest_subformatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import re as re
import typing as typing
from builtins import range as range
from itertools import chain as chain
from future.utils import viewitems as viewitems
import constants as constants
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from shared_utils import first as first
from helpers import dependency as dependency, time_utils as time_utils
from account_helpers import AccountSettings as AccountSettings
from account_helpers.AccountSettings import RANKED_YEAR_POSITION as RANKED_YEAR_POSITION
from chat_shared import SYS_MESSAGE_TYPE as SYS_MESSAGE_TYPE
from dossiers2.custom.records import DB_ID_TO_RECORD as DB_ID_TO_RECORD, RECORD_DB_IDS as RECORD_DB_IDS
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK, BADGES_BLOCK as BADGES_BLOCK
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.ranked_battles import ranked_helpers as ranked_helpers
from gui.ranked_battles.constants import YEAR_POINTS_TOKEN as YEAR_POINTS_TOKEN, RankedDossierKeys as RankedDossierKeys
from gui.ranked_battles.ranked_helpers.web_season_provider import TOP_LEAGUE_ID as TOP_LEAGUE_ID, UNDEFINED_LEAGUE_ID as UNDEFINED_LEAGUE_ID
from gui.server_events.bonuses import getBonuses as getBonuses, getMergedBonusesFromDicts as getMergedBonusesFromDicts
from gui.server_events.events_helpers import getIdxFromQuestID as getIdxFromQuestID, isACEmailConfirmationQuest as isACEmailConfirmationQuest
from gui.server_events.recruit_helper import getSourceIdFromQuest as getSourceIdFromQuest
from gui.shared.formatters import text_styles as text_styles
from gui.shared.notifications import NotificationPriorityLevel as NotificationPriorityLevel
from gui.shared.money import Currency as Currency
from messenger import g_settings as g_settings
from messenger.formatters import TimeFormatter as TimeFormatter
from messenger.formatters.service_channel import BattleMattersQuestAchievesFormatter as BattleMattersQuestAchievesFormatter, BattlePassQuestAchievesFormatter as BattlePassQuestAchievesFormatter, CollectionsFormatter as CollectionsFormatter, InvoiceReceivedFormatter as InvoiceReceivedFormatter, QuestAchievesFormatter as QuestAchievesFormatter, RankedQuestAchievesFormatter as RankedQuestAchievesFormatter, SeniorityAwardsQuestAchievesFormatter as SeniorityAwardsQuestAchievesFormatter, ServiceChannelFormatter as ServiceChannelFormatter, WaitItemsSyncFormatter as WaitItemsSyncFormatter, WinbackQuestAchievesFormatter as WinbackQuestAchievesFormatter
from messenger.formatters.service_channel_helpers import EOL as EOL, MessageData as MessageData, getCustomizationItemData as getCustomizationItemData, getRewardsForQuests as getRewardsForQuests, popCollectionEntitlements as popCollectionEntitlements
from messenger.proto.bw.wrappers import ServiceChannelMessage as ServiceChannelMessage
from skeletons.gui.battle_matters import IBattleMattersController as IBattleMattersController
from skeletons.gui.game_control import ICollectionsSystemController as ICollectionsSystemController, IRankedBattlesController as IRankedBattlesController, ISeniorityAwardsController as ISeniorityAwardsController, IWinbackController as IWinbackController, IWotPlusController as IWotPlusController
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.system_messages import ISystemMessages as ISystemMessages
_logger: Any

class ITokenQuestsSubFormatter(object):
    def getPopUps(self, message):
        ...
    @classmethod
    def getQuestOfThisGroup(cls, questIDs):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def _getDossierPopUps(self, dossierData, popUpRecords):
        ...

class TokenQuestsSubFormatter(ITokenQuestsSubFormatter):
    def getPopUps(self, message):
        ...
    def _getDossierPopUps(self, dossierData, popUpRecords):
        ...
    @classmethod
    def getQuestOfThisGroup(cls, questIDs):
        ...

class AsyncTokenQuestsSubFormatter(WaitItemsSyncFormatter, TokenQuestsSubFormatter):
    _achievesFormatter: Any
    def __init__(self):
        ...

class SyncTokenQuestsSubFormatter(ServiceChannelFormatter, TokenQuestsSubFormatter):
    _achievesFormatter: Any
    def __init__(self):
        ...

class RecruitQuestsFormatter(AsyncTokenQuestsSubFormatter):
    __eventsCache: Any
    __TEMPLATE_NAME = 'goldDataInvoiceReceived'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...

class RankedTokenQuestFormatter(AsyncTokenQuestsSubFormatter):
    _achievesFormatter: Any
    def __init__(self):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...

class RankedSeasonTokenQuestFormatter(RankedTokenQuestFormatter):
    __rankedController: Any
    __eventsCache: Any
    __R_NOTIFICATIONS = R.strings.system_messages.ranked.notifications
    __seasonAwardsFormatters: tuple
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def getPopUps(self, message):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __getRankedTokens(self, quest):
        ...
    def __packSeasonExtra(self, data):
        ...
    def __processBadges(self, data):
        ...
    def __processStyles(self, data):
        ...
    def __formatTokenQuests(self, completedQuestIDs, data):
        ...
    def __formatSeasonProgress(self, season, league, isSprinter, data):
        ...
    def __getTokensForLeague(self, tokens):
        ...
    def __packSeasonAwards(self, awardsDict):
        ...

class RankedFinalTokenQuestFormatter(RankedTokenQuestFormatter):
    __rankedController: Any
    __MESSAGE_TEMPLATE_NAME = 'RankedFinalYearAwardQuest'
    __MESSAGE_TEMPLATE_WITHOUT_AWARDS_NAME = 'RankedFinalYearWithoutAwardQuest'
    __HTML_POINTS_TEMPLATE = 'rankedFinalYearPoints'
    __HTML_COMPENSATION_TEMPLATE = 'rankedFinalYearCompensation'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def getPopUps(self, message):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __generatePointsTemplate(self, points, questData):
        ...

class SeniorityAwardsFormatter(AsyncTokenQuestsSubFormatter):
    _MESSAGE_TEMPLATE = 'SeniorityAwardsQuest'
    _MESSAGE_TEMPLATE_WITH_SELECTION = 'SeniorityAwardsQuestWithSelection'
    _seniorityAwardCtrl: Any
    _achievesFormatter: Any
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def _buildMessage(self, rewards, message):
        ...

class SeniorityAwardsVehicleSelectedFormatter(SeniorityAwardsFormatter):
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def _buildMessage(self, rewards, message):
        ...

class BattleMattersAwardsFormatterBase(ServiceChannelFormatter, TokenQuestsSubFormatter):
    __battleMattersController: Any
    __MESSAGE_TEMPLATE = 'BattleMatters{}'
    __TOKEN_TYPE = 'TokenQuest'
    __AWARD_TYPE = 'AwardsQuest'
    _achievesFormatter: Any
    def __init__(self):
        ...
    def _format(self, message, *args):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __buildMessage(self, questID, message):
        ...

class BattleMattersAwardsFormatter(AsyncTokenQuestsSubFormatter, BattleMattersAwardsFormatterBase):
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...

class BattleMattersClientAwardsFormatter(BattleMattersAwardsFormatterBase):
    def format(self, message, *args):
        ...

class LootBoxTokenQuestFormatter(AsyncTokenQuestsSubFormatter):
    __TEMPLATE_NAME = 'tokenQuestLootbox'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __getInvoiceFormatMessage(self, message):
        ...

class BattlePassDefaultAwardsFormatter(WaitItemsSyncFormatter, TokenQuestsSubFormatter):
    __MESSAGE_TEMPLATE = 'BattlePassDefaultRewardMessage'
    __COLLECTION_ITEMS_TEMPLATE = 'CollectionItemsSysMessage'
    __BATTLE_PASS_TOKEN_QUEST_PATTERN = 'battle_pass'
    __collectionsSystem: Any
    _achievesFormatter: Any
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __buildMessage(self, questID, message):
        ...
    def __makeCollectionMessage(self, entitlements, message):
        ...

class BattlePassAutoSelectRewardsFormatter(WaitItemsSyncFormatter, TokenQuestsSubFormatter):
    __MESSAGE_TEMPLATE = 'BattlePassDefaultRewardMessage'
    __BATTLE_PASS_AUTOSELECT_TOKEN_QUEST_PREFIX = 'bp_autoselect'
    _achievesFormatter: Any
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __buildMessage(self, questIDs, message):
        ...

class RankedYearLeaderFormatter(RankedTokenQuestFormatter):
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __formatFullMessage(self, yearPosition, rewardsData):
        ...
    def __formatShortMessage(self):
        ...

class WotPlusAttendanceRewardsFormatter(SyncTokenQuestsSubFormatter):
    __systemMessages: Any
    __wotPlusCtrl: Any
    __eventsCache: Any
    __lobbyContext: Any
    _STEP_PREFIX = 'step'
    _BIG_TEMPLATE = 'WotPlusAttendanceRewardsBig'
    _BIG_TEMPLATE_LVL_1 = 'WotPlusAttendanceRewardsBigLvl1'
    _SMALL_TEMPLATE = 'WotPlusAttendanceRewardsSmall'
    _STEP_DAILY_ATTENDANCE: Any
    _WOT_PLUS_CONST = constants.WoTPlusDailyAttendance
    def format(self, message, *args):
        ...
    def _collectDailyAttendanceBonuses(self, message):
        ...
    def __getSmallRewardData(self, formattedUiRewards):
        ...
    def __getBigRewardData(self, formattedUiRewards):
        ...
    def __getNotificationType(self, questID):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...

class WotPlusAttendanceRewardsFormatterTestSMViewer(WotPlusAttendanceRewardsFormatter):
    def _collectDailyAttendanceBonuses(self, message):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...

class WinbackRewardFormatterBase(ServiceChannelFormatter, TokenQuestsSubFormatter):
    __MESSAGE_TEMPLATE = 'Winback{}Award'
    __TOKEN_TYPE = 'SelectableToken'
    __AWARD_TYPE = 'Quest'
    __SIMPLE = 'Simple'
    _winbackController: Any
    _achievesFormatter: Any
    def __init__(self):
        ...
    def _format(self, message, *args):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __buildMessage(self, questID, message):
        ...

class WinbackRewardFormatter(AsyncTokenQuestsSubFormatter, WinbackRewardFormatterBase):
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...

class WinbackClientRewardFormatter(WinbackRewardFormatterBase):
    def format(self, message, *args):
        ...

class CrewPerksFormatter(AsyncTokenQuestsSubFormatter):
    __MESSAGE_TEMPLATE = 'SimpleGiftSysMessage'
    __QUEST_PREFIX = 'Crew22_'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...

class SteamCompletionFormatter(AsyncTokenQuestsSubFormatter):
    __MESSAGE_TEMPLATE = 'SteamEmailCompletionAward'
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __buildMessage(self, rewards, message):
        ...

class SkipNotificationFormatter(ServiceChannelFormatter, TokenQuestsSubFormatter):
    __NOTIFICATION_QUEST_POSTFIX = '_skip_notification'
    def format(self, message, *args):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
