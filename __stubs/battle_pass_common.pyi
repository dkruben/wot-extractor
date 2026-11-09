# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/battle_pass_common.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import bisect as bisect
import struct as struct
import time as time
from collections import namedtuple as namedtuple
from future.utils import viewitems as viewitems, viewvalues as viewvalues
from past.builtins import xrange as xrange
import typing as typing
from enum import Enum as Enum, unique as unique
from battle_pass_integration import getBattlePassByGameMode as getBattlePassByGameMode
from constants import ARENA_BONUS_TYPE as ARENA_BONUS_TYPE, MAX_VEHICLE_LEVEL as MAX_VEHICLE_LEVEL, OFFER_TOKEN_PREFIX as OFFER_TOKEN_PREFIX
from debug_utils import LOG_ERROR as LOG_ERROR, LOG_CODEPOINT_WARNING as LOG_CODEPOINT_WARNING
from items import parseIntCompactDescr as parseIntCompactDescr, vehicles as vehicles
from optional_bonuses import BONUS_MERGERS as BONUS_MERGERS
from typing import Dict as Dict, Generator as Generator, Sequence as Sequence, Tuple as Tuple, Union as Union, List as List
BATTLE_PASS_TOKEN_PREFIX = 'battle_pass:'
BATTLE_PASS_TOKEN_PASS: Any
BATTLE_PASS_ENTITLEMENT_PASS: Any
BATTLE_PASS_SHOP_ENTITLEMENT_PASS = 'battle_pass_shop_'
BATTLE_PASS_OFFER_TOKEN_PREFIX: Any
BATTLE_PASS_Q_CHAIN_TOKEN_PREFIX: Any
BATTLE_PASS_RANDOM_QUEST_TOKEN_PREFIX: Any
BATTLE_PASS_TOKEN_TROPHY_OFFER: Any
BATTLE_PASS_TOKEN_TROPHY_GIFT_OFFER: Any
BATTLE_PASS_TOKEN_NEW_DEVICE_OFFER: Any
BATTLE_PASS_TOKEN_NEW_DEVICE_GIFT_OFFER: Any
BATTLE_PASS_TOKEN_MODERNIZED_DEVICE_OFFER: Any
BATTLE_PASS_TOKEN_MODERNIZED_DEVICE_GIFT_OFFER: Any
BATTLE_PASS_TOKEN_BATTLE_BOOSTER_OFFER: Any
BATTLE_PASS_TOKEN_BATTLE_BOOSTER_GIFT_OFFER: Any
BATTLE_PASS_TOKEN_BLUEPRINT_OFFER: Any
BATTLE_PASS_TOKEN_BLUEPRINT_GIFT_OFFER: Any
BATTLE_PASS_TOKEN_BROCHURE_OFFER: Any
BATTLE_PASS_TOKEN_BROCHURE_GIFT_OFFER: Any
BATTLE_PASS_TOKEN_GUIDE_OFFER: Any
BATTLE_PASS_TOKEN_GUIDE_GIFT_OFFER: Any
BATTLE_PASS_TOKEN_CREW_BOOK_OFFER: Any
BATTLE_PASS_TOKEN_CREW_BOOK_GIFT_OFFER: Any
BATTLE_PASS_TOKEN_3D_STYLE: Any
BATTLE_PASS_RANDOM_QUEST_ID_PREFIX = 'battle_pass_random'
BATTLE_PASS_CHOICE_REWARD_OFFER_TOKENS: tuple
BATTLE_PASS_CHOICE_REWARD_OFFER_GIFT_TOKENS: tuple
BATTLE_PASS_CHOICE_REWARD_OFFER_TOKEN_FREE_POSTFIX = 'free:'
BATTLE_PASS_CHOICE_REWARD_OFFER_TOKEN_PAID_POSTFIX = 'paid:'
BATTLE_PASS_PDATA_KEY = 'battlePass'
BATTLE_PASS_CONFIG_NAME = 'battlePass_config'
BATTLE_PASS_SELECT_BONUS_NAME = 'battlePassSelectToken'
BATTLE_PASS_STYLE_PROGRESS_BONUS_NAME = 'styleProgressToken'
BATTLE_PASS_Q_CHAIN_BONUS_NAME = 'battlePassQuestChainToken'
BATTLE_PASS_RANDOM_QUEST_BONUS_NAME = 'randomQuestToken'
NON_VEH_CD = 0
NON_CHAPTER_ID = 0
MAX_NON_CHAPTER_POINTS = 1000000
MAX_POST_PROGRESSION_POINTS = 1000000
MAX_POST_PROGRESSION_LEVEL = 10000
BATTLE_PASS_TOKEN_LIFETIME = 4320
HOLIDAY_SEASON_OFFSET = 1000
STARTER_PACK_LOGGING_PARTNER_ID = 19
BATTLE_PASS_COST_CURRENCIES: set
BP_TANKMEN_ENTITLEMENT_TAG_PREFIX = 'tankmen_bp'
BATTLE_PASS_TICKETS_EVENT = 'battlePass'
BATTLE_PASS_CATEGORY_PATH = '/battlepass/battlepass/'
MASK_TO_REWARD: dict

