# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/collection/reward_info_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.collection.reward_model import RewardModel as RewardModel

class RewardState(Enum):
    JUSTRECEIVED = 'justReceived'
    RECEIVED = 'received'
    UNRECEIVED = 'unreceived'

class RewardInfoModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    def getRequiredItemsCount(self):
        ...
    def setRequiredItemsCount(self, value):
        ...
    def getState(self):
        ...
    def setState(self, value):
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
