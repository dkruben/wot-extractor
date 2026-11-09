# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/post_progression/post_progression_grid_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.multi_step_model import MultiStepModel as MultiStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.single_step_model import SingleStepModel as SingleStepModel

class PostProgressionGridModel(ViewModel):
    __slots__: tuple
    onMainStepActionClick: Any
    onMainStepSelectClick: Any
    onMultiStepActionClick: Any
    onMultiStepSelectClick: Any
    onPrebattleSwitchToggleClick: Any
    def __init__(self, properties=3, commands=5):
        ...
    def getMainSelectedIdx(self):
        ...
    def setMainSelectedIdx(self, value):
        ...
    def getMainSteps(self):
        ...
    def setMainSteps(self, value):
        ...
    @staticmethod
    def getMainStepsType():
        ...
    def getMultiSteps(self):
        ...
    def setMultiSteps(self, value):
        ...
    @staticmethod
    def getMultiStepsType():
        ...
    def _initialize(self):
        ...
