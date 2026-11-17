# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/common/comp7_common_const.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
import enum as enum
import typing as typing
from typing import Tuple as Tuple, Optional as Optional
COMP7_MASKOT_ID = '6'
SEASONS_IN_YEAR = 3
__COMP7_QUALIFICATION_TOKEN_TEMPLATE = 'comp7_{maskot}_{season}:qualification'
__COMP7_QUALIFICATION_QUEST_ID_TEMPLATE = 'comp7_{maskot}_{season}_ranks_65'
__COMP7_RENT_VEHICLES_QUEST_ID_TEMPLATE = 'comp7_{maskot}_{season}_rent_vehicles'
__COMP7_TOKEN_PREFIX_TEMPLATE = 'comp7_{maskot}_{season}'
__COMP7_SEASON_POINT_ASSET_TEMPLATE = 'comp7_season_points:{maskot}:{season}'
__COMP7_SEASON_NAME_TEMPLATE = 'comp7_{maskot}_{season}'
__COMP7_WEEKLY_QUESTS_COMPLETE_TOKEN_TEMPLATE = 'comp7_{maskot}_{season}_weekly_quests_complete'
COMP7_WEEKLY_QUESTS_COMPLETE_TOKEN_REGEXP: Any
__COMP7_SEASON_POINTS_ENTITLEMENT_TEMPLATE = 'comp7_season_points:{maskot}:{season}'
__COMP7_RATING_ENTITLEMENT_PREFIX = 'comp7_rating_points'
__COMP7_RATING_ENTITLEMENT_TEMPLATE: Any
__COMP7_ELITE_ENTITLEMENT_TEMPLATE = 'comp7_elite_rank:{maskot}:{season}'
__COMP7_ACTIVITY_ENTITLEMENT_TEMPLATE = 'comp7_activity_points:{maskot}:{season}'
__COMP7_MAX_RANK_ENTITLEMENT_TEMPLATE = 'comp7_max_achieved_rank:{maskot}:{season}'
COMP7_OFFER_GIFT_TEMPLATE = '{token}_gift'
COMP7_OFFER_PREFIX: Any
COMP7_OFFER_WEEKLY_QUESTS_REWARD_TOKEN_TEMPLATE: Any
COMP7_OFFER_WEEKLY_QUESTS_REWARD_GIFT_TOKEN_TEMPLATE: Any
COMP7_OFFER_YEARLY_REWARD_TOKEN_PREFIX: Any
COMP7_OFFER_REWARD_CATEGORY_TOKEN_TEMPLATE = '{token}:{category}'
COMP7_ENTITLEMENT_EXPIRES = None
COMP7_YEARLY_ACHIEVEMENT_PREFIX: Any
COMP7_YEARLY_REWARD_TOKEN: Any
SEASON_POINTS_ENTITLEMENTS: list
SEASON_POINTS_ASSETS: list

class Comp7EntitlementCodes(object):
    LEGEND_RANK = 'legendRank'
    RATING_POINTS = 'ratingPoints'
    ACTIVITY_POINTS = 'activityPoints'
    SEASON_POINTS = 'seasonPoints'
    ALL: tuple

# decorador original: @enum.unique
class Comp7QuestType(enum.Enum):
    RANKS = 'ranks'
    TOKENS = 'token_rewards'
    PERIODIC = 'period'
    ACTIVITY = 'activity'
    WEEKLY = 'weekly'
    def isVisible(self):
        ...

class BattleStatuses(object):
    STARTED = 0
    WIN = 1
    LOSE = 2
    DESERTER = 3
    FINISHED_WITH_ERROR = 4
    STARTED_RANGE: tuple
    FINISHED_RANGE: tuple

class Comp7QualificationState(object):
    NOT_STARTED = 'not_started'
    IN_PROGRESS = 'in_progress'
    WAITING_BATTLE_RESULTS = 'wait_battle_results'
    FINALIZING = 'finalizing'
    COMPLETED = 'completed'
    states: tuple
    @classmethod
    def isBattleAllowed(cls, state):
        ...
    @classmethod
    def isUnitAllowed(cls, state):
        ...
    @classmethod
    def isQualificationActive(cls, state):
        ...
    @classmethod
    def isResultsProcessing(cls, state):
        ...
    @classmethod
    def isCalculationQualificationRating(cls, state):
        ...

def isComp7YearlyAchievement(achievementName):
    ...
def seasonPointsCodeBySeasonNumber(seasonNumber):
    ...
def qualificationTokenBySeasonNumber(seasonNumber):
    ...
def seasonPointsAssetBySeasonNumber(seasonNumber):
    ...
def qualificationQuestIDBySeasonNumber(seasonNumber):
    ...
def rentVehiclesQuestIDBySeasonNumber(seasonNumber):
    ...
def tokenPrefixBySeasonNumber(seasonNumber):
    ...
def ratingEntNameBySeasonNumber(seasonNumber):
    ...
def eliteRankEntNameBySeasonNumber(seasonNumber):
    ...
def activityPointsEntNameBySeasonNumber(seasonNumber):
    ...
def maxRankEntNameBySeasonNumber(seasonNumber):
    ...
def seasonNameBySeasonNumber(seasonNumber):
    ...
def weeklyQuestsCompleteTokenName(seasonNumber):
    ...
def offerWeeklyQuestsRewardTokenPrefixBySeasonNumber(seasonNumber):
    ...
def offerRewardCategoryToken(token, category):
    ...
def offerRewardGiftToken(token):
    ...
def parseRatingEnt(entCode):
    ...
