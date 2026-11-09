# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/cgf_components/crest_moving_manager.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/cgf_components/crest_moving_manager.py
from __future__ import absolute_import
import logging
from typing import TYPE_CHECKING
import CGF
from cgf_common.cgf_helpers import getVehicleEntityByVehicleGameObject
from cgf_components.crest_moving_effects_component import CrestMovingEffectsComponent
from constants import CREST_MOVING_STATE
from gui.battle_control.controllers.vehicles_tracking import VehiclesTrackingWatcher
from items.vehicle_mechanics_types import VehicleMechanicKeys
if TYPE_CHECKING:
    from CrestMovingController import CrestMovingState
_logger = logging.getLogger(__name__)

class CrestMovingEffectsSystem(CGF.System, VehiclesTrackingWatcher):
    EffectsActivated = CGF.ActivateReaction(CGF.GameObject, CGF.ReactRw(CrestMovingEffectsComponent))
    EffectsDeactivated = CGF.DeactivateReaction(CGF.GameObject, CGF.ReactRw(CrestMovingEffectsComponent))
    Reactions = CGF.Reactions(EffectsDeactivated, EffectsActivated)

    def update(self):
        for go, effectsComponent in self.reaction(self.EffectsDeactivated):
            self.__stopActiveSound(effectsComponent)
            if effectsComponent.vehicleID is not None:
                self.stopVehicleMechanicsTracking(effectsComponent.vehicleID, (
                 VehicleMechanicKeys.CREST_MOVING,), effectsComponent)
                effectsComponent.vehicleID = None
            effectsComponent.onStateTransitionEvent -= self.__onStateChanged

        for go, effectsComponent in self.reaction(self.EffectsActivated):
            vehicle = getVehicleEntityByVehicleGameObject(go)
            if vehicle is None:
                _logger.debug('onAdded: vehicle not found for go=%s', go)
                continue
            effectsComponent.onStateTransitionEvent += self.__onStateChanged
            effectsComponent.vehicleID = vehicle.id
            self.startVehicleMechanicsTracking(vehicle.id, (VehicleMechanicKeys.CREST_MOVING,), effectsComponent)

        return

    def __onStateChanged(self, effectsComponent, previousState, newState):
        _logger.debug('__onStateChanged: %s -> %s', previousState, newState)
        if previousState.state.isRunning:
            self.__stopActiveSound(effectsComponent)
        if newState.state.isRunning:
            self.__startMoving(effectsComponent, newState.state)

    def __startMoving(self, effectsComponent, state):
        if state == CREST_MOVING_STATE.RUNNING_UP:
            moveSound = effectsComponent.soundMoveUp() if effectsComponent.soundMoveUp else None
            stopSound = effectsComponent.soundStopUp() if effectsComponent.soundStopUp else None
        else:
            moveSound = effectsComponent.soundMoveDown() if effectsComponent.soundMoveDown else None
            stopSound = effectsComponent.soundStopDown() if effectsComponent.soundStopDown else None
        if moveSound:
            _logger.debug('startMoving: playing %s', state.name)
            moveSound.play()
            effectsComponent.activeSound = moveSound
            effectsComponent.stopSound = stopSound
        return

    def __stopActiveSound(self, effectsComponent):
        activeSound = effectsComponent.activeSound
        stopSound = effectsComponent.stopSound
        if activeSound is not None:
            _logger.debug('stopActiveSound: stopping current sound')
            activeSound.stop()
            effectsComponent.activeSound = None
            if stopSound is not None:
                _logger.debug('stopActiveSound: playing stop sound')
                stopSound.play()
                effectsComponent.stopSound = None
        return
