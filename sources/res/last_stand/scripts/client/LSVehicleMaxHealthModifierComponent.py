# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/LSVehicleMaxHealthModifierComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/LSVehicleMaxHealthModifierComponent.py
from __future__ import absolute_import
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from skeletons.gui.battle_session import IBattleSessionProvider
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent

class LSVehicleMaxHealthModifierComponent(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def set_maxHealth(self, _):
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.LS_MAX_HEALTH, self.entity.maxHealth, self.entity.id)
        self.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.HEALTH, self.entity.health, self.entity.id)
