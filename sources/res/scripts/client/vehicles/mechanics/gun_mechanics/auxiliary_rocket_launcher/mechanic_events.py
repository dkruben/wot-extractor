# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/gun_mechanics/auxiliary_rocket_launcher/mechanic_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/gun_mechanics/auxiliary_rocket_launcher/mechanic_events.py
from __future__ import absolute_import
import typing
from cache import last_cached_method
from cgf_events import gun_events
from events_handler import eventHandler
from vehicles.components.component_events import VehicleComponentEventsCoreIntegration
from vehicles.mechanics.mechanic_states import MechanicStatesEvents, IMechanicStatesListenerLogic
if typing.TYPE_CHECKING:
    from vehicles.mechanics.gun_mechanics.auxiliary_rocket_launcher.mechanic_models import AuxiliaryRocketLauncherState

class AuxiliaryRocketLauncherStatesEvents(MechanicStatesEvents):

    def _createCoreIntegration(self):
        return AuxiliaryRocketLauncherStatesCoreIntegration(self, self._getComponent())


class AuxiliaryRocketLauncherStatesCoreIntegration(VehicleComponentEventsCoreIntegration, IMechanicStatesListenerLogic):

    @eventHandler
    def onStatePrepared(self, state):
        self.__postReloadEvent(state.isReloaded, state.reloadStartTime)

    @eventHandler
    def onStateObservation(self, state):
        self.__postReloadEvent(state.isReloaded, state.reloadStartTime)

    @last_cached_method(key=(lambda *args: args[0]))
    def __postReloadEvent(self, isReloaded, reloadStartTime):
        gun_events.postVehicularVariablesChangedEvent(self._spaceID, self._vehicleID, self._slotName, {'vehicle/secondaryGun/isReloaded': isReloaded, 
           'vehicle/secondaryGun/reloadStartTime': reloadStartTime})
