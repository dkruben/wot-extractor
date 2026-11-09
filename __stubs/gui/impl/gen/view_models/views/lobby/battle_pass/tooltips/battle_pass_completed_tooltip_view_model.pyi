# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_pass/tooltips/battle_pass_completed_tooltip_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class ChapterType(Enum):
    COMMON = 'common'
    EXTRA = 'extra'
    HOLIDAY = 'holiday'

class BattlePassCompletedTooltipViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=4, commands=0):
        ...
    def getIsBattlePassPurchased(self):
        ...
    def setIsBattlePassPurchased(self, value):
        ...
    def getNotChosenRewardCount(self):
        ...
    def setNotChosenRewardCount(self, value):
        ...
    def getIsAvailableTankmen(self):
        ...
    def setIsAvailableTankmen(self, value):
        ...
    def getChapterType(self):
        ...
    def setChapterType(self, value):
        ...
    def _initialize(self):
        ...
