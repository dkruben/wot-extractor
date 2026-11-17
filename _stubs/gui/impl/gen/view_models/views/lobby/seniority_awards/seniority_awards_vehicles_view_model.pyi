# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/seniority_awards/seniority_awards_vehicles_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.seniority_awards.seniority_awards_vehicle_model import SeniorityAwardsVehicleModel as SeniorityAwardsVehicleModel

class ViewState(Enum):
    SELECTION = 'selection'
    VIEW_REWARD_AFTER_SELECTION = 'viewRewardAfterSelection'
    VIEW_REWARD = 'viewReward'

class SeniorityAwardsVehiclesViewModel(ViewModel):
    __slots__: tuple
    onMoreRewards: Any
    onGoToHangar: Any
    onClose: Any
    onSelectVehicleReward: Any
    def __init__(self, properties=6, commands=4):
        ...
    def getCategory(self):
        ...
    def setCategory(self, value):
        ...
    def getMaxCategory(self):
        ...
    def setMaxCategory(self, value):
        ...
    def getFromEntryPoint(self):
        ...
    def setFromEntryPoint(self, value):
        ...
    def getVehicles(self):
        ...
    def setVehicles(self, value):
        ...
    @staticmethod
    def getVehiclesType():
        ...
    def getViewState(self):
        ...
    def setViewState(self, value):
        ...
    def getAvailableRewardsCount(self):
        ...
    def setAvailableRewardsCount(self, value):
        ...
    def _initialize(self):
        ...
