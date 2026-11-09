# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/entities/vehicle_events/interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/entities/vehicle_events/interfaces.py
from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener
if typing.TYPE_CHECKING:
    from gui.battle_control.components_states.ammo import IComponentAmmoState
    from items.components.gun_installation_components import GunInstallationSlot
    from vehicles.entities import ShotParams

class IVehicleEventsLogic(object):
    onAppearanceReady = None
    onAppearanceReset = None
    onSiegeStateUpdated = None
    onVehicleDestroyed = None
    onObserverVehicleDataUpdated = None
    onCollectAmmoStates = None
    onCollectShotParams = None
    onCurrentShellChanged = None
    onDynamicComponentCreated = None
    onDynamicComponentDestroyed = None
    onDiscreteShotDone = None
    onShowDamageFromShot = None
    onVehicleHealthChanged = None

    def collectAmmoStates(self):
        raise NotImplementedError


class IVehicleEvents(IClientEventsContainer, IVehicleEventsLogic):
    pass


class IVehicleEventsListenerLogic(object):

    def onAppearanceReady(self):
        pass

    def onAppearanceReset(self):
        pass

    def onSiegeStateUpdated(self, newState, timeToNextMode):
        pass

    def onVehicleDestroyed(self):
        pass

    def onObserverVehicleDataUpdated(self):
        pass

    def onCollectAmmoStates(self, ammoStates):
        pass

    def onCollectShotParams(self, shotParamsList):
        pass

    def onCurrentShellChanged(self, intCD):
        pass

    def onDynamicComponentCreated(self, component):
        pass

    def onDynamicComponentDestroyed(self, component):
        pass

    def onDiscreteShotDone(self, gunInstallationSlot):
        pass

    def onShowDamageFromShot(self, attackerID, hitPoints, effectsIndex, damageFactor, lastMaterialIsShield):
        pass

    def onVehicleHealthChanged(self, vehicleID, newHealth, oldHealth):
        pass


class IVehicleEventsListener(IClientEventsContainerListener, IVehicleEventsListenerLogic):
    pass
