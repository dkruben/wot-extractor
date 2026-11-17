# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/winback/winback_selectable_reward_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel as BonusModel
from gui.impl.gen.view_models.views.lobby.winback.selectable_reward_category_model import SelectableRewardCategoryModel as SelectableRewardCategoryModel

class SelectableRewardName(Enum):
    VEHICLE = 'vehicle'
    COMPENSATION = 'compensation'

class WinbackSelectableRewardViewModel(ViewModel):
    __slots__: tuple
    VEHICLE_LEVEL = 'vehicleLevel'
    REWARD_INDEX = 'rewardIndex'
    onCategorySelect: Any
    onFilterReset: Any
    onSelectReward: Any
    onClose: Any
    onConfirm: Any
    def __init__(self, properties=4, commands=5):
        ...
    def getCategories(self):
        ...
    def setCategories(self, value):
        ...
    @staticmethod
    def getCategoriesType():
        ...
    def getTotalRewardsCount(self):
        ...
    def setTotalRewardsCount(self, value):
        ...
    def getSelectedRewardsCount(self):
        ...
    def setSelectedRewardsCount(self, value):
        ...
    def getSelectableRewards(self):
        ...
    def setSelectableRewards(self, value):
        ...
    @staticmethod
    def getSelectableRewardsType():
        ...
    def _initialize(self):
        ...
