# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/progression/progression_main_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel
from comp7_light.gui.impl.gen.view_models.views.lobby.progression.progression_view_model import ProgressionViewModel as ProgressionViewModel

class MainViews(IntEnum):
    PROGRESSION = 0

class ProgressionMainViewModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=2, commands=0):
        ...
    @property
    def progressionModel(self):
        ...
    @staticmethod
    def getProgressionModelType():
        ...
    def getViewType(self):
        ...
    def setViewType(self, value):
        ...
    def _initialize(self):
        ...
