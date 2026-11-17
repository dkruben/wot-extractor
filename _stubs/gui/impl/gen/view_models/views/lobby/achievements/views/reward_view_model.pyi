# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/reward_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel as AdvancedAchievementModel
from gui.impl.gen.view_models.views.lobby.achievements.views.reward_view_rewards_model import RewardViewRewardsModel as RewardViewRewardsModel

class RewardViewModel(ViewModel):
    __slots__: tuple
    onGoToDogTag: Any
    onGoToAchievement: Any
    onOpenNextReward: Any
    onOpenAchievementsPage: Any
    onClose: Any
    def __init__(self, properties=4, commands=5):
        ...
    def getIsFirstEntry(self):
        ...
    def setIsFirstEntry(self, value):
        ...
    def getRewardsBalance(self):
        ...
    def setRewardsBalance(self, value):
        ...
    def getRewards(self):
        ...
    def setRewards(self, value):
        ...
    @staticmethod
    def getRewardsType():
        ...
    def getAchievements(self):
        ...
    def setAchievements(self, value):
        ...
    @staticmethod
    def getAchievementsType():
        ...
    def _initialize(self):
        ...
