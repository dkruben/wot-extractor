# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/weekly_quests_widget_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.weekly_quest_model import WeeklyQuestModel as WeeklyQuestModel

class State(Enum):
    HIDE = 'hide'
    ACTIVE = 'active'
    WAITING = 'waiting'
    REWARD = 'reward'

class WeeklyQuestsWidgetModel(ViewModel):
    __slots__: tuple
    onGoToWeeklyQuests: Any
    onMissionClick: Any
    onMarkAsViewed: Any
    onGoToRewardsSelection: Any
    onPollServerTime: Any
    def __init__(self, properties=6, commands=5):
        ...
    def getQuests(self):
        ...
    def setQuests(self, value):
        ...
    @staticmethod
    def getQuestsType():
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getQuestsCompleted(self):
        ...
    def setQuestsCompleted(self, value):
        ...
    def getTotalQuestsCount(self):
        ...
    def setTotalQuestsCount(self, value):
        ...
    def getLeftToNewQuestsTimestamp(self):
        ...
    def setLeftToNewQuestsTimestamp(self, value):
        ...
    def getServerTimestamp(self):
        ...
    def setServerTimestamp(self, value):
        ...
    def _initialize(self):
        ...
