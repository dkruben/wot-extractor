# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicle_systems/shooting_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicle_systems/shooting_helpers.py
from __future__ import absolute_import
import typing, BigWorld
from cgf_events import gun_events
from constants import IS_CLIENT, DEFAULT_GUN_INDEX
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicle_systems.instant_status_helpers import invokeShotsDoneStatus
if typing.TYPE_CHECKING:
    from items.components.gun_installation_components import GunInstallationSlot
    from Vehicle import Vehicle

def processVehicleSingleShot(vehicle, gunInstallationSlot, gunIndex=DEFAULT_GUN_INDEX):
    gun_events.postVehicularSingleShotEvent(vehicle.spaceID, vehicle.id, gunInstallationSlot.partSlotName, gunIndex)
    processVehicleDiscreteShots(vehicle, gunInstallationSlot)


def processVehicleMultiShot(vehicle, gunInstallationSlot, gunIndexes):
    gun_events.postVehicularMultiShotEvent(vehicle.spaceID, vehicle.id, gunInstallationSlot.partSlotName, gunIndexes)
    processVehicleDiscreteShots(vehicle, gunInstallationSlot)


def processVehicleDiscreteShots(vehicle, gunInstallationSlot):
    if gunInstallationSlot.isMainInstallation():
        invokeShotsDoneStatus(vehicle)
    if IS_CLIENT:
        vehicle.events.onDiscreteShotDone(gunInstallationSlot)
        notifyVehicleDiscreteShots(vehicle, gunInstallationSlot)
        if gunInstallationSlot.isMainInstallation():
            notifyArenaVehicleShot(vehicle)


@dependency.replace_none_kwargs(sessionProvider=IBattleSessionProvider)
def notifyVehicleDiscreteShots(vehicle, gunInstallationSlot, sessionProvider=None):
    feedback = sessionProvider.shared.feedback
    if feedback is not None:
        feedback.onDiscreteShotsDone(vehicle.id, gunInstallationSlot)
    return


def notifyArenaVehicleShot(vehicle):
    arena = getattr(BigWorld.player(), 'arena', None)
    if arena is not None:
        arena.onVehicleShot(vehicle.id)
    return
