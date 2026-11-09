# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/private/mechanic_logging.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/low_charge_shot/private/mechanic_logging.py
from __future__ import absolute_import
from constants import LowChargeShotReloadingState
from events_containers.common.containers import ContainersListener
from events_handler import eventHandler
from gui.battle_control.battle_constants import CANT_SHOOT_ERROR
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic
from skeletons.gui.battle_session import IBattleSessionProvider
from uilogging.vehicle_mechanics.low_charge_shot.logger import LowChargeShotUILogger
from helpers import dependency

class LowChargeShotUILogging(ContainersListener, IMechanicStatesListenerLogic):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(LowChargeShotUILogging, self).__init__()
        self.__uiLogger = LowChargeShotUILogger()
        self.__reloadingState = LowChargeShotReloadingState.EMPTY
        self.__arenaUniqueID = 0
        self.__logOnceSet = False

    def subscribe(self, mechanicComponent, arenaUniqueID):
        self.__arenaUniqueID = arenaUniqueID
        self.lateSubscribeTo(mechanicComponent.statesEvents)
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is not None:
            ammoCtrl.onShotBlocked += self.__onShotBlocked
        return

    @eventHandler
    def onStatePrepared(self, state):
        self.__reloadingState = state.reloadingState

    @eventHandler
    def onStateTransition(self, prevState, newState):
        if newState.reloadingState == LowChargeShotReloadingState.ALMOST_FINISHED:
            self.__uiLogger.onAlmostFinishedStarted()
            self.__logOnceSet = False
        else:
            self.__uiLogger.onAlmostFinishedEnded()
        self.__reloadingState = newState.reloadingState

    @eventHandler
    def onEventsContainerDestroy(self, events):
        ammoCtrl = self.__sessionProvider.shared.ammo
        if ammoCtrl is not None:
            ammoCtrl.onShotBlocked -= self.__onShotBlocked
        super(LowChargeShotUILogging, self).onEventsContainerDestroy(events)
        return

    def __onShotBlocked(self, error):
        if error == CANT_SHOOT_ERROR.LOW_CHARGE_SHOT_BLOCKING and self.__reloadingState == LowChargeShotReloadingState.ALMOST_FINISHED and not self.__logOnceSet:
            self.__uiLogger.onAlmostFinishedClicked(self.__arenaUniqueID)
            self.__logOnceSet = True
