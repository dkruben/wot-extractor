# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/tooltip/post_progression_level_tooltip_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen import R as R
from gui.impl.gen.view_models.common.bonuses_model import BonusesModel as BonusesModel

class ModificationType(Enum):
    NONE = 'none'
    PAIRMODIFICATION = 'pairModification'
    FEATURE = 'feature'

class PostProgressionLevelTooltipViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=5, commands=0):
        ...
    @property
    def modifier(self):
        ...
    @staticmethod
    def getModifierType():
        ...
    def getLevel(self):
        ...
    def setLevel(self, value):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getNameRes(self):
        ...
    def setNameRes(self, value):
        ...
    def getIsUnlocked(self):
        ...
    def setIsUnlocked(self, value):
        ...
    def _initialize(self):
        ...
