# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/VehicleHealingComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/VehicleHealingComponent.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent
from battle_royale.gui.constants import BattleRoyaleEquipments

class VehicleHealingComponent(VehicleAbilityBaseComponent):
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.HEALING
    __MARKER_ID = BATTLE_MARKER_STATES.HEALING_STATE

    def __init__(self):
        self._isDestroying = False
        super(VehicleHealingComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)

    def set_isInactivation(self, prev):
        self._updateVisuals()

    def _updateTimer(self, data):
        data.update(self._getHealingArgs())
        super(VehicleHealingComponent, self)._updateTimer(data)

    def _updateMarker(self, data, isHide=False):
        data.update({'isSourceVehicle': (self.isSourceVehicle)})
        super(VehicleHealingComponent, self)._updateMarker(data, isHide)

    def _destroy(self):
        self._isDestroying = True
        super(VehicleHealingComponent, self)._destroy()

    def _getDuration(self):
        return self._getEquipment(BattleRoyaleEquipments.HEAL_POINT).duration

    def _getHealingArgs(self):
        return {'isInactivation': (self.isInactivation), 
           'isSourceVehicle': (self.isSourceVehicle), 
           'isDestroying': (self._isDestroying), 
           'senderKey': (BattleRoyaleEquipments.HEAL_POINT)}
