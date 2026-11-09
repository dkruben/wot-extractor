# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/battle_control/controllers/vehicle_passenger/passenger_mixins.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/battle_control/controllers/vehicle_passenger/passenger_mixins.py
from __future__ import absolute_import
import typing
from constants import UNKNOWN_VEHICLE_ID
from gui.battle_control.controllers.vehicle_passenger.passenger_interfaces import IVehiclePassengerWatcher
from gui.battle_control.controllers.vehicle_passenger.passenger_wrappers import hasVehiclePassengerCtrl
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
if typing.TYPE_CHECKING:
    from gui.battle_control.controllers.vehicle_passenger.passenger_interfaces import IVehiclePassengerController

class VehiclePassengerInfoWatcher(IVehiclePassengerWatcher):

    @classmethod
    def getVehiclePassengerCtrl(cls):
        return dependency.instance(IBattleSessionProvider).shared.vehiclePassenger

    @classmethod
    @hasVehiclePassengerCtrl(defReturn=UNKNOWN_VEHICLE_ID)
    def getVehiclePassengerCurrentVehicleID(cls, passengerCtrl=None):
        return passengerCtrl.currentVehicleID

    @classmethod
    @hasVehiclePassengerCtrl()
    def startVehiclePassengerLateListening(cls, updateListener, updatingListener=None, passengerCtrl=None):
        passengerCtrl.onVehiclePassengerUpdate.lateAdd(updateListener)
        if updatingListener is not None:
            passengerCtrl.onVehiclePassengerUpdating += updatingListener
        return

    @classmethod
    @hasVehiclePassengerCtrl()
    def startVehiclePassengerListening(cls, updateListener, updatingListener=None, passengerCtrl=None):
        passengerCtrl.onVehiclePassengerUpdate += updateListener
        if updatingListener is not None:
            passengerCtrl.onVehiclePassengerUpdating += updatingListener
        return

    @classmethod
    @hasVehiclePassengerCtrl()
    def stopVehiclePassengerListening(cls, updateListener, updatingListener=None, passengerCtrl=None):
        passengerCtrl.onVehiclePassengerUpdate -= updateListener
        if updatingListener is not None:
            passengerCtrl.onVehiclePassengerUpdating -= updatingListener
        return
