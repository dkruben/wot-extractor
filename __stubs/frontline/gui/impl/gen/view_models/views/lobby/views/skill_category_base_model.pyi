# wot-extractor: STUB (.pyi) gerado a partir de sources/res/frontline/scripts/client/frontline/gui/impl/gen/view_models/views/lobby/views/skill_category_base_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.skill_base_model import SkillBaseModel as SkillBaseModel

class SkillCategoryType(Enum):
    FIRESUPPORT = 'firesupport'
    RECONNAISSANCE = 'reconnaissance'
    TACTICS = 'tactics'

class SkillCategoryBaseModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getSkills(self):
        ...
    def setSkills(self, value):
        ...
    @staticmethod
    def getSkillsType():
        ...
    def _initialize(self):
        ...
