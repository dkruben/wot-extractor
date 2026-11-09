# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/framework/entities/EventSystemEntity.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/framework/entities/EventSystemEntity.py
from __future__ import absolute_import
from gui.Scaleform.framework.entities.DisposableEntity import DisposableEntity
from gui.shared import g_eventBus, EVENT_BUS_SCOPE, EventPriority

class EventSystemEntity(DisposableEntity):

    def fireEvent(self, event, scope=EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.handleEvent(event, scope=scope)

    def addListener(self, eventType, handler, scope=EVENT_BUS_SCOPE.DEFAULT, priority=EventPriority.DEFAULT):
        g_eventBus.addListener(eventType, handler, scope=scope, priority=priority)

    def removeListener(self, eventType, handler, scope=EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.removeListener(eventType, handler, scope)

    def addRestriction(self, eventType, restriction, scope=EVENT_BUS_SCOPE.DEFAULT, priority=EventPriority.DEFAULT):
        g_eventBus.addRestriction(eventType, restriction, scope=scope, priority=priority)

    def removeRestriction(self, eventType, restriction, scope=EVENT_BUS_SCOPE.DEFAULT):
        g_eventBus.removeRestriction(eventType, restriction, scope)
