# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/requesters/vehicle_rotation_requester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/vehicle_rotation_requester.py
from __future__ import absolute_import
import BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IVehicleRotationRequester

class VehicleRotationRequester(AbstractSyncDataRequester, IVehicleRotationRequester):

    def getBattlesCount(self, groupNum):
        battlesCount = self._groupLocks['groupBattles']
        groupIdx = max(0, groupNum - 1)
        if len(battlesCount) > groupIdx:
            return battlesCount[groupIdx]
        return -1

    def isGroupLocked(self, groupNum):
        if groupNum == 0:
            return False
        groupsLocks = self._groupLocks['isGroupLocked']
        groupIdx = max(0, groupNum - 1)
        if len(groupsLocks) > groupIdx:
            return groupsLocks[groupIdx]
        return False

    def getGroupNum(self, vehIntCD):
        return self.getCacheValue('vehiclesGroupMapping', {}).get(vehIntCD, 0)

    def isInfinite(self, groupNum):
        return self.getBattlesCount(groupNum) == -1

    def unlockedBy(self, groupNum):
        playGroupsToUnlock = self._groupLocks['unlockedBy']
        return playGroupsToUnlock.get(groupNum, -1)

    @property
    def _groupLocks(self):
        return self.getCacheValue('groupLocks', {'groupBattles': [], 'isGroupLocked': [], 'unlockedBy': {}})

    def _requestCache(self, callback=None):
        BigWorld.player().vehicleRotation.getCache((lambda resID, value: self._response(resID, value, callback)))
