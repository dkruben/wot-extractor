# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fort_rush/scripts/client/fort_rush/gui/impl/gen/view_models/feature/fun_random_progression_entry_point_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from fort_rush.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage as FunRandomProgressionStage
from fort_rush.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState as FunRandomProgressionState

class FunRandomProgressionEntryPointModel(ViewModel):
    __slots__: tuple
    onShowInfo: Any
    def __init__(self, properties=2, commands=1):
        ...
    @property
    def progressionState(self):
        ...
    @staticmethod
    def getProgressionStateType():
        ...
    @property
    def currentProgressionStage(self):
        ...
    @staticmethod
    def getCurrentProgressionStageType():
        ...
    def _initialize(self):
        ...
