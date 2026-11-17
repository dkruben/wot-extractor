# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/common/selectable_reward_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.common.selectable_reward_item_model import SelectableRewardItemModel as SelectableRewardItemModel
from gui.impl.gen.view_models.views.lobby.common.selectable_reward_tab_model import SelectableRewardTabModel as SelectableRewardTabModel

class SelectableRewardModel(ViewModel):
    __slots__: tuple
    onOkClick: Any
    onCloseClick: Any
    onTabClick: Any
    onRewardAdd: Any
    onRewardReduce: Any
    def __init__(self, properties=4, commands=5):
        ...
    def getTabs(self):
        ...
    def setTabs(self, value):
        ...
    @staticmethod
    def getTabsType():
        ...
    def getRewards(self):
        ...
    def setRewards(self, value):
        ...
    @staticmethod
    def getRewardsType():
        ...
    def getTotalRewardCount(self):
        ...
    def setTotalRewardCount(self, value):
        ...
    def getSelectedTab(self):
        ...
    def setSelectedTab(self, value):
        ...
    def _initialize(self):
        ...
