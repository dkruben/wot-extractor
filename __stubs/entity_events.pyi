# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/common/entity_events.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
from events_handler import EventsHandler as EventsHandler
from events_container import EventsContainer as EventsContainer
from debug_utils import LOG_ERROR as LOG_ERROR
from constants import IS_DEVELOPMENT as IS_DEVELOPMENT
import BigWorld as BigWorld
from Event import SafeEvent as SafeEvent

class EntityEventsCoreIntegration(EventsHandler):
    spaceID: Any
    entityID: Any
    entityGO: Any
    def __init__(self, entity):
        ...

class EntityEvents(EventsContainer):
    __slots__: tuple
    _entityRef: Any
    onDynComponentGroupAdded: Any
    onDynComponentGroupRemoved: Any
    def __init__(self, entity=None):
        ...
    def createEvent(self):
        ...
    def _createCoreIntegration(self):
        ...
    def _createIntegrationInstance(self, entity):
        ...
