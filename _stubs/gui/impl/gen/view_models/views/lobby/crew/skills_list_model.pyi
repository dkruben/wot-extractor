# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/skills_list_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel as ComponentBaseModel
from gui.impl.gen.view_models.views.lobby.crew.skill_training_model import SkillTrainingModel as SkillTrainingModel

class SkillsListModel(ComponentBaseModel):
    __slots__: tuple
    onSkillClick: Any
    onSkillHover: Any
    onSkillOut: Any
    onTrain: Any
    onCancel: Any
    def __init__(self, properties=4, commands=5):
        ...
    def getIrrelevantSkillsList(self):
        ...
    def setIrrelevantSkillsList(self, value):
        ...
    @staticmethod
    def getIrrelevantSkillsListType():
        ...
    def getCommonSkillsList(self):
        ...
    def setCommonSkillsList(self, value):
        ...
    @staticmethod
    def getCommonSkillsListType():
        ...
    def getRegularSkillsList(self):
        ...
    def setRegularSkillsList(self, value):
        ...
    @staticmethod
    def getRegularSkillsListType():
        ...
    def _initialize(self):
        ...