class BattlePassTankmenSource(object):
    PROGRESSION = 'progression'
    SHOP = 'shop'
    ALL: tuple

# decorador original: @unique
class FinalReward(str, Enum):
    BATTLE_QUEST = 'battleQuest'
    PROGRESSIVE_STYLE = 'progressiveStyle'
    STYLE = 'style'
    TANKMAN = 'tankman'
    VEHICLE = 'vehicle'
    ATTACHMENTS_SET = 'attachments_set'

# decorador original: @unique
class CurrencyBP(Enum):
    BIT = 'bpbit'
    TALER = 'bptaler'

class BattlePassRewardReason(object):
    DEFAULT = 0
    BATTLE = 1
    PURCHASE_BATTLE_PASS = 2
    PURCHASE_BATTLE_PASS_LEVELS = 3
    INVOICE = 4
    STYLE_UPGRADE = 5
    SELECT_REWARD = 6
    PURCHASE_BATTLE_PASS_MULTIPLE = 7
    SELECT_CHAPTER = 8
    PURCHASE_BATTLE_PASS_WITH_LEVELS = 9
    PURCHASE_REASONS: tuple
    REASONS_WITH_STARTER_PACK: tuple

class BattlePassState(object):
    BASE = 0
    POST = 1
    COMPLETED = 2
    PAUSED = 3

class BattlePassConsts(object):
    REWARD_FREE = 'free'
    REWARD_PAID = 'paid'
    REWARD_BOTH = 'both'
    RARE_REWARD_TAG = 'rare'
    FREE_MASK = 1
    PAID_MASK = 2
    FAKE_QUEST_ID = 'battlePassFakeQuestID'
    MINIMAL_CHAPTER_NUMBER = 1

class BattlePassStatsCommon(object):
    _CNT_SEASONS_FORMAT = '<I'
    _SEASON_ID_FORMAT = '<I'
    _OTHER_STATS_FORMAT = '<3I'
    OtherStats: Any
    SeasonStats: Any
    @staticmethod
    def _packList(inputList):
        ...
    @staticmethod
    def _unpackList(packed, offset):
        ...
    @staticmethod
    def makeSeasonStats(seasonID, vehiclePoints, seasonStats):
        ...
    @staticmethod
    def packSeasonStats(seasonStats):
        ...
    @staticmethod
    def unpackSeasonStats(packed, offset=0):
        ...
    @staticmethod
    def packSeasonStatsWithPrevStats(prevPackedStats, seasonStats):
        ...
    @staticmethod
    def unpackAllSeasonStats(packedStats, curOffset=0):
        ...
    @staticmethod
    def getEmptyPackedSeasonStats():
        ...
    @staticmethod
    def initialSeasonStatsData():
        ...
    @staticmethod
    def initialChapterData():
        ...

