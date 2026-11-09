# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/messenger/formatters/token_quest_subformatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from comp7.gui.impl.lobby.comp7_helpers import comp7_quest_helpers as comp7_quest_helpers
from comp7.gui.impl.lobby.comp7_helpers import comp7_shared as comp7_shared, comp7_i18n_helpers as comp7_i18n_helpers
from comp7.messenger.formatters.service_channel import Comp7QualificationRewardsFormatter as Comp7QualificationRewardsFormatter
from comp7_common_const import Comp7QuestType as Comp7QuestType, qualificationQuestIDBySeasonNumber as qualificationQuestIDBySeasonNumber
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.server_events.bonuses import getMergedBonusesFromDicts as getMergedBonusesFromDicts
from helpers import dependency as dependency
from helpers import time_utils as time_utils
from messenger import g_settings as g_settings
from messenger.formatters import TimeFormatter as TimeFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from messenger.formatters.token_quest_subformatters import SyncTokenQuestsSubFormatter as SyncTokenQuestsSubFormatter
from skeletons.gui.game_control import IComp7Controller as IComp7Controller

class Comp7RewardsFormatter(SyncTokenQuestsSubFormatter):
    __PERIODIC_REWARD_MESSAGE_TEMPLATE = 'comp7PeriodicRewardMessage'
    __REGULAR_REWARD_MESSAGE_TEMPLATE = 'comp7RegularRewardMessage'
    __QUALIFICATION_REWARD_MESSAGE_TEMPLATE = 'comp7QualificationRewardMessage'
    __R_SYS_MESSAGES = R.strings.comp7_ext.system_messages
    __RANK_NAME_KEYS: tuple
    __comp7Ctrl: Any
    __questTypeFormatters: Any
    def __init__(self):
        ...
    def format(self, message, *_):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    def __formatPeriodicRewardMessage(self, message, questID):
        ...
    def __formatRegularRewardMessage(self, message, questID):
        ...
    def __formatTokensRewardMessage(self, message, questID):
        ...
    def __formatRegularMessage(self, message, rewardsData, rewardType):
        ...
    def __formatQualificationRewardMessage(self, message, questIDs):
        ...
    def __getQualificationRanks(self, quests):
        ...
    def __getRankName(self, rankIndex):
        ...
    def __getQualificationQuestID(self):
        ...
