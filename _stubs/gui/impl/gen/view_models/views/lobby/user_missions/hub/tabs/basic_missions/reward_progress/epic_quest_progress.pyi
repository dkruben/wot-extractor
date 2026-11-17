# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/reward_progress/epic_quest_progress.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.epic_quests_bonus_model import EpicQuestsBonusModel as EpicQuestsBonusModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.quest_progress_model import QuestProgressModel as QuestProgressModel

class EpicQuestProgress(QuestProgressModel):
    __slots__: tuple
    onTakeWinBackReward: Any
    def __init__(self, properties=6, commands=1):
        ...
    def getBonuses(self):
        ...
    def setBonuses(self, value):
        ...
    @staticmethod
    def getBonusesType():
        ...
    def getWinBackTimeLeft(self):
        ...
    def setWinBackTimeLeft(self, value):
        ...
    def _initialize(self):
        ...
