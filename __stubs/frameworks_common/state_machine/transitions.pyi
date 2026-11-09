# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/frameworks_common/state_machine/transitions.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
from enum import IntEnum as IntEnum
from .events import StringEvent as StringEvent
from .node import Node as Node
from .events import StateEvent as StateEvent

class TransitionType(IntEnum):
    EXTERNAL = 0
    INTERNAL = 1

class BaseTransition(Node):
    __slots__: tuple
    __targets: Any
    __priority: Any
    __type: Any
    def __init__(self, priority=0, transitionType=...):
        ...
    def __repr__(self):
        ...
    def clear(self):
        ...
    def getPriority(self):
        ...
    def getSource(self):
        ...
    def getTargets(self):
        ...
    def setTarget(self, state):
        ...
    def getType(self):
        ...
    def execute(self, event):
        ...

class ConditionTransition(BaseTransition):
    __slots__: tuple
    __condition: Any
    __invert: Any
    def __init__(self, condition, invert=False, priority=0):
        ...
    def clear(self):
        ...
    def execute(self, event):
        ...

class StringEventTransition(BaseTransition):
    __slots__: tuple
    __token: Any
    def __init__(self, token='', priority=0):
        ...
    def execute(self, event):
        ...
