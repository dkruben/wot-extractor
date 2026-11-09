# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vehicle_passenger/passenger_wrappers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vehicle_passenger/passenger_wrappers.py
from __future__ import absolute_import
import operator, typing
from functools import wraps
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.vehicle_passenger.passenger_interfaces import IVehiclePassengerWatcher

def hasVehiclePassengerCtrl(ctrlName='passengerCtrl', defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(passengerInfoWatcher, *args, **kwargs):
            passengerCtrl = passengerInfoWatcher.getVehiclePassengerCtrl()
            if passengerCtrl is not None:
                kwargs[ctrlName] = passengerCtrl
                return method(passengerInfoWatcher, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(passengerInfoWatcher)
                return defReturn

        return wrapper

    return decorator
