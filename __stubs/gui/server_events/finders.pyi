# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/server_events/finders.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
from helpers import dependency as dependency
from personal_missions import PM_BRANCH as PM_BRANCH
from shared_utils import findFirst as findFirst, first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache
PT_TOKEN_PREFIX = 'token:pt:'
PERSONAL_MISSION_TOKEN: Any
MAIN_PERSONAL_MISSION_TOKEN: Any
ADD_PERSONAL_MISSION_TOKEN: Any
PERSONAL_MISSION_COMPLETE_TOKEN: Any
PERSONAL_MISSION_BADGES_TOKEN: Any
FINAL_PT_TOKEN_PREFIX = 'pt_final_'
FINAL_PERSONAL_MISSION_TOKEN: Any
NO_AWARD_LIST_FINISHED_QUEST = 'pm%s_campaign_finished_honor'
NO_AWARD_LIST_OPERATION_FINISHED_HONOR_QUEST = 'pt_final_s%s_t%s_honor'
NO_AWARD_LIST_OPERATION_REWARD_QUEST = 'pm%s_operation_%s_reward'
NO_AWARD_LIST_PM_BASE_TOKEN: Any
NO_AWARD_LIST_HONOR_POSTFIX = 'honor'
NO_AWARD_LIST_PM_REWARD_CLAIMED: Any
NO_AWARD_LIST_FINISHED_CAMPAIGN_TOKEN: Any
NO_AWARD_LIST_VEHICLE_DETAIL_TOKEN: Any
NO_AWARD_LIST_QUEST_PREFIX_TEMPLATE = 'pm%s_'
NO_AWARD_LIST_MILESTONE_QUEST_PREFIX: Any
NO_AWARD_LIST_MILESTONE_QUEST_POSTFIX = 'milestone'
PM_POINTS_PREFIX = 'pm'
PM_NO_AWARD_LIST_QUESTS_PREFIX = 'pm'
PM_POINTS_POSTFIX = ':points'
PM_POINTS_TOKEN: Any
PM_OPERATION_POINTS_TOKEN: Any
isPMQuestRegExp: Any
CHAMPION_BADGES_BY_BRANCH: dict
OPERATIONS_TOKENS_PATTERNS: tuple
CHAMPION_BADGE_AT_OPERATION_ID: dict
NO_AWARD_LIST_QUEST_PREFIXES: list
PM_FINAL_TOKEN_QUEST_IDS_BY_OPERATION_ID: dict

def getBranchByOperationId(operationID):
    ...
def isPMNoAwardListMilestone(questID):
    ...
def getPMNoAwardListMilestones(quests, branch, operationID):
    ...
def isPMPoints(tokenName):
    ...
def getFinalTokenQuestIdByOperationId(operationId):
    ...
def getAdditionalTokenQuestIdByOperationId(operationId, addCamouflage=False, addBadge=False):
    ...
def getPersonalMissionDataFromToken(token):
    ...
def getQuestsByTokenAndBonus(quests, tokenFinder=None, bonusFinder=None):
    ...
def getQuestsByToken(quests, tokenFinder):
    ...
def getQuestByTokenAndBonus(quests, tokenFinder=None, bonusFinder=None):
    ...
def tokenFinder(tokenID):
    ...
def multipleTokenFinder(tokenIDs):
    ...
def pmTokenDetector(operations):
    ...
def mainQuestTokenFinder(operation):
    ...
def pmPointsTokenFinder(operation):
    ...
def addQuestTokenFinder(operation):
    ...
def tokenBonusFinder(tokenID):
    ...
def getOperationCompleteToken(operation):
    ...
def operationCompletionBonusFinder(operation):
    ...
def badgeBonusFinder():
    ...
