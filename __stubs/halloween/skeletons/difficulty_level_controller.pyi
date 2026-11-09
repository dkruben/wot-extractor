# wot-extractor: STUB (.pyi) gerado a partir de sources/res/halloween/scripts/client/halloween/skeletons/difficulty_level_controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from skeletons.gui.game_control import IGameController as IGameController
import typing as typing
from Event import Event as Event
from halloween_common.halloween_constants import QUEUE_TYPE as QUEUE_TYPE
from halloween.gui.halloween_gui_constants import DifficultyLevel as DifficultyLevel
from halloween.gui.game_control.difficulty_level_controller import _Level as _Level

class IDifficultyLevelController(IGameController):
    onChangeDifficultyLevelStatus = None
    onChangeDifficultyLevel = None
    def selectLevel(self, level):
        ...
    def getSelectedLevel(self):
        ...
    def getCurrentQueueType(self):
        ...
    def getLevelsInfo(self):
        ...
    @staticmethod
    def getLastSelectedLevel():
        ...
