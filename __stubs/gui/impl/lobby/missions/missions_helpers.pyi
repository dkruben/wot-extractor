# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/missions/missions_helpers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import PREMIUM_TYPE as PREMIUM_TYPE
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.reward_progress_block_model import RewardProgressTypes as RewardProgressTypes
from gui.server_events.events_helpers import isEpicQuestEnabled as isEpicQuestEnabled
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from shared_utils import first as first
from skeletons.gui.server_events import IEventsCache as IEventsCache
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Iterable as Iterable, Union as Union, AnyStr as AnyStr
from gui.impl.gen.view_models.common.missions.event_model import EventModel as EventModel
from gui.server_events.event_items import Quest as Quest, DailyQuest as DailyQuest, DailyEpicTokenQuest as DailyEpicTokenQuest
from gui.server_events.conditions import Token as Token
from frameworks.wulf.view.array import Array as Array
__all__: tuple
NUM_OF_COMMON_DAILY_QUESTS = 3

class IMissionsGuiHelper(object):
    @classmethod
    def isDailyMissionsSupported(cls):
        ...
    @classmethod
    def isPM3MissionsSupported(cls):
        ...

class DefaultMissionsGuiHelper(IMissionsGuiHelper):
    @classmethod
    def isDailyMissionsSupported(cls):
        ...
    @classmethod
    def isPM3MissionsSupported(cls):
        ...

class RandomMissionsGuiHelper(IMissionsGuiHelper):
    @classmethod
    def isDailyMissionsSupported(cls):
        ...
    @classmethod
    def isPM3MissionsSupported(cls):
        ...

class RandomNP2MissionsGuiHelper(IMissionsGuiHelper):
    @classmethod
    def isDailyMissionsSupported(cls):
        ...
    @classmethod
    def isPM3MissionsSupported(cls):
        ...

class WinbackMissionsGuiHelper(IMissionsGuiHelper):
    @classmethod
    def isDailyMissionsSupported(cls):
        ...
    @classmethod
    def isPM3MissionsSupported(cls):
        ...

class MapboxMissionsGuiHelper(IMissionsGuiHelper):
    @classmethod
    def isDailyMissionsSupported(cls):
        ...
    @classmethod
    def isPM3MissionsSupported(cls):
        ...

def areCommonQuestsCompleted(quests):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def isPremiumPlusAccount(itemsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getQuestsToMarkAsViewed(eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def markQuestProgressAsViewed(quests=None, eventsCache=None):
    ...
def needToUpdateQuestsInModel(quests, questsInModel):
    ...
def needToUpdateQuestsInModelByIds(quests, questIdsInModel):
    ...
def getDailyEpicQuestToken(quest):
    ...
def formatCompleteCount(completedQuestsCount, totalCount, isIncreased=False):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def getRewardProgressType(winBackData=None, eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def __hasProgressChanged(ids, eventsCache=None):
    ...
# decorador original: @dependency.replace_none_kwargs(...)
def __hasStatusChanged(ids, eventsCache=None):
    ...
def __hasDifferentQuests(questIds, viewModelIds):
    ...
def __questModelsIdGen(dailyQuests):
    ...
