# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarVehiclesInfo.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarVehiclesInfo.py
from __future__ import absolute_import
import BigWorld
from Vehicle import Vehicle
from AvatarVehiclesInfoBase import AvatarVehiclesInfoBase

class AvatarVehiclesInfo(AvatarVehiclesInfoBase):

    def setVehInfo_isAlive(self, vehInfo, diff):
        vehID = vehInfo['vehicleID']
        if BigWorld.entities.get(vehID) is None and diff.new and not diff.prev:
            Vehicle.respawnVehicle(vehID, vehInfo['compDescr'], vehInfo['outfitCD'])
        super(AvatarVehiclesInfo, self).setVehInfo_isAlive(vehInfo, diff)
        return
