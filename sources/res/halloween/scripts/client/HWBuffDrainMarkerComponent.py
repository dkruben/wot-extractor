# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/HWBuffDrainMarkerComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/HWBuffDrainMarkerComponent.py
from __future__ import absolute_import
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID
from skeletons.gui.battle_session import IBattleSessionProvider

class HWBuffDrainMarkerComponent(DynamicScriptComponent):
    _guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onDestroy(self):
        self.__updateMarkerIcon(False)
        super(HWBuffDrainMarkerComponent, self).onDestroy()

    def set_isActive(self, prev):
        self.__updateMarkerIcon(self.isActive)

    def _onAvatarReady(self):
        super(HWBuffDrainMarkerComponent, self)._onAvatarReady()
        self.__updateMarkerIcon(self.isActive)

    def __updateMarkerIcon(self, visible):
        if not self.entity.isPlayerVehicle:
            hwBattleGuiCtrl = self._guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
            if hwBattleGuiCtrl:
                hwBattleGuiCtrl.onBossAuraVictimMarkerIcon(self.entity, visible)
