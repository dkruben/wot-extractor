# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/container_views/example_view_skeleton/controller.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/container_views/example_view_skeleton/controller.py
import typing
from Event import Event
from gui.impl.lobby.container_views.base.controllers import InteractionController
from gui.impl.lobby.container_views.example_view_skeleton.events import ExampleComponentViewEvents
from helpers import dependency
from skeletons.gui.lobby_context import ILobbyContext
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Any, Callable, List, Tuple
    from gui.impl.lobby.container_views.base.components import ComponentBase
    from gui.impl.lobby.container_views.base.events import ComponentEventsBase

class ExampleInteractionController(InteractionController):
    itemsCache = dependency.descriptor(IItemsCache)
    lobbyContext = dependency.descriptor(ILobbyContext)

    def _getEventsProvider(self):
        return ExampleComponentViewEvents()

    def _getEvents(self):
        return [
         (
          self.eventProvider.onMouseEnter, self._onMouseEnter),
         (
          self.eventProvider.onMouseLeave, self._onMouseLeave),
         (
          self.eventProvider.onSelected, self._onSelected),
         (
          self.itemsCache.onSyncCompleted, self.__onCacheResync),
         (
          self.lobbyContext.getServerSettings().onServerSettingsChange, self.__onServerSettingsChange)]

    def _onMouseEnter(self, source, *args, **kwargs):
        pass

    def _onMouseLeave(self, source, *args, **kwargs):
        pass

    def _onSelected(self, source, *args, **kwargs):
        source.setData({'title': 'Selected'})
        for component in self.view.components.values():
            if source.key != component.key:
                component.setData({'title': (('Book {} Not Selected').format(component.key))})

        self.refresh()

    def __onCacheResync(self, *args, **kwargs):
        pass

    def __onServerSettingsChange(self, diff):
        pass
