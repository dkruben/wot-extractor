# wot-extractor: STUB (.pyi) gerado a partir de sources/res/fun_random/scripts/client/fun_random/gui/impl/gen/view_models/views/lobby/feature/mode_selector/fun_random_sub_selector_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_condition import FunRandomProgressionCondition as FunRandomProgressionCondition
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_stage import FunRandomProgressionStage as FunRandomProgressionStage
from fun_random.gui.impl.gen.view_models.views.lobby.common.fun_random_progression_state import FunRandomProgressionState as FunRandomProgressionState
from fun_random.gui.impl.gen.view_models.views.lobby.feature.mode_selector.fun_random_sub_selector_card_model import FunRandomSubSelectorCardModel as FunRandomSubSelectorCardModel

class FunRandomSubSelectorModel(ViewModel):
    __slots__: tuple
    onItemClicked: Any
    onInfoClicked: Any
    onBackBtnClicked: Any
    onClosed: Any
    def __init__(self, properties=6, commands=4):
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
    def getCardList(self):
        ...
    def setCardList(self, value):
        ...
    @staticmethod
    def getCardListType():
        ...
    def getAssetsPointer(self):
        ...
    def setAssetsPointer(self, value):
        ...
    def getModeName(self):
        ...
    def setModeName(self, value):
        ...
    def _initialize(self):
        ...
