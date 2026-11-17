# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/tooltips/editing_tooltip_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel

class TooltipType(Enum):
    DISABLED_LAYOUT = 'disabledLayout'
    NOT_ENOUGH_ACHIEVEMENTS = 'notEnoughAchievements'
    DISABLED = 'disabled'
    OTHER_PLAYER = 'otherPlayer'

class EditingTooltipViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getTooltipType(self):
        ...
    def setTooltipType(self, value):
        ...
    def getRequiredAchievementsCount(self):
        ...
    def setRequiredAchievementsCount(self, value):
        ...
    def _initialize(self):
        ...
