# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicle_systems/shake_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/shake_helpers.py
from __future__ import absolute_import
import typing, BigWorld, Math
from aih_constants import ShakeReason
from vehicle_systems.tankStructure import TankNodeNames
if typing.TYPE_CHECKING:
    from items.components.gun_installation_components import GunInstallationSlot
    from Vehicle import Vehicle

def shakePlayerDynamicCamera(vehicle, gunInstallationSlot, shakeReason=ShakeReason.OWN_SHOT, gunNodeName=TankNodeNames.GUN_INCLINATION, gunFireNodeName='HP_gunFire'):
    appearance = vehicle.appearance
    if appearance is None or appearance.compoundModel is None:
        return
    gunNode = appearance.compoundModel.node(gunNodeName)
    gunFireNode = appearance.compoundModel.node(gunFireNodeName)
    if gunFireNode is None or gunNode is None:
        return
    BigWorld.player().inputHandler.onVehicleShaken(vehicle, shakeReason, Math.Matrix(gunFireNode).translation, Math.Matrix(gunNode).applyVector(Math.Vector3(0, 0, -1)), gunInstallationSlot.gun.effectsCaliber)
    return


def shakeMultiGunPlayerDynamicCamera(vehicle, gunInstallationSlot, gunIndex, shakeReason=ShakeReason.OWN_SHOT):
    multiGun = gunInstallationSlot.gun.multiGun
    if multiGun is not None and 0 <= gunIndex < len(multiGun):
        shakePlayerDynamicCamera(vehicle, gunInstallationSlot, shakeReason, multiGun[gunIndex].node, multiGun[gunIndex].gunFire)
    else:
        shakePlayerDynamicCamera(vehicle, gunInstallationSlot, shakeReason)
    return


def shakeMultiGunsPlayerDynamicCamera(vehicle, gunInstallationSlot, gunIndexes, shakeReason=ShakeReason.OWN_SHOT):
    for gunIndex in gunIndexes:
        shakeMultiGunPlayerDynamicCamera(vehicle, gunInstallationSlot, gunIndex, shakeReason)
