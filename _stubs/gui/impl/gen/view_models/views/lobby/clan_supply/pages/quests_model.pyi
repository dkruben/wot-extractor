# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/pages/quests_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel as IconBonusModel
from gui.impl.gen.view_models.views.lobby.clan_supply.pages.quest_model import QuestModel as QuestModel

class ScreenStatus(IntEnum):
    PENDING = 0
    ERROR = 1
    PLAYER_NOT_IN_CLAN = 2
    REWARD_AVAILABLE = 3
    PREVIOUS_REWARDS = 4
    IN_PROGRESS = 5

class QuestsModel(ViewModel):
    __slots__: tuple
    onClaimReward: Any
    onGoToClans: Any
    onRefresh: Any
    def __init__(self, properties=6, commands=3):
        ...
    def getStatus(self):
        ...
    def setStatus(self, value):
        ...
    def getCycleDuration(self):
        ...
    def setCycleDuration(self, value):
        ...
    def getUpdateTime(self):
        ...
    def setUpdateTime(self, value):
        ...
    def getIsRewardsLoading(self):
        ...
    def setIsRewardsLoading(self, value):
        ...
    def getQuests(self):
        ...
    def setQuests(self, value):
        ...
    @staticmethod
    def getQuestsType():
        ...
    def getPreviousRewards(self):
        ...
    def setPreviousRewards(self, value):
        ...
    @staticmethod
    def getPreviousRewardsType():
        ...
    def _initialize(self):
        ...
