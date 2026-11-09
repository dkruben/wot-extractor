# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vehicles_tracking/tracking_wrappers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vehicles_tracking/tracking_wrappers.py
from __future__ import absolute_import
import operator, typing
from functools import wraps
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.vehicles_tracking.tracking_interfaces import IVehiclesTrackingWatcher

def hasVehiclesTrackingCtrl(ctrlName='vehiclesTrackingCtrl', defReturn=None, abortAction=None):

    def decorator(method):

        @wraps(method)
        def wrapper(vehiclesTrackingWatcher, *args, **kwargs):
            trackingCtrl = vehiclesTrackingWatcher.getVehiclesTrackingCtrl()
            if trackingCtrl is not None:
                kwargs[ctrlName] = trackingCtrl
                return method(vehiclesTrackingWatcher, *args, **kwargs)
            else:
                if abortAction is not None:
                    return operator.methodcaller(abortAction)(vehiclesTrackingWatcher)
                return defReturn

        return wrapper

    return decorator
