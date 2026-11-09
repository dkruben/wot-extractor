# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/entities/vehicle_trackers/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/entities/vehicle_trackers/__init__.py
from __future__ import absolute_import
from constants import UNKNOWN_VEHICLE_ID
from vehicles.entities.vehicle_trackers.events import VehicleEntityTracker
from vehicles.entities.vehicle_trackers.interfaces import IVehicleEntityTracker, IVehicleEntityTrackerListener, IVehicleEntityTrackerListenerLogic
__all__ = ('IVehicleEntityTracker', 'IVehicleEntityTrackerListener', 'IVehicleEntityTrackerListenerLogic',
           'createVehicleEntityTracker')

def createVehicleEntityTracker(vehicleID=UNKNOWN_VEHICLE_ID):
    return VehicleEntityTracker(vehicleID)
