# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gameplay/observers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from collections import defaultdict as defaultdict
from frameworks_common.state_machine import BaseStateObserver as BaseStateObserver
from gameplay.blockers import BlockingStateMixin as BlockingStateMixin

class BlockingStateClearObserver(BaseStateObserver):
    __clearIDsToBlockingStates: Any
    def __init__(self):
        ...
    def clear(self):
        ...
    def isObservingState(self, state):
        ...
    def onEnterState(self, state, event):
        ...
    def onExitState(self, state, event):
        ...
