# wot-extractor: STUB (.pyi) gerado a partir de sources/res/story_mode/scripts/client/story_mode/gui/impl/gen/view_models/views/lobby/mission_selection_view_model.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from enum import IntEnum as IntEnum
from frameworks.wulf import Array as Array, ViewModel as ViewModel
from story_mode.gui.impl.gen.view_models.views.lobby.mission_model import MissionModel as MissionModel
from story_mode.gui.impl.gen.view_models.views.lobby.parallax_model import ParallaxModel as ParallaxModel
from story_mode.gui.impl.gen.view_models.views.lobby.selected_mission_model import SelectedMissionModel as SelectedMissionModel
from story_mode.gui.impl.gen.view_models.views.lobby.task_model import TaskModel as TaskModel

class TabsEnum(IntEnum):
    NEWBIES = 0
    EVENT = 1

class MissionSelectionViewModel(ViewModel):
    __slots__: tuple
    onQuit: Any
    onMissionSelect: Any
    onLoaded: Any
    onChangeTab: Any
    onSelectedMissionTaskUnlocked: Any
    onAboutClick: Any
    onNavigate: Any
    def __init__(self, properties=8, commands=7):
        ...
    @property
    def selectedMission(self):
        ...
    @staticmethod
    def getSelectedMissionType():
        ...
    @property
    def parallax(self):
        ...
    @staticmethod
    def getParallaxType():
        ...
    def getSelectedTab(self):
        ...
    def setSelectedTab(self, value):
        ...
    def getIsParallaxEnabled(self):
        ...
    def setIsParallaxEnabled(self, value):
        ...
    def getIsTabsVisible(self):
        ...
    def setIsTabsVisible(self, value):
        ...
    def getMissions(self):
        ...
    def setMissions(self, value):
        ...
    @staticmethod
    def getMissionsType():
        ...
    def getTasks(self):
        ...
    def setTasks(self, value):
        ...
    @staticmethod
    def getTasksType():
        ...
    def getModeId(self):
        ...
    def setModeId(self, value):
        ...
    def _initialize(self):
        ...
