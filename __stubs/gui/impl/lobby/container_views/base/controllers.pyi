# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/container_views/base/controllers.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from Event import Event as Event
from helpers import dependency as dependency
from gui.impl.lobby.container_views.base.events import ComponentEventsBase as ComponentEventsBase
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Callable as Callable, List as List, Tuple as Tuple

class InteractionController(object):
    itemsCache: Any
    __eventsProvider: Any
    __view: Any
    def __init__(self, view=None):
        ...
    @property
    def context(self):
        ...
    @property
    def eventsProvider(self):
        ...
    @property
    def view(self):
        ...
    def subscribe(self):
        ...
    def unsubscribe(self):
        ...
    def refresh(self):
        ...
    def _getEventsProvider(self):
        ...
    def _getEvents(self):
        ...
