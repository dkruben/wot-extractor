# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/VehicleSkillCounter.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/VehicleSkillCounter.py
from __future__ import absolute_import
from script_component.DynamicScriptComponent import DynamicScriptComponent

class VehicleSkillCounter(DynamicScriptComponent):

    def set_counterValue(self, prev):
        if self._isAvatarReady:
            self.__updateCounter()

    def _onAvatarReady(self):
        self.__updateCounter()

    def __updateCounter(self):
        from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
        g_eventBus.handleEvent(events.RoleSkillEvent(events.RoleSkillEvent.COUNTER_CHANGED, {'value': (self.counterValue)}), scope=EVENT_BUS_SCOPE.BATTLE)
