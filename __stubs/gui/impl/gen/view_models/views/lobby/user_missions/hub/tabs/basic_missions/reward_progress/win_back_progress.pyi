# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/reward_progress/win_back_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.quest_progress_model import QuestProgressModel as QuestProgressModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.win_back_quest_model import WinBackQuestModel as WinBackQuestModel

class OffersState(Enum):
    AVAILABLE = 'available'
    DISABLED = 'disabled'
    NO_OFFERS = 'no_offers'

class WinBackProgress(QuestProgressModel):
    __slots__: tuple
    onTakeReward: Any
    onTakeAllRewards: Any
    def __init__(self, properties=8, commands=2):
        ...
    def getIsBattlePassActive(self):
        ...
    def setIsBattlePassActive(self, value):
        ...
    def getTimeLeftToClaim(self):
        ...
    def setTimeLeftToClaim(self, value):
        ...
    def getOffersState(self):
        ...
    def setOffersState(self, value):
        ...
    def getQuests(self):
        ...
    def setQuests(self, value):
        ...
    @staticmethod
    def getQuestsType():
        ...
    def _initialize(self):
        ...
