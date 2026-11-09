# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/user_missions/hangar_widget/providers/user_mission_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.server_events.events_helpers import EventInfoModel as EventInfoModel
from gui.impl.lobby.user_missions.hangar_widget.utils import DailyMissionItemPacker as DailyMissionItemPacker, WeeklyMissionItemPacker as WeeklyMissionItemPacker
from gui.shared.missions.packers.bonus import getDailyMissionsBonusPacker as getDailyMissionsBonusPacker, getWeeklyMissionsBonusPacker as getWeeklyMissionsBonusPacker, weeklyBonusSortKey as weeklyBonusSortKey
from gui.server_events.event_items import DailyQuest as DailyQuest

class MissionItem(object):
    __slots__: tuple
    itemId: Any
    itemType: Any
    weight: Any
    secondaryKey: Any
    _rawData: Any
    _isCompleted: Any
    def __init__(self, itemId, itemType, weight=0, secondaryKey=None):
        ...
    @property
    def rawData(self):
        ...
    @rawData.setter
    def rawData(self, value):
        ...
    @property
    def isCompleted(self):
        ...
    @isCompleted.setter
    def isCompleted(self, value):
        ...
    @property
    def countdown(self):
        ...
    def getMissionPacker(self):
        ...
    def getBonusPacker(self):
        ...
    def getRewardsSortKey(self):
        ...
    def getAnimationId(self):
        ...

class DailyQuestMissionItem(MissionItem):
    __slots__: tuple
    _TYPE = 'daily'
    difficulty: Any
    itemType: Any
    def __init__(self, itemId, weight, difficulty):
        ...
    def __repr__(self):
        ...
    def setItemType(self, value):
        ...
    @property
    def countdown(self):
        ...
    def getMissionPacker(self):
        ...
    def getBonusPacker(self):
        ...
    def getRewardsSortKey(self):
        ...
    def getAnimationId(self):
        ...

class PremiumDailyQuestMissionItem(MissionItem):
    __slots__: tuple
    _TYPE = 'premium_daily'
    def __init__(self, itemId, weight):
        ...
    def __repr__(self):
        ...
    def getMissionPacker(self):
        ...
    def getBonusPacker(self):
        ...
    def getRewardsSortKey(self):
        ...
    def getAnimationId(self):
        ...

class WeeklyQuestMissionItem(MissionItem):
    __slots__: tuple
    _TYPE = 'weekly'
    _commonConditionId: Any
    _specialConditionIds: Any
    _questId: Any
    def __init__(self, itemId, weight, questId):
        ...
    def __repr__(self):
        ...
    @property
    def commonConditionId(self):
        ...
    @commonConditionId.setter
    def commonConditionId(self, value):
        ...
    @property
    def specialConditionIds(self):
        ...
    @specialConditionIds.setter
    def specialConditionIds(self, value):
        ...
    def getMissionPacker(self):
        ...
    def getBonusPacker(self):
        ...
    def getRewardsSortKey(self):
        ...
    def getAnimationId(self):
        ...
