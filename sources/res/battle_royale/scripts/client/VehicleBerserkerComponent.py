# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/VehicleBerserkerComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/VehicleBerserkerComponent.py
from __future__ import absolute_import
from battle_royale.gui.constants import BattleRoyaleEquipments
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent

class VehicleBerserkerComponent(VehicleAbilityBaseComponent):
    __EQUIPMENT_NAME = BattleRoyaleEquipments.BERSERKER
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.BERSERKER
    __MARKER_ID = BATTLE_MARKER_STATES.BERSERKER_STATE

    def __init__(self):
        self.__id = id(self)
        super(VehicleBerserkerComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)

    def _updateTimer(self, data):
        data['tickInterval'] = self.tickInterval
        super(VehicleBerserkerComponent, self)._updateTimer(data)
        self.entity.guiSessionProvider.shared.vehicleState.onEquipmentComponentUpdated(self.__EQUIPMENT_NAME, self.entity.id, data)
