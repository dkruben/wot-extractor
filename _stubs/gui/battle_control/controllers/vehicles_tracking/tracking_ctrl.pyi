# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vehicles_tracking/tracking_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import typing as typing
from future.utils import viewvalues as viewvalues, viewitems as viewitems
from constants import UNKNOWN_VEHICLE_ID as UNKNOWN_VEHICLE_ID
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.vehicles_tracking.tracking_interfaces import IVehicleTrackers as IVehicleTrackers, IVehicleMechanicTrackers as IVehicleMechanicTrackers, IVehiclesTrackingController as IVehiclesTrackingController
from vehicles.entities.vehicle_trackers import createVehicleEntityTracker as createVehicleEntityTracker
from vehicles.mechanics.mechanic_trackers import createVehicleMechanicsTracker as createVehicleMechanicsTracker
from events_containers.common.containers import IClientEventsContainerListener as IClientEventsContainerListener
from gui.battle_control.controllers.vehicle_passenger import IVehiclePassengerController as IVehiclePassengerController
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from Vehicle import Vehicle as Vehicle
from vehicles.entities.vehicle_trackers import IVehicleEntityTrackerListener as IVehicleEntityTrackerListener
from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListener as IVehicleMechanicsTrackerListener
_CURR_VEH_KEY = -1

class _TrackersCollection(object):
    _trackers: Any
    def __init__(self):
        ...
    def destroy(self):
        ...
    def _addTracking(self, listener, trackerKey, trackerFactory, trackerArgs=...):
        ...
    def _removeTracking(self, listener, trackerKey):
        ...

class _VehicleTrackers(_TrackersCollection, IVehicleTrackers):
    __currentVehicleID: Any
    def __init__(self):
        ...
    def __repr__(self):
        ...
    def destroy(self):
        ...
    def startCurrentVehicleTracking(self, listener):
        ...
    def stopCurrentVehicleTracking(self, listener):
        ...
    def startVehicleTracking(self, vehicleID, listener):
        ...
    def stopVehicleTracking(self, vehicleID, listener):
        ...
    def updateCurrentVehicle(self, vehicleID=..., vehicle=None):
        ...

class _VehicleMechanicTrackers(_TrackersCollection, IVehicleMechanicTrackers):
    __vehicleTrackers: Any
    def __init__(self, vehicleTrackers):
        ...
    def __repr__(self):
        ...
    def destroy(self):
        ...
    def startCurrentMechanicsTracking(self, mechanics, listener):
        ...
    def stopCurrentMechanicsTracking(self, mechanics, listener):
        ...
    def startMechanicsTracking(self, vehicleID, mechanics, listener):
        ...
    def stopMechanicsTracking(self, vehicleID, mechanics, listener):
        ...

class VehiclesTrackingController(IVehiclesTrackingController):
    __vehiclePassengerCtrl: Any
    __vehicleTrackers: Any
    __vehicleMechanicTrackers: Any
    def __init__(self, vehiclePassengerCtrl):
        ...
    def __repr__(self):
        ...
    @property
    def vehicleTrackers(self):
        ...
    @property
    def vehicleMechanicTrackers(self):
        ...
    def getControllerID(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def __onVehiclePassengerUpdate(self, vehicle):
        ...
