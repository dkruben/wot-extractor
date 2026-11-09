# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/common/skill/skill_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_simple_model import SkillSimpleModel as SkillSimpleModel

class BattleBooster(Enum):
    NONE = 'none'
    LEARNED = 'learned'
    IMPROVED = 'Improved'

class SkillModel(SkillSimpleModel):
    __slots__: tuple
    def __init__(self, properties=7, commands=0):
        ...
    def getIsZero(self):
        ...
    def setIsZero(self, value):
        ...
    def getIsIrrelevant(self):
        ...
    def setIsIrrelevant(self, value):
        ...
    def getBattleBooster(self):
        ...
    def setBattleBooster(self, value):
        ...
    def _initialize(self):
        ...
