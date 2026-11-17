# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/catalog/details_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.achievements.advanced_achievement_model import AdvancedAchievementModel as AdvancedAchievementModel
from gui.impl.gen.view_models.views.lobby.achievements.views.catalog.rewards_model import RewardsModel as RewardsModel

class ProgressType(Enum):
    PERCENTAGE = 'percentage'
    STEPPED = 'stepped'

class DetailsModel(AdvancedAchievementModel):
    __slots__: tuple
    def __init__(self, properties=18, commands=0):
        ...
    def getProgressType(self):
        ...
    def setProgressType(self, value):
        ...
    def getSpecificItemLevel(self):
        ...
    def setSpecificItemLevel(self, value):
        ...
    def getRewards(self):
        ...
    def setRewards(self, value):
        ...
    @staticmethod
    def getRewardsType():
        ...
    def _initialize(self):
        ...
