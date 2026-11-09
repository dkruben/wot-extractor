# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/crew/conversion_confirm_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.common.reward_item_model import RewardItemModel as RewardItemModel

class ConversionConfirmViewModel(ViewModel):
    __slots__: tuple
    onConfirm: Any
    onShowTankman: Any
    onClose: Any
    onCancel: Any
    def __init__(self, properties=2, commands=4):
        ...
    def getTankmanAmount(self):
        ...
    def setTankmanAmount(self, value):
        ...
    def getRewards(self):
        ...
    def setRewards(self, value):
        ...
    @staticmethod
    def getRewardsType():
        ...
    def _initialize(self):
        ...
