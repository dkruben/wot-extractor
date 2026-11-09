# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/personal_case/tankman_skill_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_extended_model import SkillExtendedModel as SkillExtendedModel

class AnimationType(Enum):
    NONE = 'none'
    UNLOCKED = 'unlocked'
    SELECTED = 'selected'

class TankmanSkillModel(SkillExtendedModel):
    __slots__: tuple
    def __init__(self, properties=12, commands=0):
        ...
    def getIsDisabled(self):
        ...
    def setIsDisabled(self, value):
        ...
    def getIsLocked(self):
        ...
    def setIsLocked(self, value):
        ...
    def getAnimationType(self):
        ...
    def setAnimationType(self, value):
        ...
    def _initialize(self):
        ...
