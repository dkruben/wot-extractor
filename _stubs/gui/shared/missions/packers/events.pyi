# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/missions/packers/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
import constants as constants
from gui.Scaleform.daapi.view.lobby.missions.awards_formatters import CurtailingAwardsComposer as CurtailingAwardsComposer
from gui.Scaleform.daapi.view.lobby.missions.missions_helper import getMissionInfoData as getMissionInfoData
from gui.challenges.challenges_award_manager import AwardsManager as ChallengesAwardManager
from gui.challenges.challenges_bonuses_packers import getChallengesBonusPacker as getChallengesBonusPacker
from gui.impl.gen.view_models.common.missions.challenge_mission_model import ChallengeMissionModel as ChallengeMissionModel
from gui.impl.gen.view_models.common.missions.conditions.preformatted_condition_model import PreformattedConditionModel as PreformattedConditionModel
from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel as DailyQuestModel
from gui.impl.gen.view_models.common.missions.weekly_quest_model import WeeklyQuestModel as WeeklyQuestModel
from gui.impl.gen.view_models.common.missions.event_model import EventStatus as EventStatus
from gui.impl.gen.view_models.common.missions.quest_model import QuestModel as QuestModel
from gui.impl.lobby.common.view_helpers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.impl.lobby.missions.missions_helpers import getDailyEpicQuestToken as getDailyEpicQuestToken
from gui.server_events.awards_formatters import AWARDS_SIZES as AWARDS_SIZES
from gui.server_events.events_helpers import isPremium as isPremium, isDailyQuest as isDailyQuest, isWeeklyQuest as isWeeklyQuest, isDailyEpicReward as isDailyEpicReward
from gui.server_events.formatters import DECORATION_SIZES as DECORATION_SIZES
from gui.shared.missions.packers.bonus import getDefaultBonusPacker as getDefaultBonusPacker, packMissionsBonusModelAndTooltipData as packMissionsBonusModelAndTooltipData
from gui.shared.missions.packers.conditions import BonusConditionPacker as BonusConditionPacker, CONDITION_GROUP_AND as CONDITION_GROUP_AND, getDefaultPreformattedConditionModel as getDefaultPreformattedConditionModel
from gui.shared.missions.packers.conditions import PostBattleConditionPacker as PostBattleConditionPacker, ChallengePostBattleConditionPacker as ChallengePostBattleConditionPacker
from helpers import dependency as dependency
from skeletons.gui.server_events import IEventsCache as IEventsCache
from soft_exception import SoftException as SoftException
from gui.server_events.event_items import ServerEventAbstract as ServerEventAbstract
from gui.server_events.bonuses import SimpleBonus as SimpleBonus
from gui.shared.missions.packers.bonus import BonusUIPacker as BonusUIPacker
_logger: Any
DEFAULT_AWARDS_COUNT = 10
DAILY_QUEST_AWARDS_COUNT = 1000

class EventUIDataPacker(object):
    _event: Any
    def __init__(self, event):
        ...
    def pack(self, model=None):
        ...
    def _packModel(self, model):
        ...
    def _packEvent(self, model):
        ...
    def _getStatus(self):
        ...

class BattleQuestUIDataPacker(EventUIDataPacker):
    _tooltipData: Any
    def __init__(self, event):
        ...
    def pack(self, model=None):
        ...
    def getTooltipData(self):
        ...
    def _packModel(self, model):
        ...
    def _packBonuses(self, model):
        ...
    def _getBonusPacker(self):
        ...
    def _packPostBattleConds(self, model):
        ...
    def _packBonusConds(self, model):
        ...
    def _packDefaultConds(self, model):
        ...

class TokenUIDataPacker(EventUIDataPacker):
    def pack(self, model=None):
        ...

class PrivateMissionUIDataPacker(EventUIDataPacker):
    ...

class DailyQuestUIDataPacker(BattleQuestUIDataPacker):
    eventsCache: Any
    def pack(self, model=None):
        ...
    def _resolveQuestIcon(self, model):
        ...

class DailyEpicQuestUIDataPacker(TokenUIDataPacker):
    eventsCache: Any
    def _packModel(self, model):
        ...
    def _packBonusConds(self, model):
        ...

class WeeklyQuestUIDataPacker(BattleQuestUIDataPacker):
    eventsCache: Any
    def pack(self, model=None):
        ...

class ChallengeMissionUIDataPacker(BattleQuestUIDataPacker):
    _tooltipData: Any
    def pack(self, model=None):
        ...
    def _packBonuses(self, model):
        ...
    def _getBonusPacker(self):
        ...
    def _packPostBattleConds(self, model):
        ...

def packQuestBonusModel(quest, packer, array, sortKey=None):
    ...
def additionalRewardsBonusPacker(quest, packer, sortKey=None):
    ...
def packQuestBonusModelAndTooltipData(packer, array, quest, tooltipData=None, questBonuses=None):
    ...
def preformatEventBonuses(event, bonusFormatter=...):
    ...
def getEventUIDataPacker(event):
    ...
def findFirstConditionModel(root):
    ...
