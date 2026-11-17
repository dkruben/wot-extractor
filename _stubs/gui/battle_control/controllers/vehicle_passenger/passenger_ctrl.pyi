# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vehicle_passenger/passenger_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
import weakref as weakref
import Event as Event
from constants import UNKNOWN_VEHICLE_ID as UNKNOWN_VEHICLE_ID
from gui.battle_control import avatar_getter as avatar_getter
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID, VEHICLE_VIEW_STATE as VEHICLE_VIEW_STATE
from gui.battle_control.controllers.vehicle_passenger.passenger_interfaces import IVehiclePassengerController as IVehiclePassengerController
from gui.shared.utils.decorators import ReprInjector as ReprInjector
from gui.battle_control.controllers.vehicle_state_ctrl import VehicleStateController as VehicleStateController
from Vehicle import Vehicle as Vehicle

# decorador original: @ReprInjector.simple(...)
class VehiclePassengerController(IVehiclePassengerController):
    __slots__: tuple
    __vehStateCtrl: Any
    __playerVehicleID: Any
    __isCurrentVehicleAlive: Any
    __isCurrentVehicleFPV: Any
    __eManager: Any
    onVehiclePassengerUpdating: Any
    onVehiclePassengerUpdate: Any
    def __init__(self, vehStateCtrl):
        ...
    @property
    def isCurrentPlayerVehicle(self):
        ...
    @property
    def isCurrentVehicleAlive(self):
        ...
    @property
    def isCurrentVehicleFPV(self):
        ...
    @property
    def currentVehicleID(self):
        ...
    @property
    def playerVehicleID(self):
        ...
    def getControllerID(self):
        ...
    def setPlayerVehicle(self, vehicleID):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def _getCurrentVehicle(self):
        ...
    def __onVehicleStateUpdated(self, stateID, _):
        ...
    def __latePassengerUpdate(self, handler):
        ...
    def __updateCurrentVehicleInfo(self, vehicle):
        ...
    def __updateVehiclePassengerInfo(self, vehicle=None):
        ...
