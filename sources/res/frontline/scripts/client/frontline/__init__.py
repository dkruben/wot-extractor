# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/__init__.py
from __future__ import absolute_import
import BigWorld
from helpers import isPlayerAvatar

def invalidateVehicleMarkerState(entity, vehData, markerData, state, stateCallBack):
    attachedVehicle = BigWorld.player().getVehicleAttached()
    if attachedVehicle is None:
        return
    else:
        if entity.id == BigWorld.player().getObservedVehicleID() and vehData is not None:
            entity.guiSessionProvider.invalidateVehicleState(state, vehData)
        if not entity.isPlayerVehicle:
            ctrl = entity.guiSessionProvider.shared.feedback
            if ctrl is not None:
                call = getattr(ctrl, stateCallBack)
                call(entity.id, markerData)
        return


def isAvatarReady():
    return isPlayerAvatar() and BigWorld.player().userSeesWorld()
