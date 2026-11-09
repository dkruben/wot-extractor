# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_core/scripts/client/VehicleRoleSkill.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_core/scripts/client/VehicleRoleSkill.py
from __future__ import absolute_import
from helpers import fixed_dict
from script_component.DynamicScriptComponent import DynamicScriptComponent

class VehicleRoleSkill(DynamicScriptComponent):

    def set_roleEquipmentState(self, prev):
        if self._isAvatarReady:
            self.__updateRoleEquipmentState(prev)

    def _onAvatarReady(self):
        self.__updateRoleEquipmentState()

    def __updateRoleEquipmentState(self, previousState=None):
        from gui.shared import g_eventBus, events, EVENT_BUS_SCOPE
        ctx = {'state': (fixed_dict.getRoleEquipmentState(self.roleEquipmentState)), 
           'previousState': (fixed_dict.getRoleEquipmentState(previousState) if previousState is not None else None)}
        g_eventBus.handleEvent(events.RoleSkillEvent(events.RoleSkillEvent.STATE_CHANGED, ctx), scope=EVENT_BUS_SCOPE.BATTLE)
        return
