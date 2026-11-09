# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/battle_matters/battle_matters_main_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.battle_matters.quest_progress_model import QuestProgressModel as QuestProgressModel
from gui.impl.gen.view_models.views.lobby.battle_matters.quest_view_model import QuestViewModel as QuestViewModel

class BattleMattersMainViewModel(ViewModel):
    __slots__: tuple
    ARG_QUEST_ID = 'questID'
    NAME_VEHICLE_REWARD = 'vehicle'
    NAME_TOKEN_REWARD = 'token'
    onShowView: Any
    onShowManual: Any
    onShowManualForQuest: Any
    onShowAnimForQuest: Any
    onShowMainReward: Any
    onSelectDelayedReward: Any
    onClose: Any
    def __init__(self, properties=3, commands=7):
        ...
    @property
    def questProgress(self):
        ...
    @staticmethod
    def getQuestProgressType():
        ...
    def getIsRewardsViewOpen(self):
        ...
    def setIsRewardsViewOpen(self, value):
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
