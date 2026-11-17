# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/common/tutorial/tutorial_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.common.tutorial.component_model import ComponentModel as ComponentModel
from gui.impl.gen.view_models.common.tutorial.criterion_model import CriterionModel as CriterionModel
from gui.impl.gen.view_models.common.tutorial.descriptions_model import DescriptionsModel as DescriptionsModel
from gui.impl.gen.view_models.common.tutorial.effect_model import EffectModel as EffectModel
from gui.impl.gen.view_models.common.tutorial.triggers_model import TriggersModel as TriggersModel
from gui.impl.gen.view_models.common.tutorial.view_criterion_model import ViewCriterionModel as ViewCriterionModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel as ListModel

class TutorialModel(ViewModel):
    __slots__: tuple
    onComponentFound: Any
    onComponentDisposed: Any
    onEffectCompleted: Any
    onComponentUpdate: Any
    onTriggerActivated: Any
    def __init__(self, properties=7, commands=5):
        ...
    @property
    def effects(self):
        ...
    @staticmethod
    def getEffectsType():
        ...
    @property
    def triggers(self):
        ...
    @staticmethod
    def getTriggersType():
        ...
    @property
    def foundComponents(self):
        ...
    @staticmethod
    def getFoundComponentsType():
        ...
    @property
    def descriptions(self):
        ...
    @staticmethod
    def getDescriptionsType():
        ...
    @property
    def criteria(self):
        ...
    @staticmethod
    def getCriteriaType():
        ...
    @property
    def viewCriteria(self):
        ...
    @staticmethod
    def getViewCriteriaType():
        ...
    def getEnabled(self):
        ...
    def setEnabled(self, value):
        ...
    def _initialize(self):
        ...
