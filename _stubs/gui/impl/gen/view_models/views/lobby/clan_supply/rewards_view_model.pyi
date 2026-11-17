# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/clan_supply/rewards_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel as ItemBonusModel

class RewardingType(IntEnum):
    COMMON = 0
    ELITE = 1
    ELITE_WITH_VEHICLE = 2

class RewardsViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onGoToHangar: Any
    def __init__(self, properties=3, commands=2):
        ...
    def getType(self):
        ...
    def setType(self, value):
        ...
    def getRewards(self):
        ...
    def setRewards(self, value):
        ...
    @staticmethod
    def getRewardsType():
        ...
    def getAdditionalRewards(self):
        ...
    def setAdditionalRewards(self, value):
        ...
    @staticmethod
    def getAdditionalRewardsType():
        ...
    def _initialize(self):
        ...
