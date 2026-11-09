# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/vehicle_hub/views/sub_models/veh_skill_tree/prestige_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel as PrestigeEmblemModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.rewards_slot_model import RewardsSlotModel as RewardsSlotModel

class PrestigeState(Enum):
    AVAILABLE = 'available'
    COMPLETED = 'completed'
    DISABLED = 'disabled'

class PrestigeViewModel(ViewModel):
    __slots__: tuple
    onPreview: Any
    def __init__(self, properties=3, commands=1):
        ...
    @property
    def prestigeEmblem(self):
        ...
    @staticmethod
    def getPrestigeEmblemType():
        ...
    def getRewards(self):
        ...
    def setRewards(self, value):
        ...
    @staticmethod
    def getRewardsType():
        ...
    def getPrestigeState(self):
        ...
    def setPrestigeState(self, value):
        ...
    def _initialize(self):
        ...
