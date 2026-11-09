# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/parts/guns/auto_shoot/custom_integrations.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/parts/guns/auto_shoot/custom_integrations.py
from __future__ import absolute_import
import logging, TriggersManager
from events_handler import eventHandler
from TriggersManager import TRIGGER_TYPE
from vehicles.components.component_wrappers import ifPlayerVehicle
from vehicles.parts.guns.common import GunShootingCustomIntegrations
from vehicles.parts.guns.auto_shoot.guns_interfaces import IAutoShootingListenerLogic
from vehicle_systems.shake_helpers import shakePlayerDynamicCamera
from vehicle_systems.shooting_helpers import notifyArenaVehicleShot
_logger = logging.getLogger(__name__)

class AutoShootCustomIntegrations(GunShootingCustomIntegrations, IAutoShootingListenerLogic):

    @eventHandler
    def onContinuousBurstActivation(self):
        shakePlayerDynamicCamera(self._vehicle, self._gunInstallationSlot)
        notifyArenaVehicleShot(self._vehicle)
        self.__processAvatarContinuousActivation()

    @eventHandler
    def onContinuousBurstDeactivation(self):
        self.__processAvatarContinuousDeactivation()

    @eventHandler
    def onContinuousBurstUpdate(self):
        shakePlayerDynamicCamera(self._vehicle, self._gunInstallationSlot)

    @ifPlayerVehicle
    def __processAvatarContinuousActivation(self, _=None):
        TriggersManager.g_manager.fireTriggerInstantly(TRIGGER_TYPE.PLAYER_CONTINUOUS_BURST_START, gunInstallationIndex=self._gunInstallationSlot.installationIndex)

    @ifPlayerVehicle
    def __processAvatarContinuousDeactivation(self, _=None):
        TriggersManager.g_manager.fireTriggerInstantly(TRIGGER_TYPE.PLAYER_CONTINUOUS_BURST_STOP, gunInstallationIndex=self._gunInstallationSlot.installationIndex)
