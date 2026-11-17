# wot-extractor: STUB (.pyi) gerado a partir de sources/res/battle_royale/scripts/client/battle_royale/gui/impl/gen/view_models/views/lobby/views/battle_quest_awards_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.battle_royale_event_model import BattleRoyaleEventModel as BattleRoyaleEventModel
from gui.impl.gen.view_models.views.lobby.battle_pass.reward_item_model import RewardItemModel as RewardItemModel

class BattleStatus(Enum):
    INPROGRESS = 'inProgress'
    COMPLETED = 'completed'

class BattleQuestAwardsModel(ViewModel):
    __slots__: tuple
    onApprove: Any
    onClose: Any
    def __init__(self, properties=4, commands=2):
        ...
    @property
    def eventInfo(self):
        ...
    @staticmethod
    def getEventInfoType():
        ...
    def getBattleStatus(self):
        ...
    def setBattleStatus(self, value):
        ...
    def getLevel(self):
        ...
    def setLevel(self, value):
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
