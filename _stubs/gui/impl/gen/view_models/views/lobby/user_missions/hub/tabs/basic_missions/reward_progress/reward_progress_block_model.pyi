# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/user_missions/hub/tabs/basic_missions/reward_progress/reward_progress_block_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from enum import Enum as Enum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.epic_quest_progress import EpicQuestProgress as EpicQuestProgress
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.reward_progress.win_back_progress import WinBackProgress as WinBackProgress

class RewardProgressTypes(Enum):
    EPICQUEST = 'epicQuest'
    WINBACK = 'winBack'
    DISABLED = 'disabled'

class RewardProgressBlockModel(ViewModel):
    __slots__: tuple
    def __init__(self, properties=3, commands=0):
        ...
    @property
    def epicQuestProgress(self):
        ...
    @staticmethod
    def getEpicQuestProgressType():
        ...
    @property
    def winBackProgress(self):
        ...
    @staticmethod
    def getWinBackProgressType():
        ...
    def getProgressType(self):
        ...
    def setProgressType(self, value):
        ...
    def _initialize(self):
        ...
