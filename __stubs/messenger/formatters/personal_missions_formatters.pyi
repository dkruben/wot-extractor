# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/messenger/formatters/personal_missions_formatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import re as re
from itertools import chain as chain
import constants as constants
import personal_missions as pm
from gui.impl import backport as backport
from gui.server_events.bonuses import PersonalMissionsPointsTokensBonus as PersonalMissionsPointsTokensBonus
from gui.server_events.event_items import PM3_ROLE_TO_ICON_NAME as PM3_ROLE_TO_ICON_NAME
from gui.server_events.finders import NO_AWARD_LIST_FINISHED_QUEST as NO_AWARD_LIST_FINISHED_QUEST, NO_AWARD_LIST_HONOR_POSTFIX as NO_AWARD_LIST_HONOR_POSTFIX
from gui.server_events.personal_progress.formatters import PMCardConditionsFormatter as PMCardConditionsFormatter
from messenger import g_settings as g_settings
from personal_missions import PM_BRANCH as PM_BRANCH
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from helpers import dependency as dependency, i18n as i18n, int2roman as int2roman
from messenger.formatters.service_channel import PersonalMissionsQuestAchievesFormatter as PersonalMissionsQuestAchievesFormatter, PMCompletionFormatter as PMCompletionFormatter, PMMedalsFormatter as PMMedalsFormatter, WaitItemsSyncFormatter as WaitItemsSyncFormatter
from messenger.formatters.service_channel_helpers import DEFAULT_MESSAGE as DEFAULT_MESSAGE, EOL as EOL, MessageData as MessageData, getDefaultMessage as getDefaultMessage, getPMAdvancedOperationAndQuest as getPMAdvancedOperationAndQuest, getPotapovQuestPopUps as getPotapovQuestPopUps, getRewardsForQuests as getRewardsForQuests
from messenger.formatters.token_quest_subformatters import AsyncTokenQuestsSubFormatter as AsyncTokenQuestsSubFormatter, TokenQuestsSubFormatter as TokenQuestsSubFormatter
from gui.impl.gen import R as R
from shared_utils import findFirst as findFirst, first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache

class PMBasicTokenQuestsFormatter(AsyncTokenQuestsSubFormatter):
    _DEFAULT_TEMPLATE = 'tokenQuests'
    __eventsCache: Any
    __PERSONAL_MISSIONS_CUSTOM_TEMPLATE = 'personalMissionsCustom'
    __PM12_OPERATIONS_PATTERN: Any
    __PM_TOKEN_QUEST_PATTERNS: Any
    __REGEX_PATTERN_BADGE = 'pt_final_s(\\d)_t(\\d)_badge'
    __TOKENS_NAME: tuple
    _achievesFormatter: Any
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def __formatSpecialMissions(self, questIDs, pmQuestsIDs, message, rewards):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __getCamouflageGivenFor(self, quest):
        ...
    def __getCamouflageUnlockedFor(self, quest):
        ...

class PersonalMissionsBasicFormatter(PMBasicTokenQuestsFormatter):
    _DEFAULT_TEMPLATE = 'personalMissions'
    __PM_PREFIX_PATTERN: Any
    def getPopUps(self, message):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...

class PMAdvancedQuestFormatter(WaitItemsSyncFormatter):
    __TEMPLATE = 'PersonalMission3Quest'
    __TEMPLATE_AFFIRMATIVE = 'PersonalMission3Quest15'
    __PERSONAL_MISSIONS_ACHIEVES_CUSTOM_TEMPLATE = 'personalMissions3Custom'
    __MAX_AWARDS = 4
    __QUEST_GROUP = PM_BRANCH.WITHOUT_AWARD_LIST_BRANCHES
    __itemsCache: Any
    __eventsCache: Any
    __PM_PREFIX_PATTERN: Any
    _achievesFormatter: Any
    def __init__(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def __makeMessageData(self, message, vehCDs, allVehs, operation, quest):
        ...
    def __getMedalNotification(self, message, chainName, quest):
        ...
    def __packBonuses(self, bonuses, isOperationCompleted):
        ...
    def __getButtonState(self, quest):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...

class PMAdvancedCompletionFormatter(WaitItemsSyncFormatter, TokenQuestsSubFormatter):
    _PM_OPERATIONS_PATTERN: Any
    _PM_COMPAING_PATTERN: Any
    _PM_TOKEN_QUEST_PATTERNS: Any
    _OPERATION_COMPLETE_PATTERN: Any
    _PERSONAL_MISSIONS_HONOR_TEMPLATE = 'pmAdvancedCompletionHonor'
    _PERSONAL_MISSIONS_OPERATION_TEMPLATE = 'pmAdvancedOperationCompletion'
    __eventsCache: Any
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
    def __getOperationName(self, operationID):
        ...
    def __getCampaignName(self, branchID):
        ...
