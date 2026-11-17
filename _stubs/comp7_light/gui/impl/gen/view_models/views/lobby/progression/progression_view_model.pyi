# wot-extractor: STUB (.pyi) gerado a partir de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/gen/view_models/views/lobby/progression/progression_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import Enum as Enum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from comp7_light.gui.impl.gen.view_models.views.lobby.battle_quests_model import BattleQuestsModel as BattleQuestsModel
from comp7_light.gui.impl.gen.view_models.views.lobby.progression.progress_level_model import ProgressLevelModel as ProgressLevelModel
from comp7_light.gui.impl.gen.view_models.views.lobby.schedule_info_model import ScheduleInfoModel as ScheduleInfoModel

class ProgressionState(Enum):
    INPROGRESS = 'inProgress'
    COMPLETED = 'completed'

class ProgressionViewModel(ViewModel):
    __slots__: tuple
    onClose: Any
    onAboutClicked: Any
    def __init__(self, properties=7, commands=2):
        ...
    @property
    def battleQuests(self):
        ...
    @staticmethod
    def getBattleQuestsType():
        ...
    @property
    def scheduleInfo(self):
        ...
    @staticmethod
    def getScheduleInfoType():
        ...
    def getState(self):
        ...
    def setState(self, value):
        ...
    def getCurProgressPoints(self):
        ...
    def setCurProgressPoints(self, value):
        ...
    def getPrevProgressPoints(self):
        ...
    def setPrevProgressPoints(self, value):
        ...
    def getPointsForLevel(self):
        ...
    def setPointsForLevel(self, value):
        ...
    def getProgressLevels(self):
        ...
    def setProgressLevels(self, value):
        ...
    @staticmethod
    def getProgressLevelsType():
        ...
    def _initialize(self):
        ...
