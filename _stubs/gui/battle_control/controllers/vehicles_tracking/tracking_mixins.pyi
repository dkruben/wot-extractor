# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vehicles_tracking/tracking_mixins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import TYPE_CHECKING as TYPE_CHECKING
from gui.battle_control.controllers.vehicles_tracking.tracking_interfaces import IVehiclesTrackingWatcher as IVehiclesTrackingWatcher
from gui.battle_control.controllers.vehicles_tracking.tracking_wrappers import hasVehiclesTrackingCtrl as hasVehiclesTrackingCtrl
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from typing import Optional as Optional, Tuple as Tuple
from gui.battle_control.controllers.vehicles_tracking.tracking_interfaces import IVehiclesTrackingController as IVehiclesTrackingController
from items.vehicle_mechanics_types import VehicleMechanicKey as VehicleMechanicKey
from vehicles.mechanics.mechanic_trackers import IVehicleMechanicsTrackerListener as IVehicleMechanicsTrackerListener

class VehiclesTrackingWatcher(IVehiclesTrackingWatcher):
    @classmethod
    def getVehiclesTrackingCtrl(cls):
        ...
    @classmethod
    # decorador original: @hasVehiclesTrackingCtrl(...)
    def startCurrentVehicleMechanicsTracking(cls, mechanics, listener, vehiclesTrackingCtrl=None):
        ...
    @classmethod
    # decorador original: @hasVehiclesTrackingCtrl(...)
    def stopCurrentVehicleMechanicsTracking(cls, mechanics, listener, vehiclesTrackingCtrl=None):
        ...
    @classmethod
    # decorador original: @hasVehiclesTrackingCtrl(...)
    def startVehicleMechanicsTracking(cls, vehicleID, mechanics, listener, vehiclesTrackingCtrl=None):
        ...
    @classmethod
    # decorador original: @hasVehiclesTrackingCtrl(...)
    def stopVehicleMechanicsTracking(cls, vehicleID, mechanics, listener, vehiclesTrackingCtrl=None):
        ...
