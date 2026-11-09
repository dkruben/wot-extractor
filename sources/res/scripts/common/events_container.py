# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/events_container.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/events_container.py
from __future__ import absolute_import
import typing
from Event import Event, SafeEvent, EventManager, ContextEvent
from synchronous_event import SynchronousEvent
from events_debugger import EventsDebugger
if typing.TYPE_CHECKING:
    from events_handler import EventsHandler

class EventsContainer(object):
    __slots__ = ('_eventManager', '_debugger', '_coreIntegration', 'onEventsContainerDestroy')

    def __init__(self):
        self._eventManager = EventManager()
        self.onEventsContainerDestroy = self._createEvent()
        self._coreIntegration = None
        self._debugger = None
        return

    def attachCoreEvents(self):
        self._coreIntegration = self._coreIntegration or self._createCoreIntegration()

    def clear(self):
        self._eventManager.clear()

    def destroy(self):
        self.onEventsContainerDestroy(self)
        self._coreIntegration = None
        self._debugger = None
        self.clear()
        return

    def debugEvents(self):
        self._debugger = self._debugger or self._createEventsDebugger()

    def _createEvent(self):
        return SafeEvent(self._eventManager)

    def _createSynchronousEvent(self):
        return SynchronousEvent(self._eventManager)

    def _createUnsafeEvent(self):
        return Event(self._eventManager)

    def _createContextEvent(self):
        return ContextEvent(self._eventManager)

    def _createEventsDebugger(self):
        return EventsDebugger(self)

    def _createCoreIntegration(self):
        return
