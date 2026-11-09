# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/veh_mechanics/battle/updaters/mechanics/tracked_mechanics_updater.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/veh_mechanics/battle/updaters/mechanics/tracked_mechanics_updater.py
from __future__ import absolute_import
import typing
from events_containers.common.containers import ContainersListener
from events_handler import eventHandler
from gui.battle_control.controllers.vehicles_tracking import VehiclesTrackingWatcher
from gui.veh_mechanics.battle.updaters.updaters_common import ViewUpdater
from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListenerLogic
if typing.TYPE_CHECKING:
    from items.vehicle_mechanics_types import VehicleMechanicKey

class IVehicleTrackedMechanicsView(object):

    def onTrackedMechanicsUpdate(self, mechanics):
        raise NotImplementedError


class VehicleTrackedMechanicsUpdater(ViewUpdater, ContainersListener, VehiclesTrackingWatcher, IVehicleMechanicsTrackerListenerLogic):

    def initialize(self):
        super(VehicleTrackedMechanicsUpdater, self).initialize()
        self.startCurrentVehicleMechanicsTracking((), self)

    def finalize(self):
        self.stopCurrentVehicleMechanicsTracking((), self)
        super(VehicleTrackedMechanicsUpdater, self).finalize()

    @eventHandler
    def onMechanicComponentsUpdate(self, components):
        self.view.onTrackedMechanicsUpdate(set(components))
