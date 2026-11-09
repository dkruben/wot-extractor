# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/events_containers/common/containers/listener.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from events_handler import EventsHandler as EventsHandler
from events_containers.common.containers.interfaces import IClientEventsContainerListener as IClientEventsContainerListener
from events_containers.common.containers.interfaces import IClientEventsContainer as IClientEventsContainer

class ContainersListener(EventsHandler, IClientEventsContainerListener):
    def subscribeTo(self, events, raiseException=False):
        ...
    def lateSubscribeTo(self, events):
        ...
