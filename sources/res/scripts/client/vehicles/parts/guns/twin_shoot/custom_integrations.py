# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/parts/guns/twin_shoot/custom_integrations.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/parts/guns/twin_shoot/custom_integrations.py
from __future__ import absolute_import
import logging, typing
from events_handler import eventHandler
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicles.components.component_wrappers import ifPlayerVehicle, ifObservedVehicle
from vehicles.parts.guns.common import GunShootingCustomIntegrations
from vehicles.parts.guns.twin_shoot.guns_interfaces import ITwinShootingListenerLogic
if typing.TYPE_CHECKING:
    from Vehicular import DetailedGunState
_logger = logging.getLogger(__name__)

class TwinShootCustomIntegrations(GunShootingCustomIntegrations, ITwinShootingListenerLogic):

    @property
    def detailedGunState(self):
        return self._vehicle.appearance.detailedGunState

    @eventHandler
    def onAppearanceReady(self):
        super(TwinShootCustomIntegrations, self).onAppearanceReady()
        self.detailedGunState.activeGuns = self._component.getActiveGunIndexes()
        self.detailedGunState.animatedGuns = self._component.getNextGunIndexes()

    @eventHandler
    def onActiveGunsUpdate(self, gunIndexes):
        self.detailedGunState.activeGuns = gunIndexes
        self.__processAvatarActiveGunsUpdate(gunIndexes=gunIndexes)

    @eventHandler
    def onAnimatedGunsUpdate(self, gunIndexes):
        self.detailedGunState.animatedGuns = gunIndexes

    @ifPlayerVehicle
    def _processAvatarSingleDiscreteShot(self, player=None):
        player.cancelWaitingForShot()
        player.getOwnVehicleShotDispersionAngle(player.gunRotator.turretRotationSpeed, withShot=1)
        super(TwinShootCustomIntegrations, self)._processAvatarSingleDiscreteShot()

    @ifObservedVehicle
    def __processAvatarActiveGunsUpdate(self, player=None, __=None, gunIndexes=()):
        player.updateMultiGunCollisions()
        feedback = dependency.instance(IBattleSessionProvider).shared.feedback
        if feedback is not None:
            feedback.invalidateActiveGunChanges(self._vehicle.id, gunIndexes, 0.0)
        return
