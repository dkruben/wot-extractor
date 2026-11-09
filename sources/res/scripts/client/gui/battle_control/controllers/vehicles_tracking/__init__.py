# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vehicles_tracking/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vehicles_tracking/__init__.py
from __future__ import absolute_import
import typing
from gui.battle_control.controllers.vehicles_tracking.tracking_ctrl import VehiclesTrackingController
from gui.battle_control.controllers.vehicles_tracking.tracking_interfaces import IVehiclesTrackingController
from gui.battle_control.controllers.vehicles_tracking.tracking_mixins import VehiclesTrackingWatcher
from gui.battle_control.controllers.vehicles_tracking.tracking_wrappers import hasVehiclesTrackingCtrl
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.vehicle_passenger import IVehiclePassengerController
__all__ = ('IVehiclesTrackingController', 'VehiclesTrackingWatcher', 'hasVehiclesTrackingCtrl',
           'createVehiclesTrackingController')

def createVehiclesTrackingController(vehiclePassengerCtrl):
    return VehiclesTrackingController(vehiclePassengerCtrl)
