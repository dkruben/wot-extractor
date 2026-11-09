# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/client/VehicleLoot.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/client/VehicleLoot.py
from __future__ import absolute_import
import BigWorld
from constants import LootAction
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from debug_utils import LOG_DEBUG_DEV

class VehicleLoot(BigWorld.DynamicScriptComponent):

    def __invalidateState(self, action, time):
        LOG_DEBUG_DEV('__invalidateState', self.lootID, self.lootTypeID, action, time)
        self.entity.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.LOOT, (self.lootID, self.lootTypeID, action, time))

    def __init__(self):
        super(VehicleLoot, self).__init__()
        if self.pickupTotalTime:
            totalTime = self.pickupTotalTime
        else:
            totalTime = max(self.pickupEndTime - BigWorld.serverTime(), 0)
        self.__invalidateState(LootAction.PICKUP_STARTED, totalTime)

    def onDestroy(self):
        if self.pickupEndTime > 0:
            self.__invalidateState(LootAction.PICKUP_FAILED, 0)
        else:
            self.__invalidateState(LootAction.PICKUP_SUCCEEDED, 0)
