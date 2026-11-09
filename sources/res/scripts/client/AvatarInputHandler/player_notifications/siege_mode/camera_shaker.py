# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/AvatarInputHandler/player_notifications/siege_mode/camera_shaker.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/AvatarInputHandler/player_notifications/siege_mode/camera_shaker.py
from __future__ import absolute_import
import BigWorld, Math
from constants import VEHICLE_SIEGE_STATE
from vehicle_systems.tankStructure import TankNodeNames

class SiegeModeCameraShaker(object):
    SIEGE_CAMERA_IMPULSE = 0.05

    @staticmethod
    def shake(_, newState, __):
        if newState not in VEHICLE_SIEGE_STATE.SWITCHING:
            return
        else:
            vehicle = BigWorld.player().getVehicleAttached()
            if vehicle is None:
                return
            nodeGunJoint = vehicle.model.node(TankNodeNames.GUN_JOINT)
            typeDescriptor = vehicle.typeDescriptor
            if typeDescriptor.hasAutoSiegeMode or typeDescriptor.isTwinGunVehicle or nodeGunJoint is None:
                return
            handler = BigWorld.player().inputHandler
            matrix = Math.Matrix(vehicle.model.matrix)
            impulseDir = -matrix.applyToAxis(2)
            impulsePosition = Math.Matrix(nodeGunJoint).translation
            handler.onSpecificImpulse(impulsePosition, impulseDir * SiegeModeCameraShaker.SIEGE_CAMERA_IMPULSE, 'sniper')
            return
