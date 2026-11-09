# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/VehicleSelfBuffComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/VehicleSelfBuffComponent.py
from __future__ import absolute_import
import BigWorld
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from battle_royale.gui.constants import BattleRoyaleEquipments
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent

class VehicleSelfBuffComponent(VehicleAbilityBaseComponent):
    EQUIPMENT_NAME = BattleRoyaleEquipments.SELF_BUFF
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.INSPIRE
    __MARKER_ID = BATTLE_MARKER_STATES.INSPIRING_STATE

    def __init__(self):
        super(VehicleSelfBuffComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)

    def _updateTimer(self, data):
        duration = self._getDuration()
        isHide = self.entity.id != BigWorld.player().getObservedVehicleID() or duration == 0
        data['endTime'] = 0.0 if isHide else self.finishTime
        data['isInactivation'] = None if isHide else duration > 0
        data['isSourceVehicle'] = True
        super(VehicleSelfBuffComponent, self)._updateTimer(data)
        return

    def _getDuration(self):
        return self._getEquipment(self.EQUIPMENT_NAME).duration
