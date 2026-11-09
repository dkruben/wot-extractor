# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/HWVehicleDetector.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/HWVehicleDetector.py
from __future__ import absolute_import
from constants import BigWorld
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider

class HWVehicleDetector(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onDestroy(self):
        self.__fireEvent()
        vehStateCtrl = self.guiSessionProvider.shared.vehicleState
        if vehStateCtrl:
            vehStateCtrl.onVehicleControlling -= self._onVehicleControlling
        avatar = BigWorld.player()
        if avatar:
            avatar.onAvatarVehicleChanged -= self._onAvatarVehicleChanged
        super(HWVehicleDetector, self).onDestroy()

    def set_indicator(self, prev):
        self._onCheckDistanceToFollower()

    def _onAvatarReady(self):
        super(HWVehicleDetector, self)._onAvatarReady()
        vehStateCtrl = self.guiSessionProvider.shared.vehicleState
        if vehStateCtrl:
            vehStateCtrl.onVehicleControlling += self._onVehicleControlling
        avatar = BigWorld.player()
        if avatar:
            avatar.onAvatarVehicleChanged += self._onAvatarVehicleChanged
        self._onCheckDistanceToFollower()

    def _onVehicleControlling(self, vehicle):
        self._onCheckDistanceToFollower()

    def _onCheckDistanceToFollower(self):
        avatar = BigWorld.player()
        if not avatar:
            self.__fireEvent()
            return
        vehicle = avatar.getVehicleAttached()
        if not vehicle:
            self.__fireEvent()
            return
        if vehicle.id != self.entity.id:
            return
        self.__fireEvent(self.indicator)

    def _onAvatarVehicleChanged(self):
        self._onCheckDistanceToFollower()

    def __fireEvent(self, indicator=0):
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        if hwBattleGuiCtrl:
            ctx = {'indicator': indicator}
            hwBattleGuiCtrl.vehicleDetectorChangeDistance(ctx)
