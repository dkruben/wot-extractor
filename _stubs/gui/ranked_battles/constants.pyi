# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/ranked_battles/constants.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum, unique as unique
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS as RANKEDBATTLES_CONSTS
from gui.shared.money import Currency as Currency
from shared_utils import CONST_CONTAINER as CONST_CONTAINER
YEAR_AWARDS_ORDER: tuple
ZERO_RANK_ID = 0
ZERO_DIVISION_ID = 0
MAX_GROUPS_IN_DIVISION = 3
AWARDS_ORDER: tuple
YEAR_AWARDS_BONUS_ORDER: tuple
DEFAULT_REWARDS_COUNT = 7
ARCHIVE_SEASON_ID = 0
STANDARD_POINTS_COUNT = 1
NOT_IN_LEAGUES_QUEST = 'ranked_{}_0_common'
QUALIFICATION_QUEST = '_qualification_'
FINAL_QUEST_PATTERN = 'ranked_2021_{}_final'
FINAL_LEADER_QUEST = 'ranked_2021_final_leader'
RANKED_QUEST_ID_PREFIX = 'ranked'
YEAR_POINTS_TOKEN = 'rb2021'
YEAR_STRIPE_SERVER_TOKEN = 'ranked_2021_final_top'
YEAR_STRIPE_CLIENT_TOKEN = 'ranked_final_ready'
YEAR_AWARD_SELECTABLE_OPT_DEVICE_PREFIX = 'offer:ranked_battles:deluxe'
ENTITLEMENT_EVENT_TOKEN = 'ranked_entitlement_event'
LOBBY_SUB_LANDING_PARAM = '?is_landing='
SEASON_RATING_PARAM = '?spaID={}'

class RankTypes(CONST_CONTAINER):
    ACCOUNT = 'account'
    VEHICLE = 'vehicle'

class YearAwardsNames(CONST_CONTAINER):
    SMALL = RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_SMALL
    MEDIUM = RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_MEDIUM
    BIG = RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_BIG
    LARGE = RANKEDBATTLES_CONSTS.RANKED_REWARDS_YEAR_LARGE

class RankedDossierKeys(CONST_CONTAINER):
    ARCHIVE = 'Archive'
    SEASON = 'Season%s'

class RankedTokenQuestPostfix(CONST_CONTAINER):
    COMMON = 'common'
    SPRINTER = 'sprinter'
    FINAL = 'final'
    LEADER = 'leader'

class SeasonResultTokenPatterns(CONST_CONTAINER):
    RANKED_OFF_BANNED = 'ranked_{}_banned'
    RANKED_OFF_ROLLED = 'ranked_{}_rolled'
    RANKED_OFF_SPRINTER = 'ranked_{}_sprinter'
    RANKED_OFF_GOLD_LEAGUE_TOKEN = 'ranked_{}_top_1'
    RANKED_OFF_SILVER_LEAGUE_TOKEN = 'ranked_{}_top_2'
    RANKED_OFF_BRONZE_LEAGUE_TOKEN = 'ranked_{}_top_3'

class SeasonGapStates(CONST_CONTAINER):
    WAITING_IN_LEAGUES = 0
    IN_LEAGUES = 1
    BANNED_IN_LEAGUES = 2
    ROLLED_IN_LEAGUES = 3
    WAITING_IN_DIVISIONS = 4
    IN_DIVISIONS = 5
    BANNED_IN_DIVISIONS = 6
    ROLLED_IN_DIVISIONS = 7
    WAITING_NOT_IN_DIVISIONS = 8
    NOT_IN_DIVISIONS = 9
    BANNED_NOT_IN_DIVISIONS = 10
    ROLLED_NOT_IN_DIVISIONS = 11
    WAITING_NOT_IN_SEASON = 12
    NOT_IN_SEASON = 13
    BANNED_NOT_IN_SEASON = 14
    ROLLED_NOT_IN_SEASON = 15

# decorador original: @unique
class AlertTypes(Enum):
    PRIME = 'prime'
    SEASON = 'season'
    VEHICLE = 'vehicle'
