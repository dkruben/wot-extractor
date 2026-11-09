# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/DynamicCameras/twin_gun_camera.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/DynamicCameras/twin_gun_camera.py
from __future__ import absolute_import
import BigWorld
from BigWorld import TwinGunAimingSystem, TwinGunAimingSystemRemote
from AvatarInputHandler.DynamicCameras.SniperCamera import SniperCamera

def getCameraAsSettingsHolder(settingsDataSec):
    return TwinGunCamera(settingsDataSec)


class TwinGunCamera(SniperCamera):

    def _aimingSystemClass(self):
        if BigWorld.player().isObserver():
            return TwinGunAimingSystemRemote
        return TwinGunAimingSystem

    def _readConfigs(self, dataSec):
        super(TwinGunCamera, self)._readConfigs(dataSec)
        transitionTime = dataSec.readFloat('transitionTime', 0.3)
        TwinGunAimingSystem.setTransitionTime(transitionTime)
