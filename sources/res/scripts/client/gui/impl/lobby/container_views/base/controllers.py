# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/container_views/base/controllers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/container_views/base/controllers.py
import typing
from Event import Event
from helpers import dependency
from gui.impl.lobby.container_views.base.events import ComponentEventsBase
from skeletons.gui.shared import IItemsCache
if typing.TYPE_CHECKING:
    from typing import Callable, List, Tuple

class InteractionController(object):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, view=None):
        self.__eventsProvider = self._getEventsProvider()
        self.__view = view

    @property
    def context(self):
        return self.view.context

    @property
    def eventsProvider(self):
        return self.__eventsProvider

    @property
    def view(self):
        return self.__view

    def subscribe(self):
        for event, handler in self._getEvents():
            event += handler

    def unsubscribe(self):
        for event, handler in self._getEvents():
            event -= handler

    def refresh(self):
        self.view.refresh()

    def _getEventsProvider(self):
        raise NotImplementedError

    def _getEvents(self):
        return []
