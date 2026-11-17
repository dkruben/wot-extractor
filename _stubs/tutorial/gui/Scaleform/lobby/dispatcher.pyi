# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/tutorial/gui/Scaleform/lobby/dispatcher.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import TutorialEvent as TutorialEvent
from tutorial.logger import LOG_MEMORY as LOG_MEMORY, LOG_ERROR as LOG_ERROR
from tutorial.gui import GUIDispatcher as GUIDispatcher

class SfLobbyDispatcher(GUIDispatcher):
    _exit: Any
    def __init__(self):
        ...
    def __del__(self):
        ...
    def start(self, loader):
        ...
    def stop(self):
        ...
    def __handleStartTraining(self, event):
        ...
    def __handleStopTraining(self, _):
        ...
