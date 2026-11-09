# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/events_containers/common/containers/listener.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/events_containers/common/containers/listener.py
from __future__ import absolute_import
import typing
from events_handler import EventsHandler
from events_containers.common.containers.interfaces import IClientEventsContainerListener
if typing.TYPE_CHECKING:
    from events_containers.common.containers.interfaces import IClientEventsContainer

class ContainersListener(EventsHandler, IClientEventsContainerListener):

    def subscribeTo(self, events, raiseException=False):
        super(ContainersListener, self).subscribeTo(events, raiseException)

    def lateSubscribeTo(self, events):
        if events is not None:
            events.lateSubscribe(self)
        return
