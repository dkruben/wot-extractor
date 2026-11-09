# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/auxiliary_rocket_launcher/custom_integrations.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/auxiliary_rocket_launcher/custom_integrations.py
from __future__ import absolute_import
import weakref, typing
from events_containers.common.containers import ContainersListener
from events_handler import eventHandler
from gui.armor_flashlight.utils import ArmorFlashlightHideReason
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from vehicles.components.component_wrappers import ifPlayerVehicle
from vehicles.mechanics.mechanic_states import IMechanicStatesListenerLogic
if typing.TYPE_CHECKING:
    from Avatar import PlayerAvatar
    from vehicles.mechanics.gun_mechanics.auxiliary_rocket_launcher.mechanic_models import AuxiliaryRocketLauncherState

class AuxiliaryRocketLauncherCustomIntegrations(ContainersListener, IMechanicStatesListenerLogic):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self, component):
        super(AuxiliaryRocketLauncherCustomIntegrations, self).__init__()
        self._component = weakref.proxy(component)

    @eventHandler
    def onStatePrepared(self, state):
        self.__updateArmorFlashlightVisibility(state.isInAimingMode)

    @eventHandler
    def onStateTransition(self, prevState, newState):
        self.__updateArmorFlashlightVisibility(newState.isInAimingMode)

    @eventHandler
    def onEventsContainerDestroy(self, events):
        self.__updateArmorFlashlightVisibility(False)
        self._component = None
        super(AuxiliaryRocketLauncherCustomIntegrations, self).onEventsContainerDestroy(events)
        return

    def isPlayerVehicle(self, player):
        return self._component.isPlayerVehicle(player)

    @ifPlayerVehicle
    def __updateArmorFlashlightVisibility(self, _, isInAimingMode):
        armorFlashlight = self.__sessionProvider.shared.armorFlashlight
        if armorFlashlight is None:
            return
        else:
            if isInAimingMode:
                armorFlashlight.addHideReason(ArmorFlashlightHideReason.HE_ROCKET_AIMING_MODE)
            else:
                armorFlashlight.removeHideReason(ArmorFlashlightHideReason.HE_ROCKET_AIMING_MODE)
            return
