# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/tooltips/leaderboard_reward_tooltip_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class State(Enum):
    INPROGRESS = 'inProgress'
    COMPLETED = 'completed'
    SIMPLIFIED = 'simplified'

class LeaderboardRewardTooltipModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getSeasonEndTimestamp(self):
        ...
    def setSeasonEndTimestamp(self, value):
        ...
    def _initialize(self):
        ...
