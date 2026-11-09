# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicle_systems/instant_status_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/instant_status_helpers.py
from __future__ import absolute_import
import CGF, InstantStatuses

def invokeInstantStatusForVehicle(vehicle, instantStatusType):
    gameObject = vehicle.appearance.gameObject
    instantStatus = gameObject.findWrite(instantStatusType)
    if not instantStatus:
        queue = CGF.CommandQueue(gameObject.spaceID)
        queue.createComponent(gameObject, instantStatusType)
    else:
        instantStatus.addNextDone()


def invokeShotsDoneStatus(vehicle):
    invokeInstantStatusForVehicle(vehicle, InstantStatuses.ShotsDoneComponent)
