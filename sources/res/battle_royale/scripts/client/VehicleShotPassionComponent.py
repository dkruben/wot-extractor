# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/VehicleShotPassionComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/VehicleShotPassionComponent.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from battle_royale.gui.constants import BattleRoyaleEquipments
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent

class VehicleShotPassionComponent(VehicleAbilityBaseComponent):
    EQUIPMENT_NAME = BattleRoyaleEquipments.SHOT_PASSION
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.SHOT_PASSION
    __MARKER_ID = BATTLE_MARKER_STATES.SHOT_PASSION_STATE

    def __init__(self):
        super(VehicleShotPassionComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)

    def set_stage(self, prev):
        self._updateTimer(None)
        return

    def getInfo(self):
        data = self._getTimerData()
        data['stage'] = self.stage
        return data

    def _updateTimer(self, data):
        if data is None:
            data = self._getTimerData()
        data['stage'] = self.stage
        super(VehicleShotPassionComponent, self)._updateTimer(data)
        self._guiSessionProvider.shared.vehicleState.onEquipmentComponentUpdated(self.EQUIPMENT_NAME, self.entity.id, data)
        return

    def _getDuration(self):
        return self._getEquipment(BattleRoyaleEquipments.SHOT_PASSION).duration
