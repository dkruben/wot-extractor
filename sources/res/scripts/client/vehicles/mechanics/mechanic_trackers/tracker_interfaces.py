# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/mechanics/mechanic_trackers/tracker_interfaces.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/mechanics/mechanic_trackers/tracker_interfaces.py
from __future__ import absolute_import
import typing
from events_containers.common.containers import IClientEventsContainer, IClientEventsContainerListener
from vehicles.entities.vehicle_trackers import IVehicleEntityTrackerListenerLogic
if typing.TYPE_CHECKING:
    from items.vehicle_mechanics_types import VehicleMechanicKey

class IVehicleMechanicsTrackerLogic(IVehicleEntityTrackerListenerLogic):
    onMechanicComponentCatching = None
    onMechanicComponentReleasing = None
    onMechanicComponentsUpdate = None

    @property
    def trackedComponents(self):
        raise NotImplementedError

    def getTrackedComponent(self, mechanic):
        raise NotImplementedError


class IVehicleMechanicsTracker(IClientEventsContainer, IVehicleMechanicsTrackerLogic):
    pass


class IVehicleMechanicsTrackerListenerLogic(object):

    def onMechanicComponentCatching(self, component):
        pass

    def onMechanicComponentReleasing(self, component):
        pass

    def onMechanicComponentsUpdate(self, components):
        pass


class IVehicleMechanicsTrackerListener(IClientEventsContainerListener, IVehicleMechanicsTrackerListenerLogic):
    pass
