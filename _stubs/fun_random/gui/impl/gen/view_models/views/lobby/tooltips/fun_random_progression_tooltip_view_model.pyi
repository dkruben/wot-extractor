# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/tooltips/fun_random_progression_tooltip_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from frameworks.wulf import ViewModel as ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition as FunRandomProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage as FunRandomProgressionStage
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState as FunRandomProgressionState

class FunRandomProgressionTooltipViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=5, commands=0):
        ...
    @property
    def state(self):
        ...
    @staticmethod
    def getStateType():
        ...
    @property
    def condition(self):
        ...
    @staticmethod
    def getConditionType():
        ...
    @property
    def currentStage(self):
        ...
    @staticmethod
    def getCurrentStageType():
        ...
    def getAssetsPointer(self):
        ...
    def setAssetsPointer(self, value):
        ...
    def getIsMultipleSubModes(self):
        ...
    def setIsMultipleSubModes(self, value):
        ...
    def _initialize(self):
        ...
