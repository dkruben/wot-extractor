# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gameplay/blockers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import weakref as weakref
from itertools import chain as chain
import typing as typing
from wg_async import wg_async as wg_async, AsyncEvent as AsyncEvent
from frameworks_common.state_machine import StringEventTransition as StringEventTransition, State as State, StateFlags as StateFlags
from frameworks_common.state_machine import StringEvent as StringEvent
_logger: Any

class BlockingStateMixin(object):
    _enterBlockers: Any
    _exitBlockers: Any
    _blockerClearLifetimeStateID: Any
    event: Any
    _weakEvent: Any
    class _Blocker(object):
        event: Any
        _weakEvent: Any
        def __init__(self, eventToBlockOn):
            ...
        def clear(self, *_, **__):
            ...
    def __init__(self):
        ...
    @property
    def blockerClearLifetimeStateID(self):
        ...
    def clearBlockers(self):
        ...
    def addEnterBlocker(self, event):
        ...
    def addExitBlocker(self, event):
        ...
    def enterBlockersSatisfied(self):
        ...
    def exitBlockersSatisfied(self):
        ...
    # decorador original: @wg_async
    def waitEnterBlockersSatisfied(self):
        ...
    # decorador original: @wg_async
    def waitExitBlockersSatisfied(self):
        ...

class BlockingState(State, BlockingStateMixin):
    _blockerClearLifetimeStateID: Any
    def __init__(self, stateID, blockerClearLifetimeStateID, flags=...):
        ...
    def clear(self):
        ...

class BlockableTransition(StringEventTransition):
    _repostFuture: Any
    def __init__(self, token, priority=0):
        ...
    def clear(self):
        ...
    def execute(self, event):
        ...
    def _sourceAndTargetSatisfied(self):
        ...
    # decorador original: @wg_async
    def _repostWhenUnblocked(self, event):
        ...
