# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/frameworks_common/state_machine/observers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
from .states import State as State
from .exceptions import StateError as StateError
from .events import StateEvent as StateEvent

class BaseStateObserver(object):
    __slots__: tuple
    def clear(self):
        ...
    def isObservingState(self, state):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...
    def onEnterState(self, state, event):
        ...
    def onExitState(self, state, event):
        ...

class StateIdsObserver(BaseStateObserver):
    __slots__: tuple
    _stateIDs: Any
    def __init__(self, stateIDs):
        ...
    def getStateIDs(self):
        ...
    def isObservingState(self, state):
        ...

class StateObserversContainer(BaseStateObserver):
    __slots__: tuple
    _observers: Any
    def __init__(self, *observers):
        ...
    def clear(self):
        ...
    def addObserver(self, observer):
        ...
    def removeObserver(self, observer):
        ...
    def isObservingState(self, state):
        ...
    def onStateChanged(self, state, stateEntered, event=None):
        ...

class _LifetimeWrapper(object):
    _obj: Any
    def __init__(self, trackedObj, onDelete):
        ...
    @property
    def trackedObj(self):
        ...
    def makeCallable(self, fn):
        ...

class OneshotStateIdsObserver(StateIdsObserver):
    _lifetimeWrapper: Any
    _enterFn: Any
    _exitFn: Any
    _machine: Any
    def __init__(self, stateIds, machine, lifetimeObj, enterFn=None, exitFn=None):
        ...
    def clear(self):
        ...
    def onEnterState(self, state, event):
        ...
    def onExitState(self, state, event):
        ...
    def _tryDisconnect(self, forceRemove=True, *_, **__):
        ...
