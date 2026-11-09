# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/shared/utils/requesters/recycle_bin_requester.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/shared/utils/requesters/recycle_bin_requester.py
from __future__ import absolute_import
from collections import namedtuple
from future.utils import viewitems
import BigWorld
from ItemRestore import RESTORE_VEHICLE_TYPE
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from helpers import time_utils
from skeletons.gui.shared.utils.requesters import IRecycleBinRequester
_VehicleRestoreInfo = namedtuple('_VehicleRestoreInfo', ('restoreType', 'changedAt',
                                                         'restoreDuration', 'restoreCooldown'))

class VehicleRestoreInfo(_VehicleRestoreInfo):

    def getRestoreTimeLeft(self):
        if self.changedAt:
            return max(self.restoreDuration - self.__getTimeGone(), 0)
        return 0

    def getRestoreCooldownTimeLeft(self):
        if self.changedAt:
            return max(self.restoreCooldown - self.__getTimeGone(), 0)
        return 0

    def isLimited(self):
        return self.restoreType == RESTORE_VEHICLE_TYPE.PREMIUM and self.changedAt != 0

    def isInCooldown(self):
        if self.changedAt:
            return self.restoreType == RESTORE_VEHICLE_TYPE.ACTION and self.getRestoreCooldownTimeLeft() > 0
        return False

    def isUnlimited(self):
        return self.restoreType == RESTORE_VEHICLE_TYPE.ACTION and self.changedAt == 0

    def isRestorePossible(self):
        return self.restoreType == RESTORE_VEHICLE_TYPE.ACTION or self.isLimited() and self.getRestoreTimeLeft() > 0

    def __getTimeGone(self):
        if self.changedAt:
            return float(time_utils.getTimeDeltaTillNow(time_utils.makeLocalServerTime(self.changedAt)))
        return 0


class RecycleBinRequester(AbstractSyncDataRequester, IRecycleBinRequester):

    @property
    def recycleBin(self):
        return self.getCacheValue('recycleBin', {})

    @property
    def vehiclesBuffer(self):
        return self.recycleBin.get('vehicles', {}).get('buffer', {})

    def getVehicleRestoreInfo(self, intCD, restoreDuration, restoreCooldown):
        restoreData = self.vehiclesBuffer.get(intCD)
        if restoreData:
            restoreType, changedAt = restoreData
            return VehicleRestoreInfo(restoreType, changedAt, restoreDuration, restoreCooldown)
        else:
            return

    def getVehiclesIntCDs(self):
        return list(self.vehiclesBuffer)

    def getTankmen(self, maxDuration):
        filteredBuffer = {}
        tankmenBuffer = self.recycleBin.get('tankmen', {}).get('buffer', {})
        for tankmanId, (strCD, dismissedAt) in viewitems(tankmenBuffer):
            if time_utils.getTimeDeltaTillNow(dismissedAt) < maxDuration:
                filteredBuffer[tankmanId] = (
                 strCD, dismissedAt)

        return filteredBuffer

    def getTankman(self, invID, maxDuration):
        return self.getTankmen(maxDuration).get(invID)

    def _requestCache(self, callback=None):
        BigWorld.player().recycleBin.getCache((lambda resID, value: self._response(resID, value, callback)))
