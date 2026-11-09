# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/winback/winback_reward_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel as ItemBonusModel

class RewardWindowType(Enum):
    WELCOME = 'welcome'
    PROGRESSION_STEP = 'progressionStep'
    SELECTED_REWARDS = 'selectedRewards'
    WINBACK_PROGRESSION_COMPLETED = 'winbackProgressionCompleted'
    REGULAR_PROGRESSION_COMPLETED = 'regularProgressionCompleted'

class RewardName(Enum):
    VEHICLE_FOR_GIFT = 'vehicleForGift'
    VEHICLE_DISCOUNT = 'vehicleDiscount'
    VEHICLE_FOR_RENT = 'vehicleForRent'
    SELECTABLE_VEHICLE_FOR_GIFT = 'selectableVehicleForGift'
    SELECTABLE_VEHICLE_DISCOUNT = 'selectableVehicleDiscount'

class WinbackRewardViewModel(ViewModel):
    __slots__: tuple
    ARG_TOOLTIP_ID = 'tooltipId'
    onSelectReward: Any
    onClose: Any
    showInHangar: Any
    showQuests: Any
    def __init__(self, properties=4, commands=4):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getIsFirstProgressionStep(self):
        ...
    def setIsFirstProgressionStep(self, value):
        ...
    def getIsSelectableAwardAvailable(self):
        ...
    def setIsSelectableAwardAvailable(self, value):
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
