# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/lobby_state_machine/transitions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import sys as sys
from frameworks_common.state_machine import StateEvent as StateEvent, BaseTransition as BaseTransition, State as State
from frameworks_common.state_machine.transitions import TransitionType as TransitionType
from gui.lobby_state_machine.events import _StopEvent as _StopEvent
from gui.shared.events import NavigationEvent as NavigationEvent
from shared_utils import first as first

class NavigationTransition(BaseTransition):
    record: Any
    def __init__(self, transitionType=..., record=False):
        ...
    def execute(self, event):
        ...
    def getPriority(self):
        ...

class ConditionalTransition(NavigationTransition):
    condition: Any
    def __init__(self, condition, transitionType=..., record=False):
        ...
    def execute(self, event):
        ...

class GuardTransition(ConditionalTransition):
    def getPriority(self):
        ...
    def execute(self, event):
        ...

class HijackTransition(GuardTransition):
    __stateCLazz: Any
    def __init__(self, stateClazz, condition, transitionType=..., record=False):
        ...
    def getPriority(self):
        ...
    def execute(self, event):
        ...

class _StopTransition(NavigationTransition):
    def getPriority(self):
        ...
    def execute(self, event):
        ...
