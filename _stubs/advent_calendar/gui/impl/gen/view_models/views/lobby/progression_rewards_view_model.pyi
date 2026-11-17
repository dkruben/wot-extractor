# wot-extractor: STUB (.pyi) gerado a partir de sources/res/advent_calendar/scripts/client/advent_calendar/gui/impl/gen/view_models/views/lobby/progression_rewards_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from advent_calendar.gui.impl.gen.view_models.views.lobby.progression_reward_item_view_model import ProgressionRewardItemViewModel as ProgressionRewardItemViewModel

class ProgressionRewardsViewModel(ViewModel):
    __slots__: tuple
    onProgressionRewardCompleted: Any
    def __init__(self, properties=2, commands=1):
        ...
    def getIsCompleted(self):
        ...
    def setIsCompleted(self, value):
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
