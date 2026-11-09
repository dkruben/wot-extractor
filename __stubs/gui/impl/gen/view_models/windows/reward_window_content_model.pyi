# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/windows/reward_window_content_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.ui_kit.list_model import ListModel as ListModel

class RewardWindowContentModel(ViewModel):
    __slots__: tuple
    onConfirmBtnClicked: Any
    onSecondBtnClicked: Any
    onHyperLinkClicked: Any
    def __init__(self, properties=3, commands=3):
        ...
    @property
    def rewardsList(self):
        ...
    @staticmethod
    def getRewardsListType():
        ...
    def getEventName(self):
        ...
    def setEventName(self, value):
        ...
    def getShowRewards(self):
        ...
    def setShowRewards(self, value):
        ...
    def _initialize(self):
        ...
