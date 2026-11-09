# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/system_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/system_events.py
from __future__ import absolute_import
from events_container import EventsContainer

class SystemEvents(EventsContainer):

    def __init__(self):
        super(SystemEvents, self).__init__()
        self.onBeforeSend = self._createEvent()
        self.onDependencyConfigReady = self._createEvent()
        self.onDependenciesReady = self._createEvent()
        self.onFestivityConfigReady = self._createEvent()


g_systemEvents = SystemEvents()
