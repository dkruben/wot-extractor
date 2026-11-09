# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/MemoryCriticalController.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
import BigWorld as BigWorld
import Event as Event
from debug_utils import LOG_NOTE as LOG_NOTE, LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION, LOG_ERROR as LOG_ERROR
from helpers import dependency as dependency
from skeletons.gui.game_control import IGameSessionController as IGameSessionController
from uilogging.performance.critical.loggers import MemoryCriticalLogger as MemoryCriticalLogger
g_critMemHandler: Any

class MemoryCriticalController(object):
    ORIGIN_DEFAULT = -1
    gameSession: Any
    messages: Any
    __messages: Any
    __needReboot: Any
    __loweredSettings: Any
    onMemCrit: Any
    __selfCheckInProgress: Any
    _memoryLogger: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def initializeLogger(self):
        ...
    def __call__(self):
        ...
    def restore(self):
        ...
    def startSelfcheck(self):
        ...
    def cleanupCheck(self):
        ...
    def __checkStep(self, blockSize, dt):
        ...
    @staticmethod
    def __setGraphicsSetting(label, index):
        ...
    def __getLoweredOption(self, token):
        ...
    def __getLoweredOptionLabel(self, token, index):
        ...
