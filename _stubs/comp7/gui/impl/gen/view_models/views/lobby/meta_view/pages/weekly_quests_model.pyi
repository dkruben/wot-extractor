# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7/scripts/client/comp7/gui/impl/gen/view_models/views/lobby/meta_view/pages/weekly_quests_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.progress_points_model import ProgressPointsModel as ProgressPointsModel
from comp7.gui.impl.gen.view_models.views.lobby.meta_view.pages.quest_card_model import QuestCardModel as QuestCardModel

class ChoiceRewardState(IntEnum):
    DEFAULT = 0
    ACTIVE = 1
    CLAIMED = 2

class WeeklyQuestsModel(ViewModel):
    __slots__: tuple
    QUESTS_PER_WEEK = 5
    onAnimationStart: Any
    onAnimationEnd: Any
    onGoToRewardsSelection: Any
    def __init__(self, properties=6, commands=3):
        ...
    def getTimeToNewQuests(self):
        ...
    def setTimeToNewQuests(self, value):
        ...
    def getQuestCards(self):
        ...
    def setQuestCards(self, value):
        ...
    @staticmethod
    def getQuestCardsType():
        ...
    def getQuestsPassed(self):
        ...
    def setQuestsPassed(self, value):
        ...
    def getPreviousQuestsPassed(self):
        ...
    def setPreviousQuestsPassed(self, value):
        ...
    def getProgressPoints(self):
        ...
    def setProgressPoints(self, value):
        ...
    @staticmethod
    def getProgressPointsType():
        ...
    def getChoiceRewardState(self):
        ...
    def setChoiceRewardState(self, value):
        ...
    def _initialize(self):
        ...
