# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_results/progression/daily_quest_progress_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.common.missions.daily_quest_model import DailyQuestModel as DailyQuestModel

class DailyQuestTypes(Enum):
    EASY = 'easy'
    MEDIUM = 'medium'
    HARD = 'hard'
    BONUS = 'bonus'
    PREMIUM = 'premium'
    EPIC = 'epic'

class DailyQuestProgressModel(DailyQuestModel):
    __slots__: tuple
    def __init__(self, properties=14, commands=0):
        ...
    def getLevel(self):
        ...
    def setLevel(self, value):
        ...
    def getNavigationEnabled(self):
        ...
    def setNavigationEnabled(self, value):
        ...
    def _initialize(self):
        ...
