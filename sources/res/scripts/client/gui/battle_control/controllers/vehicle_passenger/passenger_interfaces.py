# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vehicle_passenger/passenger_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vehicle_passenger/passenger_interfaces.py
from __future__ import absolute_import
import typing
from gui.battle_control.controllers.interfaces import IBattleController
if typing.TYPE_CHECKING:
    from Event import LateEvent, Event

class IVehiclePassengerWatcher(object):

    @classmethod
    def getVehiclePassengerCtrl(cls):
        raise NotImplementedError


class IVehiclePassengerController(IBattleController):
    onVehiclePassengerUpdating = None
    onVehiclePassengerUpdate = None

    @property
    def isCurrentPlayerVehicle(self):
        raise NotImplementedError

    @property
    def isCurrentVehicleAlive(self):
        raise NotImplementedError

    @property
    def isCurrentVehicleFPV(self):
        raise NotImplementedError

    @property
    def currentVehicleID(self):
        raise NotImplementedError

    @property
    def playerVehicleID(self):
        raise NotImplementedError

    def setPlayerVehicle(self, vehicleID):
        raise NotImplementedError
