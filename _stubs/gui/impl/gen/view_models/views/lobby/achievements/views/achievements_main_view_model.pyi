# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/gen/view_models/views/lobby/achievements/views/achievements_main_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import ViewModel as ViewModel
from gui.impl.gen.view_models.views.lobby.achievements.views.achievements.advanced_achievements_view_model import AdvancedAchievementsViewModel as AdvancedAchievementsViewModel
from gui.impl.gen.view_models.views.lobby.achievements.views.summary.summary_view_model import SummaryViewModel as SummaryViewModel

class AchievementsViews(IntEnum):
    SUMMARY = 0
    ACHIEVEMENTS = 1

class AchievementsMainViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    def __init__(self, properties=4, commands=1):
        ...
    @property
    def summaryModel(self):
        ...
    @staticmethod
    def getSummaryModelType():
        ...
    @property
    def achievementsModel(self):
        ...
    @staticmethod
    def getAchievementsModelType():
        ...
    def getViewType(self):
        ...
    def setViewType(self, value):
        ...
    def getIsOtherPlayer(self):
        ...
    def setIsOtherPlayer(self, value):
        ...
    def _initialize(self):
        ...
