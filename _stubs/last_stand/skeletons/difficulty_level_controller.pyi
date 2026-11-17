# wot-extractor: STUB (.pyi) gerado a partir de sources/res/last_stand/scripts/client/last_stand/skeletons/difficulty_level_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from skeletons.gui.game_control import IGameController as IGameController
import typing as typing
from Event import Event as Event
from last_stand_common.last_stand_constants import QUEUE_TYPE as QUEUE_TYPE
from last_stand.gui.ls_gui_constants import DifficultyLevel as DifficultyLevel
from last_stand.gui.game_control.difficulty_level_controller import _Level as _Level

class IDifficultyLevelController(IGameController):
    onChangeDifficultyLevelStatus = None
    onChangeDifficultyLevel = None
    onLevelsInfoReady = None
    def selectLevel(self, level):
        ...
    def getSelectedLevel(self):
        ...
    def getCurrentQueueType(self):
        ...
    def getLevelsInfo(self):
        ...
    def getLevelInfo(self, levelNum):
        ...
    @staticmethod
    def getLastSelectedLevel():
        ...
