# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/turret_gun_angles.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/turret_gun_angles.py
from __future__ import absolute_import
from gui.ClientHangarSpace import hangarCFG
from skeletons.gui.turret_gun_angles import ITurretAndGunAngles

class TurretAndGunAngles(ITurretAndGunAngles):

    def __init__(self):
        self.__gunPitch = 0.0
        self.__turretYaw = 0.0

    def init(self):
        self.reset()

    def reset(self):
        cfg = hangarCFG()
        self.__gunPitch = cfg.get('vehicle_gun_pitch', 0.0)
        self.__turretYaw = cfg.get('vehicle_turret_yaw', 0.0)

    def destroy(self):
        self.__gunPitch = 0.0
        self.__turretYaw = 0.0

    def set(self, gunPitch=0.0, turretYaw=0.0):
        self.__gunPitch = gunPitch
        self.__turretYaw = turretYaw

    def getTurretYaw(self):
        return self.__turretYaw

    def getGunPitch(self):
        return self.__gunPitch
