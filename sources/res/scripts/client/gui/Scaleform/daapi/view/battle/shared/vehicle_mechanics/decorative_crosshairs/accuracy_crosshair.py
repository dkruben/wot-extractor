# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/decorative_crosshairs/accuracy_crosshair.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/decorative_crosshairs/accuracy_crosshair.py
from __future__ import absolute_import
import typing
from events_containers.common.containers import ContainersListener
from events_handler import eventHandler
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from gui.Scaleform.daapi.view.meta.AccuracyStackDecorativeCrosshairMeta import AccuracyStackDecorativeCrosshairMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater
from gui.veh_mechanics.battle.updaters.vehicle_state_updater import VehicleStateUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic
if typing.TYPE_CHECKING:
    from AccuracyStacksController import AccuracyStacksState

class AccuracyDecorativeCrosshair(AccuracyStackDecorativeCrosshairMeta, ContainersListener, IMechanicStatesListenerLogic):

    def __init__(self):
        super(AccuracyDecorativeCrosshair, self).__init__()
        self.__level = -1
        self.__progress = -1.0
        self.__speedThreshold = -1
        self.__isGainingActive = False
        self.__isSpeedLimitActive = False

    @eventHandler
    def onStatePrepared(self, state):
        self.__speedThreshold = state.speedThreshold
        self.as_setInitDataS(state.maxLevel, self.__speedThreshold)
        self.updateSpeedLimit(self.__isSpeedLimitActive, True)

    @eventHandler
    def onStateObservation(self, state):
        self.__update(state)

    @eventHandler
    def onStateTick(self, state):
        self.__update(state)

    def _getViewUpdaters(self):
        return [
         VehicleMechanicPassengerUpdater(VehicleMechanicKeys.ACCURACY_STACKS, self),
         VehicleMechanicStatesUpdater(VehicleMechanicKeys.ACCURACY_STACKS, self),
         VehicleStateUpdater(self)]

    def updateSpeedLimit(self, value, forced=False):
        if self.__isSpeedLimitActive != value or forced:
            self.__isSpeedLimitActive = value
            self.as_setSpeedLimitActiveS(self.__isSpeedLimitActive)

    def onVehicleStateUpdated(self, stateID, value):
        if stateID != VEHICLE_VIEW_STATE.SPEED:
            return
        isSpeedLimitActive = abs(value) >= self.__speedThreshold
        self.updateSpeedLimit(isSpeedLimitActive)

    def __update(self, state):
        if self.__level != state.level or self.__progress != state.progress:
            self.__level = state.level
            self.__progress = state.progress
            self.as_setStacksProgresS(self.__level, self.__progress)
        if self.__isGainingActive != state.isGainingActive:
            self.__isGainingActive = state.isGainingActive
            self.as_setGainingActiveS(self.__isGainingActive)
