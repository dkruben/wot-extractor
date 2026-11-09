# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/HWVehicleAnomaliesComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/HWVehicleAnomaliesComponent.py
from __future__ import absolute_import
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

class HWVehicleAnomaliesComponent(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def _onAvatarReady(self):
        super(HWVehicleAnomaliesComponent, self)._onAvatarReady()
        self._notifyUsedAnomaliesChanged(self.usedAnomalies)

    def onDestroy(self):
        self._notifyUsedAnomaliesChanged([])
        super(HWVehicleAnomaliesComponent, self).onDestroy()

    @property
    def hwBattleGuiCtrl(self):
        return self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)

    def set_usedAnomalies(self, _):
        self._notifyUsedAnomaliesChanged(self.usedAnomalies)

    def _notifyUsedAnomaliesChanged(self, usedAnomalies):
        hwBattleGuiCtrl = self.hwBattleGuiCtrl
        if self.entity and self.entity.isPlayerVehicle and hwBattleGuiCtrl:
            hwBattleGuiCtrl.onUpdateUsedAnomalies(usedAnomalies)
