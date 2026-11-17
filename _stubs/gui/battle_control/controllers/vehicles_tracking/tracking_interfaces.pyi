# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vehicles_tracking/tracking_interfaces.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from vehicles.entities.vehicle_trackers import IVehicleEntityTrackerListener as IVehicleEntityTrackerListener
from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListener as IVehicleMechanicsTrackerListener

class IVehicleTrackers(object):
    def startCurrentVehicleTracking(self, listener):
        ...
    def stopCurrentVehicleTracking(self, listener):
        ...
    def startVehicleTracking(self, vehicleID, listener):
        ...
    def stopVehicleTracking(self, vehicleID, listener):
        ...

class IVehicleMechanicTrackers(object):
    def startCurrentMechanicsTracking(self, mechanics, listener):
        ...
    def stopCurrentMechanicsTracking(self, mechanics, listener):
        ...
    def startMechanicsTracking(self, vehicleID, mechanics, listener):
        ...
    def stopMechanicsTracking(self, vehicleID, mechanics, listener):
        ...

class IVehiclesTrackingWatcher(object):
    @classmethod
    def getVehiclesTrackingCtrl(cls):
        ...

class IVehiclesTrackingController(IBattleController):
    @property
    def vehicleTrackers(self):
        ...
    @property
    def vehicleMechanicTrackers(self):
        ...
