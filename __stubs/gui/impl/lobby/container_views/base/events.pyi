# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/container_views/base/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from functools import partial as partial
from Event import Event as Event
from debug_utils import LOG_DEBUG_DEV as LOG_DEBUG_DEV
from events_container import EventsContainer as EventsContainer
from events_debugger import EventsDebugger as EventsDebugger

class EventsProviderSourceProxy(object):
    __component: Any
    __eventsProvider: Any
    def __init__(self, component, eventsProvider):
        ...
    def __getattr__(self, name):
        ...
    def _proxy(self, method):
        ...

class ContainerLifecycleEvents(EventsContainer):
    onLoading: Any
    onLoaded: Any
    initialize: Any
    finalize: Any
    onReady: Any
    onShown: Any
    onHidden: Any
    onFocus: Any
    swapStates: Any
    swapShowingStates: Any
    _debugger: Any
    def __init__(self):
        ...
    def debugEvents(self):
        ...
    def events(self):
        ...

class ComponentEventsBase(EventsContainer):
    onMouseEnter: Any
    onMouseLeave: Any
    logClick: Any
    _debugger: Any
    def __init__(self):
        ...
    def debugEvents(self):
        ...
    def events(self):
        ...

class ContainerLifecycleEventsDebugger(EventsDebugger):
    def __init__(self, events):
        ...
    def _getDebugPrefix(self):
        ...
    def _logEvent(self, event, *args, **kwargs):
        ...

class ComponentEventsDebugger(ContainerLifecycleEventsDebugger):
    def _getDebugPrefix(self):
        ...
