# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/mechanics_common.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/mechanics/mechanics_common.py
from __future__ import absolute_import
import typing
from events_containers.common.containers import ContainersListener
from gui.battle_control.controllers.vehicles_tracking import VehiclesTrackingWatcher
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater
from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListenerLogic
if typing.TYPE_CHECKING:
    from events_containers.common.containers import IClientEventsContainerListener
    from items.vehicle_mechanics_types import VehicleMechanicKey

class VehicleMechanicUpdater(ViewUpdater, ContainersListener, VehiclesTrackingWatcher, IVehicleMechanicsTrackerListenerLogic):

    def __init__(self, vehicleMechanic, view):
        super(VehicleMechanicUpdater, self).__init__(view)
        self.__vehicleMechanicKey = vehicleMechanic

    def initialize(self):
        super(VehicleMechanicUpdater, self).initialize()
        self.startCurrentVehicleMechanicsTracking((self.__vehicleMechanicKey,), self)

    def finalize(self):
        self.stopCurrentVehicleMechanicsTracking((self.__vehicleMechanicKey,), self)
        super(VehicleMechanicUpdater, self).finalize()
