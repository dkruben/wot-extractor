# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/vehicle_passenger/passenger_mixins.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

import typing as typing
from constants import UNKNOWN_VEHICLE_ID as UNKNOWN_VEHICLE_ID
from gui.battle_control.controllers.vehicle_passenger.passenger_interfaces import IVehiclePassengerWatcher as IVehiclePassengerWatcher
from gui.battle_control.controllers.vehicle_passenger.passenger_wrappers import hasVehiclePassengerCtrl as hasVehiclePassengerCtrl
from helpers import dependency as dependency
from skeletons.gui.battle_session import IBattleSessionProvider as IBattleSessionProvider
from gui.battle_control.controllers.vehicle_passenger.passenger_interfaces import IVehiclePassengerController as IVehiclePassengerController

class VehiclePassengerInfoWatcher(IVehiclePassengerWatcher):
    @classmethod
    def getVehiclePassengerCtrl(cls):
        ...
    @classmethod
    # decorador original: @hasVehiclePassengerCtrl(...)
    def getVehiclePassengerCurrentVehicleID(cls, passengerCtrl=None):
        ...
    @classmethod
    # decorador original: @hasVehiclePassengerCtrl(...)
    def startVehiclePassengerLateListening(cls, updateListener, updatingListener=None, passengerCtrl=None):
        ...
    @classmethod
    # decorador original: @hasVehiclePassengerCtrl(...)
    def startVehiclePassengerListening(cls, updateListener, updatingListener=None, passengerCtrl=None):
        ...
    @classmethod
    # decorador original: @hasVehiclePassengerCtrl(...)
    def stopVehiclePassengerListening(cls, updateListener, updatingListener=None, passengerCtrl=None):
        ...
