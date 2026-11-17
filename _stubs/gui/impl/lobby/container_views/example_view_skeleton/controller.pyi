# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/container_views/example_view_skeleton/controller.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
import typing as typing
from Event import Event as Event
from gui.impl.lobby.container_views.base.controllers import InteractionController as InteractionController
from gui.impl.lobby.container_views.example_view_skeleton.events import ExampleComponentViewEvents as ExampleComponentViewEvents
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from typing import Any as Any, Callable as Callable, List as List, Tuple as Tuple
from gui.impl.lobby.container_views.base.components import ComponentBase as ComponentBase
from gui.impl.lobby.container_views.base.events import ComponentEventsBase as ComponentEventsBase

class ExampleInteractionController(InteractionController):
    itemsCache: _Any
    lobbyContext: _Any
    def _getEventsProvider(self):
        ...
    def _getEvents(self):
        ...
    def _onMouseEnter(self, source, *args, **kwargs):
        ...
    def _onMouseLeave(self, source, *args, **kwargs):
        ...
    def _onSelected(self, source, *args, **kwargs):
        ...
    def __onCacheResync(self, *args, **kwargs):
        ...
    def __onServerSettingsChange(self, diff):
        ...
