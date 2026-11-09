# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/messenger/formatters/service_channel.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from itertools import chain as chain
import BigWorld as BigWorld
from comp7.gui.impl.lobby.comp7_helpers.comp7_quest_helpers import getComp7QuestType as getComp7QuestType, isComp7Quest as isComp7Quest
from comp7_common.comp7_constants import ARENA_GUI_TYPE as ARENA_GUI_TYPE
from comp7_common_const import Comp7QuestType as Comp7QuestType
from constants import FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA as FAIRPLAY_VIOLATION_SYS_MSG_SAVED_DATA, SCENARIO_RESULT as SCENARIO_RESULT
from dossiers2.custom.records import RECORD_DB_IDS as RECORD_DB_IDS
from dossiers2.ui.achievements import ACHIEVEMENT_BLOCK as ACHIEVEMENT_BLOCK
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency, time_utils as time_utils
from messenger import g_settings as g_settings
from messenger.formatters import TimeFormatter as TimeFormatter
from messenger.formatters.service_channel import QuestAchievesFormatter as QuestAchievesFormatter, BattleResultsFormatter as BattleResultsFormatter
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from skeletons.gui.game_control import IComp7Controller as IComp7Controller
_logger: Any

class Comp7BattleQuestsFormatter(object):
    __comp7Ctrl: Any
    def format(self, message):
        ...
    def __getComp7Quests(self, questIDs):
        ...
    def __formatTokensReward(self, message, questID):
        ...
    @staticmethod
    def __formatWeeklyReward(message, questID):
        ...
    @staticmethod
    def __getDossierPopUps(dossierData, popUpRecords):
        ...

class Comp7BattleResultsFormatter(BattleResultsFormatter):
    __comp7Controller: Any
    __COMP7SeasonResultsKeys: dict
    __COMP7QualificationResultsKeys: dict
    def _formatMessages(self, message, arenaType, arenaCreateTime):
        ...
    def _getFairplayData(self, message):
        ...
    def _prepareFormatData(self, message):
        ...
    def __makeComp7SeasonMsgCtx(self, battleResults, ctx):
        ...
    def __makeTournamentComp7SeasonMsgCtx(self, battleResults, ctx):
        ...

class Comp7QualificationRewardsFormatter(QuestAchievesFormatter):
    _BULLET = '\u2022 '
    _SEPARATOR: Any
    @classmethod
    def formatQuestAchieves(cls, data, asBattleFormatter, processCustomizations=True, processTokens=True):
        ...
