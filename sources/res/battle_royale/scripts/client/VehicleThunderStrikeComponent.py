# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/VehicleThunderStrikeComponent.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/VehicleThunderStrikeComponent.py
from __future__ import absolute_import
from gui.Scaleform.genConsts.BATTLE_MARKER_STATES import BATTLE_MARKER_STATES
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from VehicleAbilityBaseComponent import VehicleAbilityBaseComponent
from battle_royale.gui.constants import BattleRoyaleEquipments

class VehicleThunderStrikeComponent(VehicleAbilityBaseComponent):
    __TIMER_VIEW_ID = VEHICLE_VIEW_STATE.THUNDER_STRIKE
    __MARKER_ID = BATTLE_MARKER_STATES.THUNDER_STRIKE_STATE

    def __init__(self):
        self.__id = id(self)
        super(VehicleThunderStrikeComponent, self).__init__(self.__TIMER_VIEW_ID, self.__MARKER_ID)

    def _updateTimer(self, data):
        data['id'] = self.__id
        super(VehicleThunderStrikeComponent, self)._updateTimer(data)

    def _getDuration(self):
        return self._getEquipment(BattleRoyaleEquipments.THUNDER_STRIKE).duration
