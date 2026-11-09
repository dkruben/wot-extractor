# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vehicles_tracking/tracking_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vehicles_tracking/tracking_interfaces.py
from __future__ import absolute_import
import typing
from gui.battle_control.controllers.interfaces import IBattleController
if typing.TYPE_CHECKING:
    from items.vehicle_mechanics_types import VehicleMechanicKey
    from vehicles.entities.vehicle_trackers import IVehicleEntityTrackerListener
    from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListener

class IVehicleTrackers(object):

    def startCurrentVehicleTracking(self, listener):
        raise NotImplementedError

    def stopCurrentVehicleTracking(self, listener):
        raise NotImplementedError

    def startVehicleTracking(self, vehicleID, listener):
        raise NotImplementedError

    def stopVehicleTracking(self, vehicleID, listener):
        raise NotImplementedError


class IVehicleMechanicTrackers(object):

    def startCurrentMechanicsTracking(self, mechanics, listener):
        raise NotImplementedError

    def stopCurrentMechanicsTracking(self, mechanics, listener):
        raise NotImplementedError

    def startMechanicsTracking(self, vehicleID, mechanics, listener):
        raise NotImplementedError

    def stopMechanicsTracking(self, vehicleID, mechanics, listener):
        raise NotImplementedError


class IVehiclesTrackingWatcher(object):

    @classmethod
    def getVehiclesTrackingCtrl(cls):
        raise NotImplementedError


class IVehiclesTrackingController(IBattleController):

    @property
    def vehicleTrackers(self):
        raise NotImplementedError

    @property
    def vehicleMechanicTrackers(self):
        raise NotImplementedError
