# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/HWVehicleMaxHealthModifierComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/HWVehicleMaxHealthModifierComponent.py
from __future__ import absolute_import
import BigWorld
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from script_component.DynamicScriptComponent import DynamicScriptComponent
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class HWVehicleMaxHealthModifierComponent(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    @property
    def hwBattleGuiCtrl(self):
        return self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)

    def set_maxHealth(self, _):
        if self.hwBattleGuiCtrl:
            self.hwBattleGuiCtrl.onVehicleMaxHealthChanged(self.entity.id, self.entity.maxHealth)
        BigWorld.player().guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.HW_MAX_HEALTH, self.entity.maxHealth, self.entity.id)
        BigWorld.player().guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.HEALTH, self.entity.health, self.entity.id)
