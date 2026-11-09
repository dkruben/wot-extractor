# wot-extractor: codigo DESCOMPILADO de sources/res/halloween/scripts/client/HWVehicleStatusNotificationComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: halloween/scripts/client/HWVehicleStatusNotificationComponent.py
from __future__ import absolute_import
import BigWorld
from helpers import dependency
from script_component.DynamicScriptComponent import DynamicScriptComponent
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE

class HWVehicleStatusNotificationComponent(DynamicScriptComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(HWVehicleStatusNotificationComponent, self).__init__()
        player = BigWorld.player()
        self._isPlayerVehicle = player.vehicle and player.vehicle.id == self.entity.id
        if self._isPlayerVehicle:
            self._state = getattr(VEHICLE_VIEW_STATE, self.vehicleViewState, None)
            if self._state:
                self.guiSessionProvider.invalidateVehicleState(self._state, *self.initArgs)
        return

    def onDestroy(self):
        if self._isPlayerVehicle:
            self.guiSessionProvider.invalidateVehicleState(self._state, *self.finiArgs)
