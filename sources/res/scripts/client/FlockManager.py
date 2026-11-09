# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/FlockManager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/FlockManager.py
from __future__ import absolute_import
import BigWorld, Math
g_FlockManager = None

def getManager():
    global g_FlockManager
    if g_FlockManager is None:
        g_FlockManager = FlockManager()
    return g_FlockManager


_FLOCK_ENABLED = True

class FlockManager(object):

    def __init__(self):
        if _FLOCK_ENABLED:
            self.__flockManager = BigWorld.WGFlockManager()
            self.__flocks = []
            self.__flockManager.onTriggerCallback = self.__onTrigger

    def start(self, player):
        if _FLOCK_ENABLED:
            player.onVehicleEnterWorld += self.__onVehicleEnter
            player.onVehicleLeaveWorld += self.__onVehicleLeave

    def stop(self, player):
        if _FLOCK_ENABLED:
            self.__flockManager.stop()
            player.onVehicleEnterWorld -= self.__onVehicleEnter
            player.onVehicleLeaveWorld -= self.__onVehicleLeave
            self.__flocks = []

    def onSpaceLoaded(self):
        if _FLOCK_ENABLED:
            self.__flockManager.start(1.0)

    def onProjectile(self, position):
        if _FLOCK_ENABLED:
            self.__flockManager.addActivationPoint(Math.Vector2(position.x, position.z))

    def addFlock(self, position, radius, explosionRadius, respawnTime, flock):
        if _FLOCK_ENABLED:
            self.__flocks.append(flock)
            self.__flockManager.addFlock(Math.Vector2(position.x, position.z), len(self.__flocks) - 1, radius, explosionRadius, respawnTime)

    def __onVehicleEnter(self, vehicle):
        self.__flockManager.vehicleEnter(vehicle.matrix)

    def __onVehicleLeave(self, vehicle):
        self.__flockManager.vehicleLeave(vehicle.matrix)

    def __onTrigger(self, flockId):
        self.__flocks[flockId].onTrigger()
