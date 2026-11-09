# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/events_containers/common/containers/events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from Event import LateEvent as LateEvent
from events_containers.common.containers.interfaces import IClientEventsContainer as IClientEventsContainer
from events_containers.common.containers.listener import ContainersListener as ContainersListener
from events_container import EventsContainer as EventsContainer
from events_debugger import EventsDebugger as EventsDebugger

class ClientEventsContainer(EventsContainer, IClientEventsContainer):
    @property
    def hasListeners(self):
        ...
    def _createLateEvent(self, lateCallback):
        ...
    def _createTimeIntervalEvent(self, interval, timeCallback=None):
        ...
    def _createCoreIntegration(self):
        ...
    def _createEventsDebugger(self):
        ...

class ClientEventsContainerCoreIntegration(ContainersListener):
    def __init__(self, events):
        ...
    def _attachToEventsContainer(self, events):
        ...

class ClientEventsContainerDebugger(EventsDebugger):
    IGNORED_EVENTS: tuple
    def _getDebugPrefix(self):
        ...
    def _shouldHandle(self, eventName):
        ...
