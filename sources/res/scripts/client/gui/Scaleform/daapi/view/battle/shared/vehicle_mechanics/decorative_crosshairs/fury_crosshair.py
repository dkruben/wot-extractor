# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/decorative_crosshairs/fury_crosshair.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/battle/shared/vehicle_mechanics/decorative_crosshairs/fury_crosshair.py
from __future__ import absolute_import
import typing, BattleReplay
from ReplayEvents import g_replayEvents
from events_containers.common.containers import ContainersListener
from events_handler import eventHandler
from gui.Scaleform.daapi.view.meta.FuryDecorativeCrosshairMeta import FuryDecorativeCrosshairMeta
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_passenger_updater import VehicleMechanicPassengerUpdater
from gui.veh_mechanics.battle.updaters.mechanics.mechanic_states_updater import VehicleMechanicStatesUpdater
from items.vehicle_mechanics_types import VehicleMechanicKeys
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic
if typing.TYPE_CHECKING:
    from typing import List
    from BattleFuryController import BattleFuryState
    from gui.veh_mechanics.battle.updaters.updaters_common import IViewUpdater

class FuryDecorativeCrosshair(FuryDecorativeCrosshairMeta, ContainersListener, IMechanicStatesListenerLogic):

    def __init__(self):
        super(FuryDecorativeCrosshair, self).__init__()
        self.__level = -1
        self.__progress = -1.0

    def _populate(self):
        super(FuryDecorativeCrosshair, self)._populate()
        if BattleReplay.g_replayCtrl.isPlaying:
            g_replayEvents.onTimeWarpFinish += self.__onReplayTimeWarpFinished

    def _dispose(self):
        if BattleReplay.g_replayCtrl.isPlaying:
            g_replayEvents.onTimeWarpFinish -= self.__onReplayTimeWarpFinished
        super(FuryDecorativeCrosshair, self)._dispose()

    @eventHandler
    def onStatePrepared(self, state):
        self.__invalidateState(state)

    @eventHandler
    def onStateTick(self, state):
        self.__invalidateState(state)

    @eventHandler
    def onStateObservation(self, state):
        self.__invalidateState(state)

    def _getViewUpdaters(self):
        return [
         VehicleMechanicPassengerUpdater(VehicleMechanicKeys.BATTLE_FURY, self),
         VehicleMechanicStatesUpdater(VehicleMechanicKeys.BATTLE_FURY, self)]

    def __onReplayTimeWarpFinished(self):
        self.as_setGunStackProgressS(self.__level, self.__progress)

    def __invalidateState(self, state):
        if state.level != self.__level or state.progress != self.__progress:
            self.__level = state.level
            self.__progress = state.progress
            self.as_setGunStackProgressS(self.__level, self.__progress)
