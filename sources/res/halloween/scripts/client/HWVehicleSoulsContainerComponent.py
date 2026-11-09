# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/HWVehicleSoulsContainerComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/HWVehicleSoulsContainerComponent.py
from __future__ import absolute_import
import BigWorld, Event
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

class HWVehicleSoulsContainerComponent(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(HWVehicleSoulsContainerComponent, self).__init__()
        self.onChangeSoulsCount = Event.Event()

    def _onAvatarReady(self):
        super(HWVehicleSoulsContainerComponent, self)._onAvatarReady()
        from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        if hwBattleGuiCtrl and self.entity.id == BigWorld.player().playerVehicleID:
            hwBattleGuiCtrl.onSoulsContainerReady(self)

    def set_capacity(self, _):
        self.onChangeSoulsCount(self.souls, 0)

    def set_lastCollected(self, _):
        _, reason = self.lastCollected
        self.onChangeSoulsCount(self.souls, reason)

    def onDestroy(self):
        self.onChangeSoulsCount.clear()
        super(HWVehicleSoulsContainerComponent, self).onDestroy()
