# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/feature/fun_random_progression_quests_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_infinite_progression_condition import FunRandomInfiniteProgressionCondition as FunRandomInfiniteProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition as FunRandomProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState as FunRandomProgressionState

class FunRandomProgressionQuestsModel(ViewModel):
    __slots__: tuple
    onMissionClick: Any
    onMarkAsViewed: Any
    def __init__(self, properties=4, commands=2):
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
    def infiniteCondition(self):
        ...
    @staticmethod
    def getInfiniteConditionType():
        ...
    def getAssetsPointer(self):
        ...
    def setAssetsPointer(self, value):
        ...
    def _initialize(self):
        ...
