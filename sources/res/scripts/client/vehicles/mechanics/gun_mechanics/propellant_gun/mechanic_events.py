# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/propellant_gun/mechanic_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/propellant_gun/mechanic_events.py
from __future__ import absolute_import
import typing
from cache import last_cached_method
from cgf_events import gun_events
from events_handler import eventHandler
from vehicles.components.component_events import VehicleComponentEventsCoreIntegration
from vehicles.mechanics.mechanic_states import MechanicStatesEvents, IMechanicStatesListenerLogic
if typing.TYPE_CHECKING:
    from vehicles.mechanics.gun_mechanics.propellant_gun.mechanic_interfaces import IPropellantGunMechanicState

class PropellantStatesEvents(MechanicStatesEvents):

    def _createCoreIntegration(self):
        return PropellantStatesCoreIntegration(self, self._getComponent())


class PropellantStatesCoreIntegration(VehicleComponentEventsCoreIntegration, IMechanicStatesListenerLogic):

    @eventHandler
    def onStatePrepared(self, state):
        self.__postPropellantChangedEvent(state.lastShotTimestamp, state.lastShotCharge)

    @eventHandler
    def onStateObservation(self, state):
        self.__postPropellantChangedEvent(state.lastShotTimestamp, state.lastShotCharge)

    @last_cached_method()
    def __postPropellantChangedEvent(self, lastShotTimestamp, lastShotCharge):
        gun_events.postVehicularVariablesChangedEvent(self._spaceID, self._vehicleID, self._slotName, {'vehicle/gun/lastSingleShotTimeServer': lastShotTimestamp, 
           'vehicle/gun/lastShotPropellantProgress': lastShotCharge})