class BattlePassConfig(object):
    REWARD_IDX = 0
    TAGS_IDX = 1
    _config: Any
    _season: Any
    _rewards: Any
    _regularChapterIds: Any
    _extraChapterIds: Any
    _mainChapterIds: Any
    def __init__(self, config):
        ...
    @property
    def mode(self):
        ...
    @property
    def seasonID(self):
        ...
    @property
    def seasonNum(self):
        ...
    @property
    def currentCollectionId(self):
        ...
    @property
    def seasonStart(self):
        ...
    @property
    def seasonFinish(self):
        ...
    @property
    def finalOfferTime(self):
        ...
    @property
    def points(self):
        ...
    @property
    def chapters(self):
        ...
    @property
    def vehLevelCaps(self):
        ...
    @property
    def vehCDCaps(self):
        ...
    @property
    def isHoliday(self):
        ...
    @property
    def isPostProgressionPresent(self):
        ...
    @property
    def postProgressionChapterID(self):
        ...
    @property
    def postProgressionCycleLength(self):
        ...
    def getRewardTypes(self, chapterID):
        ...
    def getChapterLevels(self, chapterID):
        ...
    def getMaxChapterLevel(self, chapterID):
        ...
    def getMaxChapterPoints(self, chapterID):
        ...
    def getRegularChapterIds(self):
        ...
    def getMainChapterIds(self):
        ...
    def getExtraChapterIds(self):
        ...
    def getBattlePassCost(self, chapterID):
        ...
    def getChapterStarterPack(self, chapterID):
        ...
    def getAllRegularChaptersStarterPack(self):
        ...
    def getTankmenScreens(self):
        ...
    @staticmethod
    def iterRewardRanges(prevLvl, newLvl, rewardMask):
        ...
    def isGameModeEnabled(self, gameMode):
        ...
    def isBuyingAllowed(self):
        ...
    def isActive(self, curTime):
        ...
    def isEnabled(self):
        ...
    def isPaused(self):
        ...
    def isDisabled(self):
        ...
    def isSeasonTimeOver(self, curTime):
        ...
    def isExtraChapter(self, chapterID):
        ...
    def isRegularChapter(self, chapterID):
        ...
    def getChapterExpireTimestamp(self, chapterID):
        ...
    def getSpecialVehicles(self):
        ...
    def getSpecialVehiclesByGameMode(self, gameMode=...):
        ...
    def isSpecialVehicle(self, vehTypeCompDescr, gameMode=...):
        ...
    def capBonusList(self):
        ...
    def capBonus(self, vehLevel):
        ...
    def vehicleContribution(self, vehTypeCompDescr):
        ...
    def capBonusForVehTypeCompDescr(self, vehTypeCompDescr):
        ...
    def vehicleCapacity(self, vehTypeCompDescr):
        ...
    def bonusPointsList(self, vehTypeCompDescr=None, isWinner=True, gameMode=...):
        ...
    def getSeasonRewards(self):
        ...
    def getChapterRewards(self, chapterID, rewardType):
        ...
    def getTags(self, chapterID, level, rewardType):
        ...
    def getRewardByMask(self, chapterID, level, rewardMask):
        ...
    def getFreeReward(self, chapterID, level):
        ...
    def getPaidReward(self, chapterID, level):
        ...
    def getRewardByType(self, chapterID, level, rewardType):
        ...
    def getChapterBorders(self, chapterID):
        ...
    def getChapterIDs(self):
        ...
    def getAvailableStyles(self):
        ...
    def getChapterStyleID(self, chapterID):
        ...
    def getChapter(self, chapterID):
        ...

def getVehicleLevel(vehTypeCompDescr):
    ...
def getBattlePassPassTokenName(season, chapter):
    ...
def getBattlePassPassEntitlementName(season):
    ...
def getBattlePassShopEntitlementName(season):
    ...
def getSeasonAndChapterFromBattlePassToken(tokenID):
    ...
def isBattlePassPassToken(token):
    ...
def getLevel(curPoints, levelPoints, prevLevel=0):
    ...
def getPostProgressionLevel(curPoints, cyclePoints, prevLevel=0):
    ...
def getMaxAvalable3DStyleProgressInChapter(seasonID, chapter, tokensIds):
    ...
def get3DStyleProgressToken(seasonID, chapter, progressLevel):
    ...
def getPresentLevel(rawLevel):
    ...
def isPostProgressionChapter(chapterID):
    ...
def getPostProgressionChapterID(seasonNum):
    ...
def getPostProgressionLevelInCycleForRewards(cycleLength, level):
    ...
def mergeRewards(storage, rewardsToMerge):
    ...
