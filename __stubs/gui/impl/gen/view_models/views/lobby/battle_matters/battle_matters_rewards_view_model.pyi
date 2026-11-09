# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/battle_matters_rewards_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum, IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.item_bonus_model import ItemBonusModel as ItemBonusModel
from gui.impl.gen.view_models.views.lobby.battle_matters.battle_matters_vehicle_model import BattleMattersVehicleModel as BattleMattersVehicleModel

class State(IntEnum):
    REGULAR = 0
    INTERMEDIATE = 1
    TOKEN = 2
    TOKENVEHICLE = 3
    FINAL = 4

class RewardViewsSequenceNumber(IntEnum):
    SINGLE = 0
    FIRST = 1
    MIDDLE = 2
    LAST = 3

class RewardType(Enum):
    REGULAR = 'regular'
    INTERMEDIATE = 'intermediate'
    VEHICLE = 'vehicle'

class BattleMattersRewardsViewModel(ViewModel):
    __slots__: tuple
    ARG_REWARD_TYPE = 'type'
    ARG_REWARD_INDEX = 'tooltipId'
    onClose: Any
    onNextTask: Any
    onShowVehicle: Any
    onChooseVehicle: Any
    def __init__(self, properties=6, commands=4):
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getRewardViewsSequenceNumber(self):
        ...
    def setRewardViewsSequenceNumber(self, value):
        ...
    def getQuestNumber(self):
        ...
    def setQuestNumber(self, value):
        ...
    def getVehicles(self):
        ...
    def setVehicles(self, value):
        ...
    @staticmethod
    def getVehiclesType():
        ...
    def getRegularRewards(self):
        ...
    def setRegularRewards(self, value):
        ...
    @staticmethod
    def getRegularRewardsType():
        ...
    def getIntermediateRewards(self):
        ...
    def setIntermediateRewards(self, value):
        ...
    @staticmethod
    def getIntermediateRewardsType():
        ...
    def _initialize(self):
        ...
