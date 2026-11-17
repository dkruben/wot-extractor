# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/messenger/formatters/token_quest_subformatters.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import re as re
from adisp import adisp_async as adisp_async, adisp_process as adisp_process
from advent_calendar.gui.feature.constants import ADVENT_CALENDAR_PROGRESSION_QUEST as ADVENT_CALENDAR_PROGRESSION_QUEST, ADVENT_CALENDAR_QUEST_POSTFIX as ADVENT_CALENDAR_QUEST_POSTFIX, ADVENT_CALENDAR_QUEST_PREFIX as ADVENT_CALENDAR_QUEST_PREFIX
from advent_calendar.gui.shared.advent_system_factory import collectQuestRewardFormatter as collectQuestRewardFormatter
from advent_calendar.messenger.formatters.service_channel import AdventCalendarProgressionAchievesFormatter as AdventCalendarProgressionAchievesFormatter
from advent_calendar.skeletons.game_controller import IAdventCalendarController as IAdventCalendarController
from gui.impl import backport as backport
from gui.impl.gen import R as R
from helpers import dependency as dependency
from messenger import g_settings as g_settings
from messenger.formatters.service_channel_helpers import MessageData as MessageData
from messenger.formatters.token_quest_subformatters import AsyncTokenQuestsSubFormatter as AsyncTokenQuestsSubFormatter
_logger: Any

class AdventCalendarQuestRewardFormatter(AsyncTokenQuestsSubFormatter):
    __COMPLETED_PROGRESSION_QUEST_TEMPLATE = 'adventCalendarProgressionQuestReward'
    __COMPLETED_LAST_PROGRESSION_QUEST_TEMPLATE = 'adventCalendarProgressionFinishedReward'
    __COMPLETED_QUESTS_TEMPLATE = 'adventCalendarQuestReward'
    __DAY_PATTERN: Any
    __adventCalendarCtrl: Any
    def getCollectedQuestFormatter(self):
        ...
    # decorador original: @adisp_async
    # decorador original: @adisp_process
    def format(self, message, callback):
        ...
    def _format(self, message, *args):
        ...
    def __getTemplateData(self, questID, detailRewards):
        ...
    def __handleProgressionQuests(self, questID, rewards):
        ...
    def __handleQuests(self, questID, rewards):
        ...
    @classmethod
    def _isAdventDayQuest(cls, questID):
        ...
    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        ...
    @classmethod
    def __getDayIdFromQuest(cls, questID):
        ...
