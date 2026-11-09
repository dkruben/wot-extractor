# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/components/component_events.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/components/component_events.py
from __future__ import absolute_import
import typing
from events_containers.common.containers import ClientEventsContainerCoreIntegration
if typing.TYPE_CHECKING:
    from events_containers.common.containers.interfaces import IClientEventsContainer

class VehicleComponentEventsCoreIntegration(ClientEventsContainerCoreIntegration):

    def __init__(self, events, component):
        self._spaceID = component.entity.spaceID
        self._vehicleID = component.entity.id
        self._slotName = component.getVehicleSlotName()
        super(VehicleComponentEventsCoreIntegration, self).__init__(events)

    def _attachToEventsContainer(self, events):
        self.lateSubscribeTo(events)
