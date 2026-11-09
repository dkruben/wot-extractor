# wot-extractor: codigo DESCOMPILADO de sources/res/last_stand/scripts/client/LSVehicleSoulsContainerComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: last_stand/scripts/client/LSVehicleSoulsContainerComponent.py
from __future__ import absolute_import
import BigWorld, Event
from helpers import dependency
from last_stand_common.last_stand_constants import LSSoulsChangeReason
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

class LSVehicleSoulsContainerComponent(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(LSVehicleSoulsContainerComponent, self).__init__()
        self.onChangeSoulsCount = Event.Event()

    def _onAvatarReady(self):
        super(LSVehicleSoulsContainerComponent, self)._onAvatarReady()
        from last_stand.gui.ls_gui_constants import BATTLE_CTRL_ID
        lsBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.LS_BATTLE_GUI_CTRL)
        if lsBattleGuiCtrl and self.entity.id == BigWorld.player().playerVehicleID:
            lsBattleGuiCtrl.onSoulsContainerReady(self)

    def set_lastCollected(self, _):
        _, reason = self.lastCollected
        self.onChangeSoulsCount(self.souls, reason)

    def set_capacity(self, _):
        self.onChangeSoulsCount(self.souls, LSSoulsChangeReason.CAPACITY)

    def onDestroy(self):
        self.onChangeSoulsCount.clear()
        super(LSVehicleSoulsContainerComponent, self).onDestroy()
