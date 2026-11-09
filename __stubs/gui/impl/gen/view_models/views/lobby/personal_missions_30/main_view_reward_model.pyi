# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/personal_missions_30/main_view_reward_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.personal_missions_30.style_bonus_model import StyleBonusModel as StyleBonusModel

class RewardsType(Enum):
    MAIN = 'main'
    OPERATION = 'operation'
    CAMPAIGN = 'campaign'

class MainViewRewardModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getItems(self):
        ...
    def setItems(self, value):
        ...
    @staticmethod
    def getItemsType():
        ...
    def getRewardsType(self):
        ...
    def setRewardsType(self, value):
        ...
    def getCompletedTasks(self):
        ...
    def setCompletedTasks(self, value):
        ...
    def getTasksNumber(self):
        ...
    def setTasksNumber(self, value):
        ...
    def _initialize(self):
        ...
