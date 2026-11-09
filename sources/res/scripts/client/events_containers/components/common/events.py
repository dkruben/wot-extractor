# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/events_containers/components/common/events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/events_containers/components/common/events.py
from __future__ import absolute_import
import weakref
from events_containers.common.containers import ClientEventsContainerDebugger

class ClientComponentEventsDebugger(ClientEventsContainerDebugger):
    _EVENTS_DEBUG_PREFIX = ''

    def __init__(self, events, component):
        super(ClientComponentEventsDebugger, self).__init__(events)
        self.__componentRef = weakref.ref(component)
        self.__entityID = component.entity.id

    def _getDebugPrefix(self):
        return ('[{}][{}][{}]').format(self._EVENTS_DEBUG_PREFIX, self.__entityID, self.__componentRef())
