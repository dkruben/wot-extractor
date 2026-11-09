# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/avatar_components/VehiclesSpawnListStorage.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/avatar_components/VehiclesSpawnListStorage.py
from __future__ import absolute_import
import logging
from future.moves import pickle
from Event import Event
from VehiclesSpawnListStorageCommon import convertTuplesToVehicleSpawnData
_logger = logging.getLogger(__name__)

class VehiclesSpawnListStorage(object):

    def __init__(self):
        super(VehiclesSpawnListStorage, self).__init__()
        self.onSpawnListUpdated = Event()

    def handleKey(self, isDown, key, mods):
        pass

    def onBecomePlayer(self):
        pass

    def onBecomeNonPlayer(self):
        pass

    def updateSpawnList(self, spawnListData):
        spawnList = convertTuplesToVehicleSpawnData(pickle.loads(spawnListData))
        self.onSpawnListUpdated(spawnList)
