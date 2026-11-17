# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/events_container.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event, SafeEvent as SafeEvent, EventManager as EventManager, ContextEvent as ContextEvent
from synchronous_event import SynchronousEvent as SynchronousEvent
from events_debugger import EventsDebugger as EventsDebugger
from events_handler import EventsHandler as EventsHandler

class EventsContainer(object):
    __slots__: tuple
    _eventManager: Any
    onEventsContainerDestroy: Any
    _coreIntegration: Any
    _debugger: Any
    def __init__(self):
        ...
    def attachCoreEvents(self):
        ...
    def clear(self):
        ...
    def destroy(self):
        ...
    def debugEvents(self):
        ...
    def _createEvent(self):
        ...
    def _createSynchronousEvent(self):
        ...
    def _createUnsafeEvent(self):
        ...
    def _createContextEvent(self):
        ...
    def _createEventsDebugger(self):
        ...
    def _createCoreIntegration(self):
        ...
