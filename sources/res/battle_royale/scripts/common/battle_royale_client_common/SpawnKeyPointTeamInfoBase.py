# wot-extractor: codigo DESCOMPILADO de sources/res/battle_royale/scripts/common/battle_royale_client_common/SpawnKeyPointTeamInfoBase.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: battle_royale/scripts/common/battle_royale_client_common/SpawnKeyPointTeamInfoBase.py
from __future__ import absolute_import
import Event

class SpawnKeyPointTeamInfoBase(object):

    def __init__(self):
        super(SpawnKeyPointTeamInfoBase, self).__init__()
        self.__placed = self.isVehiclePlaced()
        self.__em = em = Event.EventManager()
        self.onReceiveAvailableSpawnKeyPoints = Event.Event(em)
        self.onReceiveTeamSpawnKeyPoints = Event.Event(em)
        self.onReceiveSpawnKeyPointsCloseTime = Event.Event(em)
        self.onCloseChooseSpawnKeyPointsWindow = Event.Event(em)

    def _avatar(self):
        pass

    def onDestroy(self):
        self.__em.clear()

    def _doLog(self, msg):
        pass

    def set_availableSpawnKeyPoints(self, prev):
        self.onReceiveAvailableSpawnKeyPoints(self.availableSpawnKeyPoints)

    def set_teamSpawnKeyPoints(self, prev):
        if self.__placed:
            return
        self.__placed = self.isVehiclePlaced()
        if self.__placed:
            self.onCloseChooseSpawnKeyPointsWindow()
            return
        self.onReceiveTeamSpawnKeyPoints(self.teamSpawnKeyPoints)

    def set_spawnKeyPointsCloseTime(self, prev):
        self.onReceiveSpawnKeyPointsCloseTime(self.spawnKeyPointsCloseTime)

    @property
    def placed(self):
        return self.__placed

    def isVehiclePlaced(self):
        vehicleID = self._avatar().playerVehicleID
        for keyPoint in self.teamSpawnKeyPoints:
            if keyPoint.vehID == vehicleID:
                return keyPoint.placed

        return False
