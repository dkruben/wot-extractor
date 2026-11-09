# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/shared/event_bus.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import functools as functools
import heapq as heapq
import logging as logging
from collections import defaultdict as defaultdict
from future.utils import viewvalues as viewvalues
from BWUtil import AsyncReturn as AsyncReturn
from debug_utils import LOG_CURRENT_EXCEPTION as LOG_CURRENT_EXCEPTION
from adisp import adisp_process as adisp_process, isAsync as isAsync
from shared_utils import safeExecute as safeExecute
from wg_async import wg_async as wg_async, wg_await as wg_await, await_callback as await_callback, isWgAsync as isWgAsync
_logger: Any
SharedEventType: Any

class EVENT_BUS_SCOPE(object):
    GLOBAL = 0
    LOBBY = 1
    STATS = 2
    BATTLE = 3
    STRONGHOLD = 4
    DEFAULT = GLOBAL
    ALL: tuple

class EventPriority(object):
    HIGH = 0
    LOW = 1
    VERY_LOW = 2
    DEFAULT = LOW

class _PriorityQueue(object):
    _queue: Any
    _finder: Any
    def __init__(self):
        ...
    def add(self, item, priority):
        ...
    def remove(self, item):
        ...
    def __contains__(self, item):
        ...
    def __iter__(self):
        ...

class EventBus(object):
    __slots__: tuple
    __handlers: Any
    __restrictions: Any
    def __init__(self):
        ...
    def addListener(self, eventType, handler, scope=..., priority=...):
        ...
    def removeListener(self, eventType, handler, scope=...):
        ...
    def addRestriction(self, eventType, restriction, scope=..., priority=...):
        ...
    def removeRestriction(self, eventType, restriction, scope=...):
        ...
    # decorador original: @wg_async
    def handleEvent(self, event, scope=...):
        ...
    def clear(self):
        ...
    # decorador original: @wg_async
    def __verify(self, event, scope):
        ...
    # decorador original: @adisp_process
    def __verifyAsyncProcess(self, restriction, event, callback=None):
        ...

class SharedEvent(object):
    __hash__: Any
    eventType: Any
    def __init__(self, eventType=None):
        ...
    def __eq__(self, other):
        ...
