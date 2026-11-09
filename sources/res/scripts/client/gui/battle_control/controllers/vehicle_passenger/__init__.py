# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vehicle_passenger/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vehicle_passenger/__init__.py
from __future__ import absolute_import
import typing
from gui.battle_control.controllers.vehicle_passenger.passenger_ctrl import VehiclePassengerController
from gui.battle_control.controllers.vehicle_passenger.passenger_interfaces import IVehiclePassengerController
from gui.battle_control.controllers.vehicle_passenger.passenger_mixins import VehiclePassengerInfoWatcher
from gui.battle_control.controllers.vehicle_passenger.passenger_wrappers import hasVehiclePassengerCtrl
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.vehicle_state_ctrl import VehicleStateController
__all__ = ('IVehiclePassengerController', 'VehiclePassengerInfoWatcher', 'hasVehiclePassengerCtrl',
           'createVehiclePassengerController')

def createVehiclePassengerController(vehStateCtrl):
    return VehiclePassengerController(vehStateCtrl)
