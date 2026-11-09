# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/events_containers/common/containers/events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/events_containers/common/containers/events.py
from __future__ import absolute_import
from Event import LateEvent
from events_containers.common.containers.interfaces import IClientEventsContainer
from events_containers.common.containers.listener import ContainersListener
from events_container import EventsContainer
from events_debugger import EventsDebugger

class ClientEventsContainer(EventsContainer, IClientEventsContainer):

    @property
    def hasListeners(self):
        return self._eventManager.hasAnyListener

    def _createLateEvent(self, lateCallback):
        return LateEvent(lateCallback, self._eventManager)

    def _createTimeIntervalEvent(self, interval, timeCallback=None):
        from gui.shared.utils.TimeInterval import TimeIntervalEvent
        return TimeIntervalEvent(interval, timeCallback, self._eventManager)

    def _createCoreIntegration(self):
        return ClientEventsContainerCoreIntegration(self)

    def _createEventsDebugger(self):
        return ClientEventsContainerDebugger(self)


class ClientEventsContainerCoreIntegration(ContainersListener):

    def __init__(self, events):
        self._attachToEventsContainer(events)

    def _attachToEventsContainer(self, events):
        self.subscribeTo(events)


class ClientEventsContainerDebugger(EventsDebugger):
    IGNORED_EVENTS = ('onEventsContainerDestroy', )

    def _getDebugPrefix(self):
        return '[CLIENT_EVENT]'

    def _shouldHandle(self, eventName):
        return eventName not in self.IGNORED_EVENTS
