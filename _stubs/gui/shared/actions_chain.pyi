# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/actions_chain.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import BigWorld as BigWorld
import Event as Event
from debug_utils import LOG_DEBUG as LOG_DEBUG

class Action(object):
    _completed: Any
    _running: Any
    def __init__(self):
        ...
    def invoke(self):
        ...
    def isInstantaneous(self):
        ...
    def isRunning(self):
        ...
    def isCompleted(self):
        ...

class ActionsChain(object):
    __callbackID: Any
    __actions: Any
    __current: Any
    __isStopped: Any
    __eManager: Any
    onStarted: Any
    onStopped: Any
    def __init__(self, actions):
        ...
    def start(self):
        ...
    def stop(self):
        ...
    def __timeLoop(self):
        ...
    def __tick(self):
        ...
    def __goToNextAction(self):
        ...
